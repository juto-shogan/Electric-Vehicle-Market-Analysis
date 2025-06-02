import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.title("Electric Vehicle Market Analysis")

st.write("""
This application analyzes the electric vehicle market using data from the U.S. Department of Energy's Alternative Fuels Data Center (AFDC). The dataset includes information on various electric vehicles, their specifications, and market trends.
""")
st.write("""
        The tasks for this analysis include:
- EV Adoption Over Time: Analyze the growth of the EV population by model year.

- Geographical Distribution: Understand where EVs are most commonly registered (e.g., by county or city).

- EV Types: Breakdown of the dataset by electric vehicle type (BEV, etc.).

- Make and Model Popularity: Identify the most popular makes and models among the registered EVs.

- Electric Range Analysis: Analyze the electric range of vehicles to see how EV technology is progressing.

- Estimated Growth in Market Size: Analyze and find the estimated growth in the market size of electric vehicles.
         """)