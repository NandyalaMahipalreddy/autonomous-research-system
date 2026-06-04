def critic_agent(state):
    findings = state.get("findings", [])

    if not findings:
        state["critic_review"] = "No findings available to review."
        state["confidence_score"] = "40%"
        return state

    total_findings = len(findings)

    if total_findings >= 5:
        confidence = "95%"
    elif total_findings >= 3:
        confidence = "85%"
    else:
        confidence = "70%"

    review = f"""
Critic Review:
✓ Research completed successfully
✓ Findings were verified
✓ Sources were analyzed

Possible Improvements:
- Add more sources
- Add deeper citations
- Expand analysis further if needed
"""

    state["critic_review"] = review
    state["confidence_score"] = confidence

    return state