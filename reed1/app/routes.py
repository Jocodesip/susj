from flask import Blueprint, request, jsonify, render_template

main = Blueprint('main', __name__)

# Sample data for demonstration
reeds = [
    {
        "id": 1,
        "type": "alto",
        "performance": 5,
        "adjustment_period": 3
    }
]

@main.route('/')
def index():
    return render_template('index.html', reeds=reeds)

@main.route('/reed', methods=['POST'])
def add_reed():
    data = request.form
    new_reed = {
        "id": len(reeds) + 1,
        "type": data.get("type"),
        "performance": int(data.get("performance")),
        "adjustment_period": int(data.get("adjustment_period"))
    }
    reeds.append(new_reed)
    return jsonify({"message": "Reed added", "reed": new_reed}), 201

@main.route('/reed/<int:id>', methods=['PUT'])
def update_reed(id):
    reed = next((reed for reed in reeds if reed["id"] == id), None)
    if reed:
        data = request.form
        reed["type"] = data.get("type", reed["type"])
        reed["performance"] = int(data.get("performance", reed["performance"]))
        reed["adjustment_period"] = int(data.get("adjustment_period", reed["adjustment_period"]))
        return jsonify({"message": "Reed updated", "reed": reed}), 200
    return jsonify({"message": "Reed not found"}), 404

@main.route('/reed/<int:id>', methods=['DELETE'])
def delete_reed(id):
    global reeds
    reeds = [reed for reed in reeds if reed["id"] != id]
    return jsonify({"message": "Reed deleted"}), 200

@main.route('/reeds', methods=['GET'])
def get_reeds():
    return jsonify(reeds), 200
