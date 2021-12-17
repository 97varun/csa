from nltk.corpus import words
from tqdm import tqdm

import csa_constants
import csa_data
import csa_structure
import csa_setup
import csa_clean

ENGLISH_WORDS = set(words.words('en'))


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


if __name__ == '__main__':
    csa_setup.setup_nltk_corpus()

    chat_data = csa_data.get_json_data(csa_constants.CHAT_DATA_FILE)
    messages = csa_structure.get_flattened_messages(chat_data['messages'])

    filtered_messages = filter_messages(
        csa_clean.convert_to_lowercase(messages))

    print(f'Number of filtered messages: {len(filtered_messages)}')
    print(filtered_messages[:100])

    csa_data.save_json_data(
        csa_constants.FILTERED_CHAT_DATA_FILE, {'messages': filtered_messages})
