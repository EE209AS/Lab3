# EE 209AS Lab2 -- Simple Mechanical Pianist

## Introduction
The pianist is controlled by two motors, each further controlled by an Edison board. The rotation angle of motor's blade is determined by the pulse width output from edison's PWM interface.  
User are able to control the motor to play music on a remote host by logging into the webpage on Webpage/Lab2.html via Browser, select the song he wanna play and click "start" button to play; click "stop" to stop playing, and click "tempo" to accelerate the speed of play -- note that the 4th time clicking on this button will set to the initial speed. Currently we only support 2 songs, each music score is pre-installed on the edison board.

## Team Green
* Gautham Adireddy 
* Shubham Agarwal
* Yingnan Wang
* Sherman Wong

## Demo
Please follow this link to checkout our video demo of the pianist [video]()

## Things Needed
1. Two Intel Edison boards  
2. Four Micro USB cables  
3. Two Servo motors
4. Computer running music software  
5. Stable local area network(LAN)  


## How It Works
### Servo Control
  The servo in our work is TowerPro SG90 [reference](http://www.micropik.com/PDF/SG90Servo.pdf), which provides 1 DOF rotation with fixed speed. The edison board need to be installed with Yocto linux first, together with the arduino breakout board we are able to use the edison's MRAA library to output the PWM signals to the servo. The method we use to tune the tempo of tapping is to modify the delay between pulses, hence change the interval of each tap.  
  We have included two "music files" -- "Song1.out" and "Song2.out" which control the motion of the motor using the PWM so as to hit the keys on the keyboard. And we have pre-setup and position and orientation of the servo so that when it rotates it can hit the keyboard precisely and in the desired frequency.   
### System Communication Setup
  Since we are controlling two motors & edisons tapping simultaneously, we implemented a "double server" approach to achieve double command. Each time we issue and command on Lab2.html webpage, it will issue two http request (POST or GET) to each edison board. Our goal is to serve a beautiful frontend webpage while providing a dynamic, executing linux CLI commands web interface. Additionally, we don't want to introduce much system overhead on the edison board and reduce computation complexity. So eventually we go for a simple TCP level server, instead of installing web frameworks like Apache or Express or Django sort of. To ensure development efficiency, we programmed two servers, one running on port 8080, serving static html and css/js contents, while the other running on port 8000, accepting post request which execute CLI commands on edison's linux -- the latter one ("server.py") is of great essence to our work, feel free to check it out. Basically it try to execute the C programm song.out on edison and terminate it by grabbing the PID of the subprocess and kill it directly.  
  As long as the network latency is small, we can assure a fair enough level of concurrency of two motors, and thus guaranteee the quality of the music. We also made a video demo of our work and uploaded it on YouTube.
  
  Note: One limitation of the web interface is that the edison and user host should exist under the same subnet, thus without setting up DNS for edison, we need to specify the IP address of each edison each time we log into it -- this feature is illustrated on our webpage, remember to type in 2 edisons' IP address for sucessful redirection. 
  
  
## Scope


