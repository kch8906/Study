# syntax=docker/dockerfile:1
FROM jupyter/base-notebook
WORKDIR /home/jovyan
COPY . /home/jovyan

RUN conda install -c conda-forge mmh3 -y 
RUN pip3 install -r requirements.txt

USER jovyan
RUN feast init feature_repo && cd /home/jovyan/feature_repo/feature_repo && feast apply && feast materialize-incremental $(date +%Y-%m-%d)

COPY feature_server.py /opt/conda/lib/python3.9/site-packages/feast/feature_server.py
CMD [ "/bin/sh", "-c", "cd /home/jovyan/feature_repo/feature_repo && feast serve -h 0.0.0.0" ]

WORKDIR /home/jovyan
