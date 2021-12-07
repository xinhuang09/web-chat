from app import app
from flask import render_template, redirect, url_for
from models import Message, db
import forms
from datetime import datetime

@app.route('/')
@app.route('/index')
def index():
    messages = Message.query.all()
    return render_template('index.html', messages=messages)

@app.route('/message', methods=['GET', 'POST'])
def about():
    form = forms.AddMessage()
    if form.validate_on_submit():
        M = Message(title=form.title.data, date=datetime.utcnow())
        db.session.add(M)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('message.html', form=form)