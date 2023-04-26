from flask import Flask, request, url_for, flash, redirect
from flask import render_template


app = Flask(__name__)
messages = [{'title': 'Message One',
             'content': 'Message One Content'},
            {'title': 'Message Two',
             'content': 'Message Two Content'}
            ]

@app.route('/', methods=('GET', 'POST'))
def home():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:
            messages.append({'title': title, 'content': content})
            return redirect(url_for('index'))
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/sources')
def sources():
	return render_template("sources.html")


if __name__ == '__main__':
    app.run(debug=True)