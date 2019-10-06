import requests

TG_URL = 'https://api.telegram.org/bot{}/{}'
TOKEN = '761834074:AAFYxXQN8QTNG0MAx2-qy38sf_EbiEnfzrE'

def process_update(update):
    chat_id = update.get('message', {}).get('id')
    message_text = update.get('message', {}).get('text')
    if message_text:
        requests.post(url=TG_URL.format(TG_URL, 'sendmessage'),
                      data={'chat_id': chat_id,
                            'text': 'you sent me {}'.format(message_text)})


if __name__ == '__main__':
    offset = 0
    while True:
        response = requests.get(url=TG_URL.format(TOKEN, 'getUpdates'),
                                params={'offset': offset})
        if response.ok:
            data = response.json()['result']
            print('update:', data)
            try:
                offset = data[-1]['update_id'] + 1
            except IndexError:
                pass
            for update in data:
                process_update(update)