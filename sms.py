import os
import time
from termcolor import colored
import requests
import sys


def main():
    proxies = {'http': 'socks5://127.0.0.1:9050',
               'https': 'socks5://127.0.0.1:9050'
               }

    def logo():
        print(colored(
            """
    @@@@@@@@@@@@@@@@@@@@@@@@@@**********@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@*****************************@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@**************************************@@@@@@@@@@@@
    @@@@@@**************@@@@@@@@@@@@@@@@@@@@@@@**************@@@@@
    @@@***    *****@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*****    ***@@
    @@***      **@@@@@@@@@@*****************@@@@@@@@@@**      **@@
    @@@****  ***@@@@@@***************************@@@@@@***  ***@@@
    @@@@@@@@@@@@*************@@@@@@@@@@@@@*************@@@@@@@@@@@
    @@@@@@@@@@***    ***@@@@@@@@@@@@@@@@@@@@@@@***    **@@@@@@@@@@
    @@@@@@@@@@@***  ***@@@@@@@***********@@@@@@@**   ***@@@@@@@@@@
    @@@@@@@@@@@@@@*@@@@@***********************@@@@*@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@**    *****@@@@@*****    **@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@***  ***@@@@@@@@@@@***  **@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@*******@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@*********@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@********@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@**@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    **@@@**@@@@@@@@@@@@@@@@@@**@@@@@@*@@@@@*@@@@@@@@@@@@@@@@@*@@@@
    **@@@**@*@@@*@*****@@******@@*****@@@@****@*****@@*****@@*****
    **@@@**@@*@*@@*@@@**@*@@@**@**@@@*@@@@@**@@*@***@@*@@@@@@*@@@*
    **@@@**@@@**@@*@***@@*@@@**@****@*@@@@@***@*****@@*****@@*@@@*
    @@@@@@@@**@@@@*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    
    
    We are not responsible of any illegal action
    """, 'blue'))

    logo()

    time.sleep(1)

    print('1: Send sms')
    print('-1: Exit!')

    choices = input("\nPlease choice: ")

    def SMS():
        os.system('clear')
        time.sleep(1)
        logo()
        time.sleep(1)
        smsnumb = input("Input the number of the target: ")
        message = input("Please input the message: ")

        resp = requests.post('https://textbelt.com/text', {
            'phone': f'{smsnumb}',
            'message': f'{message}',
            'key': 'textbelt',
        }, proxies=proxies)

        print(resp.json())
        time.sleep(3)
        return main()

    if choices == "1":
        SMS()

    elif choices == "2":
        os.system("clear")
        time.sleep(1)
        logo()
        time.sleep(1)
        lines = "=========================================================================================="
        print(
            "Your phone number was not provided in E.164 format: you need to input the country code ex.+91"
        )
        print(lines)
        print(
            "Only one test text message is allowed per day: you can't send more than one message per day, however you could use vpn"
        )
        print(lines)
        print(
            "Else: please contact hyprid tech in github or youtube"
        )
        print(lines)
        print(
            ""
        )

    elif choices == "-1":
        os.system("clear")
        time.sleep(1)
        return


main()
