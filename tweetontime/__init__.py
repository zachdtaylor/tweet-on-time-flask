import atexit
import os
from datetime import datetime
from flask import Flask
from .tweet_on_time import tweet_scheduler
from .settings import SECRET_KEY


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY=SECRET_KEY or 'dev',
            DATABASE=os.path.join(app.instance_path, 'tweetontime.sqlite')
        )
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import tweet
    app.register_blueprint(tweet.bp)
    app.add_url_rule('/', endpoint='index')

    tweet_scheduler.start()
    atexit.register(lambda: tweet_scheduler.shutdown(wait=False))

    return app
