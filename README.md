# machine-state-tracker
### Name: Chinmayee Tandon
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

<b>c. Class Structure and Roles:</b> Subject, Observer, Machine and Employee are the four classes made:<br>
<b>1. Subject:</b><br>
This is the base class. As per the assessment, machines are the subjects where name represents the name of machine, state represents the state of the machine and observers is the list of all the observation registered to the machine.<br>
<b>2. Machine:</b><br>
It can be referred as a sub-class of Subject class whose state changes during production cycles.<br>
<b>3. Observer:</b><br>
It is a base class for observers that wants to receive an update from the subject. It only stores a name and requires a sub-class to implement update method.<br>
<b>4. Employee:</b><br>
It is a sub-class of the observer class that receives real-time notifications when the state of a subject changes. It overrides the update() function to print useful information.<br><br>

<b>d. OOPs Concepts Used:</b><br>
<b>1. Inheritance:</b><br>
Classes reuse functionality from the parent class. The Machine class is inherited from Subject class and Employee class inherits from Observer class.<br>
<b>2. Polymorphism:</b><br>
update() function is defined in Observer class but overridden in Employee class so that each employee reacts uniquely to machine state changes.<br>
<b>3. Encapsulation:</b><br>
Each object manages its own state through functions like setState() rather than exposing variables directly.<br>
<b>4. Abstraction:</b><br>
Complex logic is hidden behind simple interfaces. Observers only call update() function, and subjects only call notifyAllObservers function, without knowing the inner workings of each class.<br><br>

<b>e. Implementation:</b><br>
Each instance in the system updates its internal state through a simulated cycle, and whenever a change occurs, all registered observers are automatically notified. Notifications include the machine’s name and its updated operational state, allowing the system to mimic live production-line behaviour. The communication flow is event-driven, reducing the need for continuous polling and improving efficiency.<br><br>

<b>f. Summary:</b><br>
Simulation successfully applies to the observer design pattern, allowing employees to remotely monitor machine activity in real time. The machine acts as a subject while employees or managers act as observers who receives these updates. This design ensures clean separation of responsibilities, scalability for machines and observers and a clear visibility into operational performance.
