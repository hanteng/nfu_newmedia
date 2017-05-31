# -*- coding: utf-8 -*- 
# 使用模块module country
import country  
c = country.country_list_name()
c_list = [c.data[k] for k in sorted(c.data.keys())]
c_dict_reverse = {v:k for k, v in c.data.items()}


from flask import Flask, render_template, request, escape

app = Flask(__name__)

@app.route('/')
@app.route('/entry')

def entry_page() -> 'html':
    """Display this webapp's HTML form."""
    return render_template('entry.html',
                           the_list_items = c_list ,
                           the_title='欢迎来到网上选国！')

@app.route('/pick_a_country', methods=['POST'])
def pick_a_color() -> 'html':
    """提取用户web 请求POST方法提交的数据（输入），不执行任何动作（处理），直接返回（输出）。"""
    user_country_name = request.form['user_country']	
    user_country_code = c_dict_reverse[user_country_name]	
    return render_template('results.html',
                           the_title = '以下是您选取的国：',
                           the_country_code = user_country_code,
                           the_country_name = user_country_name,
                           )

if __name__ == '__main__':
    app.run(debug=True)
