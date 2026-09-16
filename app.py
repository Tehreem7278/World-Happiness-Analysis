import streamlit as st
import pandas as pd
import plotly.express as px
from utils import load_happiness_data, get_yearly_summary, get_correlations

st.set_page_config(
    page_title="World Happiness Analysis",
    page_icon="😊",
    layout="wide"
)

st.title("World Happiness Analysis & Visualization")
st.caption("Interactive analysis of World Happiness Report datasets, 2015–2019")

@st.cache_data
def get_data():
    return load_happiness_data("data")

df = get_data()
years = sorted(df["Year"].unique())
min_year, max_year = int(min(years)), int(max(years))

st.sidebar.header("Filters")
selected_years = st.sidebar.multiselect(
    "Select year(s)", years, default=years
)
country_options = sorted(df["Country"].dropna().unique())
selected_countries = st.sidebar.multiselect(
    "Compare countries (optional)", country_options
)

filtered = df[df["Year"].isin(selected_years)].copy()
if selected_countries:
    filtered = filtered[filtered["Country"].isin(selected_countries)]

c1, c2, c3, c4 = st.columns(4)
c1.metric("Countries / records", f"{len(filtered):,}")
c2.metric("Average happiness", f"{filtered['Score'].mean():.2f}" if len(filtered) else "—")
c3.metric("Highest score", f"{filtered['Score'].max():.2f}" if len(filtered) else "—")
c4.metric("Lowest score", f"{filtered['Score'].min():.2f}" if len(filtered) else "—")

tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Country Comparison", "Drivers", "Data"])

with tab1:
    st.subheader("Average happiness score by year")
    summary = get_yearly_summary(filtered)
    fig = px.line(summary, x="Year", y="Average_Score", markers=True,
                  labels={"Average_Score":"Average Happiness Score"},
                  title="Average Happiness Score, 2015–2019")
    st.plotly_chart(fig, use_container_width=True)

    if selected_years:
        chosen_year = st.selectbox("Show ranking for year", selected_years, index=len(selected_years)-1)
        ranking = filtered[filtered["Year"] == chosen_year].sort_values("Rank").head(10)
        fig2 = px.bar(ranking.sort_values("Score"), x="Score", y="Country", orientation="h",
                      title=f"Top 10 happiest countries — {chosen_year}",
                      labels={"Score":"Happiness Score"})
        st.plotly_chart(fig2, use_container_width=True)

with tab2:
    if selected_countries:
        compare = filtered.sort_values(["Country", "Year"])
        fig = px.line(compare, x="Year", y="Score", color="Country", markers=True,
                      title="Happiness score comparison")
        st.plotly_chart(fig, use_container_width=True)
        st.dataframe(compare[["Year","Country","Rank","Score"]], use_container_width=True)
    else:
        st.info("Select countries from the sidebar to compare them across years.")

with tab3:
    st.subheader("Factors associated with happiness")
    corr = get_correlations(filtered).reset_index()
    corr.columns = ["Factor", "Correlation"]
    fig = px.bar(corr.sort_values("Correlation"), x="Correlation", y="Factor",
                 orientation="h", title="Correlation with Happiness Score")
    st.plotly_chart(fig, use_container_width=True)

    factor = st.selectbox("Choose a factor for scatter analysis", [
        "GDP per capita", "Social support", "Healthy life expectancy",
        "Freedom", "Generosity", "Perceptions of corruption"
    ])
    fig2 = px.scatter(filtered, x=factor, y="Score", color="Year",
                      hover_name="Country", trendline="ols",
                      title=f"Happiness Score vs {factor}")
    st.plotly_chart(fig2, use_container_width=True)

with tab4:
    st.subheader("Filtered data")
    st.dataframe(filtered, use_container_width=True, height=500)
    st.download_button(
        "Download filtered CSV",
        filtered.to_csv(index=False).encode("utf-8"),
        "filtered_happiness_data.csv",
        "text/csv"
    )

st.divider()
st.caption("Author: Tehreem Batool | Data source: World Happiness Report datasets (2015–2019)")
