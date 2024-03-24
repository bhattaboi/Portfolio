import numpy as np
import pandas as pd
import matplotlib
from pathlib import Path

path = Path.cwd() / "athlete_events.csv"
path1 = Path.cwd() / "noc_regions.csv"

athletedata = pd.read_csv(path)

## Creating a method to drop any columns with more than 5 nulls
def dropnulls(input:pd.DataFrame):
    for column in input.columns[1:]:
        if input[column].isnull().sum() > 5:
            input = input.drop(column,axis=1)
        
dropnulls(athletedata)
athletedata.head()

females = athletedata.query("Sex == 'F'")
females.head()
## Mean height for females in the summer games:
table1 = females.query("Season == 'Summer'").groupby(['Year','Event'])['Height'].mean().dropna()
## need to drop na's for summer because no female participants in earlier years
print(table1)
## Mean height for females in the winter games:
table2 = females.query("Season == 'Winter'").groupby(['Year','Event'])['Height'].mean().dropna()
print(table2)

## Let's do the same for males:
males = athletedata.query("Sex == 'M'")
males.head()
## Mean height for females in the summer games:
table3 = males.query("Season == 'Summer'").groupby(['Year','Event'])['Height'].mean().dropna()
## need to drop na's for summer because no female participants in earlier years
print(table3)
## Mean height for females in the winter games:
table4 = males.query("Season == 'Winter'").groupby(['Year','Event'])['Height'].mean().dropna()
print(table4)

## plot over time:
females.query("Season == 'Summer'").groupby(['Year'])['Height'].mean().dropna().plot(label="Females Summer",legend=True)
## The plot shows that while there was a huge dip in average height for females in the 
## summer olympics in the 1960's, the average height has rebounded to its levels in the 1920's 
## since.
females.query("Season == 'Winter'").groupby(['Year'])['Height'].mean().dropna().plot(label="Females Winter",legend=True)
males.query("Season == 'Summer'").groupby(['Year'])['Height'].mean().dropna().plot(label="Males Summer",legend=True)
males.query("Season == 'Winter'").groupby(['Year'])['Height'].mean().dropna().plot(label="Males Winter",legend=True)

## The plot above shows that average height has generally increased over time for both males and females
## Males, however, tend to have a much higher average height than females

## Gold medals by country:
golds = athletedata.query("Medal == 'Gold'").groupby(['Team','Year'])
golds.head()

## Average age by country by year:
avgage = athletedata.groupby(['Team','Year'])['Age'].mean()
avgage.head()