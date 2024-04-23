import pandas as pd

german_credit_data = pd.read_csv("german_credit_data_target.csv")
loans_data = pd.read_csv("loans_full_schema.csv")


german_credit_data_extended = german_credit_data.sample((len(german_credit_data)*10), replace=True)
loans_data_extended = loans_data.sample((len(loans_data)*10), replace=True)

german_credit_data_extended.to_csv("german_credit_data_extended.csv", index=False)
loans_data_extended.to_csv("loans_data_extended.csv", index=False)
