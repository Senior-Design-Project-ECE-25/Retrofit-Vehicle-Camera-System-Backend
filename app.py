from flask import Flask
from flask_restful import Api

from classes.endpoints.index import Index
from classes.endpoints.videoFeed import VideoFeed
from classes.endpoints.systemInformation import SystemInformation

app = Flask(__name__)
api = Api(app)

api.add_resource(Index, Index.endpoint)
api.add_resource(VideoFeed, VideoFeed.endpoint)
api.add_resource(SystemInformation, SystemInformation.endpoint)


if __name__ == '__main__':
    from config import API_HOST, API_PORT
    app.run(host=API_HOST, port=API_PORT)
