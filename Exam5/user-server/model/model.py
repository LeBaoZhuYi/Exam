# coding=utf8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
from flask import Flask
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:!23$56@localhost:3306/exam5?charset=utf8'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)


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
    questionAanswer = db.Column(db.String(511))
    questionBanswer = db.Column(db.String(511))
    questionCanswer = db.Column(db.String(511))
    questionDanswer = db.Column(db.String(511))
    questionEanswer = db.Column(db.String(511))
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


if __name__ == '__main__':
    db.create_all()
