import aws_cdk as core
import aws_cdk.assertions as assertions
from iac.iac_stack import IacStack


def test_dynamodb_table_created() -> None:
    app = core.App()
    stack = IacStack(app, "agentforge-iac")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties(
        "AWS::DynamoDB::Table",
        {
            "TableName": "AgentForge-Marketplace",
            "BillingMode": "PAY_PER_REQUEST",
        },
    )
