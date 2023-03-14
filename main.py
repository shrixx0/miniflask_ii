from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= "sqlite:///todo.db"
db = SQLAlchemy(app)


@app.route("/")
def hello():
    return render_template("index.html")
    #return "Hello, World!"


@app.route("/project")
def project():
    return "here is the project"


if __name__ == "__main__":
    app.run(debug=True)