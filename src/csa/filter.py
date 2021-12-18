from nltk.corpus import words
from tqdm import tqdm

from . import clean


ENGLISH_WORDS = set(words.words('en'))
MATCH_PERCENTAGE = 0.5


def is_english(message):
    words = set(message.split())
    num_match_words = len([word for word in words if word in ENGLISH_WORDS])

    return num_match_words > MATCH_PERCENTAGE * len(words)


def has_word(message, word):
    return word in message.split()


def filter_messages(messages):
    messages = clean.convert_to_lowercase(messages)

    def crypto_filter(message):
        return has_word(message, 'shib') or has_word(message, 'doge')

    print('Filtering messages...')

    return [m for m in tqdm(messages)
            if is_english(m['text']) and crypto_filter(m['text'])]


if __name__ == '__main__':
    messages = [
        {'text': 'I love Shib', 'date': '2018-01-01'},
        {'text': 'I love doge', 'date': '2018-01-01'},
        {'text': 'random', 'date': '2018-01-01'},
        {'text': 'Привет мир', 'date': '2018-01-02'},
    ]

    filtered_messages = filter_messages(messages)

    print(f'Number of filtered messages: {len(filtered_messages)}')
    print(filtered_messages)
