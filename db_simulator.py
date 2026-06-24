import pandas as pd

def sample_table():

    data = {
        "EmployeeID":[101,102,103,104],
        "Name":[
            "John",
            "David",
            "Sarah",
            "Michael"
        ],
        "Department":[
            "HR",
            "IT",
            "Finance",
            "Marketing"
        ],
        "Salary":[
            50000,
            60000,
            70000,
            55000
        ]
    }

    return pd.DataFrame(data)