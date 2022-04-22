#!/usr/bin/env python3

from flask import render_template, request, redirect, url_for
from app import app

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def list_task():
    return render_template("bingo.html",
                           title="Minecraft Bingo",
                           title_body="Bingo")