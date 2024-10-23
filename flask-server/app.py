from flask import Flask, jsonify, request, render_template
from flask_restful import Api, Resource, abort

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/quotes')
def quotes():
    return render_template("quotes.html")

@app.route('/search', methods=['POST'])
def search():
    req = request.get_json(force=True)
    return jsonify("test")

if __name__ == "__main__":
    app.run() 