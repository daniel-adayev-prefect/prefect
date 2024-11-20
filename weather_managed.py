import pandas as pd
from prefect import flow

@flow(log_prints=True)
def run_pandas():
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'Age': [24, 27, 22, 32, 29],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
    }

    # Create a pandas DataFrame from the dictionary
    df = pd.DataFrame(data)

    # Print the first 5 lines of the DataFrame
    print(df.head())
    return data
