import pandas as pd

df = pd.DataFrame(all_data)

df.to_csv("airport_data.csv", index=False)