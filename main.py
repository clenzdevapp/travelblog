from flask import Flask, render_template,request, redirect, url_for, make_response

import sqlite3
import hashlib
import datetime
import uuid

#import models.User

app=Flask(__name__)#MODEL
#db.create_all()

@app.route("/", methods=["GET"])#CONTROLLER
def index():
