try:

    from flask import (Blueprint,
                       render_template,
                       redirect, url_for, session)

    from flask import Flask, request, session, send_file
    import json
    from time import time
    from random import random
    from flask import Flask, render_template, make_response
    import eventlet
    import json
    import paho.mqtt.client as mqtt
    import numpy as np

    eventlet.monkey_patch()

    # mqtt_username = "mqtt"
    # mqtt_password = "mqtt"
    # mqtt_topic = "topic/baru"
    # mqtt_broker_ip = "mqtt.danova.id"
    # mqtt_port = 1883

    # client = mqtt.Client()
    # # Set the username and password for the MQTT client
    # client.username_pw_set(mqtt_username, mqtt_password)

except Exception as e:
    print("Some modules didnt load {}".format(e))

humidity_blueprint = Blueprint('Humidity', __name__)
# # suhu_blueprint = Blueprint('Suhu', __name__)
  



@humidity_blueprint.route('/humidity', methods=['GET'])

# def on_connect(client, userdata, flags, rc):
#         # rc is the error code returned when connecting to the broker
#     print ("Connected!", str(rc))
#         # Once the client has connected to the broker, subscribe to the topic
#     self.subscribe(mqtt_topic, 0)

# def on_message(client, userdata, msg):
#     # Create a PHP array and echo it as JSON

#     data1 = msg.payload
#     baru = data1.decode()
#     # data = np.array(baru)


    # # terbaru = [time() * 1000, baru * 100]
    # response = make_response(json.dumps(data))
    # response.content_type = 'application/json'
    # print(data)
    # print(type(data))
    # print(type(response))
    # return response

    # client.on_connect = on_connect
    # client.humidity = humidity

    #     # Once everything has been set up, we can (finally) connect to the broker
    #     # 1883 is the listener port that the MQTT broker is using
    # client.connect(mqtt_broker_ip, int(mqtt_port))

    #     # Once we have told the client to connect, let the client object run itself
    # client.loop_forever()
    # client.disconnect()
def humidity():
    data1 = [time() * 1000, random() * 100]
    response1 = make_response(json.dumps(data1))
    response1.content_type = 'application/json'
    return response1






 



     

  

# @suhu_blueprint.route('/suhu', methods=['GET'])
# def suhu(): 
#     data1 = [time() * 1000, random() * 100]
#     response1 = make_response(json.dumps(data1))
#     response1.content_type = 'application/json'
#     return response1

