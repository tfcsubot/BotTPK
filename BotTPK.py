import requests
import datetime

class Bot:

    def __init__(self,token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, offset = None, timeout = 30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url+method,params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_last_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result[len(get_result)]

        return last_update
token = '689934930:AAE6uhU21M7ml6EXqgLdfogh7IJO6fujf5M'
BotTPK = Bot(token)

def main():
    new_offset = None

    while True:
        BotTPK.get_updates(new_offset)
        
        last_update = BotTPK.get_last_update()
        
        last_update_id = last_update['update_id']
        last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        last_chat_name = last_update['message']['chat']['first_name']
        
        BotTPK.send_message(last_chat_id,'Hello, {}'.format(last_chat_name))
        
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
    
