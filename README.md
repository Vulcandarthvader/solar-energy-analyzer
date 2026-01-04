# ☀️ Solar Power ROI Analyzer — A Personal Case Study 
**TL;DR**  
 Using real household electricity and solar data, this project shows that our rooftop solar installation breaks even in ~9 years and delivers ~5× returns over its lifetime.


This project started as a personal question in my own home:

“We installed rooftop solar panels — but are they actually saving us money?
When will we recover the installation cost, and how much will we really benefit in the long run?”

Instead of relying on estimates or generic calculators, I decided to answer this using our actual household electricity bills and real solar generation data.

This repository documents that journey — from raw bills to a clear, data-driven answer.



## 🏠 Background & Motivation

My family has been using grid electricity for years, and in 2023 we installed a rooftop solar system at our home.
After installation, the electricity bills changed due to net metering, making it difficult to intuitively understand:

How much solar energy we are actually generating

How much money we save each year

Whether the ₹1.7 lakh installation cost is financially worth it

When the system will truly “pay for itself”

This project was built to make sense of our own household data, while also serving as a practical ML + sustainability case study.



## 📊 Data Source (Real Household Data)

All data used in this project is real and collected from our home, spanning 2016–2025.

Data includes:

Electricity consumption from official utility bills

Bill amounts before and after solar installation

Solar energy generation data from the inverter monitoring app

Dataset columns:
Column	Description
year	Billing year
month	Billing month
grid_kwh	Electricity drawn from the grid (kWh)
bill_amount	Electricity bill amount (₹)
solar_kwh	Solar energy generated (kWh)

Important notes:

Solar was installed in 2023

Before 2023, solar_kwh = 0

After installation, bills reflect net (grid − export) units

Solar generation is measured independently from billing data



## 🧠 What This Project Does
1️⃣ Cleans & structures messy real-world data

Converts year–month billing records into a time series

Handles partial billing periods and installation-year effects

Separates grid usage from solar generation correctly

2️⃣ Analyzes solar performance

Monthly solar generation trends

Seasonal variation (monsoon vs summer)

Year-wise total solar output

3️⃣ Computes real financial savings

Calculates year-wise savings based on grid tariff

Computes cumulative savings over time

Accounts for partial years and realistic assumptions

4️⃣ Uses ML to look ahead

Trains a regression model on historical solar data

Forecasts future solar generation

Extends savings projections over the system lifetime

5️⃣ Answers the core question

When does solar actually break even for my house?



## 📈 Key Findings (From Our Home)

**Annual solar generation:** ~2,300–2,500 kWh

**Estimated system size:** ~1.5–2 kW

**Installation cost:** ₹1.7 lakh

**Average annual savings:** ~₹15,000–₹17,000

**Break-even year:** 2032

**Payback period:** ~9 years

**Long-term savings (25+ years):** ~₹8–9 lakh

These results align closely with real rooftop solar economics in India, confirming that solar is a long-term investment rather than a quick return.



## 🖥️ Interactive Dashboard (Small UI)

To make the analysis easier to understand (even for non-technical users at home), I built a simple Streamlit dashboard.

The dashboard allows you to:

Upload household electricity + solar data

Adjust grid tariff and installation cost

Visualize:

Monthly solar generation

Year-wise savings

Cumulative ROI and break-even point

Run locally:
pip install streamlit pandas matplotlib
streamlit run app.py



## 🛠️ Tech Stack

Python

Pandas – data cleaning & aggregation

Matplotlib – visual analytics

Scikit-learn – regression-based forecasting

Streamlit – lightweight interactive UI



## 📂 Project Structure
solar-energy-analyzer/
│
├── data/
│   └── billdata.csv
│
├── notebooks/
│   └── eda.ipynb
│
├── app.py
├── README.md



## 🌱 Why This Project Matters

Uses real household data, not toy datasets

Demonstrates practical ML, not overfitting

Shows how sustainability decisions can be data-driven

Bridges ML, finance, and environmental impact



## 🚀 Future Improvements

Add electricity tariff escalation (inflation-aware savings)

Integrate weather/irradiance data

Generalize for other households

Deploy the dashboard publicly



👩‍💻 Author

Nandita Udupa
BTech CSE, NIT Goa
Interests: Sustainability, Data Science, Machine Learning, Full-Stack Development
