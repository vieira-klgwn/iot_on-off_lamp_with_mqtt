import paho.mqtt.client as mqtt

# Callback when a message is received from the broker
def on_message(client, userdata, message):
    payload = message.payload.decode("utf-8")
    if payload == "ON":
        print("💡 Light is TURNED ON")
    elif payload == "OFF":
        print("💡 Light is TURNED OFF")

# MQTT broker address (same as the one used in the web interface)
broker = "ws://157.173.101.159:9001/mqtt"
port = 1883
topic = "/student_group/light_control"

# Initialize MQTT client
client = mqtt.Client()

# Set the on_message callback function
client.on_message = on_message

# Connect to the broker
client.connect(broker, port)

# Subscribe to the topic
client.subscribe(topic)

# Loop forever to listen for messages
client.loop_forever()

