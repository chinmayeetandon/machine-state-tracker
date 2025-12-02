# machine-state-tracker
Real-time remote monitoring of machine operational states in a production line.

## Description:
<p>A production line is composed of many machines that sequentially manipulate material flowing through the process, resulting in a finished product. Machines situated within a process can be in one of the following operational states:<br>
PRODUCING: The machine is currently working.<br>
IDLE: The machine is waiting for work.<br>
STARVED: There is no material available for the machine to complete its work.<br>
Production managers and technicians would like to view the state of machines remotely in real-time, to ensure that production is running smoothly.</p>

# Solution:

a. Programming language used: Python
b. Libraries used: random, time
   These libraries are used to simulate unpredictable machine behaviour by slowing down the output such that simulation looks more realistic.

c. Subject, Observer, Machine and Employee are the four classes made:
   1. 
