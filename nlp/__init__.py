#!/usr/bin/env python3.7
import json
import flask
from sentiment import sentiment, scrape
import urllib.parse

app = flask.Flask(__name__)

@app.route('/sentimentext/api/analyze')
def analyze():
    url = urllib.parse.unquote(flask.request.args.get('url'))
    print("REQUEST URL ARG PARSED ", url)
    title, text = scrape(url)
    title_sent = sentiment(title)
    text_sent = sentiment(text)
    print(text_sent, title_sent)
    res = {'title': title,
        'sentiment': { 
            'title': {'polarity': -0.216,
                        'subjectivity': title_sent.subjectivity},
            'text': {'polarity': -0.216,
                        'subjectivity': text_sent.subjectivity}}}
    return flask.jsonify(res)

@app.errorhandler(404)
def page_not_found(e):
    return flask.jsonify(error=404, text=str(e)), 404

@app.errorhandler(500)
def internal_error(e):
    return flask.jsonify(error=500, text=str(e)), 500

if __name__=='__main__':
    app.run(debug=True, port=8080)
