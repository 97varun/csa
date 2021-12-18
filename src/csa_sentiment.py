from tqdm import tqdm
from textblob import TextBlob

import csa_data
import csa_structure
import csa_filter
import csa_constants


def get_sentiment(messages):
    def compute_sentiment(message):
        blob = TextBlob(message['text'])
        return {**message, 'sentiment': blob.sentiment.polarity}

    print('Computing sentiment...')
    messages = list(map(lambda m: compute_sentiment(m), tqdm(messages)))

    return messages


if __name__ == '__main__':
    chat_data = csa_data.get_json_data(csa_constants.CHAT_DATA_FILE)

    messages = csa_structure.get_flattened_messages(chat_data['messages'])

    messages = csa_filter.filter_messages(messages)

    messages = get_sentiment(messages)

    print(messages[:10])
