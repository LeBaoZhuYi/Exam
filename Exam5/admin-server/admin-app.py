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
    if not user or not loginName == 'admin':
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


@app.route('/questionList', methods=['GET'])
def questionList():
    accessToken = request.cookies.get('examAdminToken')
    token = Token.query.filter_by(accessToken=accessToken).first()
    if not token:
        return responseData('', 1, '尚未登录')
    user = User.query.filter_by(id=token.userId).first()
    if not user:
        return responseData('', 2, '用户不存在')
    questionList = Question.query.order_by(Question.ctime.desc()).all()
    questionJsonList = [question.to_json() for question in questionList]
    return responseData(questionJsonList)

@app.route('/paperList', methods=['GET'])
def paperList():
    accessToken = request.cookies.get('examAdminToken')
    token = Token.query.filter_by(accessToken=accessToken).first()
    if not token:
        return responseData('', 1, '尚未登录')
    user = User.query.filter_by(id=token.userId).first()
    if not user:
        return responseData('', 2, '用户不存在')
    paperList = Paper.query.order_by(Paper.ctime.desc()).all()
    paperJsonList = [paper.to_json() for paper in paperList]
    return responseData(paperJsonList)

@app.route('/examList', methods=['GET'])
def examList():
    accessToken = request.cookies.get('examAdminToken')
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
    accessToken = request.cookies.get('examAdminToken')
    token = Token.query.filter_by(accessToken=accessToken).first()
    if not token:
        return responseData('', 1, '尚未登录')
    user = User.query.filter_by(id=token.userId).first()
    if not user:
        return responseData('', 2, '用户不存在')
    historyList = History.query.order_by(History.ctime.desc()).all()
    historyJsonList = []
    for history in historyList:
        history_json = history.to_json()
        if history.score == None:
            exam = Exam.query.filter_by(id=history.examId).first()
            paper = Paper.query.filter_by(id=exam.paperId).first()
            questionEidList = json.loads(paper.questionElist)
            questionElist = Question.query.filter(Question.id.in_(questionEidList)).all()
            questionEanswer = json.loads(history.questionEanswer)
            history_json['questionEinfoList'] = [{'title': questionElist[i].title, 'answer': questionEanswer[i], 'score': 0} for i in range(0, len(questionElist))]
        historyJsonList.append(history_json)
    return responseData(historyJsonList)

@app.route('/userList', methods=['GET'])
def userList():
    accessToken = request.cookies.get('examAdminToken')
    token = Token.query.filter_by(accessToken=accessToken).first()
    if not token:
        return responseData('', 1, '尚未登录')
    user = User.query.filter_by(id=token.userId).first()
    if not user:
        return responseData('', 2, '用户不存在')
    userList = User.query.order_by(User.ctime.desc()).all()
    userJsonList = []
    for user in userList:
        if not user.loginName == 'admin':
            userJsonList.append(user.to_json())
    return responseData(userJsonList)

@app.route('/addUser', methods=['POST'])
def addUser():
    accessToken = request.cookies.get('examAdminToken')
    token = Token.query.filter_by(accessToken=accessToken).first()
    if not token:
        return responseData('', 1, '尚未登录')
    user = User.query.filter_by(id=token.userId).first()
    if not user:
        return responseData('', 2, '用户不存在')
    data = json.loads(request.data)

    try:
        loginName= data['loginName']
        studyName= data['studyName']
        password= data['password']
        studyId= data['studyId']
        user = User()
        user.loginName = loginName
        user.studyName = studyName
        user.password = password
        user.studyId = studyId
        db.session.add(user)
    except Exception as e:
        return responseData('',1, '添加失败，请检查输入数据')
    return responseData(None)

@app.route('/addPaper', methods=['POST'])
def addPaper():
    accessToken = request.cookies.get('examAdminToken')
    token = Token.query.filter_by(accessToken=accessToken).first()
    if not token:
        return responseData('', 1, '尚未登录')
    user = User.query.filter_by(id=token.userId).first()
    if not user:
        return responseData('', 2, '用户不存在')
    data = json.loads(request.data)

    try:
        title= data['title']
        questionAlist= json.dumps(data['questionAlist'].split(','))
        questionBlist= json.dumps(data['questionBlist'].split(','))
        questionClist= json.dumps(data['questionClist'].split(','))
        questionDlist= json.dumps(data['questionDlist'].split(','))
        questionElist= json.dumps(data['questionElist'].split(','))
        questionAscore = data['questionAscore']
        questionBscore = data['questionBscore']
        questionCscore = data['questionCscore']
        questionDscore = data['questionDscore']
        questionEscore = data['questionEscore']
        degree = data['degree']
        paper = Paper()
        paper.title = title
        paper.questionAlist = questionAlist
        paper.questionBlist = questionBlist
        paper.questionClist = questionClist
        paper.questionDlist = questionDlist
        paper.questionElist = questionElist
        paper.questionAscore = questionAscore
        paper.questionBscore = questionBscore
        paper.questionCscore = questionCscore
        paper.questionDscore = questionDscore
        paper.questionEscore = questionEscore
        paper.degree = degree
        db.session.add(paper)
    except Exception as e:
        return responseData('',1, '添加失败，请检查题号格式')
    return responseData(None)

@app.route('/addExam', methods=['POST'])
def addExam():
    accessToken = request.cookies.get('examAdminToken')
    token = Token.query.filter_by(accessToken=accessToken).first()
    if not token:
        return responseData('', 1, '尚未登录')
    user = User.query.filter_by(id=token.userId).first()
    if not user:
        return responseData('', 2, '用户不存在')
    data = json.loads(request.data)

    try:
        paperId= data['paperId']
        title= data['title']
        startTime= data['startTime']
        endTime= data['endTime']
        exam = Exam()
        exam.title = title
        exam.paperId = paperId
        exam.startTime = startTime
        exam.endTime = endTime
        db.session.add(exam)
    except Exception as e:
        return responseData('',1, '添加失败，请检查输入数据')
    return responseData(None)

@app.route('/addQuestionA', methods=['POST'])
def addQuestionA():
    accessToken = request.cookies.get('examAdminToken')
    token = Token.query.filter_by(accessToken=accessToken).first()
    if not token:
        return responseData('', 1, '尚未登录')
    user = User.query.filter_by(id=token.userId).first()
    if not user:
        return responseData('', 2, '用户不存在')
    data = json.loads(request.data)
    try:
        degree= data['degree']
        title= data['title']
        optionA= data['optionA']
        optionB= data['optionB']
        optionC= data['optionC']
        optionD= data['optionD']
        answer= data['answer']
        question = Question()
        question.title = title
        question.degree = degree
        question.answer = answer
        question.options = json.dumps([{'A': optionA, 'B': optionB, 'C': optionC, 'D': optionD}])
        question.qType = '单选题'
        db.session.add(question)
    except Exception as e:
        return responseData('',1, '添加失败，请检查输入数据')
    return responseData(None)

@app.route('/addQuestionB', methods=['POST'])
def addQuestionB():
    accessToken = request.cookies.get('examAdminToken')
    token = Token.query.filter_by(accessToken=accessToken).first()
    if not token:
        return responseData('', 1, '尚未登录')
    user = User.query.filter_by(id=token.userId).first()
    if not user:
        return responseData('', 2, '用户不存在')
    data = json.loads(request.data)
    try:
        degree= data['degree']
        title= data['title']
        optionA= data['optionA']
        optionB= data['optionB']
        optionC= data['optionC']
        optionD= data['optionD']
        answer= duoxuan_r[data['answer']]
        question = Question()
        question.title = title
        question.degree = degree
        question.answer = answer
        question.options = json.dumps([{'A': optionA, 'B': optionB, 'C': optionC, 'D': optionD}])
        question.qType = '多选题'
        db.session.add(question)
    except Exception as e:
        return responseData('',1, '添加失败，请检查输入数据')
    return responseData(None)

@app.route('/addQuestionC', methods=['POST'])
def addQuestionC():
    accessToken = request.cookies.get('examAdminToken')
    token = Token.query.filter_by(accessToken=accessToken).first()
    if not token:
        return responseData('', 1, '尚未登录')
    user = User.query.filter_by(id=token.userId).first()
    if not user:
        return responseData('', 2, '用户不存在')
    data = json.loads(request.data)
    try:
        degree= data['degree']
        title= data['title']
        answer= data['answer']
        question = Question()
        question.title = title
        question.degree = degree
        question.answer = answer
        question.options = '[]'
        question.qType = '填空题'
        db.session.add(question)
    except Exception as e:
        return responseData('',1, '添加失败，请检查输入数据')
    return responseData(None)

@app.route('/addQuestionD', methods=['POST'])
def addQuestionD():
    accessToken = request.cookies.get('examAdminToken')
    token = Token.query.filter_by(accessToken=accessToken).first()
    if not token:
        return responseData('', 1, '尚未登录')
    user = User.query.filter_by(id=token.userId).first()
    if not user:
        return responseData('', 2, '用户不存在')
    data = json.loads(request.data)
    try:
        degree= data['degree']
        title= data['title']
        answer= data['answer']
        question = Question()
        question.title = title
        question.degree = degree
        question.answer = answer
        question.options = '[]'
        question.qType = '判断题'
        db.session.add(question)
    except Exception as e:
        return responseData('',1, '添加失败，请检查输入数据')
    return responseData(None)

@app.route('/addQuestionE', methods=['POST'])
def addQuestionE():
    accessToken = request.cookies.get('examAdminToken')
    token = Token.query.filter_by(accessToken=accessToken).first()
    if not token:
        return responseData('', 1, '尚未登录')
    user = User.query.filter_by(id=token.userId).first()
    if not user:
        return responseData('', 2, '用户不存在')
    data = json.loads(request.data)
    try:
        degree= data['degree']
        title= data['title']
        question = Question()
        question.title = title
        question.degree = degree
        question.answer = ''
        question.options = '[]'
        question.qType = '简答题'
        db.session.add(question)
    except Exception as e:
        return responseData('',1, '添加失败，请检查输入数据')
    return responseData(None)
if __name__ == '__main__':
    # db.create_all()
    app.run(port=5001)
