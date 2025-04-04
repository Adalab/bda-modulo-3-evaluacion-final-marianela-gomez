# Data Transformation 

## 🔗 Table of Contents

* [Description](#️description)
* [Installation](#installation)
* [Project Structure](#project-structure)
* [Dependencies](#dependencies)
* [Data](#data)
* [Key findings](#key-findings)
* [Contact](#contact)

## 🗒️ Description 

This project is part of Adalab Data Analytics Bootcamp and corresponds to the evaluation for Module 3. It focuses on analyzing two datasets: `Customer_Flight_Activity.csv` and `Customer_Loyalty_History.csv`. The goal is to identify key trends and patterns in customer behavior within an airline loyalty program. The insights derived from this analysis will help the company make data-driven decisions. By applying various data analysis techniques learned in Module 3, this project aims to demonstrate the skills acquired in handling, cleaning, and analyzing data, as well as effectively presenting the findings.

## ⌨️ Installation

* Clone the repository:

    ````bash
    git clone https://github.com/Adalab/bda-modulo-3-evaluacion-final-marianela-gomez.git
    ````

* Create a virtual environment (recommended):

    ````bash
    python -m venv venv
    source venv/bin/activate # or venv\Scripts\activate on Windows
    ````

* Install dependencies:

    ````bash
    pip install -r requirements.txt
    ````


## 📁 Project Structure

### 📂 data 

- **raw** : Initial .csv files.

- **processed**: Files after cleaning and transformations.

### 📂 docs 

- **Documentation file**: `documentation.ipynb` 

### 📂 img 

- Map of Canada 

### 📂 notebooks

- **EDA**: `data_exploration.ipynb`
- **Visualization**: `analysis.ipynb`
- **Statistics**: `hyptothesis_testing(bonus).ipynb`

### 📂 reports/figures

- Figures of visualization analysis. 

### 📂 src

- **Statistical functions**: `support_stats.py`

### Others

- **`requirements.txt`**: List of dependencies needed to set up this project.

## Dependencies

* `pandas`
* `numpy`
* `matplotlib`
* `seaborn`
* `scipy`

## 💡 Key findings

* **Flight Reservations**: Follow a seasonal pattern, with lows in winter and peaks in March (Spring Break), July (summer vacations), and December (Christmas). In 2018, more flights were booked from April to December compared to 2017.

* **Distance vs. Points Accumulated**: There is a strong correlation between both. Aurora cardholders accumulate more points per distance than Nova or Star users, though many customers follow a common trend regardless of their loyalty card.

* **Customer Distribution by Province**: Ontario has the highest number of customers, followed by British Columbia and Quebec. Prince Edward Island has the fewest, reflecting its low population.

* **Average Salary by Education Level**:

    - PhD holders have the highest average salary, while those with high school education or below have the lowest.

    - Master’s degree holders earn more than those with a bachelor’s degree.

    - PhD holders show the widest salary range, while high school or below has the narrowest.

* **Loyalty Card Distribution**: The majority of customers own a Star loyalty card.

* **Customers by Marital Status and Gender**: There are more female than male customers, with married individuals being the majority and divorced the least. The male-to-female ratio is similar across marital statuses, except among single customers, where women outnumber men.

## Contact

* ✉️ marianela.gomez.linkedin@gmail.com
* 🔶 [GitHub profile](https://github.com/marianela-gomez)
