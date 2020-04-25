#!/usr/bin/env python3.7

import json

from flask import Flask, request

from sentiment import sentiment, scrape

app = Flask(__name__)

@app.route('/')
def analyze():
    url = request.args.get('url')
    #print('URL', url)
    title, text = scrape(url)
    title_sent = sentiment(title)
    text_sent = sentiment(text)
    res = {'title': title,
           'sentiment': {
               'title': {'polarity': title_sent.polarity,
                         'subjectivity': title_sent.subjectivity},
               'text': {'polarity': text_sent.polarity,
                        'subjectivity': text_sent.subjectivity}}}
    return json.dumps(res)

if __name__=='__main__':
    app.run(debug=True, port=8080)
