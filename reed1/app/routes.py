from flask import Blueprint, request, jsonify, render_template

main = Blueprint('main', __name__)

# Uzorak podataka za demonstraciju
jezičci = [
    {
        "id": 1,
        "tip": "alt",
        "performanse": 5,
        "period_prilagodbe": 3
    }
]

@main.route('/')
def index():
    return render_template('index.html', jezičci=jezičci)

@main.route('/jezičak', methods=['POST'])
def dodaj_jezičak():
    podaci = request.form
    novi_jezičak = {
        "id": len(jezičci) + 1,
        "tip": podaci.get("tip"),
        "performanse": int(podaci.get("performanse")),
        "period_prilagodbe": int(podaci.get("period_prilagodbe"))
    }
    jezičci.append(novi_jezičak)
    return jsonify({"poruka": "Jezičak dodan", "jezičak": novi_jezičak}), 201

@main.route('/jezičak/<int:id>', methods=['PUT'])
def azuriraj_jezičak(id):
    jezičak = next((jezičak for jezičak in jezičci if jezičak["id"] == id), None)
    if jezičak:
        podaci = request.form
        jezičak["tip"] = podaci.get("tip", jezičak["tip"])
        jezičak["performanse"] = int(podaci.get("performanse", jezičak["performanse"]))
        jezičak["period_prilagodbe"] = int(podaci.get("period_prilagodbe", jezičak["period_prilagodbe"]))
        return jsonify({"poruka": "Jezičak ažuriran", "jezičak": jezičak}), 200
    return jsonify({"poruka": "Jezičak nije pronađen"}), 404

@main.route('/jezičak/<int:id>', methods=['DELETE'])
def obrisi_jezičak(id):
    global jezičci
    jezičci = [jezičak for jezičak in jezičci if jezičak["id"] != id]
    return jsonify({"poruka": "Jezičak obrisan"}), 200

@main.route('/jezičci', methods=['GET'])
def dohvati_jezičke():
    return jsonify(jezičci), 200
