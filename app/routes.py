from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, moons):
        self.id = id
        self.name = name
        self.description = description
        self.moons = moons


planets = [
    Planet(1, "Mercury", "solid", 0),
    Planet(2, "Venus", "bright and volcanic", 0),
    Planet(3, "Earth", "half and half", 1)
]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET"])
def planets_endpoint():
    response = []
    for planet in planets:
        response.append(dict(
            id = planet.id,
            name = planet.name,
            description = planet.description,
            moons = planet.moons
        ))
    return jsonify(response)