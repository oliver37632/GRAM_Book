from flask import request
from flask_restful import Resource

from flask_jwt_extended import get_jwt_identity, jwt_required

from controller.post import post, post_update, post_get, post_delete


class Post(Resource):
    @jwt_required
    def post(self):
        title = request.json['title']
        content = request.json['content']
        nickname = get_jwt_identity

        return post(
            title=title,
            content=content,
            nickname=nickname
        )


class GetPost(Resource):
    @jwt_required
    def get(self):
        return post_get()


class UpdatePost(Resource):
    @jwt_required
    def patch(self, id):
        title = request.json['title']
        content = request.json['content']
        token = get_jwt_identity

        return post_update(
            title=title,
            content=content,
            token=token,
            id=id
        )


class DeletePost(Resource):
    @jwt_required
    def delete(self, id):
        token = get_jwt_identity()

        return post_delete(
            id=id,
            token=token
        )




