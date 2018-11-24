import json


def hello(event, context):
    ## for challenge and response authentication
    ebody = json.loads(event['body'])
    if 'challenge' in ebody:
        return {
            "statusCode": 200,
            "body": ebody['challenge']
        }
    else:
        return {
            "statusCode": 200,
            "body": "non-challege request"
        }
