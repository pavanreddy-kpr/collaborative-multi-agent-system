from agents.planner import planner_agent
from agents.developer import developer_agent
from agents.reviewer import reviewer_agent


def coordinator_agent(user_request):
    print("\nCoordinator Agent received the task.")

    print("\nPlanner Agent is working...")
    plan = planner_agent(user_request)

    print("\n--- PLAN ---")
    print(plan)

    print("\nDeveloper Agent is working...")
    solution = developer_agent(plan)

    print("\n--- DEVELOPER SOLUTION ---")
    print(solution)

    max_iterations = 2

    for iteration in range(max_iterations):

        print(f"\nReviewer Agent is working... Review #{iteration + 1}")

        review = reviewer_agent(solution)

        print("\n--- REVIEW ---")
        print(review)

        if "STATUS: APPROVED" in review:
            print("\nSolution approved by Reviewer Agent.")
            break

        if "STATUS: NEEDS IMPROVEMENT" in review:
            print("\nReviewer requested improvements.")
            print("\nDeveloper Agent is revising the solution...")

            solution = developer_agent(
                plan,
                feedback=review
            )

            print("\n--- REVISED DEVELOPER SOLUTION ---")
            print(solution)

    return {
        "plan": plan,
        "solution": solution,
        "review": review
    }