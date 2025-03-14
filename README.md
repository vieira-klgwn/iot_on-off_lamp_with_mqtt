# iot_on-off_lamp_with_mqtt


MQTT Light Control Project
Overview

This project demonstrates how to control a light using a web interface over MQTT (Message Queuing Telemetry Transport) and simulate an IoT device (like an ESP8266) that responds to MQTT messages.
Features:

    Web Interface: A simple webpage with buttons to turn the light ON/OFF using MQTT.
    Simulated IoT Device: A Python script that simulates an IoT device (ESP8266) that listens for MQTT messages and prints whether the light is ON or OFF.
    Real-time Communication: The web interface and Python script communicate in real-time using MQTT, allowing for seamless control and monitoring of the light.

Project Structure

/mqtt-light-control
│
├── index.html               # Web interface for light control
├── light_simulation.py       # Simulated IoT device (Python script)
├── README.md                # Project explanation and setup instructions

Getting Started
Prerequisites

Before running the project, ensure you have the following installed:

    Web Interface: No special software is needed, just a modern web browser (Chrome, Firefox, etc.).
    Simulated IoT Device:
        Python 3.x
        paho-mqtt Python package (can be installed via pip).

#Step 1: Setting Up the MQTT Broker

The web interface and Python script communicate via MQTT. You'll need an MQTT broker to handle the messaging. You can use a public MQTT broker or set up your own broker.

    For a public broker, we use ws://broker.hivemq.com:8000/mqtt in the example (it supports WebSockets).
    Alternatively, you can set up your own broker like Mosquitto on your machine or a cloud service.

Make sure the broker's WebSocket URL is configured correctly in the index.html file:

const broker = "ws://broker.hivemq.com:8000/mqtt"; // Example public broker

#Step 2: Running the Simulated IoT Device (Python Script)

    Install the required MQTT Python library by running the following command:

pip install paho-mqtt

Run the Python script (light_simulation.py) on your local machine. This will simulate the IoT device (e.g., ESP8266) that listens to the MQTT topic and responds with the current light status.

    python light_simulation.py

    When the Python script is running, it will print messages like:
        💡 Light is TURNED ON when the web interface sends an "ON" command.
        💡 Light is TURNED OFF when the web interface sends an "OFF" command.

#Step 3: Running the Web Interface (index.html)

    Open the index.html file in any modern web browser (Chrome, Firefox, etc.).
    The page will display two buttons: "Turn ON" and "Turn OFF".
    When you click the "Turn ON" or "Turn OFF" buttons, the web interface sends the corresponding MQTT message (ON or OFF) to the MQTT broker.
    The status will update on the webpage, and the Python script will print the light status to the console.

#Step 4: Testing

    Click the "Turn ON" button on the web page, and the Python script will print 💡 Light is TURNED ON.
    Click the "Turn OFF" button, and the Python script will print 💡 Light is TURNED OFF.
    The web interface will show the corresponding status message (green for ON, red for OFF).

MQTT Communication Flow

    The web interface connects to the MQTT broker via WebSockets.
    When a button is clicked on the web interface, the client publishes a message (ON or OFF) to the MQTT topic /student_group/light_control.
    The Python script, acting as the simulated IoT device, subscribes to the same topic and listens for messages.
    When the Python script receives a message (ON or OFF), it prints the corresponding light status to the console.

How It Works Together

    Web Interface: Allows users to interact with the light and send commands (ON/OFF) over MQTT.
    Simulated IoT Device (Python): Listens for MQTT messages and simulates the light's behavior by printing the status to the console.

Example Output (Python Console)

When the light is turned ON or OFF, the Python console will show:

💡 Light is TURNED ON

or

💡 Light is TURNED OFF

Troubleshooting
Common Issues:

    MQTT Connection Errors: If the web interface or Python script cannot connect to the MQTT broker, make sure the broker address and port are correct.
    No Status Updates: Ensure the MQTT broker is running and accessible. The web interface and Python script should be able to communicate with it.
    Firewall/Network Issues: If you're using a local MQTT broker, ensure that it's accessible from the web interface (check for any firewall or network configuration issues).

License

This project is open-source and licensed under the MIT License.
