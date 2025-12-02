"""
    Assessment 1 Task 1: Observer Pattern
    Employee Name: Chinmayee Tandon
    Employee ID: HAYS2525
"""

# Importing libraries
import random
import time


class Subject:
    def __init__(self, name):
        """Initialising """
        self.name = name
        self.state = None
        self.observers = []

    def attach(self, observer):
        """Register an observer."""
        self.observers.append(observer)

    def setState(self, new_state):
        """Update state and notify observers."""
        self.state = new_state
        self.notifyAllObservers()

    def notifyAllObservers(self):
        """Notify all observers."""
        for obs in self.observers:
            obs.update(self.state, self.name)


class Observer:
    def __init__(self, name):
        self.name = name

    def update(self, state, from_machine):
        """Abstract method; overridden by Employee.
        from_machine is the variable used because from is a defined keyword in Python"""
        pass


class Machine(Subject):
    def __init__(self, name):
        super().__init__(name)

    def run_cycle(self):
        """Randomly assigning a state to simulate a production machine."""
        value = random.randint(1, 3)

        match value:
            case 1:
                self.setState("PRODUCING")
            case 2:
                self.setState("IDLE")
            case 3:
                self.setState("STARVED")
            case _:
                self.setState("UNKNOWN")


class Employee(Observer):
    def __init__(self, name, role):
        super().__init__(name)
        self.role = role

    def update(self, state, from_machine):
        """Output machine updates as per requirement."""
        print(
            f"[UPDATE] Employee: {self.name} | Role: {self.role}\n"
            f"Machine '{from_machine}' changed to state: {state}\n"
        )


def main():
    # Creating employee instances
    tech = Employee("Clayson", "Technician")
    manager = Employee("Matt", "Manager")

    # Creating machine instances
    m1 = Machine("Panasonic SPI")
    m2 = Machine("AOI")
    m3 = Machine("BOI")

    # Attach employees to machines
    m1.attach(tech)  # Only technician watches Machine 1
    m2.attach(manager)  # Only manager watches Machine 2
    m3.attach(tech)  # Both watch Machine 3
    m3.attach(manager)

    print("\n===== Production Line Simulation Started =====\n")

    # Limiting to 5 cycles
    for cycle in range(5):
        print(f"----- Cycle {cycle + 1} -----")
        for machine in [m1, m2, m3]:
            machine.run_cycle()
            time.sleep(1)

        # Pausing before next cycle
        time.sleep(1)

    print("===== Simulation Ended =====")


if __name__ == "__main__":
    main()
