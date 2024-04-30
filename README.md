# Chicago Crime Analysis 
* According to reports, Chicago is the 3rd most popular city in the USA, but is also considered as one of the violent ones. With population of 2.7M, Chicago is densely populated, and that has a direct impact on the crime rate. However, the crimes in the city are not evenly distributed, depending on various factors. It is important to find the location, the time and the type of crimes that are taking place. For this reason, we are going to embark on an exploratory data analysis of crimes in Chicago, and also make predictions about the type of crimes in this city, using Random Forest Classifier algorithm. 
* Data source: 
The data for this analysis is taken from the source [Kaggle](https://www.kaggle.com/datasets/onlyrohit/crimes-in-chicago?resource=download&fbclid=IwAR2CbYaDRwKgWVlj5yJsYn1m2VMwNvXyhPBZDzCBRVG-WABM_ihdljQ-qzs), which reports incidents of crime that occured in the City of Chicago from 2010 to present. On this analysis, we will use the data that contains the crimes that took place from 2020 to 2022. Furthermore, data from  [Wikipedia](https://en.wikipedia.org/wiki/Community_areas_in_Chicago) is utilized, in order to use the population of each community area of Chicago on the analysis. 

The analysis is uploaded in 3 separate files due to maximum capacity constraints. 
  
 [Dashboards](https://github.com/cfragiadakis/Crime-Analysis-in-Chicago/blob/main/Part%201%20Dashboards.ipynb)
 
 [Dashboards 2](https://github.com/cfragiadakis/Crime-Analysis-in-Chicago/blob/main/Part%202%20Dashboards%20.ipynb)
 
 [Clustering & Random Forest Classifier predictive model](https://github.com/cfragiadakis/Crime-Analysis-in-Chicago/blob/main/Part%203%20Clustering%20%26%20Random%20Forest%20Classifier.ipynb)


# Step 1: Load the Data

We can start by downloading the Chicago crime dataset on [kaggle.com](https://www.kaggle.com/). Once the dataset is downloaded, we place the CSV files in our working folder. The dataset contains all the incidents of crime that occured in Chicago from 2010 to present. We will use only the CSV's from 2020 to 2022. Once we have successfully read the files, we exclude the columns that we will not use for our analysis (for example "Ward", "District"). The columns that remain in our dataset are: 
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

Next, we have to merge df, with the pop dataframe to get the remaining columns. Full code is available on the uploaded files.

# Step 2: Explore the data 
At the beginning of a project, it is usual to not quite understand the data very well. For this reason, the following examples will help us understand them better.

 **2.1 Primary Type frequency**

The plot below shows the frequency of the Primary type labels that occur in our data 

<img src="https://user-images.githubusercontent.com/72870088/212781303-07ffa1e6-ea2a-4184-a8d6-d0af7ab6313b.png" width="800" height="446" alt="Image Alt Text">

Theft and battery are the most frequent crimes that occur in Chicago. We can easily observe that our data is highly imbalanced. This will affect the accuracy of the model that we will use later, so we have to consider this when we will measure its performance. 

 **2.2 Crime map of Chicago**

Next, we can use the Plotly library of Python to create a Chicago crime map. For this purpose, we will use only the 4% of our data for this plot, due to the plugin's capacity constraints for processing data at the same time. The end result is an interactive map of Chicago that demonstrates how each crime type is distributed across the city. 

Below we can see the distribution of the most often Primary type, which is Theft (as shown from the previous plot).

<img src="https://user-images.githubusercontent.com/72870088/212782919-c51925ba-b7f3-4580-908d-85d282fbdcd7.PNG" width="600" height= "444" alt="Image Alt Text">

We observe that theft is more intense in the east of Chicago, and next in the northeast. We can use this crime map to see the distribution of other crimes also. If we hover over a dot, we can see the details we have of the specific crime.  

**2.3 Time when a crime occured**

With the following plot we select the most common types of crime, and we see how they behave throughout the day.

<img src="https://user-images.githubusercontent.com/72870088/212784307-e5872f40-9fcf-4174-be16-7f35d9582cc2.PNG" width="800" height= "371" alt="Image Alt Text">

Our findings suggest that criminals are more active during the early afternoon and midnight. The peak of the most common crime occurs most often at 19:00. Also, there are crimes such as "NARCOTICS" that occur rarely in the night, but most of the times in the day. 

If we want, we can be more specific and add more parameters (for example when the location is "Residence" or "Apartment")

**2.4 In which area the most crime incidents are recorded**

Using a bar chart of Plotly, we can find out which area records the most crime incidents in Chicago.

<img src="https://user-images.githubusercontent.com/72870088/212785296-db7f4404-7f86-4436-9439-a47d3418d41e.PNG" width="600" height= "250" alt="Image Alt Text">

West Side is by far the busiest area, and on the contrary, the least crime incidents are recorded in the north. 

**2.5 Crime heatmap of Chicago**

With the Python library folium, we can create a heatmap of Chicago to visualize the density of criminal activity in the city. 

<img src="https://user-images.githubusercontent.com/72870088/212914577-7ab9efd9-8dc9-4a73-806c-dccf724395a0.png" width="599" height= "400" alt="Image Alt Text">

The most heavily affected part of Chicago is in the Central region, and upon zooming in the map we can find the North State Street that stands out as a hotspot. This street is one of the most popular shopping destinations of the city, and is also the block with the most crime incidents recorded (particularly theft). 


**2.6 Location analysis on a specific day**

Proceeding with the analysis, we can become more specific and visualize the crimes that occurred a specific day, on a specific location of Chicago. If we group our data by date, we will find out that the date with the most crime incidents occur on 31st of May 2020 (George Floyd protests). We can choose one of the 77 community areas, we will pick for this example Near West Side.

<img src="https://user-images.githubusercontent.com/72870088/212920038-1c4dcf29-421f-45a2-b5a9-10aecd6c0be7.PNG" width="600" height= "328.5" alt="Image Alt Text">

The first step is to visualize all the crimes that occurred with a heatmap on the location. Next, using the latitude and longitude of these crimes, we find the centroid of these incidents and mark it with a black circle. In case we have one ambulance or patrol car available, it would be most efficient to place it in the spot of this circle, for quickest average response time. Therefore, it would be beneficial to station emergency services between Eisenhover Expressway and South Ashland Avenue, in the event of similar situations in the future.

Additional visualizations, deeper analysis and complete code are available on the dashboards files. While there is still room for further exploration, we have a solid understanding of the data, and we can continue with clustering. 


# Step 3: Clustering
Clustering is a technique that groups similar data points together without using pre-labeled information. This process organizes data into various sets based on how closely they resemble each other. We will apply this method to discover the similarities between different regions in Chicago by utilizing the types of crimes recorded in each area. 

 **3.1 Finding the optimal number of clusters**

First, we have to find the K number, that will make our number of clusters optimal. To achieve this, we will use The Elbow method. The Elbow Method is a widely used approach to determine the ideal number of clusters in a given dataset. This method utilizes the Within Cluster Summed Squares (WCSS) parameter, which is calculated based on the location of the centroids of each group. The WCSS parameter decreases as the number of clusters increases. As more clusters are added, the difference in decrease of WCSS becomes less significant. The optimal number of clusters is reached when the decrease in WCSS is not significant.

<img src="https://user-images.githubusercontent.com/72870088/212945388-18d8ae13-8f97-4235-af1c-80d7f75feaf5.PNG" width="500" height= "318.6" alt="Image Alt Text">

Based on the image above, there is a significant difference when the number of clusters is 3. Once this number is reached, the distinction between clusters becomes less significant. In this example, the optimal number of clusters is 3.

**3.2 Division of Chicago regions**

We can observe the geographical location of each cluster with the help of a map created with the Plotly library, in order to identify each region by its corresponding cluster colour assigned by the K-Means algorithm.

<img src="https://user-images.githubusercontent.com/72870088/212947716-a8d6508a-4294-4655-a7d6-a62eaf075e1b.PNG" width="400" height= "518" alt="Image Alt Text">

We can notice that there is a geographical relationship in the way our clusters are grouped, thus we can make observations about the division of them and the regions they contain. 

 **Cluster 1**
 
 **Regions:**  Far North Side, Far Southeast Side, South Side, Southwest Side
 
The areas that participate in this cluster are located mainly in the southern part of Chicago. These areas have the highest crime rates, and all of them are characterized by high incidents of battery

 **Cluster 2**
 
 **Regions:**  West Side
 
 On this cluster participates only the West Side of Chicago. However, it is the cluster with the highest number of crimes. The difference compared to the rest of the regions is so significant to the point that the region is classified in a cluster by itself. The most prevalent crimes in West Side are battery and theft
 
 **Cluster 3**
 
  **Regions:**  Central, Far Southwest Side, Far North Side, North Side, Northwest Side
  
  The last  cluster includes the areas that make up the northern part of Chicago, as well as its center. These areas are grouped into a cluster due to their     comparatively low  number of recorded crimes than the rest of the city, with theft being the most frequent type of crime recorded. 
  

# Step 4: Prediction model 

Our target is to develop a model that can make predictions of the type of a crime with high accuracy, giving to the model as input, features like date and the area. To achieve this, we use Random Forest Classifier. Random Forest is a machine learning  technique, used to solve classification and regression problems. It combines multiple decision trees and uses ensemble learning, which combines multiple classifiers to tackle complex problems. The algorithm can only handle integer and boolean values, but no categorical data. Therefore, we need to prepare our data before utilizing Random Forest. 

From our dataset, we will use in our model the features: 

* **Date & Time:** The date and time feature plays a crucial role in our model as it helps to understand certain patterns of crimes. For instance, the nightlife district experiences an increase in certain types of crimes during Saturday nights due to the presence of more people.

* **Area:** In order to add area feature, we have to use dummy variables, since we have already mentioned that our model will be able to handle only integer and boolean values.

* **Latitude & Longitude:** For the latitude and longitude features, we firstly remove the outliers of our dataset. Then, we convert them into polar coordinates. This allows our model to better understand the location.
 
 Taking account of these features, the primary input to our crime type prediction model is the information of the time and location where a crime takes place. 
 
 The next step is to divide our data into two separate sets, one for training and one for testing. We will use 80% of the data for training and the remaining 20% for testing. Once this is done, we can use the training dataset to train our Random Forest model.
 
<img src="https://user-images.githubusercontent.com/72870088/213052794-35be8294-b853-48e9-8d2c-3adc6c856785.PNG" width="350" height= "110" alt="Image Alt Text">

Our model achieves 28% accuracy. At first glance, this might not seem very impressive, but considering that we have 32 types of crime and only 620.000 records in our dataset, the number is respectable. Lastly, let's observe some predictions made by our model and compare them to the actual crime types.

<img src="https://user-images.githubusercontent.com/72870088/213156193-e159de51-2df7-4f3b-b6fd-2667289a4712.PNG" width="191" height= "200" alt="Image Alt Text">

Our model mostly predicts the labels of crimes of 1 and 4. This is also confirmed by the confusion matrix below. 

<img src="https://user-images.githubusercontent.com/72870088/213156204-9bdc4705-d603-4a3c-8bee-2968fe9d3858.PNG" width="574" height= "400" alt="Image Alt Text">



The confusion matrix shows that our model frequently predicts crime categories 1 and 4, neglecting the rest crime types. This is due to the uneven distribution of crime types in the training data.




# **Conclusion**

This crime analysis presents multiple ways to visualize our data, so we can have a better understanding of them. We depicted our data in an interactive map of Chicago, using Plotly library, and heatmaps were used in order to highlight hotspots. Furthermore, we divided the city of Chicago into 3 clusters based on the location and frequent crime types in each region. Finally, we trained a Random Forest Classifier model with 28% accuracy, a satisfying result, considering our dataset is highly imbalanced and contains 32 possible crime types. 



