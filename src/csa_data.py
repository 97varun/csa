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
    chat_data = get_json_data(csa_constants.CHAT_DATA_FILE)

    print(len(chat_data['messages']))

    save_json_data(csa_constants.NEW_CHAT_DATA_FILE, chat_data)
