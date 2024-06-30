from flask import Blueprint, request, jsonify, render_template
from app import db
from app.models import Reed

main = Blueprint('main', __name__)

@main.route('/')
def index():
    reeds = Reed.query.all()
    return render_template('index.html', reeds=reeds)

@main.route('/reed', methods=['POST'])
def add_reed():
    data = request.form
    new_reed = Reed(
        type=data.get("type"),
        performance=int(data.get("performance")),
        adjustment_period=int(data.get("adjustment_period"))
    )
    db.session.add(new_reed)
    db.session.commit()
    return jsonify({"message": "Reed added", "reed": new_reed.to_dict()}), 201

@main.route('/reed/<int:id>', methods=['PUT'])
def update_reed(id):
    reed = Reed.query.get_or_404(id)
    data = request.form
    reed.type = data.get("type", reed.type)
    reed.performance = int(data.get("performance", reed.performance))
    reed.adjustment_period = int(data.get("adjustment_period", reed.adjustment_period))
    db.session.commit()
    return jsonify({"message": "Reed updated", "reed": reed.to_dict()}), 200

@main.route('/reed/<int:id>', methods=['DELETE'])
def delete_reed(id):
    reed = Reed.query.get_or_404(id)
    db.session.delete(reed)
    db.session.commit()
    return jsonify({"message": "Reed deleted"}), 200

@main.route('/reeds', methods=['GET'])
def get_reeds():
    reeds = Reed.query.all()
    return jsonify([reed.to_dict() for reed in reeds]), 200
