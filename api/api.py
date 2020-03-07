#!/usr/bin/python
import json
import uuid

from flask import jsonify, request, Response

from config import app
from model_building import Building

buildings = []
bldg = Building()


@app.route('/')
def get_root():
    return 'Hello World!'


@app.route('/player')
def get_player():
    return jsonify(
        id=1,
        name="Player1",
        funds=10021.43,
    )


@app.route('/buildings')
def get_buildings():
    return jsonify({'buildings': bldg.get_all_buildings()})


@app.route('/buildings/<int:id>')
def get_building_by_id(id):
    found_building = bldg.get_building_by_id(id)
    return found_building


def validBuildingObject(buildingObject):
    if (
            "name" in buildingObject
            and "value" in buildingObject
            and "id" in buildingObject
    ):
        return True
    else:
        return False


@app.route('/buildings', methods=["POST"])
def add_building():
    request_data = request.get_json()
    if validBuildingObject(request_data):
        new_building_id = uuid.uuid4()
        bldg.add_building(new_building_id, request_data["name"], request_data["value"])
        response = Response("", 201, mimetype="application/json")
        response.headers['Location'] = "/buildings/" + str(request_data["id"])
        return response
    else:
        invalid_building_error_msg = {
            "error": "Invalid building object passed in request",
            "helpString": "Data did not match model"
        }
        response = Response(json.dumps(invalid_building_error_msg), 400, mimetype="application/json")
        return response


@app.route('/buildings/<int:id>', methods=['PUT'])
def update_building(id):
    request_data = request.get_json()
    bldg.replace_building(id, request_data['name'], request_data['value'])
    response = Response("", status=204)
    return response

app.run(port=5000)
