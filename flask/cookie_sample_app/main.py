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

@app.route('/')
def static_main_page():

    #
    #cookie の有無を確認し、出力を行う
    #
    privious_word = request.cookies.get('cookie_sample')
    print (privious_word)
    if privious_word is None:
        print ("is None type.")
        pword_text = 'ex) Hello World.'
    else :
        pword_text = 'ex)' + privious_word

    print(pword_text)
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

        #cookieの設定を行う
        key_name = "cookie_sample"
        key_value = input_value
        max_age = 60 * 24 #expire 1day.
        expires = int(datetime.now().timestamp()) + max_age
        path = "/"
        domain = None
        
        response.set_cookie(key_name,key_value,max_age,expires,path,domain,secure=None, httponly=False)
        return response

    return render_template("article1.html", output_value=input_value)

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
