import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Set the page title
st.set_page_config(page_title="Retail Sales Trend Analysis Dashboard")

# Load the cleaned dataset
file_path = r".\archive\Online Retail.csv"
df = pd.read_csv(file_path, encoding='ISO-8859-1')

# Convert InvoiceDate to datetime format
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Remove rows with negative Quantity (returns or errors)
df = df[df["Quantity"] > 0]

# Create Year and Month columns
df["Year"] = df["InvoiceDate"].dt.year
df["Month"] = df["InvoiceDate"].dt.month

# Create Total Sales column
df["TotalSales"] = df["Quantity"] * df["UnitPrice"]

# Sidebar Filters
st.sidebar.header("Filter Data")
start_date = st.sidebar.date_input("Start Date", df['InvoiceDate'].min())
end_date = st.sidebar.date_input("End Date", df['InvoiceDate'].max())
df_filtered = df[(df['InvoiceDate'] >= pd.to_datetime(start_date)) & (df['InvoiceDate'] <= pd.to_datetime(end_date))]

# Display Total Sales in the sidebar
total_sales = df_filtered['TotalSales'].sum()
st.sidebar.metric(label="Total Sales", value=f"${total_sales:,.2f}")

# Display Top 5 Products by Revenue in the sidebar
product_sales = df_filtered.groupby('Description').agg({'Quantity': 'sum', 'TotalSales': 'sum'}).sort_values('TotalSales', ascending=False)
st.sidebar.subheader("Top 5 Products by Revenue")
st.sidebar.write(product_sales.head(5)['TotalSales'])

# Page Title
st.title("Retail Sales Trend Analysis Dashboard")

# EDA 1: General Sales Trends (Yearly and Monthly)
# Yearly sales trend
yearly_sales = df_filtered.groupby('Year')['TotalSales'].sum()
st.subheader("Yearly Sales Trend")
st.line_chart(yearly_sales)

# Monthly sales trend
monthly_sales = df_filtered.groupby('Month')['TotalSales'].sum()
st.subheader("Monthly Sales Trend")
st.bar_chart(monthly_sales)

st.subheader("Stacked Area Chart for Seasonal Sales Trends")
month_sales_stacked = df_filtered.groupby(['Year', 'Month'])['TotalSales'].sum().unstack().T
fig = px.area(month_sales_stacked, labels={'value': 'Total Sales', 'Month': 'Month', 'Year': 'Year'},
              title='Stacked Area Chart of Monthly Sales Across Years')
st.plotly_chart(fig)

# EDA 3: Top Product Insights
st.subheader("Top 10 Products by Total Sales")
top_10_products = product_sales.head(10)
fig = px.bar(top_10_products, x=top_10_products.index, y='TotalSales', title='Top 10 Products by Total Sales')
st.plotly_chart(fig)

# EDA 4: Regional Sales Analysis (Sales by Country)
if 'Country' in df_filtered.columns:
    country_sales = df_filtered.groupby('Country')['TotalSales'].sum().sort_values(ascending=False)
    st.subheader("Top 10 Sales by Country")
    fig = px.bar(country_sales.head(10), x=country_sales.head(10).index, y='TotalSales', title='Top 10 Countries by Total Sales', labels={'TotalSales': 'Total Sales', 'Country': 'Country'})
    st.plotly_chart(fig)

# EDA 5: Customer Segmentation (Sales and Transactions per Customer)
if 'CustomerID' in df_filtered.columns:
    customer_sales = df_filtered.groupby('CustomerID')['TotalSales'].sum().sort_values(ascending=False)
    customer_transactions = df_filtered.groupby('CustomerID')['InvoiceNo'].nunique().sort_values(ascending=False)

    st.subheader("Top 10 Customers by Total Sales")
    fig = px.bar(customer_sales.head(10), x=customer_sales.head(10).index, y='TotalSales', title='Top 10 Customers by Total Sales')
    st.plotly_chart(fig)

    st.subheader("Top 10 Customers by Number of Transactions")
    fig2 = px.bar(customer_transactions.head(10), x=customer_transactions.head(10).index, y='InvoiceNo', title='Top 10 Customers by Number of Transactions')
    st.plotly_chart(fig2)

# CSV Download of Filtered Data
st.subheader("Download Filtered Data")
st.download_button(
    label="Download Filtered Data as CSV",
    data=df_filtered.to_csv(index=False),
    file_name="filtered_sales_data.csv",
    mime="text/csv"
)

# Add Tooltip for metrics
st.sidebar.markdown("""
    ### **Metrics and Insights:**
    - Use the filters to modify the range of dates to explore different trends in the sales data.
    - Top 5 Products based on total sales will display in the sidebar.
    - Interactive charts help understand the monthly/yearly patterns and sales regions.
    - You can export the data filtered based on your inputs to a CSV file.
""")
