from flask import request
from flask_restful import Resource

from flask_jwt_extended import get_jwt_identity, jwt_required

from controller.comment import comment, comment_get


class PostComment(Resource):
    @jwt_required()
    def post(self):
        post_id = request.args.get('post_id')
        content = request.json["content"]
        user_id = get_jwt_identity()

        return comment(
            post_id=post_id,
            content=content,
            user_id=user_id
        )


class GetComment(Resource):
    @jwt_required()
    def get(self):
        post_id = request.args.get('post_id')
        return comment_get(
            post_id=post_id
        )
