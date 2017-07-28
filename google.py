from google.cloud import language

def language_analysis(text):
    client = language.Client()
    document = client.document_from_text(text)
    sent_analysis = document.analyze_sentiment()
    print(dir(sent_analysis))
    sentiment = sent_analysis.sentiment
    ent_analysis = document.analyze_entities()
    entities = ent_analysis.entities

    example_text = 'Is it not obvious that Python is the best programming language of them all'
    print(sentiment.score, sentiment.magnitude)
    return sentiment, entities

def print_entites(entities):
    for e in entities:
        print(e.name, e.entity_type, e.metadata, e.salience)