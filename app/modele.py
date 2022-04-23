#!/usr/bin/env python3

import pymysql
import json


def get_config(config_file_path):
    file = open(config_file_path)
    json_format_file = json.load(file)

    username = json_format_file["username"]
    password = json_format_file["password"]
    ddb_host = json_format_file["ddb_host"]
    ddb_name = json_format_file["ddb_name"]
    file.close()
    return ddb_host, username, password, ddb_name

def get_ddb_acces() :
    try:
        ddb_host, user, password, ddb_name = get_config("config.json")
        acces = pymysql.connect(host = ddb_host, user = user, password = password, database = ddb_name)
    except pymysql.Error as err:
        print("can't connect to database %d: %d" %(err.args[0], err.args[1]))
        exit(84)
    return acces
