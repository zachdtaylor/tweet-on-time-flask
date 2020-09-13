from sqlite3 import OperationalError
from werkzeug.security import generate_password_hash

from .db import get_db


class User:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.username = kwargs.get('username', None)
        self.password = kwargs.get('password', None)

    @classmethod
    def get(cls, id=None, username=None):
        sql = 'SELECT * FROM user WHERE'
        params = []
        if id:
            sql += ' id = ?'
            params.append(id)
        elif username:
            sql += ' username = ?'
            params.append(username)

        db = get_db()
        try:
            row = db.execute(sql, params).fetchone()
        except OperationalError:
            raise ValueError('Must provide id or username')
        if not row:
            return None
        return cls(**row)

    def save(self):
        db = get_db()
        if not self.id:
            db.execute(
                'INSERT INTO user (username, password) VALUES (?, ?)',
                (self.username, generate_password_hash(self.password))
            )
        else:
            db.execute(
                'UPDATE user SET username = ?, password = ? WHERE id = ?',
                (self.username, generate_password_hash(self.password), self.id)
            )
        db.commit()

        user = User.get(username=self.username)
        self.id = user.id
        self.password = user.password

    def __str__(self):
        return self.username

    def __repr__(self):
        return f"<User: id={self.id} username='{self.username}'>"
