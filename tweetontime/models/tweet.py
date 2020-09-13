from datetime import datetime
from sqlite3 import OperationalError
from .db import get_db


class Tweet:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.body = kwargs.get('body', None)
        self.tweet_on = kwargs.get('tweet_on', None)

    @classmethod
    def get(cls, id=None):
        sql = 'SELECT * FROM tweet WHERE id = ?'
        params = [id]

        db = get_db()
        try:
            row = db.execute(sql, params).fetchone()
        except OperationalError:
            raise ValueError('Must provide id')
        if not row:
            return None
        return cls(
            id=row['id'],
            body=row['body'],
            tweet_on=str(datetime.fromtimestamp(row['tweet_on']))
        )

    def save(self):
        db = get_db()
        if not self.id:
            cursor = db.execute(
                "INSERT INTO tweet (body, tweet_on) VALUES (?, strftime('%s', ?))",
                (self.body, self.tweet_on)
            )
            self.id = cursor.lastrowid
        else:
            db.execute(
                'UPDATE tweet SET body = ?, tweet_on = ? WHERE id = ?',
                (self.body, self.tweet_on, self.id)
            )
        db.commit()

    def __repr__(self):
        return f"<Tweet: id={self.id} body='{self.body}' tweet_on='{self.tweet_on}'>"
