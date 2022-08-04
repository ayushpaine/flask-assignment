import collections
from crypt import methods
import json
from flask import Flask, render_template
from flask import jsonify
from collections import OrderedDict
from matplotlib import use
from requests import request

from sklearn.exceptions import DataDimensionalityWarning

app = Flask(__name__)


@app.route('/<int:number>', methods=['GET'])
def data(number):
    datadict = OrderedDict()
    for i in range(number, number + 50):
        datadict[f"user{i}"] = {'name': f"name{i}",
                                'phone': f"phone{i}", "email": f"email{i}", "timestamp": "1st aug 9am"}

    data = json.dumps(datadict, indent=3)
    response = app.response_class(
        response=data,
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/users/<int:user_id>', methods=["GET"])
def renderData(user_id):

    return render_template("index.html", user_id=user_id)


@app.route("/", methods=["GET"])
def home():

    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
