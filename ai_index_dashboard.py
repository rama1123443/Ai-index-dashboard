import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
sns.set_palette("pastel")

# Load dataset
df = pd.read_csv("group1.csv")

# Title and intro
st.title("Global AI Index Dashboard")
st.markdown("""
This dashboard provides an interactive way to explore AI readiness across 62 countries.
It uses six key dimensions: Talent, Infrastructure, Research, Development, Government Strategy, and Commercial Use.
The goal is to help users compare countries and regions based on their AI maturity.
You can use the filters on the left to explore specific regions and income groups, and all charts update instantly based on your selection.
""")

# Filters
regions = st.multiselect("Select Region(s)", options=df['Region'].dropna().unique(), default=df['Region'].dropna().unique())
income_group = st.radio("Select Income Group", df['Income group'].dropna().unique())
filtered_df = df[(df['Region'].isin(regions)) & (df['Income group'] == income_group)]

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Visualizations", "Data Table", "Conclusion & Recommendations"])

# Overview
with tab1:
    st.header("Project Overview and Summary")
    st.markdown("""
    This dashboard analyzes AI readiness across 62 countries using various metrics like Talent, Infrastructure, Research, Development, Government Strategy, and Commercial Use.  
    Use the filters below to dynamically explore the data by selecting one or more Regions and an Income Group.
    """)
    st.subheader("Summary Metrics")
    top_country = filtered_df.loc[filtered_df['Total score'].idxmax(), 'Country']
    top_score = filtered_df['Total score'].max()
    avg_score = filtered_df['Total score'].mean()
    col1, col2, col3 = st.columns(3)
    col1.metric("Top Country", top_country)
    col2.metric("Highest Score", f"{top_score:.2f}")
    col3.metric("Average Score", f"{avg_score:.2f}")

# Visualizations
with tab2:
    st.header("Visual Analysis")

    def region_data(df): return df[df['Region'].isin(regions)]

    # 1
    st.subheader("1. Distribution of AI Readiness Scores")
    fig1, ax1 = plt.subplots()
    sns.histplot(filtered_df['Total score'], kde=True, ax=ax1)
    ax1.set_title("Total AI Score Distribution")
    st.pyplot(fig1)
    st.markdown("""
    **Insight:**  
    This histogram helps us understand the distribution of overall readiness across selected countries.  
    Most countries fall below the 60 mark, suggesting that only a minority are significantly prepared for AI integration.  
    The tail on the right indicates a few countries with very high scores.
    """)

    # 2
    st.subheader("2. Government Strategy vs Total Score")
    fig2, ax2 = plt.subplots()
    sns.scatterplot(data=filtered_df, x='Government Strategy', y='Total score', hue='Country', ax=ax2)
    ax2.set_title("Government Strategy vs Total Score")
    ax2.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    st.pyplot(fig2)
    st.markdown("""
    **Insight:**  
    There is a positive correlation: countries that score higher in AI government strategy also tend to score higher in overall AI readiness.  
    However, a few outliers show strong strategies without corresponding execution—indicating the need to bridge policy with action.
    """)

    # 3
    st.subheader("3. Commercial AI Use by Income Group")
    fig3, ax3 = plt.subplots()
    sns.barplot(data=region_data(df), x='Income group', y='Commercial', estimator='mean', ci=None, ax=ax3)
    ax3.set_title("Commercial Use by Income Level")
    st.pyplot(fig3)
    st.markdown("""
    **Insight:**  
    High-income countries tend to lead in commercial AI use due to stronger private sector adoption.  
    Interestingly, some upper-middle income countries are catching up, especially in Asia and Latin America, showing market-driven AI integration.
    """)

    # 4
    st.subheader("4. Total AI Readiness by Region")
    fig4, ax4 = plt.subplots()
    sns.boxplot(data=region_data(df), x='Region', y='Total score', ax=ax4)
    ax4.set_title("AI Readiness by Region")
    st.pyplot(fig4)
    st.markdown("""
    **Insight:**  
    This visualization shows median, spread, and outliers in AI readiness by region.  
    Asia-Pacific and Europe appear more consistent and higher-performing, while Africa and the Middle East have a broader variance and lower median.
    """)

    # 5
    st.subheader("5. Infrastructure vs Total Score")
    fig5, ax5 = plt.subplots()
    sns.scatterplot(data=filtered_df, x='Infrastructure', y='Total score', hue='Region', ax=ax5)
    ax5.set_title("Infrastructure vs Total Score")
    ax5.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    st.pyplot(fig5)
    st.markdown("""
    **Insight:**  
    Stronger digital infrastructure correlates with higher AI readiness scores.  
    However, some countries with modest infrastructure still perform well due to strong education, governance, or innovation hubs.
    """)

    # 6
    st.subheader("6. Total Score by Income Group")
    fig6, ax6 = plt.subplots()
    sns.boxplot(data=region_data(df), x='Income group', y='Total score', ax=ax6)
    ax6.set_title("AI Readiness by Income Group")
    st.pyplot(fig6)
    st.markdown("""
    **Insight:**  
    Income is a strong but not absolute determinant of AI readiness.  
    While high-income countries dominate, certain lower-income countries are innovating rapidly and closing the gap.
    """)

    # 7
    st.subheader("7. Research Score by Region")
    fig7, ax7 = plt.subplots()
    sns.barplot(data=region_data(df), x='Region', y='Research', estimator='mean', ci=None, ax=ax7)
    ax7.set_title("Research Score by Region")
    st.pyplot(fig7)
    st.markdown("""
    **Insight:**  
    Europe and Asia-Pacific lead in research intensity, with strong academic networks and public funding.  
    Other regions may benefit from increased investment in university-industry partnerships.
    """)

    # 8
    st.subheader("8. Development Score by Region")
    fig8, ax8 = plt.subplots()
    sns.barplot(data=region_data(df), x='Region', y='Development', estimator='mean', ci=None, ax=ax8)
    ax8.set_title("Development Score by Region")
    st.pyplot(fig8)
    st.markdown("""
    **Insight:**  
    Development measures real-world execution of AI strategies.  
    While some countries rank high on policy, they lag in development, indicating a need for cross-sector collaboration and private sector enablement.
    """)

    # 9
    st.subheader("9. Talent Score vs Total Score")
    fig9, ax9 = plt.subplots()
    sns.scatterplot(data=filtered_df, x='Talent', y='Total score', hue='Region', ax=ax9)
    ax9.set_title("Talent vs Total Score")
    ax9.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    st.pyplot(fig9)
    st.markdown("""
    **Insight:**  
    Talent is a major driver of AI readiness.  
    Nations that invest in STEM education and attract skilled AI professionals perform better overall.  
    This plot highlights how building human capital accelerates readiness.
    """)

# Data Table
with tab3:
    st.header("Filtered Data Table")
    st.dataframe(filtered_df)

# Conclusion
with tab4:
    st.header("Conclusion & Recommendations")
    st.markdown("""
    ### Key Conclusions:

    - Top Adopters: USA, China, and the UK lead in Total Score and Commercial AI use.
    - AI Readiness is Uneven: Most countries still fall below a readiness score of 60.
    - Government Strategy Matters: Strong policies help, but without execution they are ineffective.

    ### Strategic Recommendations:

    1. Strengthen National AI Policies  
       Especially in low-scoring regions, governments should develop or refine national AI strategies.

    2. Bridge Research-to-Business Gaps  
       Encourage industry adoption of academic research to improve commercial scores.

    3. Invest in Talent Development  
       Focus on STEM education, workforce training, and AI-specific programs.

    4. Strengthen Infrastructure  
       Build reliable digital infrastructure: data, computing, and connectivity layers.

    5. Translate Strategy into Action  
       Ensure national AI policies include clear timelines, KPIs, and implementation plans.

    6. Promote Research Collaboration  
       Support partnerships between universities, industries, and government to foster innovation.
    """)
