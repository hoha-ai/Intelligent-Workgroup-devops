import os
import requests
import argparse

# 定义API的URL
url = "http://120.196.67.248:18123/api/files/database/upload"

# 定义请求头，包含token和其他必要字段
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiNDExNjFiNjgtNTU0Yy00NWQzLTkxOGItNWJjZTc4MzdiNmRjIiwiZXhwIjoxNzQzMjA4NDU3fQ.zc8uq0bZ5TUDcMuHe7jAWcnY4Ijpc30CTcsmxkHhFn4",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Origin": "http://120.196.67.248:18123",
    "Referer": "http://120.196.67.248:18123/api/files/database/upload_to/e794f9da-77a5-4a0f-848b-8ecd1a90c8aa/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiNDExNjFiNjgtNTU0Yy00NWQzLTkxOGItNWJjZTc4MzdiNmRjIiwiZXhwIjoxNzQzMjA4NDU3fQ.zc8uq0bZ5TUDcMuHe7jAWcnY4Ijpc30CTcsmxkHhFn4",
    "X-Requested-With": "XMLHttpRequest"
}

def upload_files(directory, extension):
    """遍历目录并上传指定扩展名的文件"""
    # 遍历目录下所有文件
    for filename in os.listdir(directory):
        # 检查文件是否以指定扩展名结尾
        if filename.endswith(extension):
            # 构建文件的完整路径
            file_path = os.path.join(directory, filename)
            
            # 打开文件并准备上传
            with open(file_path, 'rb') as file:
                # 定义请求体，包含文件内容和 database_id
                files = {
                    "file": (filename, file, "text/plain")  # 文件部分
                }
                data = {
                    "database_id": "e794f9da-77a5-4a0f-848b-8ecd1a90c8aa"  # database_id 部分
                }
                
                # 发送POST请求，包含 headers、files 和 data
                response = requests.post(url, headers=headers, files=files, data=data)
                
                # 输出上传结果
                print(f"文件 {filename} 上传结果:")
                print(f"状态码: {response.status_code}")
                print(f"响应内容: {response.text}")
                print("-" * 40)

def main():
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(description="上传指定目录下所有指定扩展名的文件")
    parser.add_argument("directory", type=str, help="要遍历的目录路径")
    parser.add_argument("extension", type=str, help="要上传的文件扩展名，例如 .txt, .csv 等")
    
    # 解析命令行参数
    args = parser.parse_args()
    
    # 调用上传函数
    upload_files(args.directory, args.extension)

if __name__ == "__main__":
    main()