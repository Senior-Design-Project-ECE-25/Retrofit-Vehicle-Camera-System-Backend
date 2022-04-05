from flask import jsonify
from flask_restful import Resource

from ..utilities.utils import log_request



class logs(Resource):

    endpoint = '/api/v1/logs'

    def __init__(self) -> None:
        super(logs, self).__init__()
    
    @log_request
    def get(self):
        data = []
        open(self)
        for i in enumerate(self):
            data.append(i)
        return jsonify(data=data)

# class Parse:

#     def get_app(nums):
#         app = []
#         app.append(nums)
#         res = app[-25:]

#         return res

#     def get_vs(nums):
#         vs = []
#         vs.append(nums)
#         res = vs[-25:]

#         return res

