def find_customers(name):
    customers = [
        {"id": 1, "name": "ABC", "email": "abc@example.com"},
        {"id": 2, "name": "XYZ", "email": "xyz@example.com"},
    ]
    return [c for c in customers if name.lower() in c['name'].lower()]