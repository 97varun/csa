import os
import sys

import csa_data
import csa_structure
import csa_filter
import csa_sentiment
import csa_constants

if __name__ == '__main__':
    data_directory = sys.argv[1]

    chat_data = csa_data.get_json_data(
        os.path.join(data_directory, csa_constants.CHAT_DATA_FILE))

    messages = csa_structure.get_flattened_messages(chat_data['messages'])

    messages = csa_filter.filter_messages(messages)

    messages = csa_sentiment.get_sentiment(messages)

    result_file_path = os.path.join(
        data_directory, csa_constants.SENTIMENT_CHAT_DATA_FILE)

    csa_data.save_json_data(result_file_path, {'messages': messages})

    print(f'Computed sentiment for messages and saved to {result_file_path}')
