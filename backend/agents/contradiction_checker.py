from backend.state import ResearchState


def contradiction_checker_agent(state: ResearchState):
    findings = state["findings"]

    contradictions = []

    if len(findings) >= 2:
        if findings[0] != findings[1]:
            contradictions.append(
                "⚠ Contradiction detected between research sources."
            )

    return {
        "contradictions": contradictions
    }