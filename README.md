# 🎬 Netflix Data Analysis Using Python

## 📌 Project Overview

This project explores and analyzes the Netflix Movies and TV Shows dataset to uncover trends in content distribution, content growth, genre popularity, country-wise production, ratings, and release patterns.

Using Python and powerful data analysis libraries such as Pandas, NumPy, and Matplotlib, this project demonstrates the complete data analytics workflow including data cleaning, feature engineering, exploratory data analysis (EDA), visualization, and insight generation.

The objective is to transform raw Netflix content data into meaningful business insights that help understand Netflix's content strategy and growth over time.

---

## 🎯 Project Objectives

- Analyze the distribution of Movies and TV Shows on Netflix.
- Examine Netflix's content growth over the years.
- Identify top content-producing countries.
- Explore content ratings and audience targeting.
- Analyze genre distribution and popularity.
- Study release year trends and content age.
- Generate actionable insights through data visualization.

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- VS Code / Jupyter Notebook

---

## 📂 Dataset Information

Dataset Source:
Netflix Movies and TV Shows Dataset

The dataset contains information about Netflix content including:

| Column Name | Description |
|------------|-------------|
| show_id | Unique content identifier |
| type | Movie or TV Show |
| title | Content title |
| director | Director name |
| cast | Cast members |
| country | Country of production |
| date_added | Date added to Netflix |
| release_year | Original release year |
| rating | Content rating |
| duration | Duration of movie/show |
| listed_in | Genre/category |
| description | Content description |

---

## 🧹 Data Cleaning

The following preprocessing steps were performed:

- Handled missing values in director, cast, country, and rating columns.
- Removed records with invalid or missing date information.
- Converted date_added column to datetime format.
- Removed duplicate records.
- Verified data consistency and quality.

---

## ⚙️ Feature Engineering

Additional features were created to support deeper analysis:

### Year Added
Extracted the year when content was added to Netflix.

### Month Added
Extracted month names to analyze seasonal trends.

### Content Age
Calculated content age using:

Content Age = Current Year - Release Year

### Decade
Grouped content by release decade to identify long-term trends.

---

## 🔍 Exploratory Data Analysis (EDA)

The project investigates several important business questions:

### Content Distribution
- Movies vs TV Shows comparison
- Overall content composition

### Growth Analysis
- Content additions over time
- Netflix expansion trends

### Country Analysis
- Top content-producing countries
- Geographic content distribution

### Genre Analysis
- Most common content categories
- Genre popularity trends

### Ratings Analysis
- Audience targeting patterns
- Content maturity levels

### Release Analysis
- Distribution of release years
- Content age trends
- Decade-wise content production

### Director Analysis
- Most featured directors on Netflix

---

## 📊 Data Visualizations

The project includes multiple visualizations:

### 📺 Movies vs TV Shows
Comparison of content types available on Netflix.

### 📈 Content Growth Over Time
Year-wise additions to Netflix's content library.

### 🌎 Top Producing Countries
Countries contributing the highest number of titles.

### ⭐ Ratings Distribution
Analysis of audience ratings across content.

### 🎭 Genre Distribution
Most popular genres available on Netflix.

### 📅 Release Year Distribution
Trend of content releases across years.

### ⏳ Content Age Analysis
Distribution of content age on the platform.

### 🎬 Decade-wise Content Analysis
Content grouped by release decade.

---

## 📌 Key Insights

Some notable findings from the analysis include:

- Movies significantly outnumber TV Shows on Netflix.
- The United States contributes the highest number of titles.
- Netflix experienced rapid content growth after 2015.
- Most content available on Netflix was released in the last decade.
- TV-MA is one of the most common content ratings, indicating a strong focus on mature audiences.
- Drama and International content dominate the platform.
- Netflix prioritizes relatively recent content over older releases.

---

## 📈 Skills Demonstrated

This project demonstrates practical experience in:

- Data Cleaning
- Data Preprocessing
- Missing Value Handling
- Feature Engineering
- Exploratory Data Analysis (EDA)
- Data Visualization
- Business Analytics
- Insight Generation
- Python Programming

---

## 🚀 Learning Outcomes

Through this project, I gained hands-on experience in:

- Working with a real-world entertainment dataset.
- Performing end-to-end data analysis using Python.
- Extracting meaningful insights from large datasets.
- Creating effective visualizations for storytelling.
- Understanding content trends and audience segmentation.

---

## 🔮 Future Enhancements

Potential improvements for future versions:

- Interactive dashboard using Power BI.
- Genre recommendation analysis.
- Content trend forecasting.
- SQL-based analytical queries.
- Advanced visualizations using Seaborn and Plotly.
- Sentiment analysis using content descriptions.

---

## 📁 Project Structure
Netflix-Data-Analysis/
│
├── Data
│ ├── netflix_titles.csv
├── netflix_analysis.py
├── README.md
│
├── charts/
│ ├── movies_vs_tvshows.png
│ ├── content_growth.png
│ ├── top_countries.png
│ ├── ratings_distribution.png
│ ├── genre_analysis.png
│ ├── release_year_distribution.png
│ ├── content_age_distribution.png
│ └── decade_analysis.png

## 👨‍💻 Author

### Gaurav Rawat

BCA Student | Aspiring Data Analyst