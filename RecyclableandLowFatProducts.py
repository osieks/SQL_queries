import pandas as pd
import pandasql as ps

data = [['0', 'Y', 'N'], ['1', 'Y', 'Y'], ['2', 'N', 'Y'], ['3', 'Y', 'Y'], ['4', 'N', 'N']]
products = pd.DataFrame(data, columns=['product_id', 'low_fats', 'recyclable']).astype({'product_id':'int64', 'low_fats':'category', 'recyclable':'category'})

print(products)

print(products.dtypes)

q1 = """
SELECT product_id 
FROM products 
WHERE low_fats = 'Y' 
AND recyclable = 'Y'"""

print(ps.sqldf(q1, locals()))

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return products.query('low_fats == "Y" & recyclable == "Y"')[["product_id"]]

print(find_products(products))