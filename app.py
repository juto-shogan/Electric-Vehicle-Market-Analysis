import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px


df = pd.read_csv('data/data1.csv', encoding='latin1')

st.title("Electric Vehicle Market Analysis")

st.write("""
This application analyzes the electric vehicle market using data from the U.S. Department of Energy's Alternative Fuels Data Center (AFDC). The dataset includes information on various electric vehicles, their specifications, and market trends.
""")

st.subheader(" The tasks for this analysis include:")
st.write("""
- EV Adoption Over Time: Analyze the growth of the EV population by model year.

- Geographical Distribution: Understand where EVs are most commonly registered (e.g., by county or city).

- EV Types: Breakdown of the dataset by electric vehicle type (BEV, etc.).

- Make and Model Popularity: Identify the most popular makes and models among the registered EVs.

- Electric Range Analysis: Analyze the electric range of vehicles to see how EV technology is progressing.

- Estimated Growth in Market Size: Analyze and find the estimated growth in the market size of electric vehicles.
         """)

# plot 1
st.subheader('EV Adoption Over Time: Analyze the growth of the EV population by model year.')

vehicle_count = df['Model Year'].value_counts()
fig = px.bar(
    x=vehicle_count.index,
    y=vehicle_count.values,
    labels={'x': 'Model Year', 'y': 'Number of EVs'},
    title='EV Population Growth by Model Year'
)
st.plotly_chart(fig)
st.write("- Notice ho there was a spike of EVs in 2019, which is likely due to the increasing popularity and availability of electric vehicles in the market.")

# plot 2
st.subheader('Geographical Distribution: Understand where EVs are most commonly registered')

ev_county_distribution = df['County'].value_counts()
top_counties = ev_county_distribution.head(3).index

# filtering the dataset for these top counties
top_counties_data = df[df['County'].isin(top_counties)]

# analyzing the distribution of EVs within the cities of these top counties
ev_city_distribution_top_counties = top_counties_data.groupby(['County', 'City']).size().sort_values(ascending=False).reset_index(name='Number of Vehicles')

# visualize the top 10 cities across these counties
top_cities = ev_city_distribution_top_counties.head(10)


# graph by city
fig1 = px.bar(
        top_cities,
        x='Number of Vehicles',
        y='City',
        color='County',
        title='Top Cities in Top Counties by EV Registrations',
        labels={'Number of Vehicles': 'Number of Vehicles Registered', 'City': 'City'}
)

fig1.update_layout(
        xaxis_title='Number of Vehicles Registered',
        yaxis_title='City',
        legend_title='County'
)
st.plotly_chart(fig1)


fig2 = px.bar(
        top_cities,
        x='Number of Vehicles',
        y='County',
        color='City',
        title='Top Cities in Top Counties by EV Registrations',
        labels={'Number of Vehicles': 'Number of Vehicles Registered', 'City': 'City'}
)
fig2.update_layout(
        xaxis_title='Number of Vehicles Registered',
        yaxis_title='County',
        legend_title='City'
)
st.plotly_chart(fig2)

st.write("""
         - By this we see that seattle and bellevue are the top cities in the state of Washington with the most EV registrations, followed by King County and Pierce County. This indicates a strong presence of electric vehicles in urban areas, likely due to better infrastructure and incentives for EV adoption.
         """)        

# plot 3
st.subheader('EV Types: Breakdown of the dataset by electric vehicle type')

ev_types = df['Electric Vehicle Type'].value_counts()
# 1
fig3 = px.bar(
    x=ev_types.index,
    y=ev_types.values,
    labels={'x': 'Electric Vehicle Type', 'y': 'Number of Vehicles'},
    title='Distribution of Electric Vehicle Types'
)
fig3.update_layout(
    xaxis_title='Electric Vehicle Type',
    yaxis_title='Number of Vehicles'
)
st.plotly_chart(fig3)

# 2
fig4 = px.scatter(
    df,
    x='Model Year',
    y='Make',
    color='Electric Vehicle Type',
    category_orders={'Electric Vehicle Type': ['Battery Electric Vehicle (BEV)', 'Plug-in Hybrid Electric Vehicle (PHEV)']},
    title='BEV vs PHEV Distribution by Model Year and Make',
    labels={'Make': 'Car Make', 'Model Year': 'Model Year', 'Electric Vehicle Type': 'EV Type'},
    opacity=0.6
)
fig4.update_traces(marker=dict(size=7))
fig4.show()
st.plotly_chart(fig4)

st.write("""
        - The analysis shows that Battery Electric Vehicles (BEVs) are more prevalent than Plug-in Hybrid Electric Vehicles (PHEVs) in the dataset, indicating a strong preference for fully electric vehicles among consumers. The scatter plot further illustrates the distribution of these vehicle types across different makes and model years.
                """)

# plot 4
st.subheader('Make and Model Popularity: Identify the most popular makes and models among the registered EVs')


popularity = df['Make'].value_counts()
most_pop = popularity.head(10)
# 1

fig5 = px.bar(
        x=most_pop.index,
        y=most_pop.values,
        labels={'x': 'Electric Vehicle Type', 'y': 'Number of Vehicles'},
        title='Distribution of Electric Vehicle Types'
)
fig.update_layout(
        xaxis_title='Electric Vehicle Type',
        yaxis_title='Number of Vehicles'
)
st.plotly_chart(fig5)

# 2

fig6 = px.histogram(
        df,
        x='Make',
        color='Electric Vehicle Type',
        title='Distribution of Electric Vehicle Makes by Type',
        labels={'Make': 'Car Make', 'Electric Vehicle Type': 'EV Type'},
        category_orders={'Electric Vehicle Type': ['Battery Electric Vehicle (BEV)', 'Plug-in Hybrid Electric Vehicle (PHEV)']},
        opacity=0.7
)
st.plotly_chart(fig6)

st.write("""
        - The analysis reveals that Tesla is the most popular make of electric vehicles in the dataset, followed by Nissan and Chevrolet. The histogram further breaks down the distribution of these makes by vehicle type, showing a strong preference for Battery Electric Vehicles (BEVs) over Plug-in Hybrid Electric Vehicles (PHEVs).
                """)

# plot 5
st.subheader('Electric Range Analysis: Analyze the electric range of vehicles to see how EV technology is progressing.')
