from fastapi import FastAPI
from app.models import RunTestsRequest, RunTestsResponse
from app.services import run_tests

app = FastAPI()

@app.get("/")
def root():
    return {"message": "AI Model Validator API is live!"}

@app.post("/run-tests", response_model=RunTestsResponse)
def run_tests_endpoint(request: RunTestsRequest):
    results = run_tests(request.test_cases)
    return {"results": results}
