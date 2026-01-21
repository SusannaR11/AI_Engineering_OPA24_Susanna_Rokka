from fastapi import FastAPI
from backend.rag import rag_agent
from backend.data_models import Prompt

app = FastAPI()

@app.get("/test")
async def test():
    return {"test": "hello"}


@app.post("/rag/query")
async def query_documentation(query: Prompt):
    result = await rag_agent.run(query.prompt)
    
    return result.data  # data or output ??

# to run the API run the following command:
# uvicorn api:app --reload
# 127.0.0.1:8000/docs