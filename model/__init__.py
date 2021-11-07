import boto3
from config import AWS_SECRET_ACCESS_KEY, AWS_ACCESS_KEY, AWS_S3_BUCKET_REGION

from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from config import MYSQL_DB_URL


@contextmanager
def session_scope():
    engine = create_engine(
        MYSQL_DB_URL,
        encoding="utf-8",
        pool_recycle=3600,
        pool_size=20,
        max_overflow=20,
        pool_pre_ping=True
    )
    Session = scoped_session(sessionmaker(bind=engine, autocommit=False, autoflush=False))
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

Base = declarative_base()


def s3_connection():
    '''
    s3 bucket에 연결
    :return: 연결된 s3 객체
    '''
    try:
        s3 = boto3.client(
            service_name='s3',
            region_name=AWS_S3_BUCKET_REGION,
            aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY
        )
    except Exception as e:
        print(e)
        exit("ERROR_S3_CONNECTION_FAILED")
    else:
        print("s3 bucket connected!")
        return s3


