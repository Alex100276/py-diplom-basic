import requests


url = "https://id.vk.com/auth?return_auth_hash=82f9e4906b5c207a05&redirect_uri=https%3A%2F%2Foauth.vk.com%2Fblank.html&redirect_uri_hash=edbe78e331722e2068&force_hash=1&app_id=52094214&response_type=token&code_challenge=&code_challenge_method=&scope=0&state="

payload = {}
headers = {
    'Cookie':
    'remixlang=3; remixstid=47879508_KzHidIUA6Tkj9vbY4z6ZeWTJy3zLVxKhZWjAmHLgTZX; remixstlid=9094635281859578785_EDGB1qfJlw3CsZuXzmxW98rx2467xqmaouDEGX0tfd0; remixuas=OTk4NmNmYjcxMDk4ODYzZmM5MTcwMWNm'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
