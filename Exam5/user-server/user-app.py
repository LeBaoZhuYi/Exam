#coding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from model.user import User
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, redirect, url_for, request, flash, render_template
from flask_login import LoginManager, login_user, login_required, logout_user

app = Flask(__name__)
app.secret_key = 'Sqsdsffqrhgh.,/1#$%^&'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:!23$56@localhost:3306/school?charset=utf8mb4'
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

@app.route('/login/', methods=['GET', 'POST'])
def login():
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


@app.route('/')
@login_required
def index():
    return 'Hello Tank'


@app.route('/succees')
@login_required
def login_success():
    return 'success'


@app.route('/logout')
@login_required
def logout():
    logout_user()  # 登出用户
    return '已经退出登录'


@app.errorhandler(404)
def page_not_found(error):
    return 'error'


if __name__ == '__main__':
    app.run()