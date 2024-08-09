"""
=================================================
@Project -> File    ：flask3 -> 信号
@IDE                ：PyCharm
@Author             ：沈泽昊
@Date               ：2022/8/28 15:33
@用途               ：
==================================================
"""
from flask import Flask,signals

app=Flask(__name__)
app.debug=True

def func1(*args,**kwargs):
    print("你好request_started")
def func2(*args,**kwargs):
    print("request_finished")
signals.request_started.connect(func1)
signals.request_finished.connect(func2)
@app.route("/login")
def login():
    print("你好")
    return "登录成功"





if __name__ == '__main__':
    app.run()