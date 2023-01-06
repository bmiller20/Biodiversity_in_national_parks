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
#Check to see if the Merge Worked
print(df.columns)
# Found that Conservation Status had Lots of Null Values so changed all the Null Values to 'None'
df['conservation_status']=df['conservation_status'].fillna('None')
print(df['park_name'].count())
#Make a by Park Name/Category/Observation dataset


#Make a by Conservation_Status/Category/Park dataset



