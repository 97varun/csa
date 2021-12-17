import csa_constants
import csa_data


def view_unique_nested_types(nested_messages):
    unique_types = set()
    for message in nested_messages:
        for cmpl in message['text']:
            if isinstance(cmpl, dict):
                unique_types.add(cmpl['type'])

    print(unique_types)

    # {'bold', 'link', 'phone', 'hashtag', 'mention',
    #     'cashtag', 'bot_command', 'code', 'pre', 'text_link',
    #     'underline', 'email', 'italic', 'mention_name'}


def view_message_type_stats(messages):
    nested_messages = list(
        filter(lambda x: isinstance(x['text'], list), messages))
    normal_messages = list(
        filter(lambda x: isinstance(x['text'], str), messages))

    print(f'Number of nested_messages: {len(nested_messages)}')
    print(f'Number of normal_messages: {len(normal_messages)}')

    # Number of nested_messages: 4654
    # Number of normal_messages: 44782


def get_flattened_messages(messages):
    def flatten(piece):
        if isinstance(piece, dict):
            return piece['text']
        else:
            return piece

    def stitch(pieces):
        if isinstance(pieces, list):
            return ''.join(map(flatten, pieces))
        else:
            return pieces

    def flatten_message(message):
        return {'text': stitch(message['text']), 'date': message['date']}

    flattened_messages = list(map(lambda m: flatten_message(m), messages))

    return flattened_messages


if __name__ == "__main__":
    chat_data = csa_data.get_json_data(csa_constants.CHAT_DATA_FILE)

    flattened_messages = get_flattened_messages(chat_data['messages'])

    print(f'Number of flattened_messages: {len(flattened_messages)}')
    print(flattened_messages[:100])
