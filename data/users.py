import datetime

import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from werkzeug.security import generate_password_hash, check_password_hash

from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase, UserMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    is_admin = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False, default=False)
    is_active = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False, default=False)
    username = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    discord = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    competitive_rank = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    wingman_rank = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    faceit_level = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    steam = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                     default=datetime.datetime.now)
    news = orm.relation("News", back_populates='user')

    def __repr__(self):
        return " ".join(("<User>", str(self.id), self.name,  self.email))

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)
