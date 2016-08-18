'''
Created on Jul 12, 2016

@author: sarika
'''
#import recommendationengine
import engine
from engine import RecommendationEngine
from flask import Blueprint
from flask.app import Flask
from cherrypy._cpcompat import json
from asyncio.log import logger
main = Blueprint('main',__name__)
from flask import Flask, request,render_template


@main.route("/<string:user_id>/ratings/top/<int:count>", methods=["GET"])
def top_recommendation(user_id, count):
    """Get Top Recommendations """
    top_ratings = recommendationengine.get_top_ratings_with_business_info(user_id, count);
    return json.dumps(top_ratings)

@main.route("/<string:user_id>/nearest/<int:count>/<string:address>", methods=["GET"])
def nearest_ratings(user_id, count,address):
    """Get Nearest Recommended business to user's address """
    logger.debug("User %s rating requested for nearest address", user_id, address)
    ratings = recommendationengine.get_nearest_businesses(user_id,count,address)
    return json.dumps(ratings)

@main.route("/<string:user_id>/state/<int:count>/<string:state>", methods=["GET"])
def ratings_within_state(user_id, count,state):
    """Get Top Recommendations within the state """
    logger.debug("User %s rating requested for state %s", user_id, state)
    ratings = recommendationengine.get_business_in_state(user_id,count,state)
    data = json.dumps(ratings)
    return data

@main.route("/<string:user_id>/city/<int:count>/<string:city>", methods=["GET"])
def ratings_within_city(user_id, count,city):
    """Get Top Recommendations within the city"""
    logger.debug("User %s rating requested for city %s", user_id, city)
    ratings = recommendationengine.get_business_in_city(user_id,count,city )
    return json.dumps(ratings)

@main.route("/<string:user_id>/category/<int:count>/<string:category>", methods=["GET"])
def ratings_within_category(user_id, count,category):
    """Get Top Recommendations within the category"""
    logger.debug("User %s rating requested for category %s", user_id, category)
    ratings = recommendationengine.get_business_in_categories(user_id, count,category)
    return json.dumps(ratings)

@main.route("/<string:user_id>/ratings/<string:business_id>", methods=["GET"])
def business_ratings(user_id, business_id):
    logger.debug("User %s rating requested for business %s", user_id, business_id)
    ratings = recommendationengine.get_ratings_for_business_ids(user_id, [business_id])
    return json.dumps(ratings)

@main.route("/", methods=["GET"])
def mainIndex():
    logger.debug("User %s rating requested for movie %s")
    return render_template('index.html')
    
@main.route("/users",methods=["GET"])
def get_user_Ids():
    logger.debug("Users")
    userIds=recommendationengine.get_User_Ids()
    return json.dumps(userIds)

@main.route("/<string:user_id>/ratings", methods = ["POST"])
def add_ratings(user_id):
    # get the ratings from the Flask POST request object http://<SERVER_IP>:5432/0/ratings/top/10
    ratings_list = request.form.keys()[0].strip().split("\n")
    ratings_list = map(lambda x: x.split(","), ratings_list)
    # create a list with the format required by the negine (user_id, movie_id, rating)
    ratings = map(lambda x: (user_id, int(x[0]), float(x[1])), ratings_list)
    # add them to the model using then engine API
    recommendationengine.add_ratings(ratings)
 
    return json.dumps(ratings)

def create_app(spark_context,app):
    global recommendationengine
    recommendationengine = RecommendationEngine(spark_context,app)
    
    app = Flask(__name__)
    app.register_blueprint(main)
    return app 