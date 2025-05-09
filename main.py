from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn


from get_llm_response import get_answer

app = FastAPI()

# CORS Settings
origins = ["*"]  # Allow all origins (can be restricted)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Input Request Model
class QuestionRequest(BaseModel):
    question: str

# Response Body Model
class AnswerResponse(BaseModel):
    answer: str

# POST endpoint
@app.post("/ask", response_model=AnswerResponse)
def answer_question(question: QuestionRequest):
    user_question = question.question
    # You can add logic here to generate answers
    answer = get_answer(user_question)
    return {"answer": answer}

# Only run if executed directly
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)


