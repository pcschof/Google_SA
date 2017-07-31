
import urllib.request
from google.cloud import language


class google_sent():
    # initialize connection to dynamo endpoint
    url = 'http://ec2-174-129-144-17.compute-1.amazonaws.com:8184/sbcmanager/articles/ROM'
    # request connection
    req = urllib.request.Request(url)
    # open url
    resp = urllib.request.urlopen(req)
    # read text in url
    resp_data = resp.read()
    # decode in utf-8 format
    resp_data = resp_data.decode("utf-8")
    # print results
    print(resp_data)


    def language_analysis(self, text):
        # establish connection to Google Nat Language API
        client = language.Client()
        # initialize content as a document from text
        document = client.document_from_text(text)
        # call analyze_sentiment method
        sent_analysis = document.analyze_sentiment()
        print(sent_analysis)
        sentiment = sent_analysis.sentiment
        ent_analysis = document.analyze_entities()
        entities = ent_analysis.entities
        return sentiment, entities


if __name__ == '__main__':
    sent = google_sent()
    example_text = google_sent().resp_data
    sentiment, entities = sent.language_analysis(example_text)
    print(sentiment.score, sentiment.magnitude)

    for e in entities:
       print(e.name, e.entity_type, e.metadata, e.salience)



