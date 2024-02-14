import pandas as pd
import pandasql as ps

data = [[1, 'Will', None], [2, 'Jane', None], [3, 'Alex', 2], [4, 'Bill', None], [5, 'Zack', 1], [6, 'Mark', 2]]
customer = pd.DataFrame(data, columns=['id', 'name', 'referee_id']).astype({'id':'Int64', 'name':'object', 'referee_id':'Int64'})

q1 = """
SELECT name 
FROM customer 
WHERE referee_id NOT LIKE 2 OR referee_id IS NULL"""

print("SQL1")
print(ps.sqldf(q1, locals()))

q2 = """
SELECT name 
FROM customer 
WHERE COALESCE(referee_id,0) NOT LIKE 2"""

print("SQL2")
print(ps.sqldf(q2, locals()))

print("Pandas")
def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    customer["referee_id"] = customer["referee_id"].fillna(0)
    return pd.DataFrame(customer.query('referee_id != 2')["name"])
print(find_customer_referee(customer))