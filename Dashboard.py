import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

#1
data = {
    'weather_situation_daily': ['clear', 'mist', 'heavy rain'],
    'count_daily': [11040, 5871, 468]  
}
df = pd.DataFrame(data)

def plot_weather_rental_relationship(df):
    seasonal_data = df.groupby('weather_situation_daily')['count_daily'].mean()
    plt.bar(seasonal_data.index, seasonal_data.values)
    plt.title('The influence of weather on the number of daily bicycle rentals')
    plt.xlabel('Weather')
    plt.ylabel('Average Rental')

def main():
    st.title('Weather and Daily Bicycle Rentals Relationship')

    st.subheader('Data')
    st.write(df)

    st.subheader('Relationship between Weather and Daily Bicycle Rentals')
    plot_weather_rental_relationship(df)
    st.pyplot()

    st.text("Conclusion: Weather has a significant influence on the number of daily bicycle rentals. Bicycle rentals tend to be higher on clear days and lowest during heavy rain.")

if __name__ == "__main__":
    main()

#2
data = {
    'season_daily': ['Spring', 'Winter', 'Summer', 'Fall'],  
    'count_daily': [4242, 4232, 4409, 4496]  
}
df = pd.DataFrame(data)

# Fungsi untuk membuat grafik
def plot_avg_weather_rental_relationship(df):
    avg_weather = df.groupby('season_daily')['count_daily'].mean().reset_index().sort_values("count_daily")
    plt.figure(figsize=(8, 5))
    sns.barplot(x='count_daily', y='season_daily', data=avg_weather, palette='viridis')
    plt.title('The influence of season on the number of daily bicycle rentals')
    plt.xlabel('Average Bicycle Rentals')
    plt.ylabel('Season')

# Menampilkan dashboard
def main():
    st.title('Relationship between Average Bicycle Rentals based on Weather and Daily Bicycle Rentals')

    # Menampilkan dataframe
    st.subheader('Data')
    st.write(df)

    # Menampilkan grafik
    st.subheader('Relationship between Average Bicycle Rentals based on Weather and Daily Bicycle Rentals')
    plot_avg_weather_rental_relationship(df)
    st.pyplot()

    st.text("Conclusion: Seasons have an influence on the number of daily bicycle rentals, although the differences between the four seasons are not very significant. Bike rentals tend to be higher in the fall, then summer, spring, and finally winter.")

if __name__ == "__main__":
    main()
