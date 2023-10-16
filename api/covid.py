from contextlib import nullcontext
from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
import requests  # used for testing 
import time

# Blueprints enable python code to be organized in multiple files and directories https://flask.palletsprojects.com/en/2.2.x/blueprints/
covid_api = Blueprint('covid_api', __name__,
                   url_prefix='/api/covid')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(covid_api)

"""Time Keeper
Returns:
    Boolean: is it time to update?
"""
def updateTime():
    global last_run  # the last_run global is preserved between calls to function
    try: last_run
    except: last_run = None
    
    # initialize last_run data
    if last_run is None:
        last_run = time.time()
        return True
    
    # calculate time since last update
    elapsed = time.time() - last_run
    if elapsed > 86400:  # update every 24 hours
        last_run = time.time()
        return True
    
    return False

"""API Handler
Returns:
    String: API response
"""   
def getCovidAPI():
    global covid_data  # the covid_data global is preserved between calls to function
    try: covid_data
    except: covid_data = None

    """
    Preserve Service usage / speed time with a Reasonable refresh delay
    """
    if updateTime(): # request Covid data
        """
        RapidAPI is the world's largest API Marketplace. 
        Developers use Rapid API to discover and connect to thousands of APIs. 
        """
        url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api"
        headers = {
            'x-rapidapi-key': "dec069b877msh0d9d0827664078cp1a18fajsn2afac35ae063",
            'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers)
        covid_data = response
    else:  # Request Covid Data
        response = covid_data

    return response


"""API with Country Filter
Returns:
    String: Filter of API response
"""   
def getCountry(filter):
    # Request Covid Data
    response = getCovidAPI()
    # Look for Country    
    countries = response.json().get('countries_stat')
    for country in countries:  # countries is a list
        if country["country_name"].lower() == filter.lower():  # this filters for country
            return country
    
    return {"message": filter + " not found"}


"""Defines API Resources 
  URLs are defined with api.add_resource
"""   
class CovidAPI:
    """API Method to GET all Covid Data"""
    class _Read(Resource):
        def get(self):
            return getCovidAPI().json()
        
    """API Method to GET Covid Data for a Specific Country"""
    class _ReadCountry(Resource):
        def get(self, filter):
            return jsonify(getCountry(filter))
    
    # resource is called an endpoint: base usr + prefix + endpoint
    api.add_resource(_Read, '/')
    api.add_resource(_ReadCountry, '/<string:filter>')


"""Main or Tester Condition 
  This code only runs when this file is "played" directly
"""        
if __name__ == "__main__": 
    """
    Using this test code is how I built the backend logic around this API.  
    There were at least 10 debugging session, on handling updateTime.
    """
    
    print("-"*30) # cosmetic separator

    # This code looks for "world data"
    response = getCovidAPI()
    print("World Totals")
    world = response.json().get('world_total')  # turn response to json() so we can extract "world_total"
    for key, value in world.items():  # this finds key, value pairs in country
        print(key, value)

    print("-"*30)

    # This code looks for USA in "countries_stats"
    country = getCountry("USA")
    print("USA Totals")
    for key, value in country.items():
        print(key, value)
        
    print("-"*30)
