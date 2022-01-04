![](https://img.shields.io/badge/CBPi%20addin-functionable_for_V4-green.svg)  ![](https://img.shields.io/github/license/JamFfm/cbpi4-phMeasure-ADS1115.svg?style=flat) ![](https://img.shields.io/github/last-commit/JamFfm/cbpi4-phMeasure-ADS1115.svg?style=flat) ![](https://img.shields.io/github/release-pre/JamFfm/cbpi4-phMeasure-ADS1115.svg?style=flat)

# PHMeasureADS1115 add-on for CraftBeerPi 4
# This is draft Text do not take for granted
# This text will be updated as soon as the plugin is ready

*CraftBeerPi4* sensor for measuring ph values.
Using the ADS115 A/D via I2C connection


# How to Install

### 1. I2C activation:  ###
Ensure you have activated the I2C connection in the Raspi Configurations:

![Test Graph](https://github.com/JamFfm/cbpi-PHMeasure-ADS1115/blob/master/IC2Einstellungen.jpg "I2C")

### 2. Software installation: ###

#### 2.1 Software installation via pypi (recommended but not functional jet) ####

This is the official installation via PyPI like Manuel83 (the Cbpi developer) intended.\
Do not generate a folder for the plugin as it is generated by the code.


Type in 
```python
sudo pip3 install cbpi4-phMeasure-ADS1115
sudo cbpi add phMeasure
```
The plugin will be installed in:
```python
/usr/local/lib/python3.7/dist-packages/cbpi4-phMeasure-ADS1115/*
```

<br />

#### 2.2 Software installation version1 (for developers) ####
Navigate in the Linux console to the folder from which you start cbpi4.
Usually like: cd /home/pi/cbpi4........
Do not generate a folder for the plugin as it is generated by the code.\
Then execute the commands in the raspi command box assuming you are user pi:

```python
cd /home/pi/cbpi4  # subtitude /cbpi4 with your folder where you start cbpi. In this folder run the following commands
sudo cbpi create cbpi4-phMeasure-ADS1115
sudo chown -R pi cbpi4-phMeasure-ADS1115
sudo pip3 install -e ./cbpi4-phMeasure-ADS1115
cbpi add phMeasure
sudo rm -r cbpi4-phMeasure-ADS1115/
sudo git clone https://github.com/JamFfm/cbpi4-phMeasure-ADS1115

```
What does the code? It installs a default plugin named cbpi4-phMeasure-ADS1115. During installation several registrations are made. The folder cbpi4-phMeasure-ADS1115 is deleated, and the new folder is generated by the clone process.


In the log when starting cbpi4 you hopefully will notice that cbpi4-phMeasure-ADS1115 started without errors.
Your user has to have permissions to write in the filesystem. This is usually the case when you use user pi.

<br />

#### 2.3 Software installation version2 (for developers) ####

There is another way to install like:
```python
sudo pip3 install https://github.com/JamFfm/cbpi4-phMeasure-ADS1115/archive/main.zip
cbpi add phMeasure
```

but this one installs in 
/usr/local/lib/python3.7/dist-packages/cbpi4-LCDisplay/*
This is not handy if you need to assess the code.
I do not recommend now. But this is the desired folder to install via pip package.
Please do not mix the possibilities to install.

<br />

#### 2.4 Delete plugin ####

Navigate in the Linux console to the folder from which you start cbpi4.
Usually like: cd /home/pi/cbpi4........
Then execute the commands in the raspi command box:
```python
sudo pip3 uninstall cbpi4-phMeasure-ADS1115
sudo cbpi remove cbpi4-phMeasure-ADS1115
```



# What for?

The pH has got an influence on the beer taste. Please inform yourself in the literature.
Usually the mash will be between 4.5pH and 5.8pH.

>**The target pH for the mash usually should be between 5.3pH and 5.7pH**

Therefore, it is important to know the pH of the mash.

German link to ph in Beer

- https://www.maischemalzundmehr.de/index.php?inhaltmitte=exp_maischph
- Please translate it via browser translate function.

# Advantages

- Works much more stable/precise like the MCP3008 IC Module.
- I2C connection is very easy to handle. 
- The driver is build in. No need to install software modules.
- Add ADS on the CBPi Extensionboard 3 (just solder ADS, levelshifter and connect probe board with screwterminals)
- With Extensionboard 4 just use the srew-terminals for flowmeter
 
# The probe and board for this Craftbeerpi 4 addon

at ebay
- https://www.ebay.de/i/322935814230?ul_noapp=true

but there are same in Aliexpress.
Search for this: "Liquid PH Value Erkennung Detect Modul +BNC Electrode Probe for Arduino"


![Test Graph](https://github.com/JamFfm/cbpi4-PHMeasure-ADS1115/blob/master/PHSet.jpg "set")

**The probe board is an analog sensor. RaspberryPi can read only digital sensors.
Therefore, you need an analog/digital converter like the ADS1115 (16Bit)**

![Test Graph](https://github.com/JamFfm/cbpi4-PHMeasure-ADS1115/blob/master/ADS1115.jpg  "Pins of ADS1115")
  
# How to connect

![Test Graph](https://github.com/JamFfm/cbpi4-PHMeasure-ADS1115/blob/master/WiringADS1115_Steckplatine.png "Example wiring")



## Connect I2C

To connect the ADS1115 to the Raspberry Pi use the following connections:

- ADS GND   to RASPI GND 
- ADS VDD   to RASPI 5v 
- ADS SCL   to RASPI SCL (daisy-chain possible), put a level shifter 5v/3.3v inbetween because the Raspi pins can only stand 3.3v
- ADS SCA   to RASPI SCA (daisy-chain possible), put a level shifter 5v/3.3v inbetween
- Address   have a look at the specs of ADS1115 for changing address, put a level shifter 5v/3.3v inbetween
- Alert     have a look at the specs of ADS1115 for Alert events, put a level shifter 5v/3.3v inbetween
- A0        to Po of the PhMeasure Board. 

Please have a look here:

http://www.netzmafia.de/skripten/hardware/RasPi/Projekt-ADS1115/index.html

![Test Graph](https://github.com/JamFfm/cbpi4-PHMeasure-ADS1115/blob/master/RaspiGPIOI2C.jpg "Example wiring, have a look at wiring I2C")



# Board description

![Test Graph](https://github.com/JamFfm/cbpi4-PHMeasure-ADS1115/blob/master/probeboard.jpg "powerampfilter")



* BNC plug: Where you put the probe. It seems to work with any probe with a calibration difference.

* Pin To: Should be the temperature, but I can't make it work.
* Pin Do: High/Low 3.3v adjustable limit.
* Pin G/GND: Probe ground. It may be useful when the ground is not the same as your Raspi. In fact, I use the ground of the Raspi.
  In some circumstances the ground voltage of the liquid to measure can be different.
* Pin G/GND: Power ground (ex. Raspi).
* Pin V+/VCC: Input power 5V DC (direct from Raspi).
* Blue potentiometer close to BNC: pH offset.
* Blue potentiometer close to pins: limit adjustment.
* Black component with 103 printed (not the one between potentiometers): thermistor for temperature compensation.

# Calibration: 

Steps for Calibration:
1. Adjust the offset
2. Get the voltage at pH 4.01
3. Determine the factor to calibrate the sensor
4. Key in your factor in the Hardware Section

## 1. Offset (volt7)
Remove the probe (disconnect BNC) and do a short circuit between the small BNC hole and the external part of BNC. Use a wire to do that.

Put a voltmeter to measure the voltage between probeboard GND and probeboard Po. 
Adjust the pot (close BNC) until the output is nearest to 2.5v. Keep this value(=volt7) for calibration later on.

## 2. Get the voltage at pH 4.01 (volt4)
Put the probe in a ph 4.01 liquid and measure the voltage between probeboard GND and probeboard Po. 
Keep this value(=volt4) for calibration later on.

## 3. Get the factor (pH_Step)
Place one of the 3 possible sensor types (V, Bit, Ph) on the dashboard.
Configure Action to yes.
Save the configuration.
If you push the 3 dots button, you get a window to key in the volt7 and volt4 values.
The factor is shown in the next window.
If you do not key in values in the fields, the default value is volt7=2.5 and volt4=3.05.

![Test Graph](https://github.com/JamFfm/cbpi4-PHMeasure-ADS1115/blob/master/calibrate.jpg "Window Calibrate")

![Test Graph](https://github.com/JamFfm/cbpi4-PHMeasure-ADS1115/blob/master/Factor.jpg "powerampfilter")

## 4. Key in the factor in the hardware section of the pH sensor
The factor is the same für all 3 possible sensor types but please key in for every possible Sensor types.
This is done in the hardware section where you add a ph sensor.

![Test Graph](https://github.com/JamFfm/cbpi4-PHMeasure-ADS1115/blob/master/Hardware.jpg "powerampfilter")

## The Factor explanation (you can skip this)

The ADS 1115 has got 16Bit precision.

16 Bit = 32767 possible values between 0V and Gain maxV and 32767 possible values between -Gain maxV and 0V.
We assume there is a voltage measurement while shortcut and second a voltage measurement while measuring pH 4.01 buffer.
See below at end of this text for more explanations.

Assuming voltage@PH7 = 2.5 V and voltage@PH4.01 = 3.05 V
with gain 1 (+-4.096V)

voltage = measure * 4.096 / 32768 ; //classic digital to voltage conversion

PH_step = (voltage@PH7 - voltage@PH4.01) / (PH7 - PH4.01) = (2.5-3.05) / (7-4.01) = (-.55/2.99) = -0.1839....

PH_probe = PH7 - ((voltage@PH7 - voltage@probe) / PH_step)

phvalue = 7 + ((2.5 - voltage) / **0.1839** )

0.1839 is the factor in this case. You have to adopt it for your equipment


# Sensor Usage

Use this sensor as any other sensor in Craftbeerpi 4.
The Digit and Voltage values can help to calibrate. They are not needed for pH measurement.
The main calibration is already described above and more precise at the end of this file. 

Keep in mind that it takes several minutes to get the right pH value.

When using in the rotating mash no stable values are shown but in a probe of mash (ex. a glass) it is stable.
My measured Values matched with another pH measurement tools.

According to the parameters of the probe it can be situated in max 80 °C liquid but not for longtime.
I never tried that until now.

# Parameter (old picture)

![Parameter](https://github.com/JamFfm/cbpi4-PHMeasure-ADS1115/blob/master/Hardware.jpg "Example Parameter")


## Name
Text as you want. Maybe like "pH Sensor".

## Type
Name of the pH Sensor Module to be selected from the list of sensors: PHSensorADS1x15

## ADS1x15 Address
This is the I2C address of the ADS module.
**Default ist 0x48.**
If there are two or more I2C modules with the same address you can choose a different address.
This means you have to solder connections differently. Have a look in the ADS1x15-datasheet.
This parameter is rarely used. So in most cases entering 0x48 will do it.

## ADS1x15 Channel
This is the channel you want to read. There are up to 4 channels called A0-A3.
You have to connect the sensor to one of the channels.

## ADS1x15 Gain
This is the amplifier of the ADS module.
These are the selectable ranges:

For example: Choose a gain of 1 for reading voltages from 0 to 4.09V (ok it is -4.096V to +4.096V bit negative values are scipped for now :-)).
**Gain 1 will be the right parameter for the pH probe.**

Or pick a different gain to change the range of voltages that are read:
- 2/3 = +/-6.144V     we use 0 for this range
-   1 = +/-4.096V
-   2 = +/-2.048V
-   4 = +/-1.024V
-   8 = +/-0.512V
-  16 = +/-0.256V

See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.

If you have no idea, enter 1

## Data Type

- **Digit:**  
    This shows the value of the ADS 1115 and runs from 0-32767.
    This is the basic of all measurement.



- **Voltage:** 
    This shows the calculated value of the Voltage measurement.
    It depends on the Gain selected.

    Example: Gain 1 = +/-4.096V

    Voltage = ((4.096V * Digit) / 32767) - offset

    This means 32767 digit is equal to 4.096V.

    Why only 32767? Because there are another 32767 values of the negative numbers. We only deal with the positive number range.

    Check it by this: Put a voltmeter to measure the voltage between GND and Po.
    PH ist calculated by voltage, so it should be checked with voltmeter.



- **pH Value:** 
    This shows the calculated value of the pH measurement.

    
## Factor

+ Key in the factor you calculated via action Button in dashboard  
![Parameter](https://github.com/JamFfm/cbpi4-PHMeasure-ADS1115/blob/master/Factor.jpg "Example Parameter")

# Hint

You can easily change the addon for different analog sensors.

There are only some lines to change. 

I use the ADS1115 in a CraftBeerPi Extensionboard 3 in combination with a level shifter
At CraftBeerPi Extensionboard 4 there is a build in ADS1115.

# Known Problems

- When using in the rotating mash, no stable values are shown 
- Wrong spelling in this readme
- No temperature calibration, buffer ist calibrated to 25 °C, so probes should also habe 25°C
- Unreliable probes. I bought 3 probes. Only one shows stable values. One is useless and one shows fairly credible values.
- Never let dry the probe

# Support

Report issues either in this Git section or at Facebook at the [Craftbeerpi group](https://www.facebook.com/groups/craftbeerpi/)

# Most helpful links:
## All information on this side comes from the following links

I got all my knowledge from these links:


- http://www.netzmafia.de/skripten/hardware/RasPi/Projekt-ADS1115/index.html
  
  Used this for the libs and classes
 

- https://forum.arduino.cc/index.php?topic=336012.0 

  last post first page, for understanding probe in general


- https://www.botshop.co.za/how-to-use-a-ph-probe-and-sensor/

  additional info
  
  
- https://raspberrypi.stackexchange.com/questions/96653/calibrate-ph-4502c-ph-meter


# Calibration more explanations

## The offset

The **offset** is the shifting of all pH values to a specific voltage range. If a pH 7 output a voltage of 2.2v and pH 8 a voltage of 2.1v, then a shift of +0.3v move the pH 7 to 2.5v and the pH 8 to 2.4v. 


The offset can be done on the board or via software, but it's probably easier on the board because it's probe independent and there are less programming to do.


Connect GND (both) of the probeboard to Raspi GND and probeboard Vcc to Raspi 5v. Please use a levelshifter to avoid damage at the GPIO which only support 3.3v. 

Remove the probe (disconnect BNC) and do a short circuit between the small BNC hole and the external part of BNC. Use a wire to do that. 

Put a voltmeter to measure the voltage between probeboard GND and probeboard Po. Adjust the pot (close BNC) until the output is nearest to 2.5v. 

Now the pH 7 have an exact value of 2.5v (or what you measure) because the probe will output 0 millivolt.

In my case I could only lower voltage to 2.548V. 

## The steps

Now you need one or more buffer solutions depending on the range and precision you want. Ideally you should know the range of the measure you want to do with your system. 

I use upcoming beer between pH 5 and pH 7. Therefore, I choose the buffer 4.01 (and 6.86 to verify). If you usually measure pH between 8 and 10 choose buffer 9.18 (eventually 6.86 to verify).


Connect the (clean) probe and put it in the buffer, let it stabilize for a minute. You know it's stable when it goes up and down (e.x. 3.04 then 3.05 then 3.03 then 3.04). Take note of the voltmeter value. At this Example it comes out at 3.05V at 4.01 pH buffer.

## Unit per step

The PH_step calculation is quite simple. You take the difference between the two known voltage, in my example 2.5v@pH7 and 3.05v@pH4.01 which is -0.55v. 

It's the voltage range equivalent of the pH range from 7 to 4.01, which is 2.99 pH units. A small division of the voltage by pH units gives you a volts per pH number (0,1839... in my case).

The PH_probe is calculated by taking the known pH 7 voltage (2.5v) where we add some PH_step to match the probe voltage. This means that a pH of 8 have a voltage value of 2.5v (pH 7) + 0.1839 (1 unit/step); pH 9 then is 2.5v + 0.1839 + 0.1839 = 2.87v.

To determine the Unit per Step (=PH_step in formula) is important to know.

## Finally, the code

The ADS 1115 has 16Bit precision.

16 Bit = 32767 possible values between 0V and Gain max V and
32767 possible values between -Gain max V and 0v

With gain 1 (+-4.096V)

voltage = measure * 4.096 / 32768 ; //classic digital to voltage conversion

PH_step = (voltage@PH7 - voltage@PH4.01) / (PH7 - PH4.01) = (2.5-3.05) / (7-4.01) = (-.55/2.99) = -0.1839....

PH_probe = PH7 - ((voltage@PH7 - voltage@probe) / PH_step)

phvalue = 7 + ((2.5 - voltage) / *0.1839* )
