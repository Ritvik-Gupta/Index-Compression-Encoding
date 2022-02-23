import pandas as pd
import plotly.express as px

df = pd.read_csv("docs/profile_coders.csv")

px.line(
    df,
    x="Number",
    y="Message Size",
    color="Coder Name",
    title="Index Compression Encoders",
).show()
