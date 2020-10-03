import pandas as pd
from datetime import datetime
import config_var

df = pd.DataFrame({"Timestamp": [datetime.now()], "Room": ["Lounge"]}, columns=["Timestamp", "Room"])
df.to_csv(config_var.api_csv_file_name, index=False)