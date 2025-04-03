# Matilda - Robotic chess across the internet


This project incorporates mechatronic control, through a Pi5 and six servos, as seen below by the high-level schematic.
Internetworking will allow the remote player to make moves against the robot. This will be displayed by a Pi vision camera.
The chess engine will utilize the chess bots from chess.com (Stockfish) and object detection (YOLO) to 'see' pieces.

The motivation of this project is to one day play chess with my daughter Florence remotely. Roald Dahl's Matilda
inspired me as a young child, in an attempt I hope to do the same.

![IMG-20250403-WA0000](https://github.com/user-attachments/assets/9093c39c-3aeb-4760-bead-17b0a86b5c7f)
The files attached are the starting point for this project. 
Code and STL files, staye tuned... 

# progression list to date.
1. All items have been procured.
2. The robotic arm has been selected and alterd from the original repository. 
3. Established a 'here and there' netword using my home PC and a VM. This is to establish a internetworking connection.
4. Print the 3D printed arm and test the proto type.

# Prototyping
A modern frame work that may work well for data and internetworking is Flask. 
Flask will handle web requests, allowing a remote user to interact with the chess game interface over the internet. Using Flask-SocketIO, I can implement WebSockets for real-time communication, ensuring instant moves between the player and the robot. Flask will interface with the robot arm's control API to execute moves physically. The architecture will involve Flask serving the web interface and receiving move commands, which are then sent via WebSockets to the robot controller. The robot's state and moves can be streamed back to the user, ensuring synchronized play.
The diagram below, could be a great starting framework for application!
![image](https://github.com/user-attachments/assets/80b30776-29fb-4ce6-8b74-d685594c7be4)


The basic highlevel schematic below will be a starting point for prototyping. This project, elctro-mechanically.
At some stage i may need to introduce a servo driver with multi-channel capability, if threading causes delays.
![alt text](image.png)

The capture below is the complete and updated robotic arm. This repository came from here: [text](https://howtomechatronics.com/tutorials/arduino/diy-arduino-robot-arm-with-smartphone-control/)

![Capture](https://github.com/user-attachments/assets/e8dce431-166a-4af0-a0d3-019e8ef835c1)



_Matilada Chess - Work in progress_

[back](./)
