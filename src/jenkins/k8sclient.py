import datetime
import argparse
from kubernetes import client, config
from kubernetes.client.rest import ApiException

def restart_deployment(namespace, name):
    try:
        # 加载k8s集群配置（从 Pod 内部读取配置），创建API客户端
        config.load_incluster_config()
        api_instance = client.AppsV1Api()

        # 获取现有的 Deployment
        deployment = api_instance.read_namespaced_deployment(name, namespace)

        # 修改 Deployment 的模板标签，触发滚动更新
        now = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H-%M-%S")
        if not deployment.spec.template.metadata.labels:
            deployment.spec.template.metadata.labels = {}
        deployment.spec.template.metadata.labels['restartedAt'] = now

        # 更新 Deployment
        api_response = api_instance.patch_namespaced_deployment(
            name, 
            namespace, 
            deployment
        )
        print(f"Deployment '{name}' in namespace '{namespace}' restarted. Status: {api_response.status}")
    except ApiException as e:
        print(f"Failed to restart Deployment '{name}': {e}\n")

def main():
    # 设置命令行参数解析
    parser = argparse.ArgumentParser(description="Restart a Kubernetes Deployment by name.")
    parser.add_argument("--namespace", "-n", required=True, help="Namespace of the Deployment")
    parser.add_argument("--name", "-d", required=True, help="Name of the Deployment to restart")
    args = parser.parse_args()

    # 调用重启函数
    restart_deployment(args.namespace, args.name)

if __name__ == "__main__":
    main()

