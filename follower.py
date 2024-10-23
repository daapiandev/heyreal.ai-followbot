import requests
import json
import threading
import time
from colorama import Fore, Style, init

init(autoreset=True)

with open('tokens.txt', 'r') as file:
    tokens = file.readlines()

num_threads = int(input("[?]amount off threads to use: "))
uid = input("[?]Enter the id (the last part off the profile url bar):")

url = "https://api.heyreal.ai/api/followUpdate"

headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "nl,en;q=0.9,en-GB;q=0.8,en-US;q=0.7",
    "basic-params": '{"buildVersion":"1","deviceId":"Mozilla50WindowsNT100Win64x64AppleWebKit53736KHTMLlikeGeckoChrome130000Safari53736Edg130000","lang":"nl","deviceName":"Netscape","os":"Windows","osVersion":"","platform":"web"}',
    "content-length": "30",
    "content-type": "application/json",
    "origin": "https://heyreal.ai",
    "priority": "u=1, i",
    "referer": "https://heyreal.ai/",
    "sec-ch-ua": '"Chromium";v="130", "Microsoft Edge";v="130", "Not?A_Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "traceid": "4QhUJipSkh8IePSanejixoxVT630Hz4i",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"
}

payload = {
    "uid": uid,
    "status": 1
}

def __send__(token, follower_number):
    headers["access-token"] = token.strip()
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    if response.status_code == 200:
        print(Fore.GREEN + f"[+] Follower send {follower_number}")
    else:
        print(f"Response for token: {response.status_code} - {response.text}")

def __loop__():
    follower_number = 1
    while True:
        for i in range(len(tokens)):
            thread = threading.Thread(target=__send__, args=(tokens[i], follower_number))
            thread.start()
            follower_number += 1
            time.sleep(0.1)

def __main__():
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=__loop__)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    __main__()
