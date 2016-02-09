# EE 209AS Lab3 -- Human-Robot Interaction Music Controller

## Introduction
In this lab, we extend the control of our Simple Mechanical Pianist to the environment input. When the user issues commands on browser, it activate the sensing-acutating system altogether. The two sensors are the Ultrasonic Distance Sensor and a potentiometer, connected to an Edison board respectively.The ultrasonic sensor can measure the distance of the object in front of it. We use this sensor to indicate human-attendance -- if a person is within 2 meters range of the ultrasonic receiver, it will trigger the servo on one Edison(1) to start playing music. The Potentiometer control the tempo of the servo. When user twist the knob to higher level, the servo connected on the other Edison(2) will increase its frequency. Also, the user can view on browser remotely the whole system's real-time distance information gathered by the Ultrasonic Distance Sensor and the potentiometer voltage output. The data are ploted into a graph to show the distance change and the tempo . 
##Human Robot Interaction :
In our system, the value of the distance from Ultrasonic range sensor is being updated to the webpage in realtime. We assume that two Edison boards(Music instruments) are apart. When a user passes through the first Edison(Music Instrument), the music is played if the distance Is less than 200cm. This distance data is also streamed to the Webpage. Based on this webpage value, the musician who is controlling the second Edison connected to potentiometer can vary the user may vary the tempo of music using potentiometer The(range 0-1024) is also shown on the website. This acts like a feedback to the musician.



## Team Green
* Gautham Adireddy 
* Shubham Agarwal
* Yingnan Wang
* Sherman Wong

## Demo
Please follow this link to checkout our video demo of the pianist [EE209AS Lab3 Human Robot Interaction Music Controller Demo Video](https://www.youtube.com/watch?v=u1IBEz-Xya8)

* WebPage
![WebPage](https://github.com/EE209AS/Lab2/raw/master/Images/1.jpg)
* Real-time streaming
![Webpage](https://github.com/EE209AS/Lab3/raw/master/monitor.png)
![Webpage](https://github.com/EE209AS/Lab3/raw/master/monitor2.png)
* Online Piano
![Online Piano](https://github.com/EE209AS/Lab2/raw/master/Images/2.png)
* Edison and Servo
![Edison and Servo](https://github.com/EE209AS/Lab2/raw/master/Images/3.jpg)

## Things Needed
1. Two Intel Edison boards with breakout kits
2. Four Micro USB cables  
3. Two Servo motors
4. Connecting wires
5. Computer running music software  
6. Stable local area network(LAN)  
7. Cardboard Box
8. Ultrasonic Distance Seneor
9. Potentiometer


## How It Works
### Servo Control
  The servo in our work is TowerPro SG90 [reference](http://www.micropik.com/PDF/SG90Servo.pdf), which provides 1 DOF rotation with fixed speed. The edison board need to be installed with Yocto linux first, together with the arduino breakout board we are able to use the edison's MRAA library to output the PWM signals to the servo. The method we use to tune the tempo of tapping is to modify the delay between pulses, hence change the interval of each tap.  
  We have included two "music files" -- "Song1.out" and "Song2.out" which control the motion of the motor using the PWM so as to hit the keys on the keyboard. And we have pre-setup and position and orientation of the servo so that when it rotates it can hit the keyboard precisely and in the desired frequency.

### Potentiometer
Potentiometer is a resistor with a sliding contact that forms a voltage divider. As we rotate the knob, the contact point and hence the output voltage changes.

### Ultrasonic Sensor:
Ultrasonic sensor is a range sensor which is used to detect distance. This works on the principle of echo. We send out a trigger pulse for a duaration of time and then sample the received signal. The duration for which the received singal is HIGH gives is proportional to the distance from the object.
  
### Web Page
The web page for this lab is based on the previous lab web page and we add a graph to show the data collect from the Ultrasonic Distance Measure Sensor and the output voltage of the Potentiometer. The graph is drawed on the HTML Canvas which backgroung image has been set as a Coordinate System. We map our data to that coordinate and show user the almost real-time distance change of the Ultrasonic Distance Sensor measurement. The web page actually send data request to the server every 1 second and draw the received data. The web page can filter out the wrong data collected by the sensor and only draw the correct data. It also can auto refresh when the plot reach the end of the graph. The voltage of the Potentiometer is directly show under the graph.
  
### System Communication Setup
  We no longer setup a static http python server on edison board this time, during last testing period we found that edison provided limited network capablity, and we have decided to use Ajax style request anyway; so this time the browser's webpage is accessed locally, yet localhost need to be in the same subnet as Edison. User need to specify ip addresses of the two edison when issuing commands. Each edison' board will run a python server respectively -- the same as last lab. We let one board to collect sensor output of potentialmeter and the other to collect ultrasonic sensor. The challenging part this time is to implement the real-time streaming to sensor data to remote host. The message datapath diagram is shown below: 
![schematic overview](https://github.com/EE209AS/Lab3/raw/master/diagram.png)
In order to achieve real-time data streaming pipeline, we construct a pipe between sensor module process and server main process; on browser side, we issue ajax style xmlhttprequest every 2 seconds and collect json data from the server. Each time when user click "Start" button on browser, it will start sending xmlhttprequest continuously until "stop" is pressed. The time interval between sensor's data collection is about 1sec, so each request will estimatedly gather 2-3 samples to display. The code for this part is in server.py and webpage/lab3.html.  
Note: One limitation between this approach is that the pipe is established between server's main process and sensor process, so theoretically there's no way to control the pipe remotely using http request, due to the limitation of a simple python server. For programming efficiency, we don't consider a much complicated server approahc, and our experience on http-server programming is still limited as well. Nonetheless, for our mission a single pipe suffices.
  
###Music Instrument:
 Our music instrument is a Piano keyboard running on a Laptop as shown in the figure.[Virtual Piano](http://virtualpiano.net/).

###Setup:
1. Download the files by cloning into git repository on both the Intel Edisons. 
2. Connect the servos to Intel Edisons as shown in the picture. Orange wire to PIN 6, Brown wire to GND, Red wire to 5v. (Make sure      you  power the Edison using a powered USB hub or external power source, or else the Edison board will reboot again and again) . 
3. Place them on keyboard in a desirable position so that the motors hit the keys.
4. Connect the Intel Edison and the User machine from which the control is done to a same Network.
5. Navigate to the files containing the Source Files On Edison 1 and start HTTPServer and Python server.
   python -m SimpleHTTPServer 8080 
   python server.py 8000
6. Navigate to the files contaning the Souce Files on Edison 2 and start Python server
   python server.py 8000
7. Open the webpage by using the address of Edsion 1 on which the Webpage is hosted. Enter the IP address for each Intel Edison board.
8. Now the user can control the Music using Start and Stop buttons.


## Scope
For future usage, we can create a web-based remote control robot band with each members playing different instruments so that musicians don't need to travel far to attend a concert. Also this system can be use as the door bell. When anyone walk close to the door which installed with the Ultrasonic Sensor, the music will begin to notify the host.


