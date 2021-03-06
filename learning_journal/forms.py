# -*- coding: utf-8 -*-
from wtforms import Form, BooleanField, StringField, validators


class EntryForm(Form):
    title = StringField('title', [validators.length(min=4, max=128)])
    text = StringField('text', [validators.InputRequired()])


class LoginForm(Form):
    username = StringField('username', [validators.length(min=4, max=128)])
    password = StringField('password', [validators.length(min=4, max=128)])
