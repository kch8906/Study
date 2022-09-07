import kfp
from kfp import dsl

BASE_IMAGE = 'library/bash:4.4.23'
KUBEFLOW_HOST = 'http://127.0.0.1:8080/pipeline'

def echo_op():
    return dsl.ContainerOp(
        name='echo',
        image=BASE_IMAGE,
        command=['sh', '-c'],
        arguments=['echo "hello world"'],
    )

@dsl.pipeline(name='hellow_world_bash_pipeline', description='A hello world pipeline.')
def hello_world_bash_pipeline():
    echo_task = echo_op()


if __name__ == "__main__":
    kfp.compiler.Compiler().compile(hello_world_bash_pipeline, 'hello-world-bash-pipeline.tar.gz')