import urllib.request
import urllib.parse
from google.cloud import language

class Analyze_Text():

    # def setup(self):
    #
        #  initialize Dynamo URL variable
    url = 'http://ec2-174-129-144-17.compute-1.amazonaws.com:8184/sbcmanager/articles/CMG'

            # requests connection to url variable
    req = urllib.request.Request(url)

            # retrieves data stored in url
    resp = urllib.request.urlopen(req)

            # reads the data
    resp_data = resp.read()

            # decodes the data
    resp_data = resp_data.decode("utf-8")

            # prints the data
    print(resp_data)


    def print_results(annotations):
        score = annotations.sentiment.score
        magnitude = annotations.sentiment.magnitude

        for index, sentence in enumerate(annotations.sentences):
            sentence_sentiment = sentence.sentiment.score
            print('Sentence {} has a sentiment score of {}'.format(
                index, sentence_sentiment))

            print('Overall Sentiment: score of {} with magnitude of {}'.format(
                score, magnitude))

            print('Sentiment: score of {} with magnitude of {}'.format(
                score, magnitude))
            return 0

    def analyze(self):

        # initialize connection to Google API
        client = language.Client()
        # sends data to Google API
        document = client.document_from_text(resp_data)

        annotations = document.annotate_text(include_sentiment=True,
                                             include_syntax=False,
                                             include_entities=False)
        print_results(annotations)

        # # API analyzes data sentiment
        # sentiment_response = document.annotate_text()
        #
        # # stores analysis into variable
        # sentiment = sentiment_response.sentiment

        # return sentiment




    #def analyze(self, sentiment):



        # # score = sentiment.sentence.score
        # # magnitude = sentiment.sentence.magnitude
        #
        # # iterative loop to print each sentence, its polarity, and its magnitude
        # for sentence, index in enumerate(sentiment.sentences):
        #     # score = annotations.sentiment.score
        #     # magnitude = annotations.sentiment.magnitude
        #
        #     # sentence_sentiment = sentiment.sentence.sentiment.score
        #     # sentence_magnitude = sentiment.sentence.sentiment.magnitude
        #     print(sentence)
        #     print(score)
        #     print(magnitude)


if __name__ == '__main__':
    AT = Analyze_Text()
    sentiment = AT.setup()
    AT.analyze()


