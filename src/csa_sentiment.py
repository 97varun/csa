from tqdm import tqdm
from textblob import TextBlob


def get_sentiment(messages):
    def compute_sentiment(message):
        blob = TextBlob(message['text'])
        return {**message, 'sentiment': blob.sentiment.polarity}

    print('Computing sentiment...')
    messages = list(map(lambda m: compute_sentiment(m), tqdm(messages)))

    return messages


if __name__ == '__main__':
    messages = [
        {'text': 'i love shib', 'date': '2018-01-01'},
        {'text': 'i love doge', 'date': '2018-01-01'}
    ]

    messages = get_sentiment(messages)

    print(messages)
