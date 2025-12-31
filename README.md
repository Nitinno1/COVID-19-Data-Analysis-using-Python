# 🦠 COVID-19 Data Analysis using Python

A complete **data analysis & visualization project** on COVID-19 cases in India using **Python (Pandas, NumPy, Matplotlib, Seaborn)**. This project focuses on **data cleaning, feature engineering, exploratory data analysis (EDA), and insightful visualizations**, making it suitable for **resume, portfolio, and interviews**.

---

## 📌 Project Overview

This project analyzes COVID-19 data across Indian States/UTs with respect to:

* Confirmed cases
* Recovered cases
* Deaths
* Active cases
* Lockdown phases
* Recovery rate

The project demonstrates **real-world data handling**, including missing values, duplicates, date parsing, and meaningful visual insights.

---

## 🛠️ Technologies Used

* **Python 3.x**
* **Pandas** – data manipulation
* **NumPy** – numerical operations
* **Matplotlib** – basic visualizations
* **Seaborn** – advanced visualizations

---

## 📂 Dataset Information

**File Name:** `Covid_data.csv`

### Expected Columns

| Column Name | Description              |
| ----------- | ------------------------ |
| State_UT    | State or Union Territory |
| Date        | Date of record           |
| Confirmed   | Total confirmed cases    |
| Recovered   | Total recovered cases    |
| Deaths      | Total deaths             |
| Phase       | Lockdown / Unlock phase  |

---

## 🧹 Data Cleaning & Processing

* Standardized state names
* Converted `Date` column to datetime format
* Removed invalid or missing dates
* Filled missing numerical values with `0`
* Handled missing lockdown phases
* Removed duplicate records (State + Date)
* Calculated **Active Cases**
* Ensured no negative or invalid values
* Created new time features (Month, Year)
* Calculated **Recovery Rate (%)** safely

---

## 📊 Key Analysis & Visualizations

### 1️⃣ Top 10 States by Confirmed Cases

Bar chart showing states with the highest number of confirmed cases.

### 2️⃣ State-wise COVID Trend

Interactive input-based line chart displaying:

* Confirmed cases
* Recovered cases
* Deaths

### 3️⃣ Average Active Cases by Lockdown Phase

Bar chart comparing average active cases across different phases.

### 4️⃣ Heatmap: State vs Lockdown Phase

Heatmap visualizing the intensity of active cases across states and phases.

---

## ▶️ How to Run the Project

1. Clone the repository:

```bash
git clone https://github.com/your-username/covid19-python-analysis.git
```

2. Navigate to the project folder:

```bash
cd covid19-python-analysis
```

3. Install required libraries:

```bash
pip install pandas numpy matplotlib seaborn
```

4. Run the script:

```bash
python covid_analysis.py
```

5. Enter a valid Indian state name when prompted.

---

## 📈 Sample Insights

* States like **Maharashtra, Kerala, Karnataka** recorded the highest peak cases
* Recovery rates improved significantly during later phases
* Active cases reduced drastically post-lockdown phases

---

## 💼 Use Case

✔ Resume Project
✔ Data Analyst Portfolio
✔ Python + Pandas Practice
✔ Interview Demonstration
✔ EDA Showcase

---

## 👤 Author

**Nitin**
Aspiring Data Analyst | Python | SQL | Power BI

---

⭐ If you like this project, give it a star on GitHub!
