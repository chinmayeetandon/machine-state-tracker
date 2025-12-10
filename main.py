from flask import Flask, request, jsonify


class Subject:
    def __init__(self, name):
        self.name = name
        self.state = None
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def setState(self, new_state):
        self.state = new_state
        self.notifyAllObservers()

    def notifyAllObservers(self):
        for obs in self.observers:
            obs.update(self.state, self.name)


class Observer:
    def __init__(self, name):
        self.name = name

    def update(self, state, from_machine):
        pass


class Machine(Subject):
    pass


class Employee(Observer):
    def __init__(self, name, role):
        super().__init__(name)
        self.role = role
        self.notifications = []

    def update(self, state, machine_name):
        msg = f"{self.name} ({self.role}) notified -> {machine_name} is now {state}"
        self.notifications.append(msg)

app = Flask(__name__)

machines = {}
employees = {}



@app.route("/machine/create", methods=["POST"])
def create_machine():
    data = request.json
    name = data["name"]

    machines[name] = Machine(name)
    return jsonify({"msg": f"Machine '{name}' created."})


@app.route("/employee/create", methods=["POST"])
def create_employee():
    data = request.json
    name = data["name"]
    role = data["role"]

    employees[name] = Employee(name, role)
    return jsonify({"msg": f"Employee '{name}' created."})


@app.route("/machine/attach", methods=["POST"])
def attach_employee():
    data = request.json
    machine_name = data["machine"]
    employee_name = data["employee"]

    machine = machines.get(machine_name)
    employee = employees.get(employee_name)

    if not machine or not employee:
        return jsonify({"error": "Machine or Employee not found"}), 404

    machine.attach(employee)
    return jsonify({"msg": f"Employee '{employee_name}' attached to machine '{machine_name}'."})


@app.route("/machine/state", methods=["POST"])
def change_state():
    data = request.json
    machine_name = data["machine"]
    new_state = data["state"]

    machine = machines.get(machine_name)
    if not machine:
        return jsonify({"error": "Machine not found"}), 404

    machine.setState(new_state)
    return jsonify({"msg": f"{machine_name} updated to {new_state}."})


@app.route("/employee/notifications/<name>", methods=["GET"])
def get_notifications(name):
    employee = employees.get(name)
    if not employee:
        return jsonify({"error": "Employee not found"}), 404

    return jsonify({"notifications": employee.notifications})


if __name__ == "__main__":
    app.run(debug=True)
