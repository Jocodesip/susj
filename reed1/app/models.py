from app import db

class Reed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    performance = db.Column(db.Integer, nullable=False)
    adjustment_period = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "type": self.type,
            "performance": self.performance,
            "adjustment_period": self.adjustment_period
        }
