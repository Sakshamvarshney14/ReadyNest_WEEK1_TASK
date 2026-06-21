# Climate Data Analysis & Reporting Dashboard

## Project Overview

This project focuses on climate data analysis, preprocessing, visualization, and automated reporting using Python and Power BI. The workflow transforms raw climate data into meaningful insights through data cleaning, statistical analysis, exploratory data analysis (EDA), forecasting, and interactive dashboards.

The project demonstrates an end-to-end data analytics pipeline, from raw dataset processing to business-ready visual reports.

---

# Dataset Information

**Domain:** Climate & Environmental Analytics

**Dataset Size:**

* Records: 38,092
* Columns: 36

### Key Features

* Year
* Month
* Avg_Surface_Temp
* Land_Temp
* Ocean_Temp
* Day_Temp
* Max_Temp
* Min_Temp
* CO2_Concentration
* Methane_Level
* Sea_Level_Rise
* Glacier_Mass
* Latitude
* Longitude
* Aerosol_Index

---

# Tools & Technologies

### Programming

* Python

### Libraries

* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn

### Visualization

* Microsoft Power BI

---

# Data Cleaning & Preprocessing

The following preprocessing operations were performed:

* Removed duplicate records
* Removed constant-value columns
* Removed highly missing columns
* Filled missing numerical values using median
* Filled missing categorical values using mode
* Generated a cleaned dataset for analysis

### Output

* cleaned_dataset.csv

---

# Descriptive Statistics

Statistical analysis was performed on numerical features.

Metrics calculated:

* Count
* Mean
* Median
* Standard Deviation
* Variance
* Minimum Value
* Maximum Value

### Example: Avg_Surface_Temp

| Metric             | Value  |
| ------------------ | ------ |
| Count              | 37,892 |
| Mean               | 14.00  |
| Median             | 14.00  |
| Standard Deviation | 1.97   |
| Variance           | 3.89   |
| Minimum            | 6.00   |
| Maximum            | 22.40  |

### Generated Files

* descriptive_statistics.csv
* statistical_summary.txt

---

# Exploratory Data Analysis (EDA)

### Univariate Analysis

Generated:

* Histograms
* Box Plots

### Bivariate Analysis

Generated:

* Scatter Plot Analysis
* Correlation Analysis

### Correlation Heatmap

A heatmap was generated to identify relationships among climate indicators.

Generated File:

* heatmap.png

---

# Feature Engineering

A new feature was created:

### Temperature Range

Temp_Range = Max_Temp − Min_Temp

This feature captures temperature variability and enhances climate analysis.

---

# Time Series Forecasting

A forecasting model was developed using Linear Regression.

### Objective

Predict future temperature trends using historical yearly climate data.

Generated File:

* forecast.png

---

# Geographic Analysis

Climate observations were visualized geographically using latitude and longitude information.

Generated File:

* geo_map.png

---

# Automated Reporting

The project automatically generates:

* Cleaned Dataset
* Statistical Reports
* Insight Reports
* Histograms
* Boxplots
* Correlation Heatmap
* Forecast Visualization
* Geographic Visualization

Generated Files:

* cleaned_dataset.csv
* descriptive_statistics.csv
* statistical_summary.txt
* insights.txt

---

# Power BI Dashboard

The project includes a two-page interactive Power BI dashboard.

## Page 1: Dashboard Overview

Features:

* KPI Cards
* Line Charts
* Scatter Plot
* Column Chart
* Year Filter
* Month Filter

Purpose:

Provide high-level exploration and trend analysis.

---

## Page 2: Advanced Analysis

Features:

* Statistical Summary
* Correlation Heatmap
* Forecast Analysis
* Geographic Analysis
* Key Insights

Purpose:

Present deeper analytical findings and advanced visualizations.

---

# Dashboard Preview

Dashboard screenshots are available inside the **dashboard** folder:

* dashboard_page1.png
* dashboard_page2.png

---

# Key Insights

* Missing values were successfully handled during preprocessing.
* Climate variables exhibit meaningful correlations.
* Temperature indicators show variation across years.
* Forecasting highlights future temperature movement patterns.
* Feature engineering improved analytical depth.
* Automated reporting reduced manual analysis effort.

---

# Project Structure

DATASET ANALYSIS & REPORTING/

├── dataset/

├── outputs/
│   ├── charts/
│   ├── cleaned_dataset.csv
│   ├── descriptive_statistics.csv
│   ├── statistical_summary.txt
│   └── insights.txt

├── script/
│   └── code.py

├── dashboard/
│   ├── Climate_Dashboard.pbix
│   ├── page1_dashboard.png
│   └── page2_analysis.png

└── README.md

---

# Future Improvements

* Advanced forecasting techniques
* Interactive geospatial dashboards
* Real-time climate monitoring
* Machine learning based climate prediction

---

# Author

**Saksham Varshney**
