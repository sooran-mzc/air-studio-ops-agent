import boto3

client = boto3.client("bedrock-agentcore-control", region_name="us-west-2")

response = client.create_agent_runtime(
    agentRuntimeName="strands_agent",
    agentRuntimeArtifact={
        "containerConfiguration": {
            "containerUri": "684452318078.dkr.ecr.us-west-2.amazonaws.com/my-strands-agent:latest"
        }
    },
    networkConfiguration={"networkMode": "PUBLIC"},
    roleArn="arn:aws:iam::684452318078:role/agentcore-strands_claude-role",
)

print("Agent Runtime created successfully!")
print(f"Agent Runtime ARN: {response['agentRuntimeArn']}")
print(f"Status: {response['status']}")
