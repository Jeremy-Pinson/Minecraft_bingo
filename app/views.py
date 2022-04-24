#!/usr/bin/env python3

## Jérémy Pinson
## Bingo Race Minecraft
## 04/2022

from flask import render_template, request, redirect, url_for
from app import app
from app.controller import *
import random

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def display_bingo():
    return render_template("bingo.html",
                           title = "Minecraft Bingo",
                           chalenges = random.sample(getChalenges(), 25))
                        
@app.route('/chalengeManager', methods=['GET'])
def chalenge_manager():
    return render_template("chalenge.html",
                            title="Chalenge Manager",
                            chalenges = getChalenges())