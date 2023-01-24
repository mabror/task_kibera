## Installation
To install, you need create virtual environment:
```
```
After that:
```
>>> pip install -r requirements.txt
```

---
## Usage
Create superuser:
```
>>> python manage.py createsuperuser
```

Create post:
  Example request:
        {
            "name": "Abror",
            "content": "Mamadaliev",
            "user": 2
        }
    And response:
        {
        "id": 14,
        "name": "Abror",
        "content": "Mamadaliev",
        "published": "2023-01-24T16:14:58.448939Z",
        "user": 2
        }

Filter by name:
Example : http://127.0.0.1:8000/api/?name=abror

Ordering:
Example : http://127.0.0.1:8000/api/?ordering=-published
 

