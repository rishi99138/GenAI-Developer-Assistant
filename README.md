# GenAI-Powered Developer Assistant

[![Status](https://img.shields.io/badge/Status-Work%20in%20Progress-yellow)](https://github.com/your-username/your-repo-name)

### Project Vision

An intelligent developer assistant that uses a Retrieval-Augmented Generation (RAG) architecture to provide conversational answers about any public GitHub repository. This tool is designed to accelerate developer onboarding and improve codebase comprehension by acting as an on-demand expert for any project.

---

### Planned Features

* **GitHub Repo Ingestion:** Ingests documentation (`README.md`, `/docs` folder) and recent issues from a given repository URL.
* **RAG Pipeline:** Uses LangChain to build a robust pipeline that chunks, embeds, and stores the repository's knowledge in a Vector Database.
* **Conversational Q&A:** An interactive UI (built with Streamlit) for users to ask natural language questions.
* **Cloud-Native Deployment:** The entire application will be containerized with Docker for scalable, serverless deployment.

---

### Tech Stack

* **Language:** Python
* **Core Framework:** LangChain
* **LLM:** Google Gemini / OpenAI GPT
* **Vector Database:** ChromaDB
* **Frontend:** Streamlit
* **Containerization:** Docker
* **Deployment:** Streamlit Community Cloud / Hugging Face Spaces

---

### Current Status

The foundational architecture is being laid out. The project structure has been created, and the core RAG logic is currently under development.
