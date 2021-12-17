import csa_data
import csa_structure
import csa_clean
import csa_sentiment
import csa_constants

if __name__ == '__main__':
    chat_data = csa_data.get_json_data(csa_constants.CHAT_DATA_FILE)

    messages = csa_structure.get_flattened_messages(chat_data['messages'])

    messages = csa_clean.filter_messages(messages)

    messages = csa_sentiment.get_sentiment(messages)

    csa_data.save_json_data(
        csa_constants.SENTIMENT_CHAT_DATA_FILE,
        {'messages': messages})
