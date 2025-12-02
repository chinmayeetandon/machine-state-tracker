# machine-state-tracker
## Aim: Real-time remote monitoring of machine operational states in a production line.

## Description:
<p>A production line is composed of many machines that sequentially manipulate material flowing through the process, resulting in a finished product. Machines situated within a process can be in one of the following operational states:<br>
<b>PRODUCING:</b> The machine is currently working.<br>
<b>IDLE:</b> The machine is waiting for work.<br>
<b>STARVED:</b> There is no material available for the machine to complete its work.<br>
Production managers and technicians would like to view the state of machines remotely in real-time, to ensure that production is running smoothly.</p>

## Solution:

<b>a. Programming language</b> used: Python<br><br>
<b>b. Libraries used:</b> random, time<br>
These libraries are used to simulate unpredictable machine behaviour by slowing down the output such that simulation looks more realistic.<br><br>

<b>c. Method Solving Approach:</b> Subject, Observer, Machine and Employee are the four classes made:<br>
<b>1. Subject:</b><br>
This is the base class. As per the assessment, machines are the subjects where name represents the name of machine, state represents the state of the machine and observers is the list of all the observation registered to the machine.<br>
<b>2. Machine:</b><br>
It can be referred as a subclass of Subject class whose state changes during production cycles.<br>
<b>3. Observer:</b><br>
It is a base class for observers that wants to receive an update from the subject. It only stores a name and requires a sub-class to implement update method.<br>
<b>4. Employee:</b><br>
It is a subclass of the observer class that receives real-time notifications when the state of a subject changes. It overrides the update method to print useful information.<br><br>
