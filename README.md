
# Retail Sales Trend Analysis Dashboard

## Project Description
This project is a **Retail Sales Trend Analysis Dashboard** built using **Streamlit**, **Pandas**, **Matplotlib**, **Seaborn**, and **Plotly**. The dashboard provides interactive insights into retail sales data, helping users analyze trends over different time periods, top-selling products, sales by region, and customer segmentation.

The dashboard reads a cleaned retail sales dataset, processes the data, and displays various visualizations and key metrics. Users can filter data based on a date range, explore annual and monthly sales trends, identify top-selling products, analyze regional sales distributions, and segment customers based on purchases and transactions.

## Features
- **Interactive Filters**: Users can filter sales data by date range via a sidebar.
- **Sales Metrics**: Displays total sales and top 5 products by revenue.
- **Visualizations**:
  - **Yearly Sales Trends** (Line Chart)
  - **Monthly Sales Trends** (Bar Chart)
  - **Stacked Area Chart for Seasonal Sales Trends**
  - **Top 10 Products by Total Sales** (Bar Chart)
  - **Top 10 Countries by Total Sales** (Bar Chart)
  - **Top 10 Customers by Total Sales** (Bar Chart)
  - **Top 10 Customers by Number of Transactions** (Bar Chart)
- **Downloadable Data**: Users can export the filtered dataset as a CSV file.

## Installation & Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/retail-sales-dashboard.git
   cd retail-sales-dashboard
   ```
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Dataset
The dataset should be named `Online Retail.csv` and placed inside an `archive` directory. It contains sales data with columns such as:
- **InvoiceDate**: Date and time of the purchase.
- **Quantity**: Number of items purchased.
- **UnitPrice**: Price per unit of the product.
- **Description**: Product name.
- **Country**: Country where the purchase was made.
- **CustomerID**: Unique identifier for each customer.
- **InvoiceNo**: Unique invoice number.

## Required Libraries
- **Streamlit** (For web-based dashboard UI)
- **Pandas** (For data processing and analysis)
- **Matplotlib & Seaborn** (For static visualizations)
- **Plotly** (For interactive charts)

Install dependencies using:
```bash
pip install -r requirements.txt
```

## Folder Structure
```
retail-sales-dashboard/
│-- archive/
│   ├── Online Retail.csv  # Retail sales dataset
│-- app.py                 # Main Streamlit dashboard script
│-- requirements.txt       # Dependencies file
│-- README.md              # Documentation file
```

## Usage
- Run the dashboard using `streamlit run app.py`.
- Adjust the date range filters to explore different time periods.
- Analyze sales trends with various visualizations.
- Identify top-performing products and customer segments.
- Download filtered sales data as a CSV file.


