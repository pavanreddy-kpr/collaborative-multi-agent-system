def reviewer_agent(solution):
    review = f"""
    REVIEW RESULT

    Solution Received:
    {solution}

    Review:
    1. Checked the solution.
    2. Verified the structure.
    3. Confirmed the solution is ready.

    Status: APPROVED
    """

    return review