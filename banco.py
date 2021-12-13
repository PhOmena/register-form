import sqlite3
from sqlite3 import Error
import os

pastaApp=os.path.dirname(__file__)
name_database=pastaApp+"\\itens.db"

def db_connection():
    con=None
    try:
        con=sqlite3.connect(name_database)
    except Error as ex:
        print(ex)
    return con

def dql(query):
    vcon=db_connection()
    c=vcon.cursor()
    c.execute(query)
    res=c.fetchall()
    vcon.close()
    return res

def dml(query):
    try:
        vcon=db_connection()
        c=vcon.cursor()
        c.execute(query)
        vcon.commit()
        vcon.close()
    except Error as ex:
        print(ex)
    