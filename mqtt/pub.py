import paho.mqtt.client as mqtt

# MQTT Broker details
BROKER = "192.168.118.192"  # Replace with your broker address
PORT = 1883  # Default MQTT port
USERNAME = "admin"
PASSWORD = "admin"  
TOPIC = "test/topic"
MESSAGE = "Hello, MQTT!"


# Create an MQTT client instance
client = mqtt.Client()

# Set username and password 
# client.username_pw_set(USERNAME, PASSWORD)

# Connect to the broker
client.connect(BROKER, PORT, 60)
client.loop_start()
print("mqtt started")

# client.loop_start()
def mqtt_publish_msg(topic, msg):
    if not client.is_connected():
        print("Client Disconnected!!")
    # print("Client Conneted?",client.is_connected())
    
    client.publish(topic=topic, payload=msg)
    client.loop()

# Disconnect from the broker
# client.disconnect()

