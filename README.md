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
At the beginning of a project, it is usual to not quite understand the data very well. For this reason, the following examples will help us understand them better.

**2.1 Primary Type frequency**

The plot below shows the frequency of the Primary type labels that occur in our data 

<img src="https://user-images.githubusercontent.com/72870088/212781303-07ffa1e6-ea2a-4184-a8d6-d0af7ab6313b.png" width="800" height="446" alt="Image Alt Text">

We can easily observe that our data is highly imbalanced. This will affect the accuracy of the model that we will use later, so we have to consider this when we will measure its performance. 

**2.2 Crime map of Chicago**

Next, we can use the Plotly library of Python to create a Chicago crime map. For this purpose, we will use only the 4% of our data for this plot, due to the plugin's capacity constraints for processing data at the same time. The end result is an interactive map of Chicago that demonstrates how each crime type is distributed across the city. 

Below we can see the distribution of the most often Primary type, which is Theft (as shown from the previous plot).

<img src="https://user-images.githubusercontent.com/72870088/212782919-c51925ba-b7f3-4580-908d-85d282fbdcd7.PNG" width="600" height= "444" alt="Image Alt Text">

We observe that theft is more intense in the east of Chicago, and next in the northeast. We can use this crime map to see the distribution of other crimes also. If we hover over a dot, we can see the details we have of the specific crime.  

**2.3 At what time a crime occured**

Wih the following plot we select the most common types of crime, and wee see how they behave throughout the day.

<img src="https://user-images.githubusercontent.com/72870088/212784307-e5872f40-9fcf-4174-be16-7f35d9582cc2.PNG" width="800" height= "371" alt="Image Alt Text">

Our findings suggest that criminals are more active during the early afternoon and midnight. The peak of the most common crime occurs most often at 19:00. Also, there are crimes such as "NARCOTICS" that occur rarely in the night, but most of the times in the day. 

If we want, we can be more specific and add more parameters (for example when the location is "Residence" or "Apartment")

**2.4 In which area occur the most crime incidents**

Using a bar chart of Plotly, we can find out which area records the most crime incidents in Chicago

<img src="https://user-images.githubusercontent.com/72870088/212785296-db7f4404-7f86-4436-9439-a47d3418d41e.PNG" width="600" height= "250" alt="Image Alt Text">

West Side is by far the busiest area, and on the contrary, the least crime incidents are recorded in the north. 

More plots and further analysis are available on the dashboards files.



