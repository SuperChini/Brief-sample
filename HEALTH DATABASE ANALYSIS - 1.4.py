print('\n')
print('                                              HEALTH DATABASE ANALYSIS 1.4')
print('\n')
print('-------------TASK 1---------------------------------------------------------------------------------------------------------------')
print('\n')

from queue import Empty
from tkinter.tix import COLUMN
import pandas as pd #Calling the libraries
import numpy as np
from pandas import DataFrame
from scipy import stats
import statistics
from subprocess import PIPE,Popen
from ast import Index
import pandas_profiling 
from pandas_profiling import ProfileReport
import seaborn as sb 
import matplotlib.pyplot as plt
import matplotlib 
matplotlib.use('agg') 
matplotlib.rcParams["backend"]
matplotlib.use('qtagg')
matplotlib.get_backend()
import plotly.express as px
import sqlite3 

#### TASK 1 #################################################################################################

datos = pd.read_excel('C:/Users/User/Desktop/Amplity Health/Libro5.xlsx', header = None) #Bringing the Excel sheet from the storage location
datos.to_csv('C:/Users/User/Downloads/Demographics Dataset - Fixed.csv') #Store in file directory with csv extension
data=pd.Cov = pd.read_csv('C:/Users/User/Downloads/Demographics Dataset - Fixed.csv', names=['All','PatientID','Gender','Age','Ethnicity','State','Treatment','Pain Level','Source','#Docs','Miscellaneous','Assignments']) # Reading the DataFrame from the local directory location

data = data.drop(['All','Source','#Docs'], axis=1) #Elimination of the indicated columns
data_fixed=data.drop(data.index[0])

data_fixed = pd.DataFrame(data_fixed, columns=['PatientID','Gender','Age','Ethnicity','State','Treatment','Pain Level','Miscellaneous'])
profile = pandas_profiling.ProfileReport(data_fixed) 

print('Data Fixed:', data_fixed)
print('\n')
print('\n')
print('-------------TASK 2---------------------------------------------------------------------------------------------------------------')

      
#############################################################################################################

#### TASK 2 #################################################################################################

# Age analysis considering the treatment of the patients:
#Acute cases:
first_filter = data_fixed['Treatment'] == 'Acute'  #Filtering by the kind of treatment
Acute_Treatment = data_fixed[first_filter]
Acute_Treatment.describe(include= 'all')
#print('Acute Treatment: ')
#print('\n')
#print(Acute_Treatment)
print('\n')
Stats_Acute_Treatment = pd.crosstab(Acute_Treatment['Treatment'], columns = 'Abs. Frecuency')
print('Stats_Acute_Treatment: ')
print(Stats_Acute_Treatment)
print('\n')
second_filter=Acute_Treatment['Age']
Stats_Acute_Treatment_Age = pd.crosstab(second_filter, columns = 'Abs. Frecuency')
print('Stats_Acute_Treatment_Age: ')
print(Stats_Acute_Treatment_Age)
print('\n')

#Preventative cases:
first_filter = data_fixed['Treatment'] == 'Preventative'  #Filtering by the kind of treatment
Preventative_Treatment = data_fixed[first_filter]
Preventative_Treatment.describe(include= 'all')
#print('Preventative Treatment: ') 
#print('\n')
#print(Preventative_Treatment)
#print('\n')
Stats_Preventative_Treatment = pd.crosstab(Preventative_Treatment['Treatment'], columns = 'Abs. Frecuency')
print('Stats_Prevnetative_Treatment: ')
print(Stats_Preventative_Treatment)
print('\n')
second_filter=Preventative_Treatment['Age']
Stats_Preventative_Treatment_Age = pd.crosstab(second_filter, columns = 'Abs. Frecuency')
print('Stats_Prevnetative_Treatment_Age: ')
print(Stats_Preventative_Treatment_Age)
print('\n')

#----------------------------------------------------------------------------------------------------------#

print('#**********************************************************************************************************************#')
print('\n')
# Age analysis considering the ethnicity of the patients:
first_filter = data_fixed['Ethnicity']  #Filtering by the kind of treatment
print('Ethnicity Cases Distribution: ','\n')
first_filter.describe(include= 'all')
Stats_Ethnicity = pd.crosstab(data_fixed['Ethnicity'], columns = 'Abs. Frecuency')
print(Stats_Ethnicity)
print('\n')

for i in range(0,6):   
  if (i==0):
      print('*Age Stats for the African-American Ethnicity case: ')
      second_filter = data_fixed['Ethnicity'] == 'African-American'
      Stats_Age_Ethnicity_Case = data_fixed[second_filter]  #Filtering by the kind of treatment
      Stats_Age_Ethnicity_Case1 = Stats_Age_Ethnicity_Case['Age']
      Stats_Age_Ethnicity_Case1_1 = pd.crosstab(Stats_Age_Ethnicity_Case['Age'], columns = 'Absolute Age Frecuency')
      print(Stats_Age_Ethnicity_Case1_1)
      Stats_Age_Ethnicity_Case2 = statistics.median(Stats_Age_Ethnicity_Case1)
      Stats_Age_Ethnicity_Case3 = statistics.mode(Stats_Age_Ethnicity_Case1)
      Stats_Age_Ethnicity_Case = Stats_Age_Ethnicity_Case.describe()
      Stats_Age_Ethnicity_Case1 = Stats_Age_Ethnicity_Case1.describe()
      print(Stats_Age_Ethnicity_Case)
      print('Stats Age Only Ethnicity Case African-American = ', Stats_Age_Ethnicity_Case1)
      print('African-American Age Median = ', Stats_Age_Ethnicity_Case2)
      print('African-American Age Mode = ', Stats_Age_Ethnicity_Case3)
      print('\n')
      
  elif (i==1):
      print('*Age Stats for the Asian Ethnicity case: ')
      second_filter = data_fixed['Ethnicity'] == 'Asian'
      Stats_Age_Ethnicity_Case = data_fixed[second_filter]  #Filtering by the kind of treatment
      Stats_Age_Ethnicity_Case1 = Stats_Age_Ethnicity_Case['Age']
      Stats_Age_Ethnicity_Case1_1 = pd.crosstab(Stats_Age_Ethnicity_Case['Age'], columns = 'Absolute Age Frecuency')
      print(Stats_Age_Ethnicity_Case1_1)
      Stats_Age_Ethnicity_Case2 = statistics.median(Stats_Age_Ethnicity_Case1)
      Stats_Age_Ethnicity_Case3 = statistics.mode(Stats_Age_Ethnicity_Case1)
      Stats_Age_Ethnicity_Case = Stats_Age_Ethnicity_Case.describe()
      Stats_Age_Ethnicity_Case1 = Stats_Age_Ethnicity_Case1.describe()
      print(Stats_Age_Ethnicity_Case)
      print('Stats Age Only Ethnicity Case Asian = ', Stats_Age_Ethnicity_Case1)
      print('Asian Age Median = ', Stats_Age_Ethnicity_Case2)
      print('Asian Age Mode = ', Stats_Age_Ethnicity_Case3)
      print('\n')
      
  elif (i==2):
      print('*Age Stats for the Caucasian Ethnicity case: ')
      second_filter = data_fixed['Ethnicity'] == 'Caucasian'
      Stats_Age_Ethnicity_Case = data_fixed[second_filter]  #Filtering by the kind of treatment
      Stats_Age_Ethnicity_Case1 = Stats_Age_Ethnicity_Case['Age']
      Stats_Age_Ethnicity_Case1_1 = pd.crosstab(Stats_Age_Ethnicity_Case['Age'], columns = 'Absolute Age Frecuency')
      print(Stats_Age_Ethnicity_Case1_1)
      Stats_Age_Ethnicity_Case2 = statistics.median(Stats_Age_Ethnicity_Case1)
      Stats_Age_Ethnicity_Case3 = statistics.mode(Stats_Age_Ethnicity_Case1)
      Stats_Age_Ethnicity_Case = Stats_Age_Ethnicity_Case.describe()
      Stats_Age_Ethnicity_Case1 = Stats_Age_Ethnicity_Case1.describe()
      print(Stats_Age_Ethnicity_Case)
      print('Stats Age Only Ethnicity Case Caucasian = ', Stats_Age_Ethnicity_Case1)
      print('Caucasian Age Median = ', Stats_Age_Ethnicity_Case2)
      print('Caucasian Age Mode = ', Stats_Age_Ethnicity_Case3)
      print('\n')
      
  elif (i==3):
      print('*Age Stats for the Hispanic Ethnicity case: ')
      second_filter = data_fixed['Ethnicity'] == 'Hispanic'
      Stats_Age_Ethnicity_Case = data_fixed[second_filter]  #Filtering by the kind of treatment
      Stats_Age_Ethnicity_Case1 = Stats_Age_Ethnicity_Case['Age']
      Stats_Age_Ethnicity_Case1_1 = pd.crosstab(Stats_Age_Ethnicity_Case['Age'], columns = 'Absolute Age Frecuency')
      print(Stats_Age_Ethnicity_Case1_1)
      Stats_Age_Ethnicity_Case2 = statistics.median(Stats_Age_Ethnicity_Case1)
      Stats_Age_Ethnicity_Case3 = statistics.mode(Stats_Age_Ethnicity_Case1)
      Stats_Age_Ethnicity_Case = Stats_Age_Ethnicity_Case.describe()
      Stats_Age_Ethnicity_Case1 = Stats_Age_Ethnicity_Case1.describe()
      print(Stats_Age_Ethnicity_Case)
      print('Stats Age Only Ethnicity Case Hispanic = ', Stats_Age_Ethnicity_Case1)
      print('Hispanic Age Median = ', Stats_Age_Ethnicity_Case2)
      print('Hispanic Age Mode = ', Stats_Age_Ethnicity_Case3)
      print('\n')
      
  elif (i==4):
      print('*Age Stats for the Middle-Eastern Ethnicity case: ')
      second_filter = data_fixed['Ethnicity'] == 'Middle-Eastern'
      Stats_Age_Ethnicity_Case = data_fixed[second_filter]  #Filtering by the kind of treatment
      Stats_Age_Ethnicity_Case1 = Stats_Age_Ethnicity_Case['Age']
      Stats_Age_Ethnicity_Case1_1 = pd.crosstab(Stats_Age_Ethnicity_Case['Age'], columns = 'Absolute Age Frecuency')
      print(Stats_Age_Ethnicity_Case1_1)
      Stats_Age_Ethnicity_Case2 = statistics.median(Stats_Age_Ethnicity_Case1)
      Stats_Age_Ethnicity_Case3 = statistics.mode(Stats_Age_Ethnicity_Case1)
      Stats_Age_Ethnicity_Case = Stats_Age_Ethnicity_Case.describe()
      Stats_Age_Ethnicity_Case1 = Stats_Age_Ethnicity_Case1.describe()
      print(Stats_Age_Ethnicity_Case)
      print('Stats Age Only Ethnicity Case Middle-Eastern = ', Stats_Age_Ethnicity_Case1)
      print('Middle-Eastern Age Median = ', Stats_Age_Ethnicity_Case2)
      print('Middle-Eastern Age Mode = ', Stats_Age_Ethnicity_Case3)
      print('\n')
      
  elif (i==5):
      print('*Age Stats for the Pacific Islander Ethnicity case: ')
      second_filter = data_fixed['Ethnicity'] == 'Pacific Islander'
      Stats_Age_Ethnicity_Case = data_fixed[second_filter]  #Filtering by the kind of treatment
      Stats_Age_Ethnicity_Case1 = Stats_Age_Ethnicity_Case['Age']
      Stats_Age_Ethnicity_Case1_1 = pd.crosstab(Stats_Age_Ethnicity_Case['Age'], columns = 'Absolute Age Frecuency')
      print(Stats_Age_Ethnicity_Case1_1)
      Stats_Age_Ethnicity_Case2 = statistics.median(Stats_Age_Ethnicity_Case1)
      Stats_Age_Ethnicity_Case3 = statistics.mode(Stats_Age_Ethnicity_Case1)
      Stats_Age_Ethnicity_Case = Stats_Age_Ethnicity_Case.describe()
      Stats_Age_Ethnicity_Case1 = Stats_Age_Ethnicity_Case1.describe()
      print(Stats_Age_Ethnicity_Case)
      print('Stats Age Only Ethnicity Case Pacific Islander = ', Stats_Age_Ethnicity_Case1)
      print('Pacific Islander Age Median = ', Stats_Age_Ethnicity_Case2)
      print('Pacific Islander Age Mode = ', Stats_Age_Ethnicity_Case3)
      print('\n')
      print('-------------TASK 3---------------------------------------------------------------------------------------------------------------')
      print('\n')
      

#############################################################################################################

#### TASK 3 #################################################################################################

# Gender Filters:

Female = data_fixed['Gender'] == 'Female'
Description = Female.describe()
#print(Description)
#print('\n')
data_fixed=data.drop(data.index[0])
DF = pd.DataFrame(data_fixed, columns=['PatientID','Gender','Age','Ethnicity','State','Treatment','Pain Level','Miscellaneous','Assignments']) # Creating the dataframe
DF_Ages_description = DF['Age'].describe()
Female2 =  DF[Female]

#***********************************************************************************************************#

print('                     Age Distribution: ')
print('\n')
DF2 = DF['Age'].unique()
DF3 =pd.DataFrame(DF2, columns=["Age"]) # Creating the dataframe
#print(DF3)
#print('\n')
data_frecuencies = pd.crosstab(index=DF["Age"], columns = "Abs.Frecuencies")
frecuencies=data_frecuencies.values
DF3['Abs.Frecuencies'] = frecuencies
print(DF3)

#***********************************************************************************************************#

Female2 = Female2.drop(['PatientID', 'Treatment', 'Ethnicity', 'Miscellaneous', 'Assignments', 'State', 'Pain Level', 'Gender'], axis=1)
Female3= Female2['Age'].unique()
data_Female_frecuencies = pd.crosstab(Female2['Age'], columns = "Female Ages Absolute Frecuencies")
Female_Frecuencies=data_Female_frecuencies.values
data_Female_frecuencies= pd.DataFrame(data_Female_frecuencies)
print(data_Female_frecuencies)
print('\n')


Male = data_fixed['Gender'] == 'Male'
Description = Male.describe()
#print(Description)
#print('\n')
data_fixed=data.drop(data.index[0])
DF = pd.DataFrame(data_fixed, columns=['PatientID','Gender','Age','Ethnicity','State','Treatment','Pain Level','Miscellaneous','Assignments']) # Creating the dataframe
Male2 =  DF[Male]
#print(Male2)
#print('\n')
Male2 = Male2.drop(['PatientID', 'Treatment', 'Ethnicity', 'Miscellaneous', 'Assignments', 'State', 'Pain Level', 'Gender'], axis=1)
Male3= Male2['Age'].unique()
data_Male_frecuencies = pd.crosstab(Male2['Age'], columns = "Male Ages Absolute Frecuencies")
Male_Frecuencies=data_Male_frecuencies.values
data_Male_frecuencies= pd.DataFrame(data_Male_frecuencies)
print(data_Male_frecuencies)
print('\n')

xx= data_Female_frecuencies.values
data_Female_frecuencies['Female Ages Absolute Frecuencies'].plot.bar(xx, label='Female Patients', alpha=0.7, width=1, color='red', edgecolor ='red')

xy= data_Male_frecuencies.values
data_Male_frecuencies['Male Ages Absolute Frecuencies'].plot.bar(xy, label='Male Patients', alpha=0.6, width=1 ,color='blue', edgecolor = 'blue')

plt.legend('Patients Age/Gender Distributions')

matplotlib.colors.cnames.items()

plt.show()

plt.clf()

print('\n')
print('-------------TASK 4---------------------------------------------------------------------------------------------------------------')
print('\n')
      
#############################################################################################################


#### TASK 4 #################################################################################################

#
# print('#**********************************************************************************************************************#')
print('\n')
# Pain Level Analysis considering the Ethnicity of the patients:
first_filter = data_fixed['Ethnicity']  #Filtering by the kind of treatment
print('Ethnicity Cases Distribution: ','\n')
first_filter.describe(include= 'all')
Stats_Ethnicity = pd.crosstab(data_fixed['Ethnicity'], columns = 'Ethnicity Cases Absolute Frecuencies')
print(Stats_Ethnicity)
print('\n')

#***********************************************************************************************************#

for i in range(0,6):   
  if (i==0):
      print('*Pain Level Stats for the African-American Ethnicity case: ')
      second_filter = data_fixed['Ethnicity'] == 'African-American'
      Stats_Pain_Level_Ethnicity_Case = data_fixed[second_filter]  #Filtering by the kind of treatment
      Stats_Pain_Level_Ethnicity_Case1 = Stats_Pain_Level_Ethnicity_Case['Pain Level']
      Stats_Pain_Level_Ethnicity_Case1_1 = pd.crosstab(Stats_Pain_Level_Ethnicity_Case['Pain Level'], columns = 'Pain Level Absolute Frecuencies')
      print(Stats_Pain_Level_Ethnicity_Case1_1)
      Stats_Pain_Level_Ethnicity_Case2 = statistics.median(Stats_Pain_Level_Ethnicity_Case1)
      Stats_Pain_Level_Ethnicity_Case3 = statistics.mode(Stats_Pain_Level_Ethnicity_Case1)
      Stats_Pain_Level_Ethnicity_Case = Stats_Pain_Level_Ethnicity_Case.describe()
      Stats_Pain_Level_Ethnicity_Case1 = Stats_Pain_Level_Ethnicity_Case1.describe()
      #print(Stats_Pain_Level_Ethnicity_Case)
      print('Stats Pain Level Only Ethnicity Case African-American = ', Stats_Pain_Level_Ethnicity_Case1)
      print('African-American Pain Level Median = ', Stats_Pain_Level_Ethnicity_Case2)
      print('African-American Pain Level Mode = ', Stats_Pain_Level_Ethnicity_Case3)
      print('\n')
      
  elif (i==1):
      print('*Pain Level Stats for the Asian Ethnicity case: ')
      second_filter = data_fixed['Ethnicity'] == 'Asian'
      Stats_Pain_Level_Ethnicity_Case = data_fixed[second_filter]  #Filtering by the kind of treatment
      Stats_Pain_Level_Ethnicity_Case1 = Stats_Pain_Level_Ethnicity_Case['Pain Level']
      Stats_Pain_Level_Ethnicity_Case1_1 = pd.crosstab(Stats_Pain_Level_Ethnicity_Case['Pain Level'], columns = 'Pain Level Absolute Frecuencies')
      print(Stats_Pain_Level_Ethnicity_Case1_1)
      Stats_Pain_Level_Ethnicity_Case2 = statistics.median(Stats_Pain_Level_Ethnicity_Case1)
      Stats_Pain_Level_Ethnicity_Case3 = statistics.mode(Stats_Pain_Level_Ethnicity_Case1)
      Stats_Pain_Level_Ethnicity_Case = Stats_Pain_Level_Ethnicity_Case.describe()
      Stats_Pain_Level_Ethnicity_Case1 = Stats_Pain_Level_Ethnicity_Case1.describe()
      #print(Stats_Pain_Level_Ethnicity_Case)
      print('Stats Pain Level Only Ethnicity Case Asian = ', Stats_Pain_Level_Ethnicity_Case1)
      print('Asian Pain Level Median = ', Stats_Pain_Level_Ethnicity_Case2)
      print('Asian Pain Level Mode = ', Stats_Pain_Level_Ethnicity_Case3)
      print('\n')
      
  elif (i==2):
      print('*Pain Level Stats for the Caucasian Ethnicity case: ')
      second_filter = data_fixed['Ethnicity'] == 'Caucasian'
      Stats_Pain_Level_Ethnicity_Case = data_fixed[second_filter]  #Filtering by the kind of treatment
      Stats_Pain_Level_Ethnicity_Case1 = Stats_Pain_Level_Ethnicity_Case['Pain Level']
      Stats_Pain_Level_Ethnicity_Case1_1 = pd.crosstab(Stats_Pain_Level_Ethnicity_Case['Pain Level'], columns = 'Pain Level Absolute Frecuencies')
      print(Stats_Pain_Level_Ethnicity_Case1_1)
      Stats_Pain_Level_Ethnicity_Case2 = statistics.median(Stats_Pain_Level_Ethnicity_Case1)
      Stats_Pain_Level_Ethnicity_Case3 = statistics.mode(Stats_Pain_Level_Ethnicity_Case1)
      Stats_Pain_Level_Ethnicity_Case = Stats_Pain_Level_Ethnicity_Case.describe()
      Stats_Pain_Level_Ethnicity_Case1 = Stats_Pain_Level_Ethnicity_Case1.describe()
      #print(Stats_Pain_Level_Ethnicity_Case)
      print('Stats Pain Level Only Ethnicity Case Caucasian = ', Stats_Pain_Level_Ethnicity_Case1)
      print('Caucasian Pain Level Median = ', Stats_Pain_Level_Ethnicity_Case2)
      print('Caucasian Pain Level Mode = ', Stats_Pain_Level_Ethnicity_Case3)
      print('\n')
      
  elif (i==3):
      print('*Pain Level Stats for the Hispanic Ethnicity case: ')
      second_filter = data_fixed['Ethnicity'] == 'Hispanic'
      Stats_Pain_Level_Ethnicity_Case = data_fixed[second_filter]  #Filtering by the kind of treatment
      Stats_Pain_Level_Ethnicity_Case1 = Stats_Pain_Level_Ethnicity_Case['Pain Level']
      Stats_Pain_Level_Ethnicity_Case1_1 = pd.crosstab(Stats_Pain_Level_Ethnicity_Case['Pain Level'], columns = 'Pain Level Absolute Frecuencies')
      print(Stats_Pain_Level_Ethnicity_Case1_1)
      Stats_Pain_Level_Ethnicity_Case2 = statistics.median(Stats_Pain_Level_Ethnicity_Case1)
      Stats_Pain_Level_Ethnicity_Case3 = statistics.mode(Stats_Pain_Level_Ethnicity_Case1)
      Stats_Pain_Level_Ethnicity_Case = Stats_Pain_Level_Ethnicity_Case.describe()
      Stats_Pain_Level_Ethnicity_Case1 = Stats_Pain_Level_Ethnicity_Case1.describe()
      #print(Stats_Pain_Level_Ethnicity_Case)
      print('Stats Pain Level Only Ethnicity Case Hispanic = ', Stats_Pain_Level_Ethnicity_Case1)
      print('Hispanic Pain Level Median = ', Stats_Pain_Level_Ethnicity_Case2)
      print('Hispanic Pain Level Mode = ', Stats_Pain_Level_Ethnicity_Case3)
      print('\n')
      
  elif (i==4):
      print('*Pain Level Stats for the Middle-Eastern Ethnicity case: ')
      second_filter = data_fixed['Ethnicity'] == 'Middle-Eastern'
      Stats_Pain_Level_Ethnicity_Case = data_fixed[second_filter]  #Filtering by the kind of treatment
      Stats_Pain_Level_Ethnicity_Case1 = Stats_Pain_Level_Ethnicity_Case['Pain Level']
      Stats_Pain_Level_Ethnicity_Case1_1 = pd.crosstab(Stats_Pain_Level_Ethnicity_Case['Pain Level'], columns = 'Pain Level Absolute Frecuencies')
      print(Stats_Pain_Level_Ethnicity_Case1_1)
      Stats_Pain_Level_Ethnicity_Case2 = statistics.median(Stats_Pain_Level_Ethnicity_Case1)
      Stats_Pain_Level_Ethnicity_Case3 = statistics.mode(Stats_Pain_Level_Ethnicity_Case1)
      Stats_Pain_Level_Ethnicity_Case = Stats_Pain_Level_Ethnicity_Case.describe()
      Stats_Pain_Level_Ethnicity_Case1 = Stats_Pain_Level_Ethnicity_Case1.describe()
      #print(Stats_Pain_Level_Ethnicity_Case)
      print('Stats Pain Level Only Ethnicity Case Middle-Eastern = ', Stats_Pain_Level_Ethnicity_Case1)
      print('Middle-Eastern Pain Level Median = ', Stats_Pain_Level_Ethnicity_Case2)
      print('Middle-Eastern Pain Level Mode = ', Stats_Pain_Level_Ethnicity_Case3)
      print('\n')
      
  elif (i==5):
      print('*Pain Level Stats for the Pacific Islander Ethnicity case: ')
      second_filter = data_fixed['Ethnicity'] == 'Pacific Islander'
      Stats_Pain_Level_Ethnicity_Case = data_fixed[second_filter]  #Filtering by the kind of treatment
      Stats_Pain_Level_Ethnicity_Case1 = Stats_Pain_Level_Ethnicity_Case['Pain Level']
      Stats_Pain_Level_Ethnicity_Case1_1 = pd.crosstab(Stats_Pain_Level_Ethnicity_Case['Pain Level'], columns = 'Pain Level Absolute Frecuencies')
      print(Stats_Pain_Level_Ethnicity_Case1_1)
      Stats_Pain_Level_Ethnicity_Case2 = statistics.median(Stats_Pain_Level_Ethnicity_Case1)
      Stats_Pain_Level_Ethnicity_Case3 = statistics.mode(Stats_Pain_Level_Ethnicity_Case1)
      Stats_Pain_Level_Ethnicity_Case = Stats_Pain_Level_Ethnicity_Case.describe()
      Stats_Pain_Level_Ethnicity_Case1 = Stats_Pain_Level_Ethnicity_Case1.describe()
      #print(Stats_Pain_Level_Ethnicity_Case)
      print('Stats Pain Level Only Ethnicity Case Pacific Islander = ', Stats_Pain_Level_Ethnicity_Case1)
      print('Pacific Islander Pain Level Median = ', Stats_Pain_Level_Ethnicity_Case2)
      print('Pacific Islander Pain Level Mode = ', Stats_Pain_Level_Ethnicity_Case3)
      print('\n')
      print('\n')
      
