from app import db

class Exercise(db.Model):
    __tablename__ = "exercises"   # 🔥 REQUIRED

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)