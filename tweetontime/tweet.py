from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from .auth import login_required
from .db import get_db
from .tweet_on_time import get_profile_info, schedule_tweet

bp = Blueprint('tweet', __name__)


@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        body = request.form['body']
        tweet_date = request.form['tweet-date']
        tweet_time = request.form['tweet-time']
        schedule_tweet(body, f'{tweet_date} {tweet_time}')
    profile = get_profile_info()
    return render_template('tweet/index.html', profile=profile)
