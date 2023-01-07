#Biodiversity_in_national_parks
#This script will save files on your computer for charts

# Import files needed
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
#First Things First is to Load the Data Sets

observations = pd.read_csv('observations.csv')
species = pd.read_csv('species_info.csv')
#Merging the two Datasets into one big data set based on the common scientific_name field

df = pd.merge(species, observations, on = 'scientific_name',how='outer')
#Change Null df['conservation_status'] to None

df['conservation_status'] = df['conservation_status'].fillna("None")
#Build Plot to show Observations Per National Park
ax = plt.subplot()
sns.barplot(data = df,x='park_name',y='observations',estimator='sum')
plt.title("Observations by Park Name")
ax.set_xticklabels(["Bryce","Yellow Stone","Great Smoky","Yosemite"])
plt.show()
plt.clf()

#Build Plot to show Observations per conservation_status
sns.barplot(data = df, x='conservation_status',y='observations',estimator='sum')
plt.title("Observations by Conservation Status")
plt.show()
plt.clf()
# for loop to create plots for each park, showing the observations per category
for i in df['park_name'].unique():
    idf = df[['park_name','category','observations']].where(df['park_name']==i)
    sns.barplot(data= idf,x='category',y='observations',estimator='sum')
    plt.title(i+' Observations per Category')
    plt.show()
    plt.clf()
# for loop to create plots for each category, showing the conservation_status for each observatons
for i in df['category'].unique():
    idf = df[['category','conservation_status','observations']].where(df['category']==i)
    sns.barplot(data = idf, x='conservation_status',y='observations',estimator='sum')
    plt.title(i +' Observations per Conservation Status')
    plt.show()
    plt.clf()


