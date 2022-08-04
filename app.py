import collections
import json
from flask import Flask, render_template
from flask import jsonify
from collections import OrderedDict

from sklearn.exceptions import DataDimensionalityWarning

app = Flask(__name__)


@app.route('/<int:number>')
def data(number):
    datadict = OrderedDict()
    for i in range(number, number + 50):
        datadict[f"user{i}"] = {'name': f"name{i}",
                                'phone': f"phone{i}", "email": f"email{i}", "timestamp": "1st aug 9am"}

    data = json.dumps(datadict, indent=3)
    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
