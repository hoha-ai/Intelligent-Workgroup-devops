# 🤖 hoha.ai

<p align="center"> <strong>From Solo AI to Team Genius — Together.
</strong><br /> Pioneering the AI-native workgroup: A revolutionary platform where teams and AI collaborate as a unified intelligence. </p> <p align="center"> <a href="https://github.com/hoha-ai/Intelligent-Workgroup-devops/stargazers"><img src="https://img.shields.io/github/stars/hoha-ai/Intelligent-Workgroup-devops?style=social" alt="GitHub Stars"></a> <a href="https://github.com/hoha-ai/Intelligent-Workgroup-devops/blob/master/LICENSE"><img src="https://img.shields.io/github/license/hoha-ai/Intelligent-Workgroup-devops?style=flat-square&color=blue" alt="License"></a> <a href="https://hoha.ai"><img src="https://img.shields.io/badge/Website-hoha.ai-green?style=flat-square" alt="Website"></a> </p>
***

Tired of fragmented tools and siloed knowledge? hoha.ai moves beyond simple AI chatbots by creating a collaborative space where your team and multiple AIs work as a single, intelligent unit. This repository contains the open-source web platform, built from the ground up for the new era of AI-native teamwork.

## ✨ Core Features

*   **🤝 Unified Team Intelligence**: Where humans and AI agents collaborate in real-time, turning AI into a true team member, not just an assistant.
*   **🧠 Adaptive Knowledge Base**: Independent, private RAG for each workgroup. Upload your docs, and the AI learns your specific domain.
*   **📈 Evolving Insights**: Automatically captures knowledge from every interaction, providing instant expertise for new members and complex projects.
*   **🛡️ Enterprise-Ready**: Secure, scalable, and featuring comprehensive admin controls, multi-language support, and flexible LLM integrations.
*   **🌐 Open & Extensible**: A robust foundation for custom plugins and integrations, fostering innovation in AI-native collaboration.

## 💡 Real-World Use Cases

hoha.ai adapts to any knowledge-intensive workflow. Here are a few ideas to get you started:

*   **🏢 Corporate Teams**: Create a "department brain" for marketing or R\&D, where AI assists with strategy, research, and onboarding new employees.
*   **🩺 Professional Services**: A therapist or lawyer can create a private, secure workgroup for each client, where AI helps manage case files and communication.
*   **🎓 Education & Training**: Build a "Classroom Hub" with an AI teaching assistant that answers student questions 24/7 based on your course materials.
*   **🎨 Creative Studios**: For a new design project, use a workgroup as a shared inspiration board where AI helps generate ideas and drafts based on uploaded assets.
*   **📈 Investment Research**: For an investment firm, create a workgroup where AI analyzes market data and financial reports in real-time, helping analysts generate insights faster.
*   👥 **Community Building:** Use the SiteMind™ feature to convert website visitors into an engaged community, turning casual traffic into loyal customers.

**➡️ Want to see more detailed scenarios? Check out our [Use Cases Guide](https://demo.hoha.ai:18124/to-case_study.md).** 

## 🛠️ Technology Stack

Powered by a modern, scalable stack designed for real-time, AI-driven applications:

*   **Backend**: FastAPI
*   **AI Orchestration**: LangChain
*   **Vector Database**: Milvus
*   **File Storage**: SeaweedFS
*   **Database**: PostgreSQL
*   **Data Ingestion**: Unstructured

## 🚀 Quick Start

Deploy and run the hoha.ai web platform locally in minutes.
1.  **Install k3s**
    ```ruby
    curl -sfL https://get.k3s.io | INSTALL_K3S_VERSION=v1.28.8+k3s1 INSTALL_K3S_EXEC="--disable traefik --kube-apiserver-arg service-node-port-range=20-65535" sh -
    ```
2.  **Clone the repository:**
    ```ruby
    https://github.com/hoha-ai/Intelligent-Workgroup-devops/
    cd Intelligent-Workgroup-devops/
    ```
3.  **Create k8s resource**
    ```ruby
    kubectl create ns deeptalk
    kubectl apply -f k8s/pvc
    kubectl apply -f k8s/busi
    ```
5.  **Enter backend pod edit .env file**
    ```ruby
    root@root123-NF5568M4:~# kubectl -n deeptalk get pod | grep xboom
    deeptalk-xboom-549ccbc49c-8zn78            1/1     Running     4              126d
    root@root123-NF5568M4:~# kubectl -n deeptalk exec -it pod/deeptalk-xboom-549ccbc49c-8zn78 -- bash
    ls -al .env
    -rw-r--r-- 1 root root 3779 Sep 18 11:06 .env
    ```
    change mail server to send register code
    ```ruby
    MAIL_USERNAME=aiservice@aidynamic.com
    MAIL_PASSWORD=xxxxxx
    MAIL_FROM=aiservice@aidynamic.com
    MAIL_PORT=465
    MAIL_SERVER=smtp.qiye.aliyun.com
    ```
    change web search api address and token
    ```ruby
    WEB_API_URL=https://api.xxx.com/v1/web-search
    WEB_API_KEY=sk-xxxxx
    ```
    change embedding/reranking/chat model address and token
    ```ruby
    EMBEDDING_MODEL_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
    EMBEDDING_MODEL_NAME=text-embedding-v4
    EMBEDDING_MODEL_KEY=sk-xxx

    RERANKER_MODEL_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
    RERANKER_MODEL_NAME=gte-rerank
    RERANKER_MODEL_KEY=sk-xxx

    LOCAL_MODEL_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
    LOCAL_MODEL_NAME=qwen-plus
    LOCAL_MODEL_KEY=sk-xxx
    ```
7.  **Start backend server**
    start server and access http://youip:18123
    ```ruby
    root@root123-NF5568M4:~# bash restart.sh
    root@root123-NF5568M4:~# tail -f nohup.out
    ```
## 📱 Platforms

This repository focuses on the open-source web version. For an enhanced native experience and advanced features like **SiteMind™**, explore our commercial offerings on [hoha.ai](https://hoha.ai/).

*   ✅ **Backend** (Open Source)  [Github](https://github.com/hoha-ai/Intelligent-Workgroup-backend)
*   ✅ **Frontend** (Open Source)  [Github](https://github.com/hoha-ai/Intelligent-Workgroup-frontend)
*   🔒 **Windows App** (Commercial)
*   🔒 **macOS App** (Commercial)
*   🔒 **Android App** (Commercial)
*   🔒 **iOS App** (Commercial)

## 🤝 How to Contribute

We're building the future of AI-native collaboration, and we welcome you to join us! Please read our **[Contributing Guidelines](https://sider.ai/zh-CN/CONTRIBUTING.md)** to get started.

## 📄 License

Licensed under the **Apache License 2.0**. Full details in the [LICENSE](https://github.com/hoha-ai/Intelligent-Workgroup-devops/blob/master/LICENSE) file.

For inquiries about commercial licensing, please contact us at `hoha@leoyoung.tech`.

## 📞 Contact

*   **Website**: [hoha.ai](https://hoha.ai/)
*   **Business Inquiries**: `hoha@leoyoung.tech`
*   **Community & Support**: open [GitHub Issue](https://github.com/hoha-ai/Intelligent-Workgroup-devops/issues).

***

**If you believe in AI-native teamwork, give us a star! ⭐**
