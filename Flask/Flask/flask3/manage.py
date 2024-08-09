"""
=================================================
@Project -> File    ：flask3 -> manage
@IDE                ：PyCharm
@Author             ：沈泽昊
@Date               ：2022/8/27 8:50
@用途               ：
==================================================
"""
from flask3 import create_app,db
from flask_migrate import Migrate
app = create_app()

migrate=Migrate(app,db)


if __name__ == '__main__':
    app.run()


