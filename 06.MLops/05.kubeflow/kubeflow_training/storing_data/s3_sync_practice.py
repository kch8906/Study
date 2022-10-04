import kfp
from kfp import dsl
from kfp.aws import use_aws_secret

S3_PATH = 's3://changhyun-kubeflow/LPOINT_BIG_COMP_01_DEMO.csv'

def s3_sync():
    return kfp.dsl.ContainerOp(
        name='s3_sync',
        image='amazon/aws-cli:latest',
        command=['aws', 's3', 'sync', S3_PATH, '/tmp'],
        file_outputs={
            'data': '/tmp'
        }
    )


@dsl.pipeline(name='s3_sync_pipeline', description='s3 sync pipeline.')
def s3_sync_pipeline():
    _ = s3_sync().apply(use_aws_secret('aws-secret', 'AWS_ACCESS_KEY_ID', 'AWS_SECRET_ACCESS_KEY'))


if __name__ == "__main__":
    kfp.compiler.Compiler().compile(s3_sync_pipeline, 's3_sync_pipeline.tar.gz')