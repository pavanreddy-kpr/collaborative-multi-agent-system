import requests


def planner_agent(user_request):
    prompt = f"""
You are a Planner Agent in a collaborative multi-agent system.

Your job is to:
1. Understand the user's request.
2. Break the request into clear implementation steps.
3. Identify important requirements.
4. Give the Developer Agent a practical plan.

User request:
{user_request}

Return only the development plan.
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