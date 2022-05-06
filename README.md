
# Air Quality Analysis: US Pollution 2000-2021

Group member: Jun Liu, Jiajun Wang


## Dataset:
US Pollution 2000-2021 (pollution_2000_2021.csv 93.8 MB)  
CO, NO2, O3, and SO2 pollution data in the USA between 2000-2021 from the EPA  
https://www.kaggle.com/datasets/alpacanonymous/us-pollution-20002021  
  

![1651807305(1)](https://user-images.githubusercontent.com/39075334/167061746-4a1688d1-7808-4545-a0fe-1c7d898c2c50.png)


## Additional Dataset
  1. United States Cities Database
  2. US GDP 1997 -2021
  3. US Population 2020
  4. LA Crime Records 2000-2021

## Hypothesis
### Part A
  1. Air pollution varies by region
  2. Air pollution has a time difference
### Part B
  4. There is a relation between population and air quality.
  5. There is a relation between state GDP and air quality.
  6. No relation between crime case number and air quality per day.

## Hypothesis Part A

### 1. Air pollution varies by region
- The cities with the worst air quality in the last 5 years are different from the cities with the worst average air quality in the past 20 years?
- Air quality in U.S. cities has deteriorated considerably over the past 20 years?
- Air quality in U.S. cities has improved a lot over the past 20 years?

#### 1.1 Heat Map
Using the average AQI in cities and the longitude and latitude, we plot the heat maps for each pollutant in the United States.  
  
Conclusiont: From the heat map, it can be seen that severe air pollution appeared in several major urban agglomerations, such as California, New York, and Chicago.
  
![1651806273(1)](https://user-images.githubusercontent.com/39075334/167060158-f1e07f30-8362-443f-9364-1ba3206d9362.png)


#### 1.2 The cities with the worst average air quality
  
Conclusion 1: For each air pollutant, almost all cities with the highest AQI of each air pollutant are different.  
Conclusion 2: Comparing the average of past 20-year and that of past 5-year, almost all cities with the highest AQI of each air pollutant have changed.  
  
1.2.1 The cities with the worst average air quality in the past 20 years  
![1651807764(1)](https://user-images.githubusercontent.com/39075334/167062343-0413a6b2-5cfb-4dfc-8304-fd35137f9576.png)
1.2.2 The cities with the worst air quality in the last 5 years 
![1651808107(1)](https://user-images.githubusercontent.com/39075334/167062789-d868913e-b5f1-4e4e-b291-182cd262d6ed.png)

#### 1.3 Air quality has improved over the past 20 years.
Calculate the change of each pollutant over the past 20 years:  
Change = AQI (Year2016-2021) - AQI (Year2001-2010) 
  
Conclusion 1: The highest values of increase for each pollutant are all negative.  
Conclusion 2: The average AQI level in all cities has decreased, reflecting the overall improvement in air quality in the United States over the past two decades.  
  
1.2.1 The cities with the highest increase during the past 20 years  
![1651808757(1)](https://user-images.githubusercontent.com/39075334/167063647-b6610471-1e17-49b5-bde6-7605851c23e7.png)
1.2.1 The cities with the lowest increase during the past 20 years  
![1651808829(1)](https://user-images.githubusercontent.com/39075334/167063743-719e0b62-4b85-481b-8e2c-9a735bdc7da9.png)


### 2. Air pollution has a time difference
#### 1.1 Overall year-wise box plots and monthly plots
Visualize the overall average pollutant AQI in year-wise box plots and monthly plots.  

Conclusion 1: In the year-wise box plots, AQI(SO2) and AQI(CO) have clearly decreased over the past 10 years.  
Conclusion 2: In the monthly plots, each air pollutant has a clear seasonal trend. The peaks of O3 and SO2 appear in summer, while the peaks of CO and NO2 appear in winter.
![image](https://user-images.githubusercontent.com/39075334/167064412-5f3bf4aa-f3dc-4a03-ada3-785d96fbecf6.png)

#### 1.2 AQI Plot for cities
Visualize pollutant data for several largest cities in the United States, such as 'New York', 'Los Angeles', and 'Houston'.  
  
Conclusion: A clear seasonal trend can be found for each city as well, although the magnitude of rise or fall is not significant in the graphs.  
![1651809739(1)](https://user-images.githubusercontent.com/39075334/167064909-c8baeb34-d69f-4ec3-b57c-4b01ead50410.png)

#### 1.3 Year-wise box plots and monthly plots for cities
Visualize pollutant data for several largest cities in year-wise box plots and monthly plots.  
Conclusion: Certain pollutants in some cities showed opposite trends to the overall data. For example in New York, the peak of SO2 occurs in winter rather than summer, although the trends of other pollutants are the same as overall.  
  
1.3.1 The year-wise box plot and monthly plot of SO2 in New York  
![1651810234(1)](https://user-images.githubusercontent.com/39075334/167065567-20539e07-ed29-4445-99b6-335fffe13795.png)
1.2.1 The year-wise box plot and monthly plot of SO2 in the US  
![1651810354(1)](https://user-images.githubusercontent.com/39075334/167065738-38a44fe5-f91b-4540-9776-bd88931a2adc.png)






## Hypothesis Part B: Comparison
  4. There is a relation between population and air quality.
  5. There is a relation between state GDP and air quality.
  6. No relation between crime case number and air quality per day.

This part we have 3 hypothesis total, and for each one we have another new dataset to compare its relation with the air quality.
The frist two are to explore it from two related fields and the last one is from two unrelated fields(in common sense)

Method：1. for each hypothesis, we used data normalization to make sure the data values' scale is in a same level (helping to plot in one visula).
        Part of codes below:
        min_max_scaler = lambda x: (x-np.min(x))/(np.max(x)-np.min(x))
        standardlize_p_poll = p_poll.apply(min_max_scaler).sort_values('population',ascending=False)
        2.the method we using for first two hypothesis is plot.() to show their relation in direct ways.
        3. for the last one we used .corr() and .osl()[Ordinary Least Squares regression]
        
Result Criteria:
.corr() :  value > 0: positive correlation   value < 0： negitive correlation 
           0 - 0.2:   weak correlation
           0.2 - 0.6 : normal correlation
           0.6 - 1.0: high correlation
                     
.osl():  p-value < 0.05 & r-square close to 1 means that is a good regression model.


4. There is a relation between population and air quality.
We are using popluation of each state of US of 2020 for this hypothesis, so we just gropu two data by state first and then join two dataframe and get the result.

Result:
![image](https://github.com/WangJiaJun515/2022Spring_Finals/blob/main/image/population(co)-pollution.jpeg)
this visual shows the relation between CO and population changes in 50 states, the line of CO is fulctuated but its total trend is downward.
![image](https://github.com/WangJiaJun515/2022Spring_Finals/blob/main/image/population(other3).jpeg)
this shows other three relation with population and the same x-axis. there is no clear relation.
      



