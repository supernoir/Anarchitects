#!/usr/bin/python

import json
from sqlalchemy.dialects.postgresql import UUID
from flask_sqlalchemy import SQLAlchemy
from config import app

db = SQLAlchemy(app)


class Building(db.Model):
    __tablename__ = 'buildings'
    id = db.Column(UUID(as_uuid=True), primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    value = db.Column(db.Float, nullable=False)

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'value': self.value
        }

    def add_building(self, _id, _name, _value):
        new_building = Building(id=_id, name=_name, value=_value)
        db.session.add(new_building)
        db.session.commit()

    def get_all_buildings(self):
        return [Building.json(building) for building in Building.query.all()]

    def get_building_by_id(self, _id):
        return Building.query.filter_by(id=_id).first()

    def delete_building(self, _id):
        return Building.query.filter_by(id=_id).delete()
        db.session.commit()

    def update_building_name(self, _id, _name):
        building_to_update = Building.query.filter_by(id=_id).first()
        building_to_update.name = _name
        db.session.commit()

    def update_building_value(self, _id, _value):
        building_to_update = Building.query.filter_by(id=_id).first()
        building_to_update.value = _value
        db.session.commit()

    def replace_building(self, _id, _name, _value):
        building_to_replace = Building.query.filter_by(id=_id).first()
        building_to_replace.name = _name
        building_to_replace.name = _value
        db.session.commit()

    def __repr__(self):
        building_object = {
            'id': self.id,
            'name': self.name,
            'value': self.value
        }
        return json.dumps(building_object)
