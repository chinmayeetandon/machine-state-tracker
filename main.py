from flask import Flask, jsonify, request, render_template


class Subject:
    def __init__(self):
        self.state = "IDLE"
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def setState(self, state):
        self.state = state
        self.notifyObservers()

    def notifyObservers(self):
        for obs in self.observers:
            obs.update(self.state, self.name)


class Machine(Subject):
    def __init__(self, name):
        super().__init__()
        self.name = name


class Observer:
    def update(self, state, from_machine):
        pass


class Dashboard(Observer):
    def __init__(self):
        self.machine_states = {}

    def update(self, state, from_machine):
        self.machine_states[from_machine] = state


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("dashboard.html")


machine_a = Machine("AOI")
machine_b = Machine("BOI")
machine_c = Machine("Panasonic SPI")

machines = [machine_a, machine_b, machine_c]

dashboard = Dashboard()

for m in machines:
    m.attach(dashboard)
    m.setState("IDLE")


states = ["PRODUCING", "IDLE", "STARVED"]


@app.route("/api/machines", methods=["GET"])
def get_machine_states():
    return jsonify(dashboard.machine_states)


@app.route("/api/update", methods=["POST"])
def update_machine_states():
    data = request.get_json()

    if not data or "machine" not in data or "state" not in data:
        return jsonify({"error": "Please provide 'machine' and 'state'"}), 400

    machine_name = data["machine"]
    new_state = data["state"]

    machine = next((m for m in machines if m.name == machine_name), None)
    if not machine:
        return jsonify({"error": f"Machine '{machine_name}' not found"}), 404

    machine.setState(new_state)

    return jsonify({
        "message": f"Machine '{machine_name}' updated",
        "states": dashboard.machine_states
    })



if __name__ == "__main__":
    app.run(debug=True)
