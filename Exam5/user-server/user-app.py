# coding=utf8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
import json, datetime
from flask_login import UserMixin
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
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    studyId = db.Column(db.String(32), unique=True)
    studyName = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64))
    loginName = db.Column(db.String(32), nullable=False)
    ctime = db.Column(db.DateTime, default=datetime.datetime.now)

    def to_json(self):
        json_student = {
            'id': self.id,
            'studyId': self.studyId,
            'loginName': self.loginName,
            'studyName': self.studyName,
            'ctime': str(self.ctime)
        }

        return json_student

    def __repr__(self):
        return '<User %r>' % self.username


class History(db.Model):
    __tablename__ = 'history'
    id = db.Column(db.Integer, primary_key=True)
    studyId = db.Column(db.Integer)
    studyName = db.Column(db.Integer)
    examId = db.Column(db.Integer)
    examTitle = db.Column(db.Integer)
    status = db.Column(db.String(10))
    score = db.Column(db.Integer)
    degree = db.Column(db.String(10))
    questionAanswer = db.Column(db.String(511))
    questionBanswer = db.Column(db.String(511))
    questionCanswer = db.Column(db.String(511))
    questionDanswer = db.Column(db.String(511))
    questionEanswer = db.Column(db.String(511))
    questionAright = db.Column(db.String(511))
    questionBright = db.Column(db.String(511))
    questionCright = db.Column(db.String(511))
    questionDright = db.Column(db.String(511))
    questionAscore = db.Column(db.Integer)
    questionBscore = db.Column(db.Integer)
    questionCscore = db.Column(db.Integer)
    questionDscore = db.Column(db.Integer)
    questionEscore = db.Column(db.Integer)
    ctime = db.Column(db.DateTime, default=datetime.datetime.now)

    def to_json(self):
        json_student = {
            'id': self.id,
            'studyId': self.studyId,
            'examId': self.examId,
            'studyName': self.studyName,
            'examTitle': self.examTitle,
            'status': self.status,
            'score': self.score,
            'degree': self.degree,
            'questionAanswer': self.questionAanswer,
            'questionBanswer': self.questionBanswer,
            'questionCanswer': self.questionCanswer,
            'questionDanswer': self.questionDanswer,
            'questionEanswer': self.questionEanswer,
            'questionAscore': self.questionAscore,
            'questionBscore': self.questionBscore,
            'questionCscore': self.questionCscore,
            'questionDscore': self.questionDscore,
            'questionEscore': self.questionEscore,
            'questionAright': self.questionAright,
            'questionBright': self.questionBright,
            'questionCright': self.questionCright,
            'questionDright': self.questionDright,
            'ctime': str(self.ctime)
        }

        return json_student

    def __repr__(self):
        return '<History %r>' % self.id


class Question(db.Model):
    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(511), unique=True)
    qType = db.Column(db.String(10))
    degree = db.Column(db.String(10))
    options = db.Column(db.String(511))
    answer = db.Column(db.String(64))
    ctime = db.Column(db.DateTime, default=datetime.datetime.now)

    def to_json(self):
        json_student = {
            'id': self.id,
            'title': self.title,
            'qType': self.qType,
            'degree': self.degree,
            'options': self.options,
            'answer': self.answer,
            'ctime': str(self.ctime)
        }

        return json_student

    def __repr__(self):
        return '<Question %r>' % self.title


class Paper(db.Model):
    __tablename__ = 'paper'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(511), unique=True)
    questionAlist = db.Column(db.String(100))
    questionBlist = db.Column(db.String(100))
    questionClist = db.Column(db.String(100))
    questionDlist = db.Column(db.String(100))
    questionElist = db.Column(db.String(100))
    degree = db.Column(db.String(10))
    questionAscore = db.Column(db.Integer)
    questionBscore = db.Column(db.Integer)
    questionCscore = db.Column(db.Integer)
    questionDscore = db.Column(db.Integer)
    questionEscore = db.Column(db.Integer)
    ctime = db.Column(db.DateTime, default=datetime.datetime.now)

    def to_json(self):
        json_student = {
            'id': self.id,
            'title': self.title,
            'questionAlist': self.questionAlist,
            'questionBlist': self.questionBlist,
            'questionClist': self.questionClist,
            'questionDlist': self.questionDlist,
            'questionElist': self.questionElist,
            'questionAscore': self.questionAscore,
            'questionBscore': self.questionBscore,
            'questionCscore': self.questionCscore,
            'questionDscore': self.questionDscore,
            'questionEscore': self.questionEscore,
            'degree': self.degree,
            'ctime': str(self.ctime)
        }

        return json_student

    def __repr__(self):
        return '<Question %r>' % self.title


class Exam(db.Model):
    __tablename__ = 'exam'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(511), unique=True)
    paperId = db.Column(db.Integer)
    degree = db.Column(db.String(10))
    startTime = db.Column(db.DateTime)
    endTime = db.Column(db.DateTime)
    ctime = db.Column(db.DateTime, default=datetime.datetime.now)

    def to_json(self):
        json_student = {
            'id': self.id,
            'title': self.title,
            'paperId': self.paperId,
            'degree': self.degree,
            'startTime': str(self.startTime),
            'endTime': str(self.endTime),
            'ctime': str(self.ctime)
        }

        return json_student

    def __repr__(self):
        return '<Exam %r>' % self.title


class Token(db.Model):
    __tablename__ = 'token'
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, unique=True)
    accessToken = db.Column(db.String(32), unique=True)
    ctime = db.Column(db.DateTime, default=datetime.datetime.now)

    def to_json(self):
        json_student = {
            'id': self.id,
            'userId': self.userId,
            'accessToken': self.accessToken,
            'ctime': str(self.ctime)
        }

        return json_student

    def __repr__(self):
        return '<Token %r>' % self.id

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
    examList = Exam.query.order_by(Exam.ctime.desc()).all()
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
    historyList = History.query.filter_by(studyId=user.studyId).order_by(History.ctime.desc()).all()
    # results = []
    # for history in historyList:
    #     result = history.to_json

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
                                'optionMaps': [{'k': option.keys()[0], 'v': option.values()[0]} for option in
                                               json.loads(question.options)]} for question in questionA]
    # 多选
    questionB = Question.query.filter(Question.id.in_(json.loads(paper.questionBlist))).all()
    result['questionBlist'] = [{'id': question.id,
                                'questionTitle': question.title,
                                'optionMaps': [{'k': option.keys()[0], 'v': option.values()[0]} for option in
                                               json.loads(question.options)]} for question in questionB]
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
    examId = int(data['examId'])
    exam = Exam.query.filter_by(id=examId).first()
    if not exam:
        return responseData('', 2, '考试不存在')
    paper = Paper.query.filter_by(id=exam.paperId).first()
    if not paper:
        return responseData('', 2, '考试不存在')
    questionA = Question.query.filter(Question.id.in_(json.loads(paper.questionAlist))).all()
    questionB = Question.query.filter(Question.id.in_(json.loads(paper.questionBlist))).all()
    questionC = Question.query.filter(Question.id.in_(json.loads(paper.questionClist))).all()
    questionD = Question.query.filter(Question.id.in_(json.loads(paper.questionDlist))).all()
    history = History()
    history.examId = examId
    history.examTitle = exam.title
    history.degree = exam.degree
    history.studyId = user.studyId
    history.studyName = user.studyName
    history.questionAanswer = json.dumps(data['questionAanswer'])
    history.questionBanswer = json.dumps(duoxuanTransfer(data['questionBanswer']))
    history.questionCanswer = json.dumps(data['questionCanswer'],ensure_ascii=False)
    history.questionDanswer = json.dumps(data['questionDanswer'],ensure_ascii=False)
    history.questionEanswer = json.dumps(data['questionEanswer'],ensure_ascii=False)
    history.questionAscore, history.questionBscore, history.questionCscore, history.questionDscore, history.questionEscore = 0, 0, 0, 0, 0
    questionAright,questionBright,questionCright,questionDright = [],[],[],[]
    for i, question in enumerate(questionA):
        questionAright.append(question.answer)
        if (question.answer == data['questionAanswer'][i]):
            history.questionAscore += paper.questionAscore
    for i, question in enumerate(questionB):
        questionBright.append(question.answer)
        if (question.answer == str(data['questionBanswer'][i])):
            history.questionBscore += paper.questionBscore
    for i, question in enumerate(questionC):
        questionCright.append(question.answer)
        if (question.answer == data['questionCanswer'][i]):
            history.questionCscore += paper.questionCscore
    for i, question in enumerate(questionD):
        questionDright.append(question.answer)
        if (question.answer == data['questionDanswer'][i]):
            history.questionDscore += paper.questionDscore
    history.questionAright = json.dumps(questionAright)
    history.questionBright = json.dumps(duoxuanTransfer(questionBright))
    history.questionCright = json.dumps(questionCright,ensure_ascii=False)
    history.questionDright = json.dumps(questionDright,ensure_ascii=False)
    history.status = '批卷中'
    db.session.add(history)
    return responseData(None)


if __name__ == '__main__':
    # db.create_all()
    app.run()
