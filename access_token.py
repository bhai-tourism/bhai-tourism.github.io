import requests;
import json;

client_id = "G8FvApHHuAu5AT9ZXLGs3q9nY1G3RlXSeHkbKwnC";
client_secret = "8gdA42Q6dXBtrEfckEFfl2jScfUKhs7SovI9wRGomq05I5ArMBG0kCd5ffiASUvS2anP1OkIxofUyzu0katdnGxHTzJyNlaQhpBKhUZSmBCmdquDNDnj2GKC3XMj7NeO";
env = "production";

if (client_id.startswith("test")):
    url = "https://test.instamojo.com/oauth2/token/";
    env = "test";

payload = "grant_type=client_credentials&client_id=" + client_id + "&client_secret=" + client_secret;
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers);
token = env + json.loads(response.text)["access_token"];
print(token);