#!/bin/bash

rule="$1"     # master or node
platform="$2" # x86 or arm
masterip="$3" # master ip address
token="$4"    # master token

if [ -z "$rule" -o -z "$platform" ]; then
  echo "usage: $0 [rule] [platform] [masterip] [token]"
  echo "rule:     master or node"
  echo "platform: x86 or arm"
  echo "masterip: master ip address(only for agent)"
  echo "token:    master token(only for agent)"
  exit
fi

download="stu.jxit.net.cn:88"

# 不存在K3s二进制程序则下载，无网则退出
if [ ! -e "./k3s" -a ! -e "/usr/local/bin/k3s" ]; then
  wget http://$download/uniserver/k3s/$platform/k3s
  if [ $? -ne 0 ]; then
    echo "no k3s binary and network, exit ..."
    exit
  fi
fi
chmod +x k3s && cp k3s /usr/local/bin/

# 不存在K3s镜像包则下载，无网则退出
if [ ! -e ./k3s-airgap-images-$platform.tar ]; then
  wget http://$download/uniserver/k3s/$platform/k3s-airgap-images-$platform.tar.gz
  tar -zxf k3s-airgap-images-$platform.tar.gz
  rm k3s-airgap-images-$platform.tar.gz
  if [ $? -ne 0 ]; then
    echo "no k3s-airgap-images-$platform.tar binary and network, exit ..."
    exit
  fi
fi
mkdir -p /var/lib/rancher/k3s/agent/images/
cp k3s-airgap-images-$platform.tar /var/lib/rancher/k3s/agent/images/

# 判断是否为主节点，决定安装server还是agent
if [ "$rule" == "master" ]; then
  INSTALL_K3S_SKIP_DOWNLOAD=true ./k3s-install.sh --disable=traefik
  echo "master token is $(cat /var/lib/rancher/k3s/server/node-token)"
  echo "source /usr/share/bash-completion/bash_completion" >> ~/.bashrc
  echo "source <(kubectl completion bash)" >> ~/.bashrc
  source ~/.bashrc
else
  INSTALL_K3S_SKIP_DOWNLOAD=true K3S_URL=https://$masterip:6443 K3S_TOKEN=$token ./k3s-install.sh
fi

