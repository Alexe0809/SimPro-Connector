import simpro

tools = [
    {
        "type": "function",
        "function": {
            "name": "find_customer",
            "description": "Найти клиента по имени или части имени. Возвращает список подходящих клиентов с их id.",
            "parameters": {
                "type": "object",
                "properties": {"name": {"type": "string"}},
                "required": ["name"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_jobs",
            "description": "Получить список всех заказов клиента по его id.",
            "parameters": {
                "type": "object",
                "properties": {"customer_id": {"type": "integer"}},
                "required": ["customer_id"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_job",
            "description": "Получить один заказ по его id.",
            "parameters": {
                "type": "object",
                "properties": {"job_id": {"type": "integer"}},
                "required": ["job_id"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "add_note",
            "description": "Добавить текстовую заметку к заказу по его id.",
            "parameters": {
                "type": "object",
                "properties": {
                    "job_id": {"type": "integer"},
                    "note": {"type": "string"},
                },
                "required": ["job_id", "note"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "change_status",
            "description": "Изменить статус заказа по его id. Например: new, overdue, completed.",
            "parameters": {
                "type": "object",
                "properties": {
                    "job_id": {"type": "integer"},
                    "status": {"type": "string"},
                },
                "required": ["job_id", "status"],
            },
        },
    },
]

available_functions = {
    "find_customer": simpro.find_customer,
    "get_jobs": simpro.get_jobs,
    "get_job": simpro.get_job,
    "add_note": simpro.add_note,
    "change_status": simpro.change_status,
}