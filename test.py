#!/usr/bin/env python3
import boto3
import requests
import json

def main():
    s3 = boto3.client('s3')
    print(s3.get_bucket_acl(Bucket='imessage-viz'))

    tructus = {'type': 'application/x-sqlite3', 'name': 'chat.db'}
    response = requests.post('https://68fwpup9dc.execute-api.us-west-1.amazonaws.com/api/', json=tructus)
    guy = response.json()
    print(guy)

    headers = {'Content-Type': 'application/x-sqlite3'}
    f = open('./chat.db', 'rb')
    result = requests.put(guy['body']['url'], headers=headers, data=f)


if __name__ == '__main__':
    main()