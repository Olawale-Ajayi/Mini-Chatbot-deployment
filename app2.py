from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from test import OpenAIresponse  # same function you used in Flask

# Initialize FastAPI app
app = FastAPI(
    title="OpenAI Response API",
    description="Ask a question and get an OpenAI-powered response",
    version="1.0.0"
)

# Define request body schema
class QuestionRequest(BaseModel):
    question: str

# Root endpoint
@app.get("/")
def home():
    return {"message": "Pls ask your question"}

# Response endpoint
@app.post("/response")
def ask_question(request: QuestionRequest):
    if not request.question.strip():
        raise HTTPException(status_code=400, detail="No question provided, pls provide question")

    answer = OpenAIresponse(request.question)

    return {
        "question": request.question,
        "answer": answer
    }