from backend.llm import ask_llama


def formatter_agent(state):

    query = state["query"]
    findings = state.get("findings", [])
    contradictions = state.get("contradictions", [])
    critic_notes = state.get("critic_notes", [])
    confidence_score = state.get("confidence_score", "90%")
    sources = state.get("sources", [])

    findings_text = "\n".join(findings[:5])

    prompt = f"""
Write a professional research report about:

Topic: {query}

Based on these findings:
{findings_text}

Include:
1. Summary
2. Key insights
3. Final conclusion
"""

    try:
        ai_summary = ask_llama(prompt)
    except Exception as e:
        print("GROQ ERROR:", e)
        ai_summary = "AI summary generation failed."

    report = f"Research Report\n\n"

    report += f"📌 Topic\n{query}\n\n"

    report += "🤖 AI Research Summary\n\n"
    report += f"{ai_summary}\n\n"

    report += "⚠️ Contradiction Checker\n\n"

    if contradictions:
        for contradiction in contradictions:
            report += f"• {contradiction}\n\n"
    else:
        report += "• No contradictions detected\n\n"

    report += "🧠 Critic Review\n\n"

    if critic_notes:
        for note in critic_notes:
            report += f"• {note}\n\n"
    else:
        report += "• Research reviewed successfully\n\n"

    report += "📊 Confidence Score\n\n"
    report += f"{confidence_score}\n\n"

    report += "🔗 Sources\n\n"

    if sources:
        for source in sources:
            report += f"• {source['title']}\n"
            report += f"{source['url']}\n\n"
    else:
        report += "• No sources available\n\n"

    report += "✅ Conclusion\nResearch completed successfully."

    state["report"] = report

    return state