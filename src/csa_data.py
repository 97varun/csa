import os
import sys
import json
import argparse


def get_json_data(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    return data


def save_json_data(json_file, data):
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def get_cmdline_args():
    parser = argparse.ArgumentParser(description='Data handler test')
    parser.add_argument('-i', '--input_file',
                        help='Path to raw chat data file', required=True)
    parser.add_argument('-o', '--output_file',
                        help='Path to output data file', required=True)

    return parser.parse_args()


if __name__ == "__main__":
    args = get_cmdline_args()

    chat_data = get_json_data(args.input_file)

    print(len(chat_data['messages']))

    save_json_data(args.output_file, {'messages': chat_data['messages'][:10]})
