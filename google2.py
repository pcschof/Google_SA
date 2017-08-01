import html
import urllib.request
import urllib.parse
import urllib.response
import json
from google.cloud import language

class goog:

    def __init__(self):
        url = 'http://ec2-174-129-144-17.compute-1.amazonaws.com:8184/sbcmanager/articles/ROM'
        req = urllib.request.Request(url)
        resp = urllib.request.urlopen(req)
        resp_data = resp.read()
        resp_data = resp_data.decode('utf-8')
        resp_data_to_json = json.loads(resp_data)
        self.articles = resp_data_to_json["articles"]


    def la(self, text):
        client = language.Client()
        document = client.document_from_text(text)
        sent_analysis = document.analyze_sentiment()
        sentiment = sent_analysis.sentiment
        ent_analysis = document.analyze_entities()
        entities = ent_analysis.entities
        return sentiment, entities


if __name__ == '__main__':
    sent = goog()
    articles = sent.articles
    for a in articles:
        sentiment, entities = sent.la(html.unescape(articles[a].replace("\n", "")))
        print('sentiment score:', sentiment.score, 'magnitude:', sentiment.magnitude)
        print(html.unescape(articles[a].replace("\n", "\n")))
        # for e in entities:
        #     print(e.name, e.entity_type, e.metadata, e.salience)