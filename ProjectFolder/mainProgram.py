# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 11:34:32 2022

@author: hg22aal
"""
#import libraries
import pandas as pd
import matplotlib.pyplot as plt

#bar graph
#reading data from csv file using pandas libraries
testCricketData=pd.read_csv("Most Wickets in Test Cricket .csv")

#plotting graph using library function

plt.figure(figsize=(10,5))
plt.bar(testCricketData["Player "], testCricketData["Wickets "], width=0.2, label="Match")
plt.bar(testCricketData["Player "], testCricketData["Matches"], bottom =testCricketData["Wickets "], width=0.2, label="Wickets")
plt.title("Number of wickets taken by player in test series")
plt.xlabel("Players")
plt.ylabel("Most wickets in total matches")
plt.legend()
plt.savefig("bargraph")
plt.show()


#pie chart
#reading csv file using pandas library
economyIndicatorData=pd.read_csv("Economy_Indicators.csv")

#creating array to give label
countryName = ["Euro Area", "Germany", "United Kingdom", "France", "Italy", "Russia", "Spain"]

#plotting graph using pandas library
plt.figure(figsize=(20,5))
plt.pie(economyIndicatorData["GDP"], labels=countryName, autopct='%1.1f%%',shadow=True)

plt.title("GDP of different countries")
plt.savefig("piegraph.png")
plt.show()

#line graph
#reading data from csv file using pandas libraries

happinesDataReport = pd.read_csv("world-happiness-reportmain.csv")

#plotting the line graph
plt.figure()
plt.plot(happinesDataReport["Freedom to make life choices"], label="Freedom to make life choices")
plt.plot(happinesDataReport["Social support"], label="Social support")
plt.plot(happinesDataReport["Generosity"], label="Generosity")
plt.xlabel("Year starting from 2005 to 2020")
plt.ylabel("happiness values")
plt.legend()
plt.savefig("linegraph.png")
plt.show()






