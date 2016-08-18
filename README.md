# Yelp-Recommendation-Engine
1. A recommendation engine developed for Yelp Dataset.
2. Recommends Yelpers, top best businesses according to their preferences
3. Used Apache Spark's Pyspark.
4. For recommendation engine, used Apache Spark's mlib supporting Model based Collaborative filtering that uses the alternating least squares (ALS) algorithm to learn these latent factors.
5. Used Python Flask framework for Restful APIs around the engine.
6. The CherryPy framework features a reliable, HTTP/1.1-compliant, WSGI thread-pooled webserver.
7. Used Pyspark for operations on data.
8. Provided an interactive UI for users to input preferences and a neat display of business recommendations.

#Technologies
Apache Spark, Python, Flask, Angular

#The basic flow of data is:

Initially, Yelp data is fed to Apache Spark and important details are extracted from the dataset.
Once the data set is extracted, the String Ids of users and businesses are converted to int Ids as the machine library of Spark can only take input (user,product,ratings) in the form (int, int, float).
Now we provide the userIds, business Ids and stars in the yelp_reviews for training.
Spark’s mlib for recommendation is really efficient and faster. It uses Model based Collaborative Filtering with alternating least squares (ALS) algorithm to learn the latent factors.
I tried User Based Collaborative Filtering and Trust Based Recommendations on the same dataset, but it consumed large amount of memory, were comparatively slower and not efficient. Basically my system crashed due to processing of such a huge dataset. Hence I decided to go with the Spark’s mlib for Recommendations.
After training data, it was easy to predict business for a userId. The int Ids had to be converted back to String Ids for extractings details of business.
Now, in my system, user is provided with top recommendations near the address he mentions, within city and state he provides and also the category of business he wants. This can be further modified with user’s current location which has not been implemented.
An interactive UI ensures that user easily provides input and clearly sees the results.

#WorkFlow
![alt tag](https://github.com/sarikakale/Yelp-Recommendation-Engine/blob/master/WorkFlow.png)

#Future Scope:

This project is a very simple implementation of recommendation system. It can be further enhanced with more features like more preference choices, recommendation taking into consideration user’s location, review analysis for positivity and negativity, analysis on a business’s expansion possibility, competitions around and predicting business growth. Recommendation engines provide a great deal of information for business growth and is a very profitable solution for many organizations. More efficient algorithms can be explored for accurate predictions.
