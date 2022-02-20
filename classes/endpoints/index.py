from flask import render_template
from flask_restful import Resource

from config import BASE_DIR
from utils import log_request


class Index(Resource):
    endpoint = '/'

    def __init__(self) -> None:
        super(Index, self).__init__()

    @log_request
    def get(self) -> str:
        return render_template(f'index.html')
