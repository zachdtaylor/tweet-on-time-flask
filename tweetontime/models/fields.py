import pytz
from datetime import datetime


class DateTimeField:
    format_str = '%Y-%m-%d %H:%M'

    @classmethod
    def to_db_value(cls, value):
        """Converts from local time string to UTC unix timestamp. Time string
        must be of the format %Y-%m-%d %H:%M"""
        dt = datetime.strptime(value, cls.format_str)
        return int(dt.timestamp())

    @classmethod
    def from_db_value(cls, value):
        """Converts from UTC unix timestamp to local time string. Local time
        string will be of the format %Y-%m-%d %H:%M"""
        dt = datetime.fromtimestamp(value)
        return dt.strftime(cls.format_str)
