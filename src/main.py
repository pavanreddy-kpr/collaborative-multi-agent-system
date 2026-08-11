from agents.planner import planner_agent
from agents.developer import developer_agent
from agents.reviewer import reviewer_agent


def run_multi_agent_system():
    print("Collaborative Multi-Agent System")
    print("--------------------------------")

    user_request = input("Enter your task: ")

    print("\nPlanner Agent is working...")
    plan = planner_agent(user_request)
    print(plan)

    print("\nDeveloper Agent is working...")
    solution = developer_agent(plan)
    print(solution)

    print("\nReviewer Agent is working...")
    review = reviewer_agent(solution)
    print(review)


if __name__ == "__main__":
    run_multi_agent_system()