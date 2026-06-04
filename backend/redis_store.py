import redis
import json

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

def save_state(job_id, data):
    redis_client.set(
        job_id,
        json.dumps(data)
    )

def load_state(job_id):
    data = redis_client.get(job_id)

    if data:
        return json.loads(data)

    return None

def delete_state(job_id):
    redis_client.delete(job_id)