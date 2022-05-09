# import the necessary libraries
import matplotlib
import numpy as np
import pandas as pd
import os

# Visualisation libraries
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from IPython.display import display_html
import folium
from folium.plugins import HeatMap

# Increase the default plot size and set the color scheme
plt.rcParams['figure.figsize'] = 12, 8
plt.style.use("fivethirtyeight")  # for pretty graphs

# Disable warnings
import warnings
warnings.filterwarnings('ignore')


def display_side_by_side(dfs, color):
    """
    Display a series of DataFrame tables together
    :param dfs: a series of DataFrame tables
    :param color: the color of display style
    :return: the display result
    """
    html_str = ''
    for df in dfs:
        df = df[:10].style.set_precision(2).background_gradient(cmap=color)
        html_str += df.render()
    display_html(html_str.replace('table', 'table style="display:inline"'), raw=True)


def max_polluted_city_overall(pollutant, us_pollution):
    """
    Get the max polluted cities with the highest mean AQI in Y2020-2021.
    :param pollutant: The name of pollutant such as "SO2"
    :param us_pollution: The main pollution dataset
    :return: The DataFrame of city list ordered by mean AQI
    """
    pollutant_col = f'{pollutant} AQI'
    ordered = us_pollution[[pollutant_col, 'City']].groupby(["City"]).mean().sort_values(by=pollutant_col,
                                                                                         ascending=False).reset_index()
    ordered[pollutant_col] = round(ordered[pollutant_col], 2)
    return ordered


def max_polluted_city_recent_five(pollutant, us_pollution):
    """
    Get the max polluted cities with the highest mean AQI IN Y2015-2021.
    :param pollutant: The name of pollutant such as "SO2"
    :param us_pollution: The main pollution dataset
    :return: The DataFrame of city list ordered by mean AQI
    """
    pollutant_col = f'{pollutant} AQI'
    ordered = us_pollution[us_pollution['Year'] > 2015][[pollutant_col, 'City']].groupby(["City"]).mean().sort_values(
        by=pollutant_col, ascending=False).reset_index()
    ordered[pollutant_col] = round(ordered[pollutant_col], 2)
    return ordered


def max_polluted_city_old_ten(pollutant, us_pollution):
    """
    Get the max polluted cities with the highest mean AQI IN Y2001-2010.
    :param pollutant: The name of pollutant such as "SO2"
    :param us_pollution: The main pollution dataset
    :return: The DataFrame of city list ordered by mean AQI
    """
    pollutant_col = f'{pollutant} AQI'
    ordered = us_pollution[us_pollution['Year'] < 2011][[pollutant_col, 'City']].groupby(["City"]).mean().sort_values(
        by=pollutant_col, ascending=False).reset_index()
    ordered[pollutant_col] = round(ordered[pollutant_col], 2)
    return ordered


def display_max_polluted_city_overall(us_pollution):
    """
    Display the cities with the worst average air quality in the past 20 years Y2020-2021.
    :param us_pollution: The main pollution dataset
    :return: The display result in the 'OrRd' style
    """
    o3_city = max_polluted_city_overall('O3', us_pollution)
    co_city = max_polluted_city_overall('CO', us_pollution)
    so2_city = max_polluted_city_overall('SO2', us_pollution)
    no3_city = max_polluted_city_overall('NO2', us_pollution)
    citysets = o3_city, co_city, so2_city, no3_city
    display_side_by_side(citysets, 'OrRd')


def display_max_polluted_city_recent_five(us_pollution):
    """
    Display the cities with the worst average air quality in the past 5 years Y2015-2021.
    :param us_pollution: The main pollution dataset
    :return: The display result in the 'OrRd' style
    """
    o3_city = max_polluted_city_recent_five('O3', us_pollution)
    co_city = max_polluted_city_recent_five('CO', us_pollution)
    so2_city = max_polluted_city_recent_five('SO2', us_pollution)
    no3_city = max_polluted_city_recent_five('NO2', us_pollution)
    citysets = o3_city, co_city, so2_city, no3_city
    display_side_by_side(citysets, 'OrRd')


def city_dif(pollutant, us_pollution):
    """
    Calculate the change of each pollutant over the past 20 years Y2020-2021.
    :param pollutant: The name of pollutant such as "SO2"
    :param us_pollution: The main pollution dataset
    :return: The DataFrame show the change of AQI for each city
    """
    pollutant_col = f'{pollutant} AQI'
    pollutant_change = f'{pollutant} Change'
    city = max_polluted_city_recent_five(pollutant, us_pollution)
    city_old = max_polluted_city_old_ten(pollutant, us_pollution)
    dif = city
    dif[pollutant_change] = city[pollutant_col] - city_old[pollutant_col]
    return dif


def city_increase(pollutant, us_pollution):
    """
    The cities with the highest increase during the past 20 years Y2020-2021.
    :param pollutant: The name of pollutant such as "SO2"
    :param us_pollution: The main pollution dataset
    :return: The DataFrame ordered by change of AQI from highest to lowest
    """
    dif = city_dif(pollutant, us_pollution)
    pollutant_col = f'{pollutant} AQI'
    pollutant_change = f'{pollutant} Change'
    increase = dif.sort_values(by=pollutant_change, ascending=False).reset_index()
    increase = increase[['City', pollutant_col, pollutant_change]]
    return increase


def city_decrease(pollutant, us_pollution):
    """
    The cities with the lowest increase during the past 20 years Y2020-2021.
    :param pollutant: The name of pollutant such as "SO2"
    :param us_pollution: The main pollution dataset
    :return: The DataFrame ordered by change of AQI from lowest to highest
    """
    dif = city_dif(pollutant, us_pollution)
    pollutant_col = f'{pollutant} AQI'
    pollutant_change = f'{pollutant} Change'
    decrease = dif.sort_values(by=pollutant_change, ascending=True).reset_index()
    decrease = decrease[['City', pollutant_col, pollutant_change]]
    return decrease


def display_city_increase(us_pollution):
    """
    Display the Top 10 cities with the highest increase of AQI.
    :param us_pollution: The main pollution dataset
    :return: The display result
    """
    o3_increase = city_increase('O3', us_pollution)
    co_increase = city_increase('CO', us_pollution)
    so2_increase = city_increase('SO2', us_pollution)
    no3_increase = city_increase('NO2', us_pollution)
    increasesets = o3_increase, co_increase, so2_increase, no3_increase
    display_side_by_side(increasesets, 'OrRd')


def display_city_decrease(us_pollution):
    """
    Display the Top 10 cities with the lowest increase of AQI.
    :param us_pollution: The main pollution dataset
    :return: The display result
    """
    o3_decrease = city_decrease('O3', us_pollution)
    co_decrease = city_decrease('CO', us_pollution)
    so2_decrease = city_decrease('SO2', us_pollution)
    no3_decrease = city_decrease('NO2', us_pollution)
    decreasesets = o3_decrease, co_decrease, so2_decrease, no3_decrease
    display_side_by_side(decreasesets, 'GnBu_r')


def plotcity(city, us_pollution):
    """
    AQI Plot for cities in the United States
    :param city: The name of city such as 'New York'
    :param us_pollution: The main pollution dataset
    :return: The plot result
    """
    city_data = us_pollution[us_pollution['City'] == city]
    select_city_data = city_data[['Date',
                                  'O3 AQI',
                                  'CO AQI',
                                  'SO2 AQI',
                                  'NO2 AQI']].copy(deep=False)

    select_city_data.set_index('Date', inplace=True)
    plot_title = f'{city} Pollution'
    select_city_data.plot(figsize=(10, 4), title=plot_title, xlabel='Time')


def plot_over_year_month(pollutant, us_pollution):
    """
    Overall year-wise box plots and monthly plots
    :param pollutant: The name of pollutant such as "SO2"
    :param us_pollution: The main pollution dataset
    :return: The plot result
    """
    pollutant_col = f'{pollutant} AQI'
    fig, axes = plt.subplots(1, 2, figsize=(14, 6), dpi=80)
    sns.boxplot(x='Year', y=pollutant_col, data=us_pollution[us_pollution['Year'] > 2010], ax=axes[0])
    sns.pointplot(x='Month', y=pollutant_col, data=us_pollution)
    axes[0].set_title('US Year-wise Box Plot', fontsize=18);
    axes[1].set_title('US Month-wise Plot', fontsize=18)


def plot_year_month(city, pollutant, us_pollution):
    """
    The year-wise box plot and monthly plot in a city.
    :param city: The name of city such as 'New York'
    :param pollutant: The name of pollutant such as "SO2"
    :param us_pollution: The main pollution dataset
    :return: The plot result
    """
    city_data = us_pollution[us_pollution['City'] == city]
    pollutant_col = f'{pollutant} AQI'
    select_city_data = city_data[['Date', 'Year', 'Month', pollutant_col]].copy(deep=False)
    select_city_data.set_index('Date', inplace=True)
    plot_title = f'{city} Pollution'
    fig, axes = plt.subplots(1, 2, figsize=(14, 6), dpi=80)
    sns.boxplot(x='Year', y=pollutant_col, data=select_city_data[select_city_data['Year'] > 2010], ax=axes[0])
    sns.pointplot(x='Month', y=pollutant_col, data=select_city_data)
    axes[0].set_title(f'{city} Year-wise Box Plot', fontsize=18);
    axes[1].set_title(f'{city} Month-wise Plot', fontsize=18)


def plot_heat_map(pollutant, cityindex, us_pollution, city_data):
    """
    The heat maps for each pollutant in the United States.
    :param pollutant: The name of pollutant such as "SO2"
    :param cityindex: The list of cities in the main dataset
    :param us_pollution: The main pollution dataset
    :param city_data: The cities dataset that has the longitude and latitude
    :return: The display result of heatmap
    """
    pollutant_col = f'{pollutant} AQI'
    heat_map_data = pd.DataFrame(columns=('City',
                                          pollutant,
                                          'lat',
                                          'lng'), dtype=object)
    for city in cityindex:
        city_statis = city_data[city_data['city'] == city]
        if not city_statis.empty:
            city_lat = float(city_statis.head(1)['lat'])
            city_lng = float(city_statis.head(1)['lng'])
            mean = us_pollution[us_pollution['City'] == city][pollutant_col].mean()
            new_heat_map_data = pd.DataFrame(np.insert(heat_map_data.values,
                                                       len(heat_map_data.index),
                                                       values=[city,
                                                               mean,
                                                               city_lat,
                                                               city_lng,
                                                               ],
                                                       axis=0))
            new_heat_map_data.columns = heat_map_data.columns
            heat_map_data = new_heat_map_data
    heat_map_data = heat_map_data[['lat', 'lng', pollutant]]
    map_van = folium.Map(location=[41.8373, -100], zoom_start=4)
    HeatMap(heat_map_data).add_to(map_van)
    return map_van
