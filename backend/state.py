from typing import TypedDict, List


class ResearchState(TypedDict):
    query: str
    document_path: str

    tasks: List[str]
    findings: List[str]
    contradictions: List[str]
    critic_notes: List[str]

    sources: List[dict]

    confidence_score: str

    report: str

    retrieved_docs: list

    # Statistics
    search_count: int
    llm_calls: int
    total_cost: float