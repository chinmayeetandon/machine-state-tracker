from flask import Flask, render_template
from flask_socketio import SocketIO
import random
import time
import threading

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
    def __init__(self, socketio):
        self.socketio = socketio

    def update(self, state, from_machine):
        self.socketio.emit(
            "machine_update",
            {"machine": from_machine, "state": state}
        )


app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("dashboard.html")


machine_a = Machine("AOI")
machine_b = Machine("BOI")
machine_c = Machine("Panasonic SPI")

machines = [machine_a, machine_b, machine_c]

dashboard = Dashboard(socketio)

for m in machines:
    m.attach(dashboard)

states = ["PRODUCING", "IDLE", "STARVED"]


def state_loop():
    while True:
        for m in machines:
            m.setState(random.choice(states))
        time.sleep(3)

threading.Thread(target=state_loop, daemon=True).start()


if __name__ == "__main__":
    socketio.run(app, debug=True)