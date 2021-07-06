# -*- coding: utf-8 -*-

import logging
import asyncio
import re
from cbpi.api import *
from cbpi.controller.sensor_controller import SensorController
from .ADS1x15 import ADS1115
from aiohttp import web

# Choose a gain of 1 for reading voltages from 0 to 4.09V.
# Or pick a different gain to change the range of voltages that are read:
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
# See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
# GAIN = 1 is selectable as parameter in Hardware Settings->Sensor menu of CBPi
# To determine address of ph-circuit board use command prompt in Raspi and type in:
# sudo i2cdetect -y 1 or sudo i2cdetect -y 0
VOLTAGEOFFSET = 0.009  # put here your values
DEBUG = False

logger = logging.getLogger(__name__)


@parameters([Property.Select("ADS1x15 Channel", options=["0", "1", "2", "3"],
                             description="Select hardware channel-number of ADS1x15, default is 0"),
             Property.Select("ADS1x15 Address", options=["0x48", "0x49", "0x4A", "0x4B"],
                             description="Select hardware address-number of ADS1x15, default is 0x48"),
             Property.Select("Data Type", options=["pH Value", "Voltage", "Digits"],
                             description="Select which type of data to register for this sensor, "
                                         "hint: add the same sensor several times with different units"),
             Property.Select("ADS1x15 Gain", options=["0", "1", "2", "4", "8", "16"],
                             description="Select gain of pH ADS1x15, default = 1, hint 2/3 can be selected by 0")])
class phSensorADS1x15(CBPiSensor):

    def __init__(self, cbpi, id, props):
        super(phSensorADS1x15, self).__init__(cbpi, id, props)
        self.value = 0
        self.key = self.props.get("phSensorADS1x15", None)

    def get_unit(self):
        unit = self.props.get("Data Type")
        if unit == "pH Value":
            return " ph"
        elif unit == "Voltage":
            return " V"
        elif unit == "Digits":
            return " Bit"
        else:
            return "select Data Type"

    async def run(self):
        while self.running is True:
            ch = int(self.props.get("ADS1x15 Channel"))
            gain = int(self.props.get("ADS1x15 Gain"))
            address = int(str(self.props.get("ADS1x15 Address"), 16))
            adc = ADS1115(address=address, busnum=1)

            value = adc.read_adc(ch, gain=gain)
            voltage = ((float(value) * 4.096 / 32767) - VOLTAGEOFFSET)
            # phvalue = ("%.2f" % (7 + ((2.564 - voltage) / 0.1839)))                        # better around pH 7 and 6
            phvalue = ("%.2f" % (7 + ((2.548 - voltage) / 0.17826)))                         # better around pH 5

            kind_of_data = self.props.get("Data Type")
            if kind_of_data == "pH Value":
                self.value = phvalue
            elif kind_of_data == "Voltage":
                self.value = "%.3f" % voltage
            elif kind_of_data == "Digits":
                self.value = value
            else:
                self.value = 0.00

            self.log_data(self.value)

            self.push_update(self.value)
            await asyncio.sleep(2)

    def get_state(self):
        return dict(value=self.value)


class phSensorEndpoint(CBPiExtension):

    def __init__(self, cbpi):
        '''
        Initializer
        :param cbpi:
        '''
        self.pattern_check = re.compile("^[a-zA-Z0-9,.]{0,10}$")
        self.cbpi = cbpi
        self.sensor_controller: SensorController = cbpi.sensor
        # register component for http, events
        # In addtion the sub folder static is exposed to access static content via http
        self.cbpi.register(self, "/api/phSensor/v1/data")

    async def run(self):
        await self.get_phSensor_sensor()

    @request_mapping(path='', method="POST", auth_required=False)
    async def http_new_value3(self, request):
        import time
        """
        ---
        description: Get phSensor Value
        tags:
        - phSensor 
        parameters:
        - name: "data"
          in: "body"
          description: "Data"
          required: "name"
          type: "object"
          type: string
        responses:
            "204":
                description: successful operation
        """

        global cache
        try:
            data = await request.json()
        except Exception as e:
            print(e)
        time = time.time()
        key = data['name']
        bit = round(float(data['temperature']), 2)
        voltage = data['angle']
        ph = data['battery']
        cache[key] = {'Temperature': bit, 'Angle': voltage, 'Battery': ph}

    @request_mapping(path='/gettemp/{SpindleID}', method="POST", auth_required=False)
    async def get_fermenter_temp(self, request):
        SpindleID = request.match_info['SpindleID']
        sensor_value = await self.get_phSensor_sensor(SpindleID)
        data = {'Temp': sensor_value}
        return web.json_response(data=data)

    async def get_phSensor_sensor(self, iSpindleID=None):
        self.sensor = self.sensor_controller.get_state()
        for id in self.sensor['data']:
            if id['type'] == 'phSensorADS1x15':
                name = id['props']['Data Type']
                if name == iSpindleID:
                    try:
                        sensor = id['props']['FermenterTemp']
                    except:
                        sensor = None
                    if sensor is not None:
                        sensor_value = self.cbpi.sensor.get_sensor_value(sensor).get('value')
                    else:
                        sensor_value = None
                    return sensor_value
def setup(cbpi):
    cbpi.plugin.register("phSensorADS1x15", phSensorADS1x15)
    # cbpi.plugin.register("iSpindleEndpoint", phSensorEndpoint)
    pass
