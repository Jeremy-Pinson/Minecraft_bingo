#!/usr/bin/env python3

## Jérémy Pinson
## Bingo Race Minecraft
## 04/2022

from app.modele import get_ddb_acces
import pymysql

def getChalenges():
    acces = get_ddb_acces()
    with acces:
        with acces.cursor() as cursor:
            request = "SELECT * FROM chalenges"
            cursor.execute(request)
            chalengesList = cursor.fetchall()
    return chalengesList
        
def addChalenge(cName, Cimg, Cdescription):
    acces = get_ddb_acces()
    with acces:
        with acces.cursor() as cursor:
            request = "INSERT INTO chalenges (chalenge_name, chalenge_png_location, chalenge_description) VALUES (%s, %s, %s) "
            cursor.execute(request)