FROM registry.jxit.net.cn:5000/deeptalk/cuda:12.3.2-base-ubuntu22.04

RUN apt-get -y update && \
    apt-get -y install python3 python3-pip curl wget iproute2 psmisc tcpdump vim && \
    apt-get clean && \ 
    rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY . /app
