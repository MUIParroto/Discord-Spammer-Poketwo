from webserver import keep_alive
import requests

channelID = 1069377832800755722
headers = {
    "authorization":
    "2abb6de371a192df962eaf7fcf55725ac44b2c7fde55070e0da2b78d6a06f93d"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
