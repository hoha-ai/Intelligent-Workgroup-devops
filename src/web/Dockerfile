FROM registry.jxit.net.cn:5000/alpine:3.19.1

RUN sed -i 's@dl-cdn.alpinelinux.org@mirrors.tencent.com@g' /etc/apk/repositories && \
    apk update && \
    apk add vim curl bash tcpdump tzdata nginx && \
    cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo "Asia/Shanghai" > /etc/timezone

WORKDIR /usr/share/nginx/html

COPY dist /usr/share/nginx/html
