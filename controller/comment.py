from model import session_scope
from datetime import datetime


def comment(content):
    with session_scope() as session:

        new_comment = Comment(
            content=content,
            created_at=datetime.now()
        )

    session.add(new_comment)


def comment_get(id):
    with session_scope() as session:

        comments_join = session.quey(
            User.nickname,
            Comment.content
        ).join(User, User.id == Comment.user_id).\
            filter(Comment.id == id)

        return {
            "comment_join": [{
                "name": name,
                "content": content
            } for content,  nicknaem in comment_join]
        }