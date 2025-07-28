#!/usr/bin/env python3
import aws_cdk as cdk
from iac.iac_stack import IacStack

app = cdk.App()
IacStack(
    app,
    "AgentForge-Dev",
    # env=cdk.Environment(
    #     account=os.getenv('CDK_DEFAULT_ACCOUNT'),
    #     region=os.getenv('CDK_DEFAULT_REGION')
    # ),
)

app.synth()
