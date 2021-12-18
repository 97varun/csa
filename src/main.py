import argparse

from csa import data, structure, filter, clean, sentiment


def get_cmdline_args():
    parser = argparse.ArgumentParser(description='Cryto sentiment analyzer')
    parser.add_argument('-i', '--input_file',
                        help='Path to raw chat data file', required=True)
    parser.add_argument('-o', '--output_file',
                        help='Path to output data file', required=True)

    return parser.parse_args()


if __name__ == '__main__':
    args = get_cmdline_args()

    chat_data = data.get_json_data(args.input_file)

    messages = structure.get_flattened_messages(chat_data['messages'])

    messages = filter.filter_messages(messages)

    messages = clean.clean_messages(messages)

    messages = sentiment.get_sentiment(
        messages,
        sentiment.compute_sentiment_naive_bayes
    )

    result_file_path = args.output_file

    data.save_json_data(result_file_path, {'messages': messages})

    print(f'Computed sentiment for messages and saved to "{result_file_path}"')
