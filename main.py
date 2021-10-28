from flask import Flask, redirect, request
from flask_cors import CORS, cross_origin
import os

from routes.reports import reports_blueprint

app = Flask(__name__, static_url_path='/')
app.register_blueprint(reports_blueprint)
# CORS(app, support_credentials=True, resources={r"/api/*": {"origins": "http://localhost:3000"}})
CORS(app, supports_credentials=True, origins=["http://localhost:3000", "http://127.0.0.1/3000"])


# @app.after_request
# def add_headers(response):
#     # response.headers.add('Content-Type', 'application/json')
#     # response.headers.add('Access-Control-Allow-Origin', react_base_url)
#     # response.headers.add('Access-Control-Allow-Credentials', "true")
#     response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000'),
#     response.headers.add('Access-Control-Allow-Methods', 'PUT, GET, POST, DELETE, OPTIONS')
#     response.headers.add("Access-Control-Allow-Headers",
#                          "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With, withCredentials")
#     response.headers.add('Access-Control-Expose-Headers', 'Content-Type,Content-Length,Authorization,X-Pagination')
#     return response


@app.route('/')
def index():
    return "Hello World"


@app.route("/home")
def index_home():
    return redirect('/')


@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('not_found.html')


if __name__ == "__main__":
    # if is_prod:
    #     app.run(debug=False, port=os.environ.get('PORT', 80), use_reloader=False)
    # else:
    app.run(host="localhost", threaded=True, port=5000)
