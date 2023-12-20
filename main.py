import requests
from threading import Thread

print("REMEMBER TO USE A VPN/PROXY!\n")

workers = int(input("How many workers do you want? "))
codes = int(input("Approximately how many codes do you want? "))
count = 0

def generator():
    global count
    while count < codes:
        headers = {
            "authority": "api.discord.gx.games",
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "application/json",
            "origin": "https://www.opera.com",
            "referer": "https://www.opera.com/",
            "sec-ch-ua": '"Chromium";v="116", "Not)A;Brand";v="24", "Opera";v="102"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Linux"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0",
        }

        resp = requests.post("https://api.discord.gx.games/v1/direct-fulfillment", headers=headers, json={
            "partnerUserId": "9e2d517a-001c-4de9-aa98-6c9fb26d6ac1"
        })
        if resp.status_code == 429:
            print("[ERROR] blocked")
            break

        try:
            open("nitro.txt", "a").write("https://discord.com/billing/partner-promotions/1180231712274387115/" + resp.json()["token"] + "\n")
        except Exception:
            print(f"[ERROR] Probably blocked (status code: {resp.status_code}, resp: {resp.text})")
            break

        count += 1
        print(f"[UPDATE] {count} codes generated")

threads = []
for i in range(workers):
    thread = Thread(target=generator)
    thread.start()
    threads.append(thread)
    print(f"[UPDATE] Thread {i} is now running")

for i in range(workers):
    threads[i].join()
    print(f"[UPDATE] Thread {i} is no longer running")
