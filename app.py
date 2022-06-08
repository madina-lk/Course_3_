from flask import Flask, jsonify

from main.views import main_blueprint                # Импортируем блюпринты из их пакетов
from bp_api.views import posts_blueprint

app = Flask(__name__)

app.config.from_pyfile('config.py')

app.register_blueprint(main_blueprint)              # Регистрируем блюпринт main_blueprint
app.register_blueprint(posts_blueprint)


@app.errorhandler(404)
def invalid_route(e):
    return jsonify({'errorCode': 404, 'message': 'Route not found'})


@app.errorhandler(500)
def internal_error(e):
    return "500 error"


if __name__ == '__main__':
    app.run()
