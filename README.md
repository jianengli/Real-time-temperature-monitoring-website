# Real-time-temperature-monitoring-website
A real-time temperature monitoring website based on Raspberry Pi, temperature sensor, Python, PHP and html5
## Table of Contents

- [Background](#background)
- [LiveDemo](#livedemo)
- [Prerequisites](#prerequisites)
- [RunningTheTests](#runningTheTests)
- [Maintainers](#maintainers)

## Background
This is an assignment from IK2018:https://www.du.se/en/study-at-du/kurser/course/?code=IK2018

An imagined this case: You have a mountain cabin and are afraid that the indoor temp will be so cold that water pipes freeze. You are also afraid that it is so hot inside that the electrical elements in the cabin may be wrong. Now you want live data presented in a web page to be able to see in diagram form measured temperatures in the cottage. You want to get an email if the temperature drops below and exceeds certain temperature values so you can go up to the cabin to check out what may be wrong. For example, if it is 25 celsius outside and the sensor detects 36 inside then it is probably just wrong on the sensor or it’s  some konc of fire:-(. But if it shows 28 celsius inside then it is probably wrong with the colding in the cabin and an email should be sent.

## LiveDemo
- [Live demo](http://users.du.se/~h19jiali/Github_video/live_demo.mp4)

## Prerequisites
In this project, you need hardware: Raspberry Pi, temperature sensor and you also need to install Python 3, php and html5.
1. Install apache web server and PHP on the rpi device.

1.1 https://www.raspberrypi.org/documentation/remote-access/web-server/apache.md.

1.2 Set permissions for the device on the web server's www directory 1.3 Create a folder called lab5 and set permissions for this folder as 'anyone'.

2. Change the config file so we can use the tempratur sensor.
Read more about the above in https://docs.devicehive.com/docs/raspberry-pi-and-temperature-sensor.

## Running The Tests
1. First, connect the Raspberry Pi to the temperature sensor and turn on the power.
2. Second, put the code in www directory.
3. Finally, open 130.243.35.86/lab5/ShowTheTemp.html through the browser and run obtainWeatherInfo.py, we can see that highchart updates the temperature data every 5 minutes. At the same time, in the temperature center, we can receive an email if the sensor fails

## Maintainers
[@Jianeng](https://github.com/tommyLi66).
