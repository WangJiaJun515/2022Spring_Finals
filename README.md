
# Air Quality Analysis: US Pollution 2000-2021

Group member: Jun Liu, Jiajun Wang


## Dataset:
US Pollution 2000-2021 (pollution_2000_2021.csv 93.8 MB)
https://www.kaggle.com/datasets/alpacanonymous/us-pollution-20002021

## Additional Dataset
  1. United States Cities Database, 
  2. US GDP 1997 -2021, 
  3. US Population 2020, 
  4. LA Crime Records 2000-2021

## Hypothesis
### Part A
  1. Air pollution varies by region
  2. Air pollution has a time difference

## Hypothesis Part A
### 1. Air pollution varies by region
![1651806273(1)](https://user-images.githubusercontent.com/39075334/167060158-f1e07f30-8362-443f-9364-1ba3206d9362.png)




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
      



