from flask import Flask
from flask_restful import Api
from flask_cors import CORS, cross_origin
from QuesGenSubj import QuesSub
app=Flask(__name__)
CORS(app)
cors= CORS(app, resource={r"/*":{"origins":"*"}})
api=Api(app)


@app.route('/')
def index():
    return "<h1>Flask API Server is working for Question Generation for Subjective - 5001....</h1>"

api.add_resource(QuesSub, '/api/subj')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001)