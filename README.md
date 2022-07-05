### 5G-OMLOX_NotHalt
A PoC for using Geo-fences in Omlox localized area to dynamically control the behavoiur of 5G connected devices

# Introduction

This python program use the Websocket protocol as a client to fetch data from a locaization system. WebSocket protocol is a TCP - based network protocol which is designed to establish bidirectional connection between a
web application and a WebSocket server or a web server that support websockets.

## Installation and configuration

You can use either 

`python3 setup.py install`

or 

`pip3 install webSocket to install`


This module is tested on Python 3.9.6

There are other dependencies that has  to be installed to run the code.
In this code we will be working with json files, so we need to install  json library `pip install jsons`

We need asyncio module which provides infrastructure for writing single-threaded concurrent code using coroutines, 
multiplexing I/O access over sockets.`pip install asyncio`

## Steps
1. Make sure you started the Omlox-Localization-System

2. Connect your SBC/PC or System to the omlox server using WLAN/LAN 

3. Using the given address we can access the omlox server 

    `ws://192.168.8.1:8090/json/device/all/position`
 
   the ip address can be changed using the admin access. So before, running the code check the ip address in the code.

4. Run the code

## Following zones (areas in the lab) are defined with respect to coordinates:

here x is the realtime coordinates which the client reads from the omlox system and the defined values are the boundries of each area
- Cyber-Physical Plant area:

   x <= 2.400
   
- Working-place zone:

   x > 2.410 and x <= 8.100
   
- Creative room zone:

   x > 8.200 and x <= 10.000
   
- Out of Lab zone

   y < 0

### Note
The data obtained from the omlox system was in string format. It had [] in the start and end of the string. when it was 
converted into json, its type was changed to list. Because of this accessing the obtained data became difficult. So 
before converting sting to json, the [] was removed.
For removing that, we use the function lstrip as following:

 `objects = response.lstrip("[").rstrip("]")`.

After this, it was possible to access the dictionary. 
