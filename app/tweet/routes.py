from flask import request, jsonify
from app.extensions import db

from app.tweet import tweetBp
from app.models.tweet import Tweets


@tweetBp.route("", methods=['GET'], strict_slashes = False)
def get_tweet():
    limit = request.args.get('limit', 10)
    if type(limit) is not int:
        return jsonify({'message': 'invalid parameter'}), 400

    tweets = db.session.execute(
        db.select(Tweets).limit(limit)
    ).scalars()

    result = []
    for tweet in tweets:
        result.append(tweet.serialize())

    return jsonify(data=result), 200


@tweetBp.route("", methods=['POST'], strict_slashes = False)
def post_tweet():
    data = request.get_json()
    content = data.get('content', None)

    if not content:
        return jsonify({'error': 'Invalid data'}), 422

    tweet = Tweets(content=content)
    db.session.add(tweet)
    db.session.commit()
    return jsonify(data=tweet.serialize()), 200