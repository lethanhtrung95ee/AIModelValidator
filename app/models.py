from pydantic import BaseModel
from typing import List, Optional

class TestCase(BaseModel):
    prompt: str
    expected_output: str
    actual_output: str

class RunTestsRequest(BaseModel):
    test_cases: List[TestCase]

class TestResult(BaseModel):
    prompt: str
    expected_output: str
    actual_output: str
    correctness: Optional[bool]
    consistency: Optional[bool]
    java_score: Optional[int]

class RunTestsResponse(BaseModel):
    results: List[TestResult]
