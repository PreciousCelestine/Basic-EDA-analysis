<img width="1052" height="465" alt="image" src="https://github.com/user-attachments/assets/f6cfed6b-a066-41b5-b44f-93ce66528f7c" />





#  Exploratory Data Analysis on Las Vegas Strip Hotels

A basic exploratory data analysis (EDA) project performed on the Las Vegas TripAdvisor Hotel Reviews dataset. The goal of this project is to inspect, clean, and uncover insights from user reviews on hotels located on the Las Vegas Strip, using Python and popular data analysis libraries.

---

##  Table of Contents

- [Project Overview](#project-overview)
- [Dataset Information](#dataset-information)
- [Objectives](#objectives)
- [Tools and Technologies](#tools-and-technologies)
- [EDA Process Breakdown](#eda-process-breakdown)
  - [1. Data Loading & Initial Inspection](#1-data-loading--initial-inspection)
  - [2. Data Cleaning](#2-data-cleaning)
  - [3. Univariate Analysis](#3-univariate-analysis)
  - [4. Bivariate Analysis](#4-bivariate-analysis)
  - [5. Multivariate Insights](#5-multivariate-insights)
- [Key Insights](#key-insights)
- [Visualizations](#visualizations)
- [Conclusion](#conclusion)
- [Author](#author)

---

##  Project Overview

This project demonstrates the application of exploratory data analysis to a real-world hotel review dataset, helping stakeholders understand customer behavior, hotel ratings, travel trends, and more. It showcases proficiency in data cleaning, manipulation, and visualization using Python.

---

##  Dataset Information

- **Name:** Las Vegas TripAdvisor Hotel Reviews
- **Source:** TripAdvisor (via Kaggle)
- **Format:** CSV
- **Fields Include:**
  - Country
  - Hotel Name
  - Traveler Type
  - Rating
  - Hotel Reviews
  - Stay Period
  - Membership Years

---

##  Objectives

- Clean and preprocess the dataset
- Handle anomalies and missing values
- Perform descriptive and inferential statistical analysis
- Visualize customer behaviors and preferences
- Derive actionable business insights on travel trends and hotel ratings

---

##  Tools and Technologies

- **Language:** Python
- **Libraries:** 
  - pandas
  - numpy
  - matplotlib
  - seaborn
- **Environment:** Jupyter Notebook / VSCode

---

##  EDA Process Breakdown

### 1. Data Loading & Initial Inspection
- Load the CSV dataset using `pandas`
- View sample records (`head()`/`tail()`)
- Check dataset dimensions, data types, and column names
- Investigate null values and anomalies

### 2. Data Cleaning
- Handled missing values using visual heatmaps
- Replaced erroneous data like negative `Membership Years`
- Converted problematic entries with statistical replacements (e.g., mean)
<img width="1156" height="587" alt="Screenshot 2025-07-28 200629" src="https://github.com/user-attachments/assets/8ab23ce5-0cd8-4ac7-8988-6fbe74709f2c" />

### 3. Univariate Analysis
- Counted hotels by country
<img width="1037" height="519" alt="Screenshot 2025-07-28 201812" src="https://github.com/user-attachments/assets/72a62455-f07e-466c-9114-09453c0dcd52" />


- Identified dominant traveler types
- Used bar plots and pie charts to represent top attributes

<img width="1048" height="465" alt="Screenshot 2025-07-28 202436" src="https://github.com/user-attachments/assets/0128759c-7254-48c5-8ed6-fae23b1d989e" />


### 4. Bivariate Analysis
- Compared `Hotel Name` against `Rating` using boxplots
<img width="1086" height="432" alt="Screenshot 2025-07-28 203409" src="https://github.com/user-attachments/assets/6f1e330c-62a6-4ddf-bdee-786c5e88c4cd" />

  
- Explored relationships between `Country` and `Hotel Reviews`
<img width="1152" height="850" alt="Screenshot 2025-07-28 203841" src="https://github.com/user-attachments/assets/f8bffa59-2593-41bb-bc87-cfac02dc5f84" />

  
- Aggregated hotel reviews per country

### 5. Multivariate Insights
- Analyzed traveler types over stay periods using stacked bar charts
<img width="1107" height="496" alt="Screenshot 2025-07-28 205149" src="https://github.com/user-attachments/assets/a4b2df5b-75c3-4d06-9b4f-f5a149c4e931" />

  
- Heatmap of correlations between numeric features
- Breakdown of traveler types across countries

---

##  Key Insights

- **Top Reviewed Hotel:** Certain hotels received significantly higher reviews, indicating popularity.
- **Dominant Traveler Type:** Couples are the most frequent travelers.
- **Best Rated Hotels:** 8 hotels received 5-star ratings; Circus Circus Hotel had the lowest.
- **USA Dominance:** Most reviews are from U.S.-based users.
- **Membership Years:** Some hotels enjoy long-standing loyalty from reviewers.

---

##  Visualizations

- Bar charts (Top countries, Traveler types)
- Boxplots (Ratings by Hotel)
- Heatmaps (Correlation matrix, Missing values)
- Stacked bar charts (Traveler type by stay period)
- Pie chart (Top hotels by membership)
<img width="1065" height="417" alt="Screenshot 2025-07-28 205122" src="https://github.com/user-attachments/assets/054e9c0c-33a6-42f4-b313-77e1fcf0f856" />

---

##  Conclusion

This project highlights how exploratory data analysis can uncover trends and help businesses in the hospitality industry improve customer experience. With better targeting of traveler types and deeper understanding of review trends, hotels can enhance their offerings and retention strategies.

---

## 👩‍💻 Author

**Precious Celestine**  
*Data Analyst | Excel | SQL | Power BI | Python*  
[LinkedIn](https://www.linkedin.com/in/preciouscelestine) | [GitHub](https://github.com/preciouscelestine)

---

> ⚠️ Note: The dataset used is for educational purposes and may not reflect the current state of Las Vegas hospitality data.
