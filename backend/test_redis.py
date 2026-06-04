from backend.redis_store import (
    save_state,
    load_state
)

save_state(
    "test-job",
    {
        "query": "about prabhas",
        "status": "completed"
    }
)

result = load_state(
    "test-job"
)

print(result)