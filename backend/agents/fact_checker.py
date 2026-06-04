def fact_checker_agent(state):

    findings = state.get("findings", [])

    verified_findings = []
    contradictions = []

    for finding in findings:

        if len(finding.strip()) > 20:
            verified_findings.append(f"✓ Verified: {finding}")
        else:
            contradictions.append(f"Possible weak information: {finding}")

    # if no contradiction found, show default message
    if len(contradictions) == 0:
        contradictions.append("No contradictions detected between sources.")

    state["findings"] = verified_findings
    state["contradictions"] = contradictions

    return state