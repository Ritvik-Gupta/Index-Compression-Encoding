import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("docs/profile_golomb.csv")

fig = go.Figure()
fig.update_layout(title="Golomb on `b`")

for coder_name in df["Coder Name"].unique():
    coder_df = df.loc[df["Coder Name"] == coder_name]
    fig.add_trace(
        go.Scatter(
            x=coder_df["Number"],
            y=coder_df["Message Size"],
            line_shape="spline",
            name=coder_name,
        )
    )

fig.show()
