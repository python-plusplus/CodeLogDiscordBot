from flask import Flask, render_template, request
from threading import Thread
from flask_sqlalchemy import SQLAlchemy

app = Flask('')
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///logs.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config.from_pyfile("config.py")

db = SQLAlchemy(app)

class logs(db.Model):
  id = db.Column("id", db.Integer, primary_key=True)
  name = db.Column("name", db.String(50))
  text = db.Column("text", db.String(500))
  time = db.Column("time", db.String(30))
  pplink = db.Column("pplink", db.String(50))

  def __init__(self, id, name, text, time, pplink):
    self.name = name
    self.text = text
    self.time = time
    self.pplink = pplink

@app.route('/', methods=["POST", "GET"])
def main():
  db.create_all()
  if request.method == "POST":
    log = logs(request.form["id"],request.form["name"], request.form['text'], request.form['time'], request.form["pplink"])
    db.session.add(log)
    db.session.commit()
  data = logs.query.all()[::-1]
  return render_template("index.html", logs=data)
def run():
  app.run(host="0.0.0.0", port=8080) 
def keep_alive():
    server = Thread(target=run)
    server.start()
    