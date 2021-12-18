import argparse

import csa_clean
import csa_data
import csa_filter
import csa_sentiment
import csa_structure


def get_cmdline_args():
    parser = argparse.ArgumentParser(description='Cryto sentiment analyzer')
    parser.add_argument('-i', '--input_file',
                        help='Path to raw chat data file', required=True)
    parser.add_argument('-o', '--output_file',
                        help='Path to output data file', required=True)

    return parser.parse_args()


if __name__ == '__main__':
    args = get_cmdline_args()

    chat_data = csa_data.get_json_data(args.input_file)

    messages = csa_structure.get_flattened_messages(chat_data['messages'])

    messages = csa_filter.filter_messages(messages)

    messages = csa_clean.clean_messages(messages)

    messages = csa_sentiment.get_sentiment(
        messages,
        csa_sentiment.compute_sentiment_naive_bayes
    )

    result_file_path = args.output_file

    csa_data.save_json_data(result_file_path, {'messages': messages})

    print(f'Computed sentiment for messages and saved to "{result_file_path}"')
