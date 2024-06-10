TOKEN = '7046690791:AAE2s8z8qpbLniQlYX-snEz8FcZkNJfJEGE'
CHAT_ID='1719117292'


import requests
message='hello how are you'
url=f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
r=requests.get(url)
print(r.json())

