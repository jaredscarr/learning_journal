# -*- coding: utf-8 -*-
import os
from pyramid.security import (
    Allow,
    Everyone,
    ALL_PERMISSIONS,
    Authenticated
    )

from passlib.apps import custom_app_context as pl
from wtforms.ext.csrf.form import SecureForm


class DefaultRoot(object):
    """I Hope this is the right place for an acl."""
    __acl__ = [(Allow, Everyone, 'view'),
               (Allow, Authenticated, 'edit')]

    def __init__(self, request):
        """Init."""
        self.request = request


def check_pwd(password):
    hashed = os.environ.get('AUTH_PASSWORD', 'this is not a password')
    return pl.verify(password, hashed)
