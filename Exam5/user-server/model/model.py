# coding=utf8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:!23$56@localhost:3306/school?charset=utf8mb4'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    studyId = db.Column(db.String(32), unique=True)
    studyName = db.Column(db.String(64), unique=True)
    loginName = db.Column(db.String(32), nullable=False)
    cTime = db.Column(db.DateTime, default=datetime.datetime.now)

    def to_json(self):
        json_student = {
            'id': self.id,
            'studyId': self.studyId,
            'loginName': self.loginName,
            'studyName': self.studyName,
            'cTime': str(self.cTime)
        }

        return json_student

    def __repr__(self):
        return '<User %r>' % self.username


class History(db.Model):
    __tablename__ = 'history'
    id = db.Column(db.Integer, primary_key=True)
    studyId = db.Column(db.Integer, unique=True)
    examId = db.Column(db.Integer, unique=True)
    status = db.Column(db.Integer)
    score = db.Column(db.String(10))
    questionAanswer = db.Column(db.String(511))
    questionBanswer = db.Column(db.String(511))
    questionCanswer = db.Column(db.String(511))
    questionDanswer = db.Column(db.String(511))
    questionEanswer = db.Column(db.String(511))
    questionAscore = db.Column(db.String(10))
    questionBscore = db.Column(db.String(10))
    questionCscore = db.Column(db.String(10))
    questionDscore = db.Column(db.String(10))
    questionEscore = db.Column(db.String(10))
    cTime = db.Column(db.DateTime, default=datetime.datetime.now)

    def to_json(self):
        json_student = {
            'id': self.id,
            'studyId': self.studyId,
            'examId': self.examId,
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
            'cTime': str(self.cTime)
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
    cTime = db.Column(db.DateTime, default=datetime.datetime.now)

    def to_json(self):
        json_student = {
            'id': self.id,
            'title': self.title,
            'qType': self.qType,
            'degree': self.degree,
            'options': self.options,
            'answer': self.answer,
            'cTime': str(self.cTime)
        }

        return json_student

    def __repr__(self):
        return '<Question %r>' % self.title


class Paper(db.Model):
    __tablename__ = 'paper'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(511), unique=True)
    questionAList = db.Column(db.String(100))
    questionBList = db.Column(db.String(100))
    questionCList = db.Column(db.String(100))
    questionDList = db.Column(db.String(100))
    questionEList = db.Column(db.String(100))
    degree = db.Column(db.String(10))
    options = db.Column(db.String(511))
    questionAanwser = db.Column(db.String(100))
    questionBanwser = db.Column(db.String(100))
    questionCanwser = db.Column(db.String(100))
    questionDanwser = db.Column(db.String(100))
    cTime = db.Column(db.DateTime, default=datetime.datetime.now)

    def to_json(self):
        json_student = {
            'id': self.id,
            'title': self.title,
            'questionAList': self.questionAList,
            'questionBList': self.questionBList,
            'questionCList': self.questionCList,
            'questionDList': self.questionDList,
            'questionEList': self.questionEList,
            'questionAanwser': self.questionAanwser,
            'questionBanwser': self.questionBanwser,
            'questionCanwser': self.questionCanwser,
            'questionDanwser': self.questionDanwser,
            'degree': self.degree,
            'options': self.options,
            'answer': self.answer,
            'cTime': str(self.cTime)
        }

        return json_student

    def __repr__(self):
        return '<Question %r>' % self.title


class Exam(db.Model):
    __tablename__ = 'exam'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(511), unique=True)
    paperId = db.Column(db.Integer, unique=True)
    startTime = db.Column(db.DateTime)
    endTime = db.Column(db.DateTime)
    cTime = db.Column(db.DateTime, default=datetime.datetime.now)

    def to_json(self):
        json_student = {
            'id': self.id,
            'title': self.title,
            'paperId': self.paperId,
            'startTime': str(self.startTime),
            'endTime': str(self.endTime),
            'cTime': str(self.cTime)
        }

        return json_student

    def __repr__(self):
        return '<Exam %r>' % self.title


class Token(db.Model):
    __tablename__ = 'token'
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, unique=True)
    accessToken = db.Column(db.String(32), unique=True)
    cTime = db.Column(db.DateTime, default=datetime.datetime.now)

    def to_json(self):
        json_student = {
            'id': self.id,
            'userId': self.userId,
            'accessToken': self.accessToken,
            'cTime': str(self.cTime)
        }

        return json_student

    def __repr__(self):
        return '<Token %r>' % self.id


if __name__ == '__main__':
    db.create_all()
