from flask import Flask, render_template, request
from threading import Thread
from flask_sqlalchemy import SQLAlchemy

app = Flask('')
app.config.from_pyfile("config.py")

db = SQLAlchemy(app)

class logs(db.Model):
  id = db.Column("id", db.Integer, primary_key=True)
  name = db.Column("name", db.String(50))
  text = db.Column("text", db.String(500))
  time = db.Column("time", db.String(30))

  def __init__(self, id, name, text, time):
    self.name = name
    self.text = text
    self.time = time

@app.route('/', methods=["POST", "GET"])
def main():
  db.create_all()
  if request.method == "POST":
    log = logs(request.form["id"],request.form["name"], request.form['text'], request.form['time'])
    db.session.add(log)
    db.session.commit()
  data = logs.query.all()
  return render_template("index.html", logs=data)
def run():
  app.run(host="0.0.0.0", port=8080)
def keep_alive():
    server = Thread(target=run)
    server.start()
    