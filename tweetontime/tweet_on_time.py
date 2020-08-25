import requests
from .settings import BEARER_TOKEN

url = "https://api.twitter.com/labs/2/tweets/1214281000932593667?tweet.fields=attachments,author_id,created_at,entities,geo,id,in_reply_to_user_id,lang,possibly_sensitive,public_metrics,referenced_tweets,source,text,withheld"

payload = {}
headers = {
    'Authorization': f'Bearer {BEARER_TOKEN}',
    'Cookie': 'personalization_id="v1_zNwxTIwk1n/qlXcMjaPtnA=="; guest_id=v1%3A159555219276996589'
}

if __name__ == '__main__':
    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text.encode('utf8'))
