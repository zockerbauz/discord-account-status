import requests
import time

# Setzen Sie hier Ihre API-URL
url = 'https://discord.com/api/v9/users/@me/settings-proto/1'

# Definieren Sie die Header und den Body der Anfrage
headers = {
    'authority': 'discord.com',
    'accept': '*/*',
    'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': 'process.env.token',
    'content-type': 'application/json',
    'cookie': '__dcfduid=ca1c8ba0d6e411eebb63f3acec168b78; __sdcfduid=ca1c8ba1d6e411eebb63f3acec168b78d61a959e63226577ab9d4948b2d620cb953c1cfa5d553b94d6448bbf67317cd7; _ga=GA1.1.315153795.1709203299; _ga_YL03HBJY7E=GS1.1.1709203299.1.1.1709203309.0.0.0; __stripe_mid=55ddfd73-fac1-4f0b-8089-45bfe1117322959324; __cfruid=25f63b084fc32f60f69ca2a63131e601671af714-1709976920; _cfuvid=GC_lJcQN3xtUenSiwrWsuOX1GuzXBc7Le4I282.68xA-1709976920939-0.0.1.1-604800000; OptanonConsent=isIABGlobal=false&datestamp=Sat+Mar+09+2024+10%3A35%3A48+GMT%2B0100+(Mitteleurop%C3%A4ische+Normalzeit)&version=6.33.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0; locale=de; cf_clearance=1mqpemgdSwLStrm08zWdkVYht0PzggBxZ5OJ15pkH08-1709976930-1.0.1.1-lkc7K__Evj2cGbR3HwS00YPGllknh_0xG9TWkKrbIjj8ClhHwzDEQV3egtus_4Q9BFNf69wyAXPnQScB0gIW1A',
    'origin': 'https://discord.com',
    'referer': 'https://discord.com/channels/@me/1212709849134145537',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'x-debug-options': 'bugReporterEnabled',
    'x-discord-locale': 'de',
    'x-discord-timezone': 'Europe/Berlin',
    'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImRlLURFIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyMi4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTIyLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjI3MzUwNywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=',
}

data = '{"settings":"WiwKCAoGb25saW5lEiAKHmh0dHBzOi8vY2hlcXVpdHkuaW8vci80RUU1NEZFRg=="}'

# Eine Endlos-Schleife, die jede Sekunde eine Anfrage sendet
while True:
    response = requests.patch(url, headers=headers, data=data)
    print(response.text)
    time.sleep(0.1)  # Warte 1/10 Sekunde vor dem nächsten Durchlauf
