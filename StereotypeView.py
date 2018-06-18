from flask_classful import route, FlaskView
from StereotypeMLP import StereotypeMLP
from flask import Flask, json, request

app = Flask(__name__)


class StereotypeView(FlaskView):
    def index(self):
        stereotype = StereotypeMLP()
        sunny = float(request.args.get('sunny'))
        rainy = float(request.args.get('rainy'))
        cold = float(request.args.get('rainy'))
        city_break = float(request.args.get('city_break'))
        vacantion = float(request.args.get('vacantion'))
        economic = float(request.args.get('economic'))
        pool = float(request.args.get('pool'))
        expensive = float(request.args.get('expensive'))
        user_type = stereotype.classifier.predict([[cold, sunny, rainy, city_break, vacantion, economic, pool, expensive]])
        response = app.response_class(
            response=json.dumps(user_type[0]),
            status=200,
            mimetype='application/json'
        )
        return response


StereotypeView.register(app)

if __name__ == '__main__':
    app.run()
