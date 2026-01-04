import pandas as pd
import plotly.express as px
import streamlit as st


file_path="C:\\Users\\00501203\\Downloads\\EXPORT.XLSX"

df = pd.read_excel(file_path)
print(df.head())


st.set_page_config(page_title="Indent_Status by Sales Group",
                   page_icon=":bar_chart",
                   layout="wide")

shipping_point = st.sidebar.multiselect(
    "Select the Status",
    options=df["Shipping Point/Receiving Pt"].unique(),
    default=df["Shipping Point/Receiving Pt"].unique()
)

pricing_date = st.sidebar.multiselect(
    "Select the pricing date:",
    options=df["Pricing Date"].unique(),
    default=df["Pricing Date"].unique()
)



sales_group = st.sidebar.multiselect(
    "Select the sales group:",
    options=df["Sales Group"].unique(),
    default=df["Sales Group"].unique()
)


status = st.sidebar.multiselect(
    "Select the Status",
    options=df["Status.1"].unique(),
    default=df["Status.1"].unique()
)




# df_selection = df.query("Status.1 in @status")




df_selection = df[
    (df["Sales Group"].isin(sales_group)) &
    (df["Pricing Date"].isin(pricing_date)) &
    (df["Status.1"].isin(status))&
    (df["Shipping Point/Receiving Pt"].isin(shipping_point))

    ]

pivot_df_selection = pd.pivot_table(
    df_selection,
    index="Sales Group",        # rows
    columns="Material",         # columns
    values="Order Quantity",    # values to sum
    aggfunc="sum",
    fill_value=0
)

pivot_df_selection.loc["TOTAL"] = pivot_df_selection.sum()
pivot_df_selection = pivot_df_selection.reset_index()
st.dataframe(pivot_df_selection)


plot_df_selection = pivot_df_selection.reset_index()
plot_df_selection = plot_df_selection[plot_df_selection["Sales Group"] != "TOTAL"]

plot_df_selection = plot_df_selection.melt(
    id_vars="Sales Group",
    var_name="Material",
    value_name="Order Quantity"
)

fig = px.bar(
    plot_df_selection,
    x="Sales Group",
    y="Order Quantity",
    color="Material",
    barmode="group",
    title="Sales Area-wise & Material-wise Order Quantity"
)

st.plotly_chart(fig, use_container_width=True)