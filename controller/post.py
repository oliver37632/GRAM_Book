from flask import abort
from model import session_scope
from datetime import datetime


def post(title, content, nickname):
    with session_scope() as session:
        new_post = Post(
            nickname=nickname,
            title=title,
            content=content,
            created_at=datetime.now()
        )

        session.add(new_post)
        session.commit()

        return {
            'message': 'success'
        }, 201


def post_get():
    with session_scope() as session:
        posts = session.query(Post).all()

        if posts:
            return {
                       "posts": [{
                           "nickname": nickname,
                           "id_pk": id,
                           "title": title,
                           "content": content,
                           "created_at": created_at
                       } for id, title, content, created_at, nickname in posts]
                   }, 200
        else:
            return abort("Not Found"), 404


def post_delete(id, token):
    with session_scope() as session:
        post_del = session.query(Post).filter(Post.id == id).first()

        if not post_del:
            return {
                "message": "post number not much"
            }
        post_del = session.query(Post).filter(Post.nickname == token).first()

        if not post_del:
            return {
                "message": "post nickname not match"
            }
        session.delect(post_del)
        session.commit

        return {
            "message": "success"
        }


def post_update(id, title, content, token):
    with session_scope() as session:
        post_update = session.query(Post).filter(Post.id == id).first()

        if not post_update:
            return {
                "message": "post id not match"
            }, 404

        post_update = session.query(Post).filter(Post.nickname == token).first()

        if not post_update:
            return {
                "message": "post nickname not match"
            }, 404

        post.title = title
        post.content = content

        return {
            "message": "success"
        }, 200


