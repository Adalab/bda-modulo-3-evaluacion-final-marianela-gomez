 # 📊 Project Introduction

## 📌 Overview

This project analyzes `Customer_Flight_Activity.csv` and `Customer_Loyalty_History.csv` to identify key trends and patterns in customer behavior within an airline loyalty program. The goal is to provide actionable insights that help the company make data-driven decisions.  

---

## 🎯 Objectives

- Analyze the distribution of flight reservations per month throughout the year.  
- Examine the relationship between flight distance and loyalty points accumulated by customers.  
- Understand the geographical distribution of customers by province or state.  
- Compare the average salary across different educational levels of customers.  
- Determine the proportion of customers with different types of loyalty cards.  
- Explore the distribution of customers based on marital status and gender.  

---

## 📂 Data Sources
The data consists of two sets of files that describing the behavior of customers within an airline loyalty program

- **Source:** Customer_Flight_Activity.csv
- **Format:** CSV 
- **Size:** 405624 rows, 9 columns
- **Key Variables:**
  - `Loyalty Number`(Index): Unique identifier for each customer within the airline loyalty program. Each loyalty number corresponds to a specific customer.
  - `Year` (int64): Year in which flight activities were recorded for the customer.
  - `Month`(int64): Month of the year (from 1 to 12) in which flight activities occurred.
  - `Flights Booked`(int64): Total number of flights booked by the customer in that specific month.
  - `Flights with Companions`(int64): Number of flights booked in which the customer traveled with companions.
  - `Total Flights`(int64): The total number of flights the customer has taken, which may include flights booked in previous months.
  - `Distance`(int64): The total distance (in miles or kilometers) that the customer has flown during the month.
  - `Points Accumulated`(int64): Points accumulated by the customer in the loyalty program during the month, based on distance flown or other factors.
  - `Points Redeemed`(int64): Points that the customer has redeemed in the month, possibly for benefits such as free flights, upgrades, etc.
  - `Dollar Cost Points Redeemed`(int64): The dollar value of the points that the customer has redeemed during the month."


- **Source:** Customer_Loyalty_History.csv
- **Format:** CSV 
- **Size:** 
- **Key Variables:**


---

## 🛠️ Tools & Technologies

- **Programming Language:** Python
- **Libraries:** Pandas, NumPy, Seaborn, Matplotlib, Scikit-learn
- **Jupyter Notebooks / VS Code**

---

## 🔍 Methodology

1. **Data Cleaning**: 
    - `Customer_Flight_Activity.csv`: 

      - Duplicates: It seems like there are multiples rows that show the same data. Apparently, these data correspond to customers that even being partners of the loyalty program, they haven't use it in a period of time. There are also duplicated index (Loyalty Number), however this is normal since a customers might have data of different years. 

      - Nulls: The are no missing values. 
      
    - `Customer_Loyal_History.csv`

2. **Exploratory Data Analysis (EDA)**: Identifying trends and patterns.
3. **Results & Interpretation**: Summarizing key insights.
4. **Conclusions & Next Steps**: Recommendations and future work.

