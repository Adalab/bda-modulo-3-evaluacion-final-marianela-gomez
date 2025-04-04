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
- **Size:** 405624 rows, 10 columns
- **Key Variables:**
  - `Loyalty Number`(int64): Unique identifier for each customer within the airline loyalty program. Each loyalty number corresponds to a specific customer.
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
- **Size:** 16737 rows, 16 columns
- **Key Variables:**

  - `Loyalty Number` (int64): Unique customer identifier within the loyalty program. This number allows correlating the information in this file with the flight activity file.
  - `Country` (object): Customer's country of residence.
  - `Province`: Customer's province or state of residence (applicable to countries with provincial or state divisions, such as Canada).
  - `City` (object): Customer's city of residence.
  - `Postal Code` (object): Customer's postal code.
  - `Gender` (object): Customer's gender (e.g., Male for masculine and Female for feminine).
  - `Education` (object): Customer's highest level of education attained (e.g., Bachelor for bachelor's degree, College for university or technical studies, etc.).
  - `Salary` (float64): Customer's estimated annual income.
  - `Marital Status` (object): Customer's marital status (e.g., Single, Married, Divorced, etc.).
  - `Loyalty Card` (object): Type of loyalty card held by the customer. This could indicate different levels or categories within the loyalty program.
  - `CLV` (Customer Lifetime Value) (float64) : Predicted total revenue a customer will generate for the company
  - `Enrollment Type` (object): Customer's enrollment type in the loyalty program (e.g., Standard).
  - `Enrollment Year` (int64): Year the customer enrolled in the loyalty program.
  - `Enrollment Month` (int64): Month the customer enrolled in the loyalty program.
  - `Cancellation Year` (float64): Loyalty program cancellation year (if applicable).
  - `Cancellation Month` (float64): Loyalty program cancellation month (if applicable) if applicable

---

## 🛠️ Tools & Technologies

- **Programming Language:** Python
- **Libraries:** Pandas, NumPy, Seaborn, Matplotlib, Scikit-learn
- **Jupyter Notebooks / VS Code**

---

## 🔍 Methodology and Key Insights

1. **Data Cleaning**: 
    - `Customer_Flight_Activity.csv`: 

      - Duplicates: There are 1,864 duplicate rows. These rows have been deleted.

      - Nulls: There are no missing values. 

    - `Customer_Loyal_History.csv`:

      - Duplicates: There are no duplicate rows. 

      - Nulls:  In 'Salary', 25.3% of the data is missing. Since this is needed to answer some questions, it is necessary to address them. In addition, there is a high percentage of nulls in 'Cancellation Year' and 'Cancellation Month'. However, since this data exists only if the customer leaves the program, there is no problem with leaving them as is. 

      - Change of dtype: 'Cancellation Year' and 'Cancellation Month' are changed to Int64.

      - `Salary`: The minimum value in the 'Salary' column is negative. There are 20 negative entries, which might indicate an error. These values appear to make sense when considered as positive, so the negative values have been converted to positive. All missing salary values correspond to customers with 'College' education. This made imputing the missing values more challenging, as there were no comparable values within the same education category. 'College' might refer to customers who started college but never completed their studies. It could be possible to impute the missing salary values using 'Bachelor' and 'High School or Below'. However, since this imputation would result in customers with the education level 'College' having the same salary, it may not be practical for future analysis.

      - `Country`: It only has 'Canada'. This column is deleted.  

2. **Results of EDA & Interpretation**: 

    - Flight Reservations: 

      - Flight reservations follow a seasonal pattern, with lower bookings in winter (January and February) and a peak in July, possibly linked to summer vacations. A rise is also seen in March, likely due to Spring Break, and in December due to Christmas.

      - Overall, 2018 saw more flight reservations from April to December compared to 2017.

    - Flight Distance VS Points Accumulated: 

      - A strong correlation exists between 'Points Accumulated' and 'Distance,' with distinct trends for different loyalty cards: Aurora users accumulate more points per distance than Nova or Star users.

      - Despite these trends, a significant number of users accumulate the same points per distance, regardless of their loyalty card.

3. **Next Steps**: 

    - Visualization using geopy and geopandas.

    - Handle nulls in 'Salary'.

