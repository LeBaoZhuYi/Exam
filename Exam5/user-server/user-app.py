# coding=utf8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
import json
from model.model import *
from utils import *
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, redirect, url_for, request, flash, render_template
from flask_login import LoginManager, login_user, login_required, logout_user

app = Flask(__name__)
app.secret_key = 'Sqsdsffqrhgh.,/1#$%^&'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:!23$56@localhost:3306/exam5?charset=utf8'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.debug = True

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "login"  # 定义登录的 视图
login_manager.login_message = '请登录以访问此页面'  # 定义需要登录访问页面的提示消息


@login_manager.user_loader  # 使用user_loader装饰器的回调函数非常重要，他将决定 user 对象是否在登录状态
def user_loader(id):  # 这个id参数的值是在 login_user(user)中传入的 user 的 id 属性

    user = User.query.filter_by(id=id).first()
    return user


# 添加登录视图，如果是GET方法，返回一个简单的表单

@app.route('/login', methods=['GET'])
def login():
    loginName = request.args.get('loginName')
    user = User.query.filter_by(loginName=loginName).first()
    if not user:
        res = responseData('', 1, '该用户不存在')
    elif request.args.get('password') != user.password:
        res = responseData('', 1, '密码错误')
    else:
        login_user(user, remember=True)
        oldToken = Token.query.filter_by(userId=user.id).first()
        if oldToken:
            oldToken.accessToken = encryptUserId(user.id)
            db.session.merge(oldToken)
            token = oldToken
        else:
            token = Token()
            token.userId = user.id
            token.accessToken = encryptUserId(user.id)
            db.session.add(token)
        res = responseData(token.accessToken)
    return res


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if request.method == 'GET':
        username = request.args.get('username')
        user = User.query.filter_by(username=username).first()
        if not user:
            flash('该用户不存在')
        elif request.args.get('password') != user.password:
            flash('密码错误')
        else:
            login_user(user, remember=True)
            next_url = request.args.get('next')
            return redirect(next_url or url_for('login_success'))
    return 'yeah'


@app.route('/examList', methods=['GET'])
def examList():
    accessToken = request.cookies.get('examToken')
    token = Token.query.filter_by(accessToken=accessToken).first()
    if not token:
        return responseData('', 1, '尚未登录')
    user = User.query.filter_by(id=token.userId).first()
    if not user:
        return responseData('', 2, '用户不存在')
    examList = Exam.query.all()
    examJsonList = [exam.to_json() for exam in examList]
    return responseData(examJsonList)


@app.route('/historyList', methods=['GET'])
def historyList():
    accessToken = request.cookies.get('examToken')
    token = Token.query.filter_by(accessToken=accessToken).first()
    if not token:
        return responseData('', 1, '尚未登录')
    user = User.query.filter_by(id=token.userId).first()
    if not user:
        return responseData('', 2, '用户不存在')
    historyList = History.query.filter_by(userId=user.id).all()
    historyJsonList = [history.to_json() for history in historyList]
    return responseData(historyJsonList)


@app.route('/paperInfo', methods=['GET'])
def paperInfo():
    accessToken = request.cookies.get('examToken')
    token = Token.query.filter_by(accessToken=accessToken).first()
    if not token:
        return responseData('', 1, '尚未登录')
    user = User.query.filter_by(id=token.userId).first()
    if not user:
        return responseData('', 2, '用户不存在')
    examId = request.args.get('examId')
    exam = Exam.query.filter_by(id=examId).first()
    if not exam:
        return responseData('', 3, '未找到考试')
    if datetime.datetime.now() < exam.startTime:
        return responseData('', 4, '考试未开始')
    if datetime.datetime.now() > exam.endTime:
        return responseData('', 4, '考试已结束')
    paper = Paper.query.filter_by(id=exam.paperId).first()
    if not paper:
        return responseData('', 5, '未找到试卷')

    result = paper.to_json()
    # 单选

    questionA = Question.query.filter(Question.id.in_(json.loads(paper.questionAlist))).all()
    result['questionAlist'] = [{'id': question.id,
                      'questionTitle': question.title,
                      'optionMaps': [{'k': option.keys()[0], 'v': option.values()[0]} for option in json.loads(question.options)]} for question in questionA]
    # 多选
    questionB = Question.query.filter(Question.id.in_(json.loads(paper.questionBlist))).all()
    result['questionBlist'] = [{'id': question.id,
                      'questionTitle': question.title,
                      'optionMaps': [{'k': option.keys()[0], 'v': option.values()[0]} for option in json.loads(question.options)]} for question in questionB]
    # 填空
    questionC = Question.query.filter(Question.id.in_(json.loads(paper.questionClist))).all()
    result['questionClist'] = [{'id': question.id,
                      'questionTitle': question.title} for question in questionC]
    # 判断
    questionD = Question.query.filter(Question.id.in_(json.loads(paper.questionDlist))).all()
    result['questionDlist'] = [{'id': question.id,
                      'questionTitle': question.title} for question in questionD]
    # 简答
    questionE = Question.query.filter(Question.id.in_(json.loads(paper.questionElist))).all()
    result['questionElist'] = [{'id': question.id,
                      'questionTitle': question.title} for question in questionE]


    return responseData(result)


@app.route('/exam', methods=['POST'])
def exam():
    accessToken = request.cookies.get('examToken')

    token = Token.query.filter_by(accessToken=accessToken).first()
    if not token:
        return responseData('', 1, '尚未登录')
    user = User.query.filter_by(id=token.userId).first()
    if not user:
        return responseData('', 2, '用户不存在')
    data = json.loads(request.data)
    examId = data['examId']
    exam = Exam.query.filter_by(id=token.userId).first()
    if not exam:
        return responseData('', 2, '考试不存在')
    paper = Paper.query.filter_by(id=exam.paperId).first()
    if not paper:
        return responseData('', 2, '考试不存在')
    questionA = Question.query.filter(Question.id.in_(json.loads(paper.questionAlist))).all()
    questionB = Question.query.filter(Question.id.in_(json.loads(paper.questionBlist))).all()
    questionC = Question.query.filter(Question.id.in_(json.loads(paper.questionClist))).all()
    questionD = Question.query.filter(Question.id.in_(json.loads(paper.questionDlist))).all()
    questionE = Question.query.filter(Question.id.in_(json.loads(paper.questionElist))).all()
    history = History()
    history.examId = examId
    history.studyId = user.studyId
    history.questionAanswer = json.dumps(data['questionAanswer'])
    history.questionBanswer = json.dumps(data['questionBanswer'])
    history.questionCanswer = json.dumps(data['questionCanswer'])
    history.questionDanswer = json.dumps(data['questionDanswer'])
    history.questionEanswer = json.dumps(data['questionEanswer'])
    questionAscore,questionBscore,questionCscore,questionDscore =  0, 0, 0, 0
    for i, question in enumerate(questionA):
        if (question == history.questionAanswer[i]):
            questionAscore += paper.questionAscore
    for i, question in enumerate(questionB):
        if (question == history.questionBanswer[i]):
            questionBscore += paper.questionBscore

    return responseData()

if __name__ == '__main__':
    app.run()
