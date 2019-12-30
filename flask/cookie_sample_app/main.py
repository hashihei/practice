# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python37_app]
from flask import Flask, render_template, request , make_response
from datetime import datetime

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


#
# response に対し、cookie name, cookie valueを設定する
#
def set_cookie_value(name, value, response):
    
    #cookieの値を設定する
    key_name = name
    key_value = value
    
    #cookie全般の設定を行う
    max_age = 60 * 24 #expire 1day.
    expires = int(datetime.now().timestamp()) + max_age
    path = "/"
    domain = None
    
    #cookieをセット
    response.set_cookie(key_name,key_value,max_age,expires,path,domain,secure=None, httponly=False)

    #cookieをセットしたresponseを返す
    return response

@app.route('/')
def static_main_page():

    #
    #cookie の有無を確認し、出力を行う
    #
    privious_word = request.cookies.get('cookie_test.hashihei.com')

    #cookie の有無を確認
    if privious_word is None:
        pword_text = 'ex) Hello World.'
    else :
        #cookieがセットされていれば、内容を例として表示
        pword_text = 'ex) ' + privious_word

    return render_template("index.html",pword=pword_text)


@app.route('/article1', methods=['GET', 'POST'])
def static_article_page():
    if request.method == 'GET':
        input_value = request.args.get('input1')
    elif request.method == 'POST':
        input_value = request.form['input1']

    #POSTの際はcookieに入力値を設定する
    #cookieを返すためのresponseオブジェクトを作成する
    cookie_content = render_template("article1.html", output_value=input_value)
    response = make_response(cookie_content)

    #cookieの値をセットする
    response = set_cookie_value("cookie_test.hashihei.com", input_value, response)        

    #article1を表示し、ブラウザにcookieをセットする
    return response

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
