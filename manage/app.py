from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/login',methods=['GET','POST'])
def index():
    if request.method=='GET':
        return render_template('login.html')
    #request.args #获取GET传来的参数
    request.form.get('user')#获取POST参数


if __name__=='__main__':
    app.run()