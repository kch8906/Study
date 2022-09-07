import kfp
import kfp.dsl as dsl

@dsl.pipeline(
    name='Volume Op DAG',
    description='Volumn op!!'
)

def volume_op_dag():
    vop = dsl.VolumeOp(
        name='create_pvc', resource_name='my-pvc', size='10Gi', modes=dsl.VOLUME_MODE_RWM
    )
    
    step1 = dsl.ContainerOp(
        name='step1', image='library/bash:4.4.23', command=["sh", "-c"],
        arguments=["echo 1 | tee ./mnt/file1"],
        pvolumes={"./mnt": vop.volume}
    )
    
    step2 = dsl.ContainerOp(
        name='step2', image='library/bash:4.4.23', command=["sh", "-c"],
        arguments=["echo 2 | tee ./mnt/file2"],
        pvolumes={"./mnt": vop.volume}
    )
    
    step3= dsl.ContainerOp(
        name='step3', image='library/bash:4.4.23', command=["sh", "-c"],
        arguments=["cat ./mnt/file1 ./mnt/file2"],
        pvolumes={"./mnt": vop.volume.after(step1, step2)}
    )
    
if __name__ == "__main__":
    import kfp.compiler as compiler
    compiler.Compiler().compile(volume_op_dag, 'volume_op_dag.tar.gz')