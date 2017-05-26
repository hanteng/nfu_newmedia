webapp_pick_a_color
# 简介 
webapp_pick_a_color 选取的颜色，操练Python语言开发练习：使用flask

## 档
### Python档
#### webapp_pick_a_color.py
唯一app档，可双击执行（若作业环境允许）或於命令行输入

python webapp_pick_a_color.py 

执行

### html模版档 放在目录templates下
#### base.html
基本flask html模版档

#### entry.html
flask html模版档，用户输入页使用 def entry_page() 'html': #使用了 entry.html

#### results.html
flask html模版档，用户输出结果页使用 def pick_a_color() -> 'html': #使用了 results.html


## Web App动作描述

以下按web 请求（web request） - web 响应 时序说明

1. 後端伺服器启动：执行 webapp_pick_a_color.py 启动後端伺服器，等待web 请求。启动成功应出现：  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

2. 前端浏览器web 请求：访问 http://127.0.0.1:5000/ 启动前端web 请求

3. 後端伺服器web 响应：webapp_pick_a_color.py 中 执行 了@app.route('/') 下的 entry_page()函数，产生《欢迎来到网上选色》的HTML页面
def entry_page() -> 'html': #使用了 entry.html
    ...略...
    return render_template('entry.html',

4. 前端浏览器收到web 响应：出现HTML，有HTML5表单的输入 input 类型(type) 为"color"，变数名称(name)为"user_color"

5. 前端浏览器web 请求：用户选取颜色後按了提交钮「搞吧」，则产生新的web 请求，按照form元素中定义的method='POST' action='/pick_a_color'，以POST为方法，动作为/pick_a_color的web 请求

6. 後端服务器收到用户web 请求，匹配到@app.route('/pick_a_color', methods=['POST'])的函数 pick_a_color() 

7. def pick_a_color() 函数，几乎什麽也没做，只有把用户提交的数据，以flask 模块request.form['user_color'] （注意第一行代码 from flask import Flask, render_template, request, escape 有request，是从flask模块调用的）取到Web 请求中，HTML表单变数名称user_color的值，存放在user_color这Python变数下，再使用flask模块render_template 函数把results.html模版（输出），其中模版中the_color的值，用user_color这变数之值。
def pick_a_color() -> 'html': #使用了 results.html
    ...略...
    return render_template('results.html', 以下略

8. 前端浏览器收到web 响应：results.html模版中the_color的值正确的产生的话，前端浏览器会收到正确响应，看到颜色代码。

