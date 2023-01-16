# Chicago Crime Analysis 
* According to reports, Chicago is the 3rd most popular city in the USA, but is also considered as one of the violent ones. With population of 2.7M, Chicago is densely populated, and that has a direct impact on the crime rate. However, the crimes in the city are not evenly distributed, depending on various factors. It is important to find the location, the time and the type of crimes that are taking place. For this reason, we are going to embark on an exploratory data analysis of crimes in Chicago, and also make predictions about the type of crimes in this city. 
* Data source: 
The data for this analysis is taken from the source [Kaggle](https://www.kaggle.com/datasets/onlyrohit/crimes-in-chicago?resource=download&fbclid=IwAR2CbYaDRwKgWVlj5yJsYn1m2VMwNvXyhPBZDzCBRVG-WABM_ihdljQ-qzs) , which reports incidents of crime that occured in the City of Chicago from 2010 to present. On this analysis, we will use the data that contains the crimes that took place from 2020 to 2022. Furthermore, data from  [Wikipedia](https://en.wikipedia.org/wiki/Community_areas_in_Chicago) is also used, in order to use the population of each community area of Chicago on the analysis. 

The analysis is uploaded in 3 separate files due to maximum capacity constraints. 
  
 [Dashboards](https://github.com/cfragiadakis/Crime-Analysis-in-Chicago/blob/main/Chicago%20Dashboards.ipynb)
 
 [Dashboards 2nd part](https://github.com/cfragiadakis/Crime-Analysis-in-Chicago/blob/main/Dashboards%202nd%20page.ipynb)
 
 [Clustering and Random Forest Classifier predictive model](https://github.com/cfragiadakis/Crime-Analysis-in-Chicago/blob/main/Clustering%20and%20Random%20Forest%20Classifier.ipynb)


# Step #1 Load the Data

We can start by downloading the Chicago crime dataset on [kaggle.com](https://www.kaggle.com/). Once the dataset is downloaded, we place the CSV files in our working folder. The dataset contains all the incidents of crime that occured in Chicago from 2010 to present. We will use only the CSV's from 2020 to 2022. Once we have succesfully read the files, we exclude the columns that we will not use for our analysis (for example Ward, District). The columns that remain in our dataset are: 
* **ID:** Unique identifier of the record
* **Date:** Timestamp of the crime incident
* **Block:** The block address of the crime incident
* **Primary Type:** Type of crime incident. This variable will later be used as target variable
* **Location Description:** The type of location that the crime took place 
* **Arrest:** Indicates whether an arrest was made
* **Community Area:** Indicates the number of the community area where the incident occurred
* **Name:** Indicates the name of the community area where the incident occurred (only in chicagopop.csv)
* **Population:** Population of the community area where the incident occurred (only in chicagopop.csv)
* **Area:** Indicates the area where the incident occurred (only in chicagopop.csv)
* **Latitude:** Indicates the latitude of the location where the incident occurred
* **Longitude:** Indicates the longitude of the location where the incident occurred
* **Year:** We extract this from the date column, year of the occurred incident
* **Month:** We extract this from the date column, month of the occurred incident
* **Hour:** We extract this from the date column, hour of the occurred incident

Once we load the data into dataframes and concat them into one, we use the head() command to ensure that we can see the data 
<img src="https://user-images.githubusercontent.com/72870088/212772185-76470cbd-9c47-4a2e-a150-29d3ed4ffb3f.PNG" width="656" height="437" alt="Image Alt Text">

Next, we have to merge df, with the pop dataframe to get the remaining columns. Full code is available on the uploaded files.

# Step #2 Explore the data 
At the beginning of a project, it is usual that we do not quite understand the data very well. For this reason, the following examples will help us understand better our data. 

