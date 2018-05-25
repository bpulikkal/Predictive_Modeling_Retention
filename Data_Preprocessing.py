import pandas as pd
import numpy as np
from uszipcode import ZipcodeSearchEngine
import matplotlib.pyplot as plt
import seaborn as sns; sns.set(font_scale=1.2)

#import csv data into pandas dataframe
DF=pd.read_csv(r"C:\Users\binoop pulikkal\Desktop\Cap1Data.csv",engine='python',sep='\s*,\s*',usecols=range(1,49),index_col=0,header=0)

#Covert InceptionDt column to datetime 
DF['InceptionDt']=pd.to_datetime(DF['InceptionDt'].astype(str))

#Split dataframe into dataset and target (label)
DFsorted=DF.sort_values(by=['InceptionDt'])
DataSet=DFsorted.iloc[:,:-1].copy()
Target=DFsorted.iloc[:,[46]].copy()

#Inspect dataframes
DataSet.head() #Inspect top 5 rows
Target.head() #Inspect top 5 rows

#Replace RenewalStatus column in label with 1 and 0
Target.loc[Target.RenewalStatus=="Renewed",'RenewalStatus']=1
Target.loc[Target['RenewalStatus']=="Cancelled",'RenewalStatus']=0
Target['RenewalStatus'] = pd.to_numeric(Target['RenewalStatus'],downcast='integer', errors='coerce')

#List Columns with missing values
DataSet.columns[DataSet.isnull().any()] 

#List Columns with missing values
DataSet.columns[DataSet.isnull().any()] 

#Cleanup EngineSize column
DataSet.groupby('EngineSize').size()

DataSet.loc[DataSet.EngineSize=='5500','EngineSize']="4.7" 
DataSet.loc[DataSet.EngineSize=='4.6L','EngineSize']="4.6" 
DataSet.loc[DataSet.EngineSize=='1/2','EngineSize']="3.0" 
#Replace missing values for EngineSize with its median
DataSet.loc[DataSet['EngineSize'].isna(),'EngineSize']=DataSet['EngineSize'].median()
#Convert EngineSize to float
DataSet['EngineSize'] = pd.to_numeric(DataSet['EngineSize'], errors='coerce').fillna(0)

#Cleanup EngineHorsePower column

DataSet.groupby('EngineHorsePower').size()

#Remove substring Horsepower from EngineHorsePower column
DataSet["EngineHorsePower"] = DataSet["EngineHorsePower"].str.replace("\sHorsepower", "")
#Remove white spaces from EngineHorsePower column
DataSet["EngineHorsePower"] = DataSet["EngineHorsePower"].str.strip()
#Convert EngineHorsePower to numeric
DataSet['EngineHorsePower'] = pd.to_numeric(DataSet['EngineHorsePower'], errors='coerce')
#Replace missing values for 'EngineHorsePower' with its mean
DataSet.loc[DataSet['EngineHorsePower'].isna(),'EngineHorsePower']=DataSet['EngineHorsePower'].mean()


#Cleanup RegistrationState
DataSet.groupby('RegistrationState').size()

#Replace 'RegistrationState'='false' by 'CA'
DataSet.loc[DataSet['RegistrationState']=="false",'RegistrationState']='CA'
# In[19]:

#Cleanup EngineCylinders column
DataSet.groupby('EngineCylinders').size()

#Replace strings in EngineCylinders column to numeric values
DataSet["EngineCylinders"] = DataSet["EngineCylinders"].str.replace("Zero-Cylinder Engine", "0")
DataSet["EngineCylinders"] = DataSet["EngineCylinders"].str.replace("One-Cylinder Engine", "1")
DataSet["EngineCylinders"] = DataSet["EngineCylinders"].str.replace("Two-Cylinder Engine", "2")
DataSet["EngineCylinders"] = DataSet["EngineCylinders"].str.replace("Three-Cylinder Engine", "3")
DataSet["EngineCylinders"] = DataSet["EngineCylinders"].str.replace("Four-Cylinder Engine", "4")
DataSet["EngineCylinders"] = DataSet["EngineCylinders"].str.replace("Five-Cylinder Engine", "5")
DataSet["EngineCylinders"] = DataSet["EngineCylinders"].str.replace("Six-Cylinder Engine", "6")
DataSet["EngineCylinders"] = DataSet["EngineCylinders"].str.replace("Seven-Cylinder Engine", "7")
DataSet["EngineCylinders"] = DataSet["EngineCylinders"].str.replace("Eight-Cylinder Engine", "8")
DataSet["EngineCylinders"] = DataSet["EngineCylinders"].str.replace("Nine-Cylinder Engine", "9")
DataSet["EngineCylinders"] = DataSet["EngineCylinders"].str.replace("Ten-Cylinder Engine", "10")
DataSet["EngineCylinders"] = DataSet["EngineCylinders"].str.replace("Eleven-Cylinder Engine", "11")
DataSet["EngineCylinders"] = DataSet["EngineCylinders"].str.replace("Twelve-Cylinder Engine", "12")

#Convert EngineCylinders column to integer
DataSet['EngineCylinders'] = pd.to_numeric(DataSet['EngineCylinders'],downcast='integer', errors='coerce')
#Replace missing values for 'EngineCylinders' with its median
DataSet.loc[DataSet['EngineCylinders'].isna(),'EngineCylinders']=DataSet['EngineCylinders'].median()

#More Cleanup
#Convert EstimatedAnnualDistance & OdometerReading column to float
DataSet['EstimatedAnnualDistance'] = pd.to_numeric(DataSet['EstimatedAnnualDistance'], errors='coerce')
DataSet['OdometerReading'] = pd.to_numeric(DataSet['OdometerReading'], errors='coerce')
#Replace missing values for EstimatedAnnualDistance & OdometerReading with its mean
DataSet.loc[DataSet['EstimatedAnnualDistance'].isna(),'EstimatedAnnualDistance']=DataSet['EstimatedAnnualDistance'].mean()
DataSet.loc[DataSet['OdometerReading'].isna(),'OdometerReading']=DataSet['OdometerReading'].mean()
#Convert RatingValue column to integer
DataSet['RatingValue'] = pd.to_numeric(DataSet['RatingValue'],downcast='integer', errors='coerce')
#Replace missing values for RatingValue with its median
DataSet.loc[DataSet['RatingValue'].isna(),'RatingValue']=DataSet['RatingValue'].median()
#Replace missing values for ScholasticDisc with 'No'
DataSet.loc[DataSet['ScholasticDisc'].isna(),'ScholasticDisc']='No' 
#Replace missing values for AccidentPreventionCourseInd with 'No'
DataSet.loc[DataSet['AccidentPreventionCourseInd'].isna(),'AccidentPreventionCourseInd']='No' 
#Replace missing values for GoodDriver with 'No'
DataSet.loc[DataSet['GoodDriver'].isna(),'GoodDriver']='No' 
#Replace missing values for MatureDriver with 'No'
DataSet.loc[DataSet['MatureDriver'].isna(),'MatureDriver']='No' 
#Replace missing values for ActiveMilitary with 'No'
DataSet.loc[DataSet['ActiveMilitary'].isna(),'ActiveMilitary']='No' 
#Replace missing values for PermanentLicenseInd with 'No'
DataSet.loc[DataSet['PermanentLicenseInd'].isna(),'PermanentLicenseInd']='No' 
#Replace missing values for DriverTrainingInd with 'No'
DataSet.loc[DataSet['DriverTrainingInd'].isna(),'DriverTrainingInd']='No' 
#Replace missing values for AntiBrakingSystemCd with 'Anti-Lock Brakes Not Available'
DataSet.loc[DataSet['AntiBrakingSystemCd'].isna(),'AntiBrakingSystemCd']='Anti-Lock Brakes Not Available' 
#Replace "No Information Available" for AntiBrakingSystemCd with 'Anti-Lock Brakes Not Available'
DataSet.loc[DataSet['AntiBrakingSystemCd']=="No Information Available",'AntiBrakingSystemCd']='Anti-Lock Brakes Not Available' 
#Replace missing values for AntiTheftCd with 'No Anti-Theft Device
DataSet.loc[DataSet['AntiTheftCd'].isna(),'AntiTheftCd']='No Anti-Theft Device' 
#Replace missing values for "No Information Available" with 'No Anti-Theft Device
DataSet.loc[DataSet['AntiTheftCd']=="No Information Available",'AntiTheftCd']='No Anti-Theft Device' 
#Replace missing values for DaylightRunningLightsInd with 'No'
DataSet.loc[DataSet['DaylightRunningLightsInd'].isna(),'DaylightRunningLightsInd']='No' 


##Replace missing values with most frequent values
DataSet.loc[DataSet['VehBodyTypeCd'].isna(),'VehBodyTypeCd']=DataSet['VehBodyTypeCd'].value_counts().index[0]
DataSet.loc[DataSet['EngineType'].isna(),'EngineType']=DataSet['EngineType'].value_counts().index[0]
DataSet.loc[DataSet['VehUseCd'].isna(),'VehUseCd']=DataSet['VehUseCd'].value_counts().index[0]
DataSet.loc[DataSet['Model'].isna(),'Model']=DataSet['Model'].value_counts().index[0]
DataSet.loc[DataSet['PerformanceCd'].isna(),'PerformanceCd']=DataSet['PerformanceCd'].value_counts().index[0]
DataSet.loc[DataSet['OccupationClass'].isna(),'OccupationClass']=DataSet['OccupationClass'].value_counts().index[0]
DataSet.loc[DataSet['RestraintCd'].isna(),'RestraintCd']=DataSet['RestraintCd'].value_counts().index[0]

#Clean up RACOLRatingValue
#Map RACOLRatingValue codes to dollar values
DataSet.loc[DataSet['RACOLRatingValue'].str[0]=='A','RACOLRatingValue']='10586'
DataSet.loc[DataSet['RACOLRatingValue'].str[0]=='B','RACOLRatingValue']='13200'
DataSet.loc[DataSet['RACOLRatingValue'].str[0]=='C','RACOLRatingValue']='14189'
DataSet.loc[DataSet['RACOLRatingValue'].str[0]=='D','RACOLRatingValue']='16910'
DataSet.loc[DataSet['RACOLRatingValue'].str[0]=='E','RACOLRatingValue']='18166'
DataSet.loc[DataSet['RACOLRatingValue'].str[0]=='F','RACOLRatingValue']='19244'
DataSet.loc[DataSet['RACOLRatingValue'].str[0]=='G','RACOLRatingValue']='20886'
DataSet.loc[DataSet['RACOLRatingValue'].str[0]=='H','RACOLRatingValue']='22921'
DataSet.loc[DataSet['RACOLRatingValue'].str[0]=='J','RACOLRatingValue']='26561'
DataSet.loc[DataSet['RACOLRatingValue'].str[0]=='K','RACOLRatingValue']='31190'
DataSet.loc[DataSet['RACOLRatingValue'].str[0]=='L','RACOLRatingValue']='33907'
DataSet.loc[DataSet['RACOLRatingValue'].str[0]=='M','RACOLRatingValue']='38111'
DataSet.loc[DataSet['RACOLRatingValue'].str[0]=='N','RACOLRatingValue']='51608'
DataSet.loc[DataSet['RACOLRatingValue'].str[0]=='P','RACOLRatingValue']='87479'

#Convert RACOLRatingValue codes to numeric
DataSet['RACOLRatingValue'] = pd.to_numeric(DataSet['RACOLRatingValue'], errors='coerce')


#Create Latitude and Longitude columns from zipcode
DataSet['Latitude'] = DataSet['PostalCode'].apply(lambda pcode: ZipcodeSearchEngine().by_zipcode(pcode)['Latitude'])
DataSet['Longitude'] = DataSet['PostalCode'].apply(lambda pcode: ZipcodeSearchEngine().by_zipcode(pcode)['Longitude'])

#Replace missing values for Latitude & Longitude with its mean
DataSet.loc[DataSet['Latitude'].isna(),'Latitude']=DataSet['Latitude'].mean()
DataSet.loc[DataSet['Longitude'].isna(),'Longitude']=DataSet['Longitude'].mean()

DataSet_Cleaned=DataSet.drop(['City','StateCd'],axis=1)

#DataSet.info()

#Export cleaned datasets to csv
DataSet_Cleaned.to_csv('DataSetCleanedX.csv',index=False)
Target.to_csv('DataSetCleanedY.csv',index=False)

#End of data cleanup