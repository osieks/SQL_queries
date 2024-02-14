import pandas as pd
import pandasql as ps
class PandasDF:
        products_DF=pd.DataFrame()
        def __init__(self, products):
                # Create DataFrame
                self.products_DF = products

        def print(self):
                print(self.products_DF)

                print(self.products_DF.dtypes)

        def query(self, question):
                #question = """SELECT product_id FROM products """

                print(ps.sqldf(question, locals()))