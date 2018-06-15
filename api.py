from flask import Flask, json, request
from sklearn.neural_network import MLPClassifier
import pandas as pd
from sklearn.model_selection import cross_val_predict
# read from file
attributes = []
with open('dataset.txt') as f:
    for line in f:
        inner_list = [float(elt.strip()) for elt in line.split(',')]
        attributes.append(inner_list)

with open('classes.txt') as f:
    classes = f.readlines()
classes = [x.strip() for x in classes]
# Attributes : cold, sunny , rainy , city break ,vacantion, economic, pool, expensive

clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(15,), random_state=1)
h = clf.fit(attributes, classes)

app = Flask(__name__)


@app.route('/stereotype')
def stereotype():
    sunny = float(request.args.get('sunny'))
    rainy = float(request.args.get('rainy'))
    cold = float(request.args.get('rainy'))
    city_break = float(request.args.get('city_break'))
    vacantion = float(request.args.get('vacantion'))
    economic = float(request.args.get('economic'))
    pool = float(request.args.get('pool'))
    expensive = float(request.args.get('expensive'))
    ceva = [coef.shape for coef in clf.coefs_]
    user_type = clf.predict([[cold, sunny, rainy, city_break, vacantion, economic, pool, expensive]])
    # prepare_response = pd.DataFrame(user_type, columns=clf.classes_)
    # res = prepare_response.to_json()
    response = app.response_class(
        response=json.dumps(user_type[0]),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    app.run()
