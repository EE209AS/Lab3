# EE 209AS Lab3 -- Human-Robot Interaction Music Controller

## Introduction
In this lab, we extend the control of our Simple Mechanical Pianist to the environment input. When the user issues Start and Stop , the control or output of the motor is based on the two sensors connected to our system. The two sensors are the Ultrasonic Distance Sensor and a potentiometer.The ultrasonic sensor can measure the distance of the object in front of it. We use this sensor as a switch. When the human is within 2 meters of the sensor/system, then this action will trigger the servo on one Edison(1) to start work and play music. The Potentiometer control the tempo of the servo. When user twist it to higher level, the servo connected on the other Edison(2) will increase its frequency. Also, the user can view the whole system's real-time distance information gathered by the Ultrasonic Distance Sensor and the potentiometer voltage output. The data are ploted into a graph to show the distance change and the tempo . 


## Team Green
* Gautham Adireddy 
* Shubham Agarwal
* Yingnan Wang
* Sherman Wong

## Demo
Please follow this link to checkout our video demo of the pianist [EE209AS Team Green Lab2 Demo video](https://www.youtube.com/watch?v=RMPjr53c3U0)

* WebPage
![WebPage](https://github.com/EE209AS/Lab2/raw/master/Images/1.jpg)
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
  
  
### System Communication Setup
  Since we are controlling two motors & edisons tapping simultaneously, we implemented a "double server" approach to achieve double command. Each time we issue and command on Lab2.html webpage, it will issue two http request (POST or GET) to each edison board. Our goal is to serve a beautiful frontend webpage while providing a dynamic, executing linux CLI commands web interface. Additionally, we don't want to introduce much system overhead on the edison board and reduce computation complexity. So eventually we go for a simple TCP level server, instead of installing web frameworks like Apache or Express or Django sort of. To ensure development efficiency, we programmed two servers, one running on port 8080, serving static html and css/js contents, while the other running on port 8000, accepting post request which execute CLI commands on edison's linux -- the latter one ("Server/server.py") is of great essence to our work, feel free to check it out. Basically it try to execute the C programm song.out on edison and terminate it by grabbing the PID of the subprocess and kill it directly.  
  As long as the network latency is small, we can assure a fair enough level of concurrency of two motors, and thus guaranteee the quality of the music. We also made a video demo of our work and uploaded it on YouTube.
  
  Note: One limitation of the web interface is that the edison and user host should exist under the same subnet, thus without setting up DNS for edison, we need to specify the IP address of each edison each time we log into it -- this feature is illustrated on our webpage, remember to type in 2 edisons' IP address for sucessful redirection. 
  
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
For future usage, we can create a web-based remote control robot band with each members playing different instruments so that musicians don't need to travel far to attend a concert. 


