import requests


def reviewer_agent(solution):
    prompt = f"""
You are a Reviewer Agent in a collaborative multi-agent system.

Review the Developer Agent's solution carefully.

Check:
1. Correctness
2. Code quality
3. Bugs
4. Missing edge cases
5. Error handling
6. Maintainability

Developer solution:

{solution}

At the very end, you MUST write exactly one of these:

STATUS: APPROVED

or

STATUS: NEEDS IMPROVEMENT
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "gemma3",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]