"""
=================================================
@Project -> File    ：flask2 -> xxxxxxxxx
@IDE                ：PyCharm
@Author             ：沈泽昊
@Date               ：2022/8/23 9:57
@用途               ：
==================================================
"""
from redis import Redis

conn=Redis(host="127.0.0.1")
v=conn.keys()
print(v)