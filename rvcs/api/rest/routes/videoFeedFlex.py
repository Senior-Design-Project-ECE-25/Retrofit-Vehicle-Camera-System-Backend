from flask import Response, render_template, make_response
from flask_restful import Resource

from ..utilities.utils import log_request


class Index(Resource):
    endpoint = '/api/v1/VideoFeed/flex'

    def __init__(self) -> None:
        super(Index, self).__init__()

    @log_request
    def get(self) -> Response:
        html_template = render_template('videoFeedFlex.html')
        response = make_response(html_template)
        response.headers['content-type'] = 'text/html'
        return response
