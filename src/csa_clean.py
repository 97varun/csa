from nltk.corpus import stopwords, words
from tqdm import tqdm

import csa_constants
import csa_data
import csa_structure
import csa_setup

STOP_WORDS = set(stopwords.words('english'))
ENGLISH_WORDS = set(words.words('en'))


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


def is_english(message):
    words = set(message.split())
    num_match_words = len([word for word in words if word in ENGLISH_WORDS])
    return num_match_words > csa_constants.MATCH_PERCENTAGE * len(words)


def has_word(message, word):
    return word in message.split()


def filter_messages(messages):
    def crypto_filter(message):
        return has_word(message, 'shib') or has_word(message, 'doge')

    return [m for m in tqdm(messages)
            if is_english(m['text']) and crypto_filter(m['text'])]


def convert_to_lowercase(messages):
    return [{**m, 'text': m['text'].lower()} for m in messages]


if __name__ == '__main__':
    csa_setup.setup_nltk_corpus()

    chat_data = csa_data.get_json_data(csa_constants.CHAT_DATA_FILE)
    messages = csa_structure.get_flattened_messages(chat_data['messages'])

    filtered_messages = filter_messages(convert_to_lowercase(messages))
    print(f'Number of filtered messages: {len(filtered_messages)}')
    print(filtered_messages[:100])

    csa_data.save_json_data(
        csa_constants.FILTERED_CHAT_DATA_FILE, filtered_messages)
