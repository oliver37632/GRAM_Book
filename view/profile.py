from config import AWS_S3_BUCKET_NAME, AWS_S3_BUCKET_REGION

from flask import request

import datetime

from controller.profile import s3_get_object
from model import s3_connection

s3 = s3_connection()


def s3_get_object(s3, bucket, object_name, file_name):
    '''
    s3 bucket에서 지정 파일 다운로드
    :param s3: 연결된 s3 객체(boto3 client)
    :param bucket: 버킷명
    :param object_name: s3에 저장된 object 명
    :param file_name: 저장할 파일 명(path)
    :return: 성공 시 True, 실패 시 False 반환
    '''
    try:
        s3.download_file(bucket, object_name, file_name)
    except Exception as e:
        print(e)
        return False
    return True

def upload():
    f = request.files['file']
    f.save("./temp")
    file_name=request.args.get('name')


    return s3_get_object(
        s3=s3,
        bucket=AWS_S3_BUCKET_NAME,
        object_name="./temp",
        file_name=file_name


    )

