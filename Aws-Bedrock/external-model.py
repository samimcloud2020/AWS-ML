import boto3
import json

prompt_text = f'\n\nHuman: Write {language} code for the following instructions: {message}\n\nAssistant:'
api_request = {
    "modelId": "anthropic.claude-v2:1",
    "contentType": "application/json",
    "accept": "*/*",
    "body": {
        "prompt": prompt_text,
        "max_tokens_to_sample": 300,
        "temperature": 0.5,
        "top_k": 250,
        "top_p": 1,
        "stop_sequences": ["\n\nHuman:"],
        "anthropic_version": "bedrock-2023-05-31"
    }
}

bedrock = boto3.client("bedrock-runtime", region_name="us-west-2", config=botocore.config.Config(read_timeout=300, retries={'max_attempts': 3}))
response = bedrock.invoke_model(
    modelId=api_request["modelId"],
    contentType=api_request["contentType"],
    accept=api_request["accept"],
    body=json.dumps(api_request["body"])
)

