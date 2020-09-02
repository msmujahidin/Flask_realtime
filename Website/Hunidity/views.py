try:

    from flask import (Blueprint,
                       render_template,
                       redirect, url_for, session)

    from flask import Flask, request, session, send_file
    import random
    import json
    from time import time
    from random import random
    from flask import Flask, render_template, make_response

except Exception as e:
    print("Some modules didnt load {}".format(e))

humidity_blueprint = Blueprint('Humidity', __name__)
suhu_blueprint = Blueprint('Suhu', __name__)


@humidity_blueprint.route('/humidity', methods=['GET'])
def humidity():
    # Create a PHP array and echo it as JSON

    data = [time() * 1000, random() * 10]
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response


@suhu_blueprint.route('/suhu', methods=['GET'])
def suhu(): 
    data1 = [time() * 1000, random() * 10]
    response1 = make_response(json.dumps(data1))
    response1.content_type = 'application/json'
    return response1

