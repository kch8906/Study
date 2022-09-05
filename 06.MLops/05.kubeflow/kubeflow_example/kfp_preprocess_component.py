import kfp
from kfp import dsl
from kfp.components import create_component_from_func


def preprocess_op():

    return dsl.ContainerOp(
        name='Preprocess Data',
        image='crysiss/changhyun-preprocess:0.7',
        arguments=[],
        file_outputs={
            'x_train': '/app/x_train.npy',
            'x_test': '/app/x_test.npy',
            'y_train': '/app/y_train.npy',
            'y_test': '/app/y_test.npy',
        }
    )


def train_op(x_train, y_train):

    return dsl.ContainerOp(
        name='Train Model',
        image='crysiss/changhyun-train:0.5',
        arguments=[
            '--x_train', x_train,
            '--y_train', y_train
        ],
        file_outputs={
            'model': '/app/model.pkl'
        }
    )


def test_op(x_test, y_test, model):

    return dsl.ContainerOp(
        name='Test Model',
        image='crysiss/changhyun-test:0.5',
        arguments=[
            '--x_test', x_test,
            '--y_test', y_test,
            '--model', model
        ],
        file_outputs={
            'mean_squared_error': '/app/output.txt'
        }
    )


def deploy_model_op(model):

    return dsl.ContainerOp(
        name='Deploy Model',
        image='crysiss/changhyun-deploy:0.5',
        arguments=[
            '--model', model
        ]
    )

@dsl.pipeline(
   name='Iris Pipeline',
   description='An example pipeline that trains and logs a regression model.'
)
def iris_pipeline():
    _preprocess_op = preprocess_op()
    
    _train_op = train_op(
        dsl.InputArgumentPath(_preprocess_op.outputs['x_train']),
        dsl.InputArgumentPath(_preprocess_op.outputs['y_train'])
    ).after(_preprocess_op)

    _test_op = test_op(
        dsl.InputArgumentPath(_preprocess_op.outputs['x_test']),
        dsl.InputArgumentPath(_preprocess_op.outputs['y_test']),
        dsl.InputArgumentPath(_train_op.outputs['model'])
    ).after(_train_op)

    deploy_model_op(
        dsl.InputArgumentPath(_train_op.outputs['model'])
    ).after(_test_op)

if __name__ == "__main__":
    import kfp.compiler as compiler
    compiler.Compiler().compile(iris_pipeline, "iris_pipeline.tar.gz")



