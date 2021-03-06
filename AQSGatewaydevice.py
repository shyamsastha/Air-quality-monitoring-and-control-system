'''
Created on April 12,2019
Simple Python script for running the Air Quality Management Gateway Device Application
This can be used as a standalone application that has to be run in parallel with another App.
@author: Shyama Sastha Krishnamoorthy Srinivasan
'''

from project.AirQSensorGateway import AirQSensorGateway
from time import sleep

#initiating the adaptor
airqsensorGateway = AirQSensorGateway("AirQuality")

#enabling the adaptor
airqsensorGateway.enableAdaptor = True

#starting the thread
airqsensorGateway.start()

#condition for the infinite loop
while (True):
    sleep(1)
    pass