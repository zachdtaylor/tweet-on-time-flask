from datetime import datetime
from sqlite3 import OperationalError
from .db import get_db
from .fields import DateTimeField


class Tweet:
    """This class represents an individual tweet and provides methods for interacting
    with the tweet table.

    Attributes:
        id (int): The tweet id
        body (str): The tweet body
        tweet_on (str): The date/time the tweet will be sent on. Must be of the
            format %Y-%m-%d %H:%M
    """

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.body = kwargs.get('body', None)
        self.tweet_on = kwargs.get('tweet_on', None)

    @classmethod
    def _from_row(cls, row):
        return cls(
            id=row['id'],
            body=row['body'],
            tweet_on=DateTimeField.from_db_value(row['tweet_on'])
        )

    @classmethod
    def get(cls, id=None):
        """Returns the tweet with the given id"""
        sql = 'SELECT * FROM tweet WHERE id = ?'
        params = [id]

        db = get_db()
        try:
            row = db.execute(sql, params).fetchone()
        except OperationalError:
            raise ValueError('Must provide id')
        if not row:
            return None
        return cls._from_row(row)

    @classmethod
    def get_all(cls):
        """Returns a list of all tweets"""
        db = get_db()
        rows = db.execute(
            'SELECT * FROM tweet'
        ).fetchall()
        return [cls._from_row(row) for row in rows]

    @classmethod
    def delete_stale(cls):
        """Deletes all tweets whose tweet_on time has passed"""
        db = get_db()
        db.execute(
            "DELETE FROM tweet WHERE tweet_on < strftime('%s', 'now')"
        )
        db.commit()

    def delete(self):
        """Deletes the tweet"""
        db = get_db()
        if self.id:
            db.execute(
                'DELETE FROM tweet WHERE id = ?',
                (self.id,)
            )
            db.commit()

    def save(self):
        """Creates a new tweet if self.id is None, otherwise updates the
        existing tweet"""
        db = get_db()
        if not self.id:
            cursor = db.execute(
                "INSERT INTO tweet (body, tweet_on) VALUES (?, ?)",
                (self.body, DateTimeField.to_db_value(self.tweet_on))
            )
            self.id = cursor.lastrowid
        else:
            db.execute(
                'UPDATE tweet SET body = ?, tweet_on = ? WHERE id = ?',
                (self.body, DateTimeField.to_db_value(self.tweet_on), self.id)
            )
        db.commit()

    def __repr__(self):
        return f"<Tweet: id={self.id} body='{self.body}' tweet_on='{self.tweet_on}'>"
