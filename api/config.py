# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os
from datetime import timedelta

BASE_DIR = os.path.dirname(os.path.realpath(__file__))


class BaseConfig():

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'apidata.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '_Y7y2L"Fh!i%yksfec]/'
    JWT_SECRET_KEY = '_Y7y2L"F4Q8z@q$fec]/'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
