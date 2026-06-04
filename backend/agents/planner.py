def planner_agent(state):

    query = state["query"]

    tasks = [
        f"Research background of {query}",
        f"Find latest updates about {query}",
        f"Collect important facts and statistics about {query}"
    ]

    # preserve old state
    state["tasks"] = tasks

    return state