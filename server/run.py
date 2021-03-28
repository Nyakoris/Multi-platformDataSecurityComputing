# -*- coding: UTF-8 -*-
import os
import json
from flask import Flask
from flask import request


app = Flask(__name__)

@app.route('/')
def init():
    return 'it`s init'

@app.route('/func',methods=['GET','POST'])
def cacl():
    input_data1 = int(request.args.get('text1'))
    input_data2 = int(request.args.get('text2'))
    return 'the result text1*text2 is {}'.format(input_data1*input_data2)
    
    #res=int(text1)*int(text2)


def main():
    app.run(host='127.0.0.1',port=5000)

if __name__=='__main__':
    main()

