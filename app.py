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
fig5.update_layout(
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

# Group by Model Year and calculate average electric range and count of vehicles
range_by_year = df.groupby('Model Year').agg(
    avg_range=('Electric Range', 'mean'),
    vehicle_count=('Electric Range', 'count')
).reset_index()

# Create a two-in-one plot: bar for vehicle count, line for average electric range
fig7 = px.bar(
    range_by_year,
    x='Model Year',
    y='vehicle_count',
    labels={'vehicle_count': 'Number of Vehicles', 'Model Year': 'Model Year'},
    title='EV Market Progression: Vehicle Count and Average Electric Range by Model Year'
)

fig7.add_scatter(
    x=range_by_year['Model Year'],
    y=range_by_year['avg_range'],
    mode='lines+markers',
    name='Average Electric Range',
    yaxis='y2',
    line=dict(color='red')
)

# Add secondary y-axis for average electric range
fig7.update_layout(
    yaxis=dict(title='Number of Vehicles'),
    yaxis2=dict(
        title='Average Electric Range (miles)',
        overlaying='y',
        side='right'
    ),
    legend=dict(x=0.01, y=0.99)
)
st.plotly_chart(fig7)
st.write("""
        - The analysis shows a steady increase in the average electric range of vehicles over the years, indicating advancements in battery technology. The number of vehicles registered also shows a positive trend, reflecting the growing adoption of electric vehicles in the market.
                """)

# Plot 6
st.subheader('Estimated Growth in Market Size: Analyze and find the estimated growth in the market size of electric vehicles.') 

ev_df = df[df['Electric Vehicle Type'].isin(['Battery Electric Vehicle (BEV)', 'Plug-in Hybrid Electric Vehicle (PHEV)'])]

ev_growth = ev_df.groupby('Model Year').size().reset_index(name='Number of Electric Vehicles')

# Sort by Model Year
ev_growth = ev_growth.sort_values(by='Model Year')

# Visualize the growth using Plotly
fig8 = px.line(ev_growth, x='Model Year', y='Number of Electric Vehicles',
              title='Estimated Growth of Electric Vehicle Market Size by Model Year',
              labels={'Model Year': 'Model Year', 'Number of Electric Vehicles': 'Number of Electric Vehicles'},
              markers=True)
st.plotly_chart(fig8)
st.write("""
        - The estimated growth in the market size of electric vehicles, based on the data, shows a clear upward trend from 2012 to 2024. The number of electric vehicles has steadily increased over the years, with a notable acceleration in recent years. This indicates a significant expansion in the electric vehicle market
        and suggests a growing acceptance and adoption of electric vehicles among consumers.
                """)