#coding=utf8
import sys
import random, uuid, hashlib, time
from flask import jsonify
reload(sys)
sys.setdefaultencoding('utf8')

def responseData(data, code=0, msg=''):
    res = {}
    res['status'] = code
    res['data'] = data
    res['msg'] = msg
    return jsonify(res)

def encryptUserId(userId):
    r = uuid.uuid4()
    t = time.time()
    return hashlib.md5('{}-{}-{}'.format(r, t, userId)).hexdigest()[8:-8]
