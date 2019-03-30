import json,os

from flask import Flask,flash,Session,session
from flask import make_response,Response
from flask import request,render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = os.urandom(24)
# Session(app)
bootstrap=Bootstrap(app)#Flask扩展一般都在创建实例时初始化，这行代码是Flask-Bootstrap的初始化方法
class User:
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name
@app.route('/')
def index():
    return render_template('index.html')
    # users = []
    # for i in range(1, 11):
    #     user = User(1, "zzm" + str(i))
    #     users.append(user)
    # user = User(1, "hello user")
    # return render_template("demo.html", content="hello flask "
    #         ,user=user,users=users)
@app.route('/<int:id>')
def testid(id):
    return 'Hello World!'+str(id)
@app.route('/a')
def query_user():
    id = request.args
    print(id)
    print(1)
    return "res=="+request.args.get("aaa")

def Response_headers(content):
    resp = Response(content)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp
@app.route('/test', methods=['POST'])
def test():
    if request.method == 'POST' and request.form.get('aaa'):
        datax = request.form.to_dict()
        content = str(datax)
        resp = Response_headers(content)
        return resp
    else:
        content = json.dumps({"error_code":"1001"})
        resp = Response_headers(content)
        return resp
@app.route('/flashDemo')
def flash_demo():
    flash("hello world flash")
    return render_template("flash.html")
# @app.route("/login",methods=["POST"])
@app.route("/login")
def loginPost():
    return render_template("/login.html")
    # username=request.form.get("username","")
    # password=request.form.get("password","")
    # if username=="test" and password=="123" :
    #     session["user"]=username
    #     return render_template("/index.html")
    # else:
    #     return "登录失败"

@app.errorhandler(404)
def not_fond(e):
    return render_template("404.html")
if __name__ == '__main__':
    app.run(port=8000,debug=True)
