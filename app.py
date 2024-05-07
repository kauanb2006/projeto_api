from flask import Flask,jsonify,render_template

app = Flask(__name__)

@app.route("/")
def index ():
    return render_template("index.html")



from api import bp 
app.register_blueprint(bp)
