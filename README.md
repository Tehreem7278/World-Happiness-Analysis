# World Happiness Analysis & Visualization

**Author:** Tehreem Batool  
**Project type:** Data Analysis & Interactive Visualization  
**Dataset period:** 2015–2019

## 1. Project Overview

This project analyzes global happiness data from 2015 to 2019. The goal is to understand how happiness scores changed over time, identify countries with high and low happiness scores, compare countries, and explore the relationship between happiness and factors such as GDP per capita, social support, healthy life expectancy, freedom, generosity, and perceptions of corruption.

The project includes an interactive Streamlit dashboard, a reusable data-processing module, a Jupyter analysis notebook, cleaned data, visualizations, and documentation.

## 2. Objectives

- Analyze happiness scores across 2015–2019.
- Identify the highest-ranked and lowest-ranked countries.
- Compare selected countries across multiple years.
- Explore relationships between happiness and major contributing factors.
- Provide interactive filters and downloadable filtered data.
- Present results in a clear dashboard suitable for a data-science portfolio.

## 3. Features

- Interactive year filtering.
- Optional country-to-country comparison.
- Average happiness trend visualization.
- Top-10 country ranking charts.
- Correlation analysis of happiness factors.
- Interactive scatter plots with trendlines.
- Filtered data table.
- CSV download button.
- Reusable cleaned dataset.
- Jupyter notebook for reproducible analysis.

## 4. Technologies Used

- **Python**
- **Pandas** — data cleaning and analysis
- **NumPy** — numerical operations
- **Plotly** — interactive charts
- **Streamlit** — web dashboard
- **Matplotlib** — notebook visualizations
- **Jupyter Notebook** — analysis workflow
- **Git/GitHub** — version control and project hosting

## 5. Project Structure

```text
world-happiness-analysis/
│
├── app.py
├── utils.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── 2015.csv
│   ├── 2016.csv
│   ├── 2017.csv
│   ├── 2018.csv
│   ├── 2019.csv
│   └── happiness_cleaned.csv
│
├── notebooks/
│   └── analysis.ipynb
│
└── screenshots/
    ├── dashboard_preview.png
    ├── happiness_trend.png
    └── factor_relationship.png
```

## 6. Installation / Setup

### Step 1 — Install Python

Install Python 3.10 or newer from the official Python website.

### Step 2 — Open the project

Open the project folder in VS Code or a terminal.

### Step 3 — Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

If PowerShell blocks activation, use:

```bash
venv\Scripts\Activate.ps1
```

### Step 4 — Install dependencies

```bash
pip install -r requirements.txt
```

### Step 5 — Run the dashboard

```bash
streamlit run app.py
```

Streamlit will display a local address in the terminal, normally:

```text
http://localhost:8501
```

Open that address in your browser.

## 7. Usage

1. Start the Streamlit application.
2. Select one or more years from the sidebar.
3. Optionally select countries to compare.
4. Open **Overview** to see trends and rankings.
5. Open **Country Comparison** to compare selected countries.
6. Open **Drivers** to explore correlations and scatter plots.
7. Open **Data** to inspect and download filtered records.

## 8. System Workflow / Architecture

```text
World Happiness CSV Files
          |
          v
   Data Loading
          |
          v
 Column Standardization
          |
          v
 Data Cleaning / Merging
          |
          v
 Cleaned Happiness Dataset
          |
          +----------------------+
          |                      |
          v                      v
   Jupyter Analysis       Streamlit Dashboard
          |                      |
          v                      v
 Statistical Insights     Interactive Filters
          |                      |
          +----------+-----------+
                     |
                     v
             Visualizations
                     |
                     v
          Findings & Conclusions
```

## 9. Testing / Results

The application was checked for:

- Successful loading of all five yearly datasets.
- Consistent column names after standardization.
- Correct year labels from 2015 through 2019.
- Working year and country filters.
- Correct calculation of average, highest, and lowest scores.
- Working interactive charts.
- Working CSV download.
- Missing-value handling where source datasets use different schemas.

### Dataset coverage

| Year | Records |
|---|---:|
| 2015 | 158 |
| 2016 | 157 |
| 2017 | 155 |
| 2018 | 156 |
| 2019 | 156 |

### Verified headline results

The yearly average happiness score in the supplied datasets is approximately:

| Year | Average Score |
|---|---:|
| 2015 | 5.376 |
| 2016 | 5.382 |
| 2017 | 5.354 |
| 2018 | 5.376 |
| 2019 | 5.407 |

For the supplied 2019 dataset, Finland ranks first with a score of approximately 7.769. The dashboard allows the complete ranking to be explored interactively.

## 10. Key Analytical Findings

- The datasets show that happiness scores vary substantially across countries.
- The countries at the top of the rankings tend to have strong combinations of economic conditions, social support, health, and freedom.
- Happiness is associated with several socioeconomic and wellbeing factors rather than a single variable.
- GDP per capita and social support are among the stronger positive relationships with happiness in this combined dataset.
- Correlation indicates association, not proof that one factor directly causes happiness.

## 11. Screenshots / Visuals

The `screenshots` folder contains project visuals that can be uploaded to GitHub and referenced in the README.

For the final submission, it is recommended to also take 2–3 screenshots of the running Streamlit dashboard, such as:

1. Overview page.
2. Country comparison page.
3. Drivers/correlation page.

## 12. Live URL / Video Demonstration

If the project is deployed, add the Streamlit deployment URL here:

```text
LIVE DEMO: Add your deployed URL here
```

If it is not deployed, record a 2–4 minute screen recording showing:

1. Opening the project.
2. Running `streamlit run app.py`.
3. Dashboard overview.
4. Changing year filters.
5. Comparing countries.
6. Opening the Drivers tab.
7. Downloading filtered data.

Upload the video to Google Drive, YouTube (Unlisted), or another permitted platform and add the link above.

## 13. Challenges

- The five datasets do not use identical column names.
- The 2017 file uses different naming conventions from the other years.
- The 2018 and 2019 datasets contain fewer columns than earlier datasets.
- Country and region fields are not completely consistent across every source file.
- A reliable comparison requires standardizing the schemas before analysis.

## 14. Future Improvements

- Add a world map showing happiness scores by country.
- Extend the analysis to newer World Happiness Report years.
- Add regional-level comparisons when consistent region data is available.
- Add predictive modeling for happiness scores.
- Add clustering to group countries by wellbeing profiles.
- Add automated data updates from a maintained public source.
- Deploy the dashboard publicly with Streamlit Community Cloud.

## 15. Conclusion

This project demonstrates a complete data-analysis workflow: loading real-world datasets, standardizing different schemas, cleaning and combining data, performing exploratory analysis, measuring relationships between variables, and presenting findings through an interactive dashboard.

The project shows how data visualization can make complex international wellbeing data easier to understand and compare. It also provides a foundation for future work involving geospatial analysis, machine learning, and larger historical datasets.

## 16. References

- World Happiness Report datasets, 2015–2019, supplied with this project.
- Sustainable Development Solutions Network / World Happiness Report.
- Python documentation.
- Pandas documentation.
- Plotly documentation.
- Streamlit documentation.
- Jupyter Project documentation.

## 17. Author

**Tehreem Batool**

Data Analysis | Data Visualization | Python | Pandas | Streamlit
