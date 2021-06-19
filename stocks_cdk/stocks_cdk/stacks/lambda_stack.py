from aws_cdk import aws_lambda as _lambda
from aws_cdk import core
import aws_cdk.aws_ecr as ecr


class lambda_stack(core.Stack):
    def __init__(self,scope:core.Construct,id:str,**kwargs):
        super().__init__(scope,id,**kwargs)
        repo=ecr.Repository.from_repository_name(self,"Reposirtory",repository_name="stocks-api")
        self.lambda_deployment:_lambda.DockerImageFunction=_lambda.DockerImageFunction(
            self,id,
            timeout=core.Duration.seconds(30),
            code=_lambda.DockerImageCode.from_ecr(
                repository=repo,
                tag="latest"
            ),
            function_name="test",
            description="test"
        )

