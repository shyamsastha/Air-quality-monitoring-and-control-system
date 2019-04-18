'''
Created on April 12,2019
Simple Python script for running the Air Quality Management Application
@author: Shyama Sastha Krishnamoorthy Srinivasan
'''

from time import sleep
import sys
from AirQSensorAdaptor import AirQSensorAdaptor
from AirQSensorGateway import AirQSensorGateway

#initiating the adaptor
airqsensorGateway = AirQSensorGateway("AirQuality")
airqsensorAdaptor = AirQSensorAdaptor("AirQuality")

#enabling the adaptor
airqsensorGateway.enableAdaptor = True
airqsensorAdaptor.enableAdaptor = True

#starting the thread
airqsensorGateway.start()
airqsensorAdaptor.start()

#condition for the infinite loop
if __name__ == '__main__':
    try:
        while (True):
            sleep(1)
            pass
    except KeyboardInterrupt:
        print('Program closed!!')
        sys.exit(0)
