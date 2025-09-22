# 🤖 GenAI Repo Assistant

A conversational AI assistant that uses a Retrieval-Augmented Generation (RAG) pipeline to answer questions about any public GitHub repository.

---

## 🚀 Live Demo

You can try the live application hosted on Hugging Face Spaces:

**[https://rishi99138-genai-developer-assistant.hf.space](https://rishi99138-genai-developer-assistant.hf.space)**

---

## 📋 Project Overview

This project is a full-stack Generative AI application built to solve a common developer problem: quickly understanding a new or complex codebase. Instead of manually searching through documentation and issues, this tool allows developers to ask natural language questions and receive accurate, context-aware answers.

The application ingests a repository's `README.md` file, processes the text, and uses a vector database for efficient semantic retrieval. A Large Language Model then generates a coherent answer based on the retrieved information.

## ✨ Features

* **Dynamic Data Ingestion:** Fetches and processes the `README.md` from any public GitHub repository in real-time.
* **RAG Pipeline:** Implements a Retrieval-Augmented Generation pipeline to ensure answers are factually grounded in the provided document, minimizing hallucinations.
* **Conversational Interface:** A user-friendly, chat-based UI built with Streamlit that maintains conversation history.
* **Performance Optimized:** Caches processed repositories to provide near-instant responses for subsequent queries on the same URL.
* **Cloud-Native:** Deployed and fully functional on a public cloud platform (Hugging Face Spaces).

## 🛠️ Tech Stack

* **Language:** Python
* **Core Framework:** LangChain
* **LLM:** Google Gemini
* **Embeddings:** Hugging Face `all-MiniLM-L6-v2`
* **Vector Store:** ChromaDB
* **Frontend:** Streamlit
* **Deployment:** Hugging Face Spaces / AWS App Runner (via Docker)