 # -*- coding: utf-8 -*- 
from flask import Flask, render_template, request, escape

app = Flask(__name__)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    """Display this webapp's HTML form."""
    return render_template('entry.html',
                           the_title='欢迎来到网上选色！')

@app.route('/pick_a_color', methods=['POST'])
def pick_a_color() -> 'html':
    """提取用户web 请求POST方法提交的数据（输入），不执行任何动作（处理），直接返回（输出）。"""
    user_color = request.form['user_color']	
    return render_template('results.html',
                           the_title = '以下是您选取的颜色：',
                           the_color = user_color,
                           )

if __name__ == '__main__':
    app.run(debug=True)
