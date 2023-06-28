from config import *
from softDiscordMessage import *



if __name__ == "__main__":
    print('''
✩    Одуванчик 𝐿𝒶𝓃𝒹    ✩
    ''')

    with open("Token.txt") as file:
        token = [i.strip() for i in file]

    with open("IdServermessage.txt") as file:
        chanel = [i.strip() for i in file]

    with open("Message.txt") as file:
        messages = [i.strip() for i in file]

    with open("Proxy.txt") as file:
        proxy_ = [i.strip() for i in file]

    print(f"Аккаунтов Discord: {len(token)}")
    print()


    for try_ in range(len(token)):
        message_guild(token, chanel, messages, try_, proxy_)
