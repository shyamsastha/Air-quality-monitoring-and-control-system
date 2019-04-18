# Connected Devices Project Spring 2019
## Concept: In-home Air Quality Monitoring with support for Air Conditioning and Humidification
##### This repository contains the final project for connected devices Spring 2019 Semester by Shyama Sastha Krishnamoorthy Srinivasan
### Purpose and methodology
* To provide a simple in-home automatation system using the IoT platform.
* This system can help in monitoring and controlling the air conditioning system and the humidifier.
* The necessary environmental variables like temperature, pressure, and humidity are obtained from the sensors.
* Sensors are part of the senseHAT that runs on the Pi 3B+ module to actively collect data through the GPIO ports.

### Working Principle
![Diagram](https://bitbucket.org/shyamasastha/connected-devices-project/src/9bc7820e005a/?at=master)

* It can be observed from the above diagram that this project follows a simple IoT system topology
* There are 3 different parts of the IoT ecosystem:
	* [Constrained Device](#constrained-device)
	* [Gateway Device](#gateway-device)
	* [Cloud](#cloud)
* Each part of the ecosystem has its importance and cannot perform their best without the other.

#### Constrained Device
* The foundation of the IoT ecosystem, which interacts with the local environment to obtain data for analysis.
* The data obtained from the sensors is forwarded to the gateway device through mqtt for pushing into the cloud.
	* This happens periodically for the set time interval and waits for the data to be anaylsed and ready to actuate (display critical information).

#### Gateway Device
* This part of the ecosystem acts as the middle man that pushs the data to the cloud.
* It also helps in alerting the user based on critical information obtained after processing from the cloud.
	* Sending data to the cloud happens in regular periods through https connection through a cloud API.
* Once the data is processed in the cloud, it recieves the processed information to either activate the actuator or alerting the user.
* The actuator coexists as part of the constrained device. It is called upon from the gateway to perform the action.
* The action performed is then notifed to the constrained device's LED system to display critical information.

#### Cloud
* This is the final piece in the puzzle that helps the local system connect with the internet for secure data storage.
* It obtains the data from the gateway through http. It has events that process the data and triggers system and control values.
* The system and control values are regularly checked by the gateway device that subscribes to those variables at the setup phase.
	* These values performs an important role in deciding the actuation processes.

### Instructions to run the project
#### The instructions below are given under the impression that you are running this project on Raspberry Pi 3 B+ (RBPi3B+) with a senseHAT. You must also have the latest version of git, ubidots cloud API, paho-mqtt and have updated the Raspberry Pi 3B+ to its latest version.
* Create directory called `git` under the home folder of your RBPi3B+.
* Open the git folder in command line and perform a git clone of this repository.
* After successful cloning, please run `python3.5 AirQSensorApplication.py`.
* The program will start running and you can close it anytime you want by pressing `CTRL+C` twice.

That should be it. You've got yourself a simple IoT based Air Quality monitoring system with controls for air conditioning and humidification. Have fun!!

> It is important to never forget to learn but also equally important to not forget why one found that particular concept interesting to learn.
> - An avid learner