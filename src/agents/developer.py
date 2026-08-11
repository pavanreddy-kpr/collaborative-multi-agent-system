import requests


def developer_agent(plan, feedback=None):
    if feedback:
        prompt = f"""
You are a Developer Agent in a collaborative multi-agent system.

You previously created a solution based on this plan:

{plan}

The Reviewer Agent provided this feedback:

{feedback}

Your job is to improve the solution based on that feedback.

Requirements:
1. Fix identified bugs.
2. Improve edge-case handling.
3. Improve code quality.
4. Preserve the original requirements.
5. Return the revised implementation.

Return the improved solution only.
"""
    else:
        prompt = f"""
You are a Developer Agent in a collaborative multi-agent system.

You receive a development plan from the Planner Agent.

Your job is to:
1. Understand the plan.
2. Create the requested implementation.
3. Write clean and correct Python code.
4. Handle edge cases.
5. Return the implementation.

Planner's plan:

{plan}
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