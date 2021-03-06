# Imports
import pandas as pd

# Reading original dataframe
df = pd.read_csv("../../data/hotel_bookings.csv")

# Dataframe of City Hotel's data
city_df = df[df['hotel'] == 'City Hotel'].reset_index(drop=True)

city_df['total_booked_nights'] = city_df['stays_in_weekend_nights'] + city_df['stays_in_week_nights']

city_df.drop('hotel', axis=1, inplace=True)

# Removing 'reservation_status' column to avoid 'cheating'
city_df.drop('reservation_status', axis=1, inplace=True)

# Saving new CSV file in the final directory
city_df.to_csv('../../data/city_dataframe.csv', index=False, encoding='utf-8')
