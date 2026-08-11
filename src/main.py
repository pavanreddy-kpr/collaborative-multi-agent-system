from agents.coordinator import coordinator_agent


def run_multi_agent_system():
    print("=" * 50)
    print("      COLLABORATIVE MULTI-AGENT SYSTEM")
    print("=" * 50)

    user_request = input("\nEnter your task: ")

    result = coordinator_agent(user_request)

    print("\n" + "=" * 50)
    print("MULTI-AGENT WORKFLOW COMPLETED")
    print("=" * 50)

    print("\nFinal Review:")
    print(result["review"])


if __name__ == "__main__":
    run_multi_agent_system()