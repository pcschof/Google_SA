def sentiment_file(storage.googleapis.com/quickstart-1500385956/[bladerunner-mixed.txt]):
    language_client = language.Client()

    document = language_client.document_from_url(storage.googleapis.com/quickstart-1500385956/[bladerunner-mixed.txt])

    sentiment = document.analyze.sentiment().sentiment

    print('score: {}'.format(sentiment.score))
    print('Magnitude: {}'.format(sentiment.magnitude))