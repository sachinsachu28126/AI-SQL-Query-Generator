import pandas as pd

def sample_table():

    data = {
        "EmployeeID":[101,102,103],
        "Name":["John","David","Sarah"],
        "Salary":[50000,60000,70000]
    }

    return pd.DataFrame(data)