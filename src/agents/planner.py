def planner_agent(user_request):
    plan = f"""
    PLAN

    User Request:
    {user_request}

    Steps:
    1. Understand the user's request.
    2. Break the request into smaller tasks.
    3. Determine what needs to be developed.
    4. Send the plan to the Developer Agent.
    """

    return plan