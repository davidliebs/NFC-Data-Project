import pandas as pd
from datetime import datetime

# df = pd.DataFrame({"Timestamp": [datetime.now().strftime("%H:%M")], "Room": ["Lounge"]}, columns=["Timestamp", "Room"])
# df.to_csv()

df = pd.read_csv("test.csv")
print(df)
# df1 = pd.DataFrame({"Timestamp": [datetime.now().strftime("%H:%M")], "Room": ["Best room"]}, columns=["Timestamp", "Room"])

# df2 = pd.concat([df, df1])
# print(df2)