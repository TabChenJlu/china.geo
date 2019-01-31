from flask import Flask
app = Flask(__name__)
import json

china_geo = json.load(open('china.geo.json','r'))

@app.route("/")
def hello():
    return "Hello World!"


@app.route('/chinaGeo')
def get_china_geo():
    return json.dumps(china_geo,ensure_ascii=False)

if __name__ == '__main__':
    app.run(debug=True,port=8001)
