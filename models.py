from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Destination(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    location = db.Column(db.String(255), nullable=False)

    def _repr_(self):
        return f'<Destination {self.name}>'


class Itinerary(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    destination_id = db.Column(db.Integer, db.ForeignKey(
        'destination.id'), nullable=False)
    activity = db.Column(db.Text, nullable=False)


class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    destination_id = db.Column(db.Integer, db.ForeignKey(
        'destination.id'), nullable=False)
    expense_category = db.Column(db.Text, nullable=False)
    amount = db.Column(db.Float, nullable=False)