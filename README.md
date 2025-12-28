# Mini-RAG

This is a simple RAG (Retrieval Augmented Generation) system built with Python, LangChain, and OpenAI.

## Requirements

- Python 3.8 or later 

#### install Python using miniconda

1) Download miniconda from https://docs.conda.io/en/latest/miniconda.html
2) create a new environment
```bash
conda create -n mini-rag python=3.8
``` 
3) activate the environment
```bash
conda activate mini-rag
```     
4) install requirements
```bash
pip install -r requirements.txt
```
### Set up environment variables

```bash
cp .env.example .env
```
set you environment variables in the .env file. Like OPENAI_API_KEY = your_api_key

## run the fastapi server
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 5000
```     
## postman collection
```bash
postman_collection.json
```