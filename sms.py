import os
import time
from termcolor import colored
import requests
import sys
from stem import Signal
from stem.control import Controller


def main():

    time.sleep(1)

    print('1: Send sms')
    print('2: Help!')
    print('-1:Exit')

    choices = input("\nPlease choice: ")

    def renew_tor_ip():
        with Controller.from_port(port=9051) as controller:
            controller.authenticate(password="MyStr0n9P#D")
            controller.signal(Signal.NEWNYM)

    def SMS():
        os.system('clear')

        time.sleep(1)
        session = requests.session()

        # TO Request URL with SOCKS over TOR
        session.proxies = {}
        session.proxies['http'] = 'socks5h://localhost:9050'
        session.proxies['https'] = 'socks5h://localhost:9050'

        try:
            smsnumb = input("Input the number of the target(include+): ")
            smscount = input("Input the number of messages: ")
            smscount = int(smscount)
            if smscount <= 0:
                print("error input:number must more than 0 ")
                return main()

            message = input("Please input the message: ")

            for i in range(0, smscount):
                resp = session.post('https://textbelt.com/text', {
                    'phone': f'{smsnumb}',
                    'message': f'{message}',
                    'key': 'textbelt',
                })

                print(resp.json())
                renew_tor_ip()
                time.sleep(5)

            return main()
        except Exception as e:
            print(str(e))
        else:
            return(r.text)

    if choices == "1":
        SMS()

    elif choices == "2":
        os.system("clear")

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
            "Follow the video to know more about the tool :)"
            "*Please put the video link here Hussain*"
        )

    elif choices == "-1":
        print("Exit")
        return


main()
