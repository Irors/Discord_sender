import time
import requests
import random
from config import *

def message_guild(token, chanel, messages, try_, proxy_):

    time_s = [i for i in range(time_[0], time_[1])]

    time.sleep(random.choice(time_s))

    json_data = {
        'content': random.choice(messages),
    }

    # Если токен рандомный
    if rand_token:
            headers = {
                'authorization': random.choice(token),
            }
    # Если токен НЕ рандомный
    else:
        headers = {
            'authorization': token[try_],
        }
#=========================================================================================================================================================================================================================================================================
    if use_proxy:
        try:
            proxy = [random.choice(proxy_)]
            proxies = {
                'http': f'{proxy[0]}',
                'https': f'{proxy[0]}',
            }
        except Exception as error:
            print (f'{error}. proxy Error')

    else:
        proxies = None


    # Если гилдия рандомная
    if rand_guild:
        response = requests.post(
            f'https://discord.com/api/v9/channels/{random.choice(chanel)}/messages',
            headers=headers,
            json=json_data,
            proxies = proxies
        )
        if len(response.json()) == 2:
            pass
        else:
            try:
                print( f"Сообщение : {response.json()['content']}  |  Ник : {response.json()['author']['username']}  |  Сhannel_id : {response.json()['channel_id']}" )
            except:
                print(  f"Токен {token[try_]} не смог отправить сообщение" )

    # Если гилдия НЕ рандомная
    else:
        for gld in chanel:
            response = requests.post(
                f'https://discord.com/api/v9/channels/{gld}/messages',
                headers=headers,
                json=json_data,
                proxies=proxies
            )
            if len(response.json()) == 2:
                pass
            else:
                try:
                    print( f"Сообщение : {response.json()['content']}  |  Ник : {response.json()['author']['username']}  |  Сhannel_id : {response.json()['channel_id']}" )
                except:
                    print( f"Токен {token[try_]} не смог отправить сообщение" )





