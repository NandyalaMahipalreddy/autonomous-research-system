from langgraph.graph import StateGraph, END

from backend.state import ResearchState

from backend.agents.planner import planner_agent
from backend.agents.web_research import web_research_agent
#from backend.agents.document_retrieval import document_retrieval_agent
from backend.agents.fact_checker import fact_checker_agent
from backend.agents.critic import critic_agent
from backend.agents.formatter import formatter_agent


def create_workflow():

    workflow = StateGraph(
        ResearchState
    )

    workflow.add_node(
        "planner",
        planner_agent
    )

    #workflow.add_node(
    #    "document_retrieval",
    #    document_retrieval_agent
    #)

    workflow.add_node(
        "web_research",
        web_research_agent
    )

    workflow.add_node(
        "fact_checker",
        fact_checker_agent
    )

    workflow.add_node(
        "critic",
        critic_agent
    )

    workflow.add_node(
        "formatter",
        formatter_agent
    )

    workflow.set_entry_point(
        "planner"
    )

    workflow.add_edge(
    "planner",
    "web_research"
)

    workflow.add_edge(
        "web_research",
        "fact_checker"
    )

    workflow.add_edge(
        "fact_checker",
        "critic"
    )

    workflow.add_edge(
        "critic",
        "formatter"
    )

    workflow.add_edge(
        "formatter",
        END
    )

    return workflow.compile()