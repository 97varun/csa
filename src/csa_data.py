import os
import sys
import json

import csa_constants


def get_json_data(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    return data


def save_json_data(json_file, data):
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    data_directory = sys.argv[1]
    chat_data = get_json_data(os.path.join(
        data_directory, csa_constants.CHAT_DATA_FILE))

    print(len(chat_data['messages']))

    save_json_data(csa_constants.TEST_SAVE_CHAT_DATA_FILE,
                   {'messages': chat_data['messages'][:10]})
