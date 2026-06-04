from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from backend.graph.workflow import create_workflow
from backend.pdf_generator import generate_pdf
import backend.llm as llm
from backend.database import (
    create_table,
    save_research,
    get_history,
    delete_research
)
from backend.database import get_report
import os
from backend.redis_store import (
    save_state,
    load_state
)
from backend.database import delete_research

app = FastAPI()
create_table()

# Create folders
os.makedirs("documents", exist_ok=True)
os.makedirs("reports", exist_ok=True)

# Static PDF serving
app.mount(
    "/reports",
    StaticFiles(directory="reports"),
    name="reports"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

workflow = create_workflow()


@app.get("/")
def home():
    return {
        "message": "Autonomous Multi-Agent Research System Running 🚀"
    }


@app.post("/research")
async def research(
    query: str = Form(...),
    depth: str = Form("Medium"),
    max_iterations: int = Form(5),
    cost_limit: int = Form(2),
    output_format: str = Form("PDF"),
    file: UploadFile = File(None)
):

    document_path = None

    # Save uploaded file
    if file:

        document_path = f"documents/{file.filename}"

        with open(document_path, "wb") as f:
            f.write(await file.read())

    # Run Workflow
    result = workflow.invoke({

        "query": query,
        "depth": depth,
        "max_iterations": max_iterations,
        "cost_limit": cost_limit,
        "output_format": output_format,
        "document_path": document_path,

        "tasks": [],
        "findings": [],
        "contradictions": [],
        "critic_notes": [],
        "sources": [],
        "retrieved_docs": [],

        "confidence_score": "90%",
        "report": "",

        # Statistics
        "search_count": 0,
        "llm_calls": 0,
        "total_cost": 0
    })
    try:
        save_state(
        query,
        result
    )
    except Exception as e:
        print("Redis Error:", e)

    
    

    # Generate PDF
    pdf_file = generate_pdf(result["report"])

    # Safe access
    search_count = result.get("search_count", 0)

    search_cost = search_count * 0.001

    llm_cost = llm.LLM_CALLS * 0.001

    total_cost = search_cost + llm_cost

    save_research(
    query=query,
    report=result["report"],
    cost=round(total_cost, 4),
    pdf_file=pdf_file
)

    return {

        "report": result["report"],

        "pdf_file": pdf_file,

        "search_count": search_count,

        "llm_calls": llm.LLM_CALLS,

        "total_cost": round(total_cost, 4),

        "tokens_used": 4250,

        "estimated_cost": round(total_cost, 4),

        "budget_limit": cost_limit
    }

@app.get("/history")
def history():

    rows = get_history()

    history = []

    for row in rows:

        history.append({

            "id": row[0],
            "query": row[1],
            "cost": row[2],
            "pdf_file": row[3],
            "created_at": row[4]

        })

    return history

@app.get("/history/{report_id}")
def get_history_report(report_id: int):

    report = get_report(report_id)

    return {
        "report": report
    }

@app.get("/state/{job_id}")
def get_saved_state(job_id: str):

    data = load_state(job_id)

    if not data:
        return {
            "message": "No state found"
        }

    return data

@app.delete("/history/{research_id}")
def delete_history(
    research_id: int
):

    delete_research(
        research_id
    )

    return {
        "message":
        "Research deleted successfully"
    }