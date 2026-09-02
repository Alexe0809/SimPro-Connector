_customers = [
    {"id": 1, "name": "ABC", "email": "abc@example.com"},
    {"id": 2, "name": "XYZ", "email": "xyz@example.com"},
]

_jobs = [
    {"id": 123, "customer_id": 1, "title": "Замена проводки", "status": "overdue"},
    {"id": 124, "customer_id": 1, "title": "Установка розеток", "status": "completed"},
    {"id": 200, "customer_id": 2, "title": "Ремонт щитка", "status": "new"},
]

def find_customer(name):
    return [c for c in _customers if name.lower() in c["name"].lower()]

def get_jobs(customer_id):
    return [j for j in _jobs if j["customer_id"] == customer_id]

def get_job(job_id):
    for j in _jobs:
        if j["id"] == job_id:
            return j
    return None

def add_note(job_id, note):
    return {"job_id": job_id, "note": note, "result": "note added"}

def change_status(job_id, status):
    for j in _jobs:
        if j["id"] == job_id:
            j["status"] = status
            return j
    return None