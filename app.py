from flask import Flask
from sqlalchemy import SQLAlchemy
from migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///workouts.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)



@app.route('/')
def home():
    return 'WELCOME TO THE WORKOUT APP!'

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    
    