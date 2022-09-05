import kfp
from kfp import dsl
from kfp.components import create_component_from_func

@create_component_from_func
def preprocess_op():

    return dsl.ContainerOp(
        name='Preprocess Data',
        image='gnovack/boston_pipeline_preprocessing:latest',
        arguments=[],
        file_outputs={
            'x_train': '/app/x_train.npy',
            'x_test': '/app/x_test.npy',
            'y_train': '/app/y_train.npy',
            'y_test': '/app/y_test.npy',
        }
    )


@dsl.pipeline(
   name='Iris Pipeline',
   description='An example pipeline.'
)
def boston_pipeline():
    _preprocess_op = preprocess_op()
    client = kfp.Client()
    client.create_run_from_pipeline_func(boston_pipeline, arguments={})

