 # -*- coding: utf-8 -*- 
from flask import Flask, render_template, request, escape
from datetime import datetime, timedelta
app = Flask(__name__)


def log_request(req: 'flask_request', res: str) -> None:
    """Log details of the web request and the results."""
    with open('appoint.log', 'a', encoding='utf8') as log:
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')


@app.route('/appointment', methods=['POST'])
def do_appointment() -> 'html':
    """Extract the posted data; perform the search; return results."""
    print(request.form)
    title = '以下是您預约的结果：'
    #user_datetime_end = user_datetime + 30
    #print (type(user_datetime_end))
    results = {k:request.form[k] for k in {'user_email', 'user_github','user_date', 'user_time'}}
    user_date = request.form['user_date']	
    user_time = request.form['user_time']
    datetime_begin = datetime.strptime(user_date+" "+user_time, '%Y-%m-%d %H:%M')	
    datetime_end = timedelta(minutes=30) + datetime_begin	
    print (datetime_begin)
    log_request(request, results)
    return render_template('results.html',
                           the_title = title,
                           the_id = results['user_github'],
                           the_email = results['user_email'],
                           the_dt_begin=datetime_begin,
                           the_dt_end=datetime_end,
                           )


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    """Display this webapp's HTML form."""
    return render_template('entry.html',
                           the_title='欢迎来到网上預约！')


@app.route('/viewlog')
def view_the_log() -> 'html':
    """Display the contents of the log file as a HTML table."""
    contents = []
    with open('vsearch.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('表单内容', '访问者IP', '浏览器', '运行结果')
    return render_template('viewlog.html',
                           the_title='查看日志',
                           the_row_titles=titles,
                           the_data=contents,)


if __name__ == '__main__':
    app.run(debug=True)
