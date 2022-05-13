from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(name='phMeasure',
      version='0.0.1',
      description='CraftBeerPi4 phMeasure sensor plugin',
      author='Jan Battermann',
      author_email='Jan.Battermann@t-online.de',
      url='https://github.com/JamFfm/cbpi4-phMeasure',
      license='GPLv3',
      include_package_data=True,
      package_data={
        # If any package contains *.txt or *.rst files, include them:
      '': ['*.txt', '*.rst', '*.yaml'],
      'LCDisplay': ['*','*.txt', '*.rst', '*.yaml']},
      packages=['phMeasure'],
	    install_requires=[
      #      'cbpi>=4.0.0.33',
	          'smbus2',
      ],
      long_description=long_description,
      long_description_content_type='text/markdown'
     )
