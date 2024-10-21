import http.client, urllib
from pushoverSecrets import token,user

class SendMessage:
    def send(self,message):
        conn = http.client.HTTPSConnection("api.pushover.net:443") #create connection with the api

# make a POST request to send message
        conn.request("POST", "/1/messages.json",
        urllib.parse.urlencode({
            "token": token,
            "user": user,
            "title":"FP Notification",
            "message": message,
            "priority":0
        }), { "Content-type": "application/x-www-form-urlencoded" })
        conn.getresponse()

SendMessage()