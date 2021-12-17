import tqdm
from nltk.corpus import stopwords

STOP_WORDS = set(stopwords.words('english'))


def remove_non_alnum_chars(word):
    return ''.join(c for c in word if c.isalnum() or c.isspace())


def remove_stop_words(message):
    return [w for w in message if w not in STOP_WORDS]


def clean_message(message):
    message = message.lower()
    message = remove_non_alnum_chars(message)
    message = remove_stop_words(message.split())
    return message


def clean_messages(messages):
    return [{**m, 'text': clean_message(m['text'])} for m in tqdm(messages)]


def convert_to_lowercase(messages):
    return [{**m, 'text': m['text'].lower()} for m in messages]
