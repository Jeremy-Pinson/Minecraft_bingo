#!/usr/bin/env python3

from flask import Flask
import os

app = Flask(__name__)
app.config.from_mapping(SECRET_KEY='dev', DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'))
from app import views
