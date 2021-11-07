from model import session_scope

from flask_jwt_extended import create_access_token, create_refresh_token
from flask import abort

from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta


def signup(nickname, id, password):
    with session_scope() as session:
        new_user = User(
            nickname=nickname,
            id=id,
            password=generate_password_hash(password)
        )

        session.add(new_user)
        session.commit()

        return {
            "message": "success"
        }, 201


def login(nickname, password):
    with session_scope() as session:
        ck_nick = session.query(User).filter(User.nickname == nickname).scalar()

        if not ck_nick:
            return abort(409, 'user id code does not match')

        ck_nick = ck_nick.first()
        ck_user_password = check_password_hash(ck_nick.password, password)

        if not ck_user_password:
            return abort(409, 'user password code does not match')

        access_expires_delta = timedelta(minutes=60)
        refresh_expires_delta = timedelta(weeks=1)

        access_token = create_access_token(expires_delta=access_expires_delta,
                                           identity=nickname
                                           )
        refresh_token = create_refresh_token(expires_delta=refresh_expires_delta,
                                             identity=nickname
                                             )
        return {
                   'access_token': access_token,
                   'refresh_token': refresh_token
               }, 201


def idauth(id):
    with session_scope() as session:
        ck_id = session.query(User).filter(User.id == id)

        if ck_id.scalar():
            return abort(400, 'overlap')
        else:
            return abort(200, 'usable')


def nickauth(nickname):
    with session_scope() as session:
        ck_nick = session.query(User).filter(User.nickname == nickname)

        if ck_nick.scalar():
            return abort(400, 'overlap')
        else:
            return abort(200, 'usable')