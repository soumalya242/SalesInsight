<div align="center">

# SalesInsight

**Turn raw sales data into clear business decisions.**

Upload a CSV, then explore KPIs, trends, top products and regional performance in one clean dashboard.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white)

[Features](#features) · [Screenshots](#screenshots) · [Quick Start](#quick-start) · [Dataset Format](#dataset-format) · [Troubleshooting](#troubleshooting)

</div>

---

## Overview

**SalesInsight** is a web-based sales analytics dashboard built with **Python, Flask, MySQL, Pandas and Plotly.js**.

After you upload a valid CSV file, the app validates the data, stores the sales records in MySQL, and shows them on the dashboard as interactive charts and summary cards.

---

## Features

| Feature | What you get |
|---|---|
| **CSV Upload** | Drag and drop your sales file. Required columns and values are validated. |
| **KPI Overview** | Total Sales, Total Profit, Total Orders, Total Quantity and Average Order Value. |
| **Sales Trends** | Sales by month and monthly profit trends. |
| **Category Analysis** | Compare sales across product categories. |
| **Top Products** | The top 10 products by sales. |
| **Regional Analysis** | Sales and profit performance across regions. |

---

## Technology Stack

| Area | Technology |
|---|---|
| Frontend | HTML, CSS, Tailwind CSS, JavaScript |
| Backend | Python, Flask |
| Data analysis | Pandas, NumPy |
| Visualizations | Plotly.js |
| Database | MySQL |
| Database integration | Flask-SQLAlchemy, PyMySQL |

---

## Screenshots

Add screenshots of your running application to a `screenshots` folder in the project root, using the file names below.

| Dashboard | Upload Dataset |
|---|---|
| ![SalesInsight Dashboard](screenshots/dashboard.png) | ![SalesInsight Upload Page](screenshots/upload.png) |
| **Product Analysis** | **Regional Analysis** |
| ![SalesInsight Product Analysis](screenshots/products.png) | ![SalesInsight Regional Analysis](screenshots/region.png) |
| **Home Page** |**Database** |
| ![SalesInsight Product Analysis](screenshots/home.png) | ![SalesInsight Regional Analysis](screenshots/database.png) |

---

## Quick Start

**Prerequisites:** Python 3, MySQL (installed and running) and Git.

### 1. Clone the repository

```bash
git clone https://github.com/soumalya242/SalesInsight.git
cd SalesInsight
```

### 2. Create and activate a virtual environment

Windows (Command Prompt):

```cmd
python -m venv venv
venv\Scripts\activate.bat
```

macOS / Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create the MySQL database

Open MySQL and run:

```sql
CREATE DATABASE salesinsight_db;
```

### 5. Configure environment variables

Create a `.env` file in the project root:

```env
SECRET_KEY=replace_with_a_secret_key
DATABASE_URL=mysql+pymysql://YOUR_USERNAME:YOUR_PASSWORD@localhost/salesinsight_db
```

Replace the username and password with your local MySQL credentials. If your password contains URL-special characters, URL-encode them in the connection string.

> [!CAUTION]
> Do not commit `.env` to GitHub. Keep it listed in `.gitignore`.

### 6. Run the application

```bash
python app.py
```

Open the address shown in the terminal, usually `http://127.0.0.1:5000`. Go to the **Upload** page, select a valid CSV file and upload it, then open the **Dashboard**.

> [!WARNING]
> In the current MVP upload workflow, uploading a new valid dataset **replaces** the existing sales records in the database. Keep a backup of any data you want to retain.

---

## Dataset Format

Upload a **CSV (`.csv`) file** with these 15 fields:

| Field | Description |
|---|---|
| `order_id` | Unique or shared identifier for an order. Multiple product rows may belong to the same order. |
| `order_date` | Date the order was placed. |
| `ship_date` | Date the order was shipped. |
| `customer_id` | Identifier for the customer. |
| `customer_name` | Customer's name. |
| `segment` | Customer segment, such as Consumer, Corporate or Home Office. |
| `region` | Sales region. |
| `category` | Product category. |
| `sub_category` | Product sub-category. |
| `product_id` | Identifier for the product. |
| `product_name` | Product name. |
| `sales` | Sales amount for the record. |
| `quantity` | Number of units sold. |
| `discount` | Discount as a decimal between `0` and `1`. |
| `profit` | Profit amount for the record. |

> [!NOTE]
> The database table has an `id` primary-key column that is generated automatically. **Do not include `id` in your CSV.**

> [!IMPORTANT]
> **Header names must match what the app expects.** The fields above are the database column names. The current upload validator expects the original Superstore-style headings with spaces and title case (for example `Order ID`, `Order Date`, `Sub-Category` and `Sales`). Either rename your CSV headers to match the validator, or update the validator and upload-field mapping to accept the lowercase names. Do not mix both styles in one file.

### Example CSV

Database-style layout, with illustrative values only:

```csv
order_id,order_date,ship_date,customer_id,customer_name,segment,region,category,sub_category,product_id,product_name,sales,quantity,discount,profit
ORD-001,2017-11-08,2017-11-11,CUST-001,Alex Morgan,Consumer,West,Technology,Phones,PROD-001,Example Smartphone,999.99,1,0.10,120.00
ORD-002,2017-11-09,2017-11-12,CUST-002,Jamie Lee,Corporate,East,Furniture,Chairs,PROD-002,Example Office Chair,250.00,2,0.20,-15.00
```

### Before you upload

- Save the file as `.csv` and include all 15 fields.
- Leave no blank values in required fields.
- Use valid dates for `order_date` and `ship_date`, such as `2017-11-08` or `11/8/2017`.
- Use numeric values for `sales`, `quantity`, `discount` and `profit`.
- `quantity` must be greater than zero.
- `discount` must be between `0` and `1` (for example, `0.20` means 20%).
- `sales` must not be negative. `profit` may be negative, because a sale can result in a loss.

---

## Troubleshooting

| Problem | What to check |
|---|---|
| MySQL connection error | Confirm MySQL is running and the `.env` connection URL has the correct credentials and database name. |
| CSV upload is rejected | Check the column names, missing values, date fields and numeric values. |
| Invalid quantity | Every quantity must be greater than zero. |
| Invalid discount | Discount must be between `0` and `1`, not between `0` and `100`. |
| Dashboard shows zero values | Confirm a dataset was uploaded successfully and that records exist in the `sales_records` table. |
| Screenshot not shown on GitHub | Check that the image exists in the `screenshots` folder and the file name matches the path in this README. |

---
