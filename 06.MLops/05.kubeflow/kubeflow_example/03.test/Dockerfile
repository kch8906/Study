FROM python:3.7-slim

WORKDIR /app

RUN pip install -U scikit-learn numpy

COPY kubeflow_pipelines_test.py ./test.py

ENTRYPOINT [ "python", "test.py" ]