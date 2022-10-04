FROM python:3.7-slim

WORKDIR /app

RUN pip install -U scikit-learn numpy

COPY kubeflow_pipelines_train.py ./train.py

ENTRYPOINT [ "python", "train.py" ]
