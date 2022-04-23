#!/usr/bin/env python3

from flask import render_template, request, redirect, url_for
from app import app
from app.controller import *

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def display_bingo():
    return render_template("bingo.html",
                           title = "Minecraft Bingo",
                           title_body = "Bingo")
                        
@app.route('/chalengeManager', methods=['GET'])
def chalenge_manager():
    return render_template("chalenge.html",
                            title="Chalenge Manager",
                            chalenges = getChalenges())