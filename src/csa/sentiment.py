from textblob import Blobber, TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from tqdm import tqdm

blobber = Blobber(analyzer=NaiveBayesAnalyzer())


def compute_sentiment_naive_bayes(message):
    blob = blobber(message['clean_text'])

    return {**message,
            'sentiment': blob.sentiment.p_pos
            if blob.sentiment.classification == 'pos'
            else -blob.sentiment.p_neg}


def compute_sentiment_pattern_analyzer(message):
    blob = TextBlob(message['clean_text'])

    return {**message,
            'sentiment': blob.sentiment.polarity}


def get_sentiment(messages, compute_sentiment_func):
    print('Computing sentiment...')
    messages = list(map(lambda m: compute_sentiment_func(m), tqdm(messages)))

    return messages


if __name__ == '__main__':
    messages = [
        {'clean_text': 'love shib', 'date': '2018-01-01'},
        {'clean_text': 'love doge', 'date': '2018-01-01'},
        {'clean_text': 'rip doge', 'date': '2018-01-01'},
    ]

    messages = get_sentiment(messages, compute_sentiment_naive_bayes)

    print(messages)
