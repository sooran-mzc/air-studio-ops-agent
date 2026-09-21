import json

import boto3

agent_core_client = boto3.client("bedrock-agentcore", region_name="us-west-2")
payload = json.dumps({"input": {"prompt": "チ。という漫画について魅力を教えて"}})

response = agent_core_client.invoke_agent_runtime(
    agentRuntimeArn="arn:aws:bedrock-agentcore:us-west-2:684452318078:runtime/strands_agent-jMiZQZ49Tz",
    runtimeSessionId="dfmeoagmreaklgmrkleafremoigrmtesogmtrskhmtkrlshmt",  # Must be 33+ chars
    payload=payload,
    qualifier="DEFAULT",
)

response_body = response["response"].read()
response_data = json.loads(response_body)
print("Agent Response:", response_data)
