"""
=================================================
@Project -> File    ：flask3 -> models
@IDE                ：PyCharm
@Author             ：沈泽昊
@Date               ：2022/8/27 9:49
@用途               ：
==================================================
"""
from sqlalchemy import Column, Integer, UniqueConstraint, Index, DateTime, ForeignKey,String
from flask3 import db



class Users(db.Model):
    __tablename="lianxi"
    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String(32),nullable=False,unique=True)





