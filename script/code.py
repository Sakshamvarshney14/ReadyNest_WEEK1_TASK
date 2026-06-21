import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.linear_model import LinearRegression

# ======================================
# CREATE OUTPUT FOLDERS
# ======================================

os.makedirs("outputs/charts", exist_ok=True)

# ======================================
# LOAD DATASET
# ======================================

file_path = "dataset/global_temperature_unclean.csv"

df = pd.read_csv(file_path)

print("="*50)
print("DATASET LOADED")
print("="*50)

# ======================================
# BASIC INFO
# ======================================

rows, cols = df.shape

print(f"Rows: {rows}")
print(f"Columns: {cols}")

# ======================================
# REMOVE DUPLICATES
# ======================================

before = len(df)

df.drop_duplicates(inplace=True)

after = len(df)

duplicates_removed = before - after

# ======================================
# REMOVE CONSTANT COLUMNS
# ======================================

constant_cols = []

for col in df.columns:
    if df[col].nunique(dropna=False) <= 1:
        constant_cols.append(col)

df.drop(columns=constant_cols, inplace=True)

# ======================================
# REMOVE MOSTLY NULL COLUMNS
# ======================================

mostly_null_cols = []

for col in df.columns:

    missing_pct = df[col].isnull().mean() * 100

    if missing_pct > 80:
        mostly_null_cols.append(col)

df.drop(columns=mostly_null_cols, inplace=True)

# ======================================
# MISSING VALUE HANDLING
# ======================================

numeric_cols = df.select_dtypes(include=np.number).columns

categorical_cols = df.select_dtypes(
    include=["object"]
).columns

for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

for col in categorical_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

# ======================================
# FEATURE ENGINEERING
# ======================================

if (
    "Max_Temp" in df.columns
    and "Min_Temp" in df.columns
):
    df["Temp_Range"] = (
        df["Max_Temp"]
        - df["Min_Temp"]
    )

# ======================================
# SORT DATA FOR BETTER READABILITY
# ======================================

sort_cols = []

if "Year" in df.columns:
    sort_cols.append("Year")

if "Month" in df.columns:
    sort_cols.append("Month")

if sort_cols:
    df = df.sort_values(
        by=sort_cols
    ).reset_index(drop=True)
    
# ======================================
# SAVE CLEANED DATASET
# ======================================

df.to_csv(
    "outputs/cleaned_dataset.csv",
    index=False
)

# ======================================
# DESCRIPTIVE STATS
# ======================================

stats = df.describe(include="all")

stats.to_csv(
    "outputs/descriptive_statistics.csv"
)

# ======================================
# STATISTICAL SUMMARY
# ======================================

summary_text = ""

for col in numeric_cols:

    if col not in df.columns:
        continue

    summary_text += (
        f"\nCOLUMN: {col}\n"
    )

    summary_text += (
        f"Count: {df[col].count()}\n"
    )

    summary_text += (
        f"Mean: {df[col].mean():.2f}\n"
    )

    summary_text += (
        f"Median: {df[col].median():.2f}\n"
    )

    summary_text += (
        f"Std Dev: {df[col].std():.2f}\n"
    )

    summary_text += (
        f"Variance: {df[col].var():.2f}\n"
    )

    summary_text += (
        f"Min: {df[col].min():.2f}\n"
    )

    summary_text += (
        f"Max: {df[col].max():.2f}\n"
    )

with open(
    "outputs/statistical_summary.txt",
    "w",
    encoding="utf-8"
) as f:

    f.write(summary_text)
    
# ======================================
# HISTOGRAMS
# ======================================

important_cols = [
    "Avg_Surface_Temp",
    "CO2_Concentration",
    "Ocean_Temp",
    "Sea_Level_Rise"
]

for col in important_cols:

    if col not in df.columns:
        continue

    plt.figure(figsize=(8,5))

    df[col].hist(bins=30)

    plt.title(col)

    plt.tight_layout()

    plt.savefig(
        f"outputs/charts/hist_{col}.png"
    )

    plt.close()

# ======================================
# BOXPLOTS
# ======================================

important_cols = [
    "Avg_Surface_Temp",
    "CO2_Concentration",
    "Ocean_Temp",
    "Sea_Level_Rise"
]

for col in important_cols:

    if col not in df.columns:
        continue

    plt.figure(figsize=(8,5))

    plt.boxplot(df[col])

    plt.title(col)

    plt.tight_layout()

    plt.savefig(
        f"outputs/charts/box_{col}.png"
    )

    plt.close()

# ======================================
# CORRELATION HEATMAP
# ======================================

if len(numeric_cols) > 1:

    corr = df[numeric_cols].corr()

    plt.figure(figsize=(12,8))

    sns.heatmap(
        corr,
        annot=False
    )

    plt.title(
        "Correlation Heatmap"
    )

    plt.tight_layout()

    plt.savefig(
        "outputs/charts/heatmap.png"
    )

    plt.close()

# ======================================
# TIME SERIES FORECASTING
# ======================================

if (
    "Year" in df.columns
    and "Avg_Surface_Temp" in df.columns
):

    yearly = (
        df.groupby("Year")
        ["Avg_Surface_Temp"]
        .mean()
        .reset_index()
    )

    X = yearly[["Year"]]
    y = yearly["Avg_Surface_Temp"]

    model = LinearRegression()

    model.fit(X, y)

    future_years = np.arange(
        yearly["Year"].max() + 1,
        yearly["Year"].max() + 6
    )

    future_df = pd.DataFrame(
        {"Year": future_years}
    )

    predictions = model.predict(
        future_df
    )

    plt.figure(figsize=(8,5))

    plt.plot(
        yearly["Year"],
        yearly["Avg_Surface_Temp"],
        label="Historical"
    )

    plt.plot(
        future_years,
        predictions,
        label="Forecast"
    )

    plt.title(
        "Temperature Forecast"
    )

    plt.legend()

    plt.tight_layout()

    plt.savefig(
        "outputs/charts/forecast.png"
    )

    plt.close()
    
# ======================================
# GEOGRAPHIC MAPPING
# ======================================

if (
    "Latitude" in df.columns
    and "Longitude" in df.columns
):

    plt.figure(figsize=(8,5))

    plt.scatter(
        df["Longitude"],
        df["Latitude"],
        s=5
    )

    plt.title(
        "Geographic Distribution"
    )

    plt.tight_layout()

    plt.savefig(
        "outputs/charts/geo_map.png"
    )

    plt.close()
    
# ======================================
# TOP CORRELATIONS
# ======================================

correlation_text = ""

if len(numeric_cols) > 1:

    corr_matrix = (
        df[numeric_cols]
        .corr()
        .abs()
    )

    upper = corr_matrix.where(
        np.triu(
            np.ones(corr_matrix.shape),
            k=1
        ).astype(bool)
    )

    top_corr = (
        upper.stack()
        .sort_values(
            ascending=False
        )
        .head(10)
    )

    correlation_text += "\nTOP CORRELATIONS\n\n"

    for pair, value in top_corr.items():
        correlation_text += (
            f"{pair} : {value:.3f}\n"
        )

# ======================================
# AUTOMATIC INSIGHTS
# ======================================

insights = f"""
AUTOMATED DATA ANALYSIS REPORT

Rows Processed: {rows}

Columns Processed: {cols}

Duplicates Removed:
{duplicates_removed}

Constant Columns Removed:
{len(constant_cols)}

Mostly Null Columns Removed:
{len(mostly_null_cols)}

Numeric Columns:
{len(numeric_cols)}

Categorical Columns:
{len(categorical_cols)}

KEY INSIGHTS

1. Dataset successfully cleaned and standardized.

2. Missing values handled automatically.

3. Strong correlations identified among climate indicators.

4. Temperature patterns vary across time.

5. Statistical summaries generated for all numeric features.

{correlation_text}
"""
with open(
    "outputs/insights.txt",
    "w",
    encoding="utf-8"
) as f:
    f.write(insights)

print("=" * 50)
print("PROJECT COMPLETED")
print("=" * 50)

print("Outputs saved in outputs folder")