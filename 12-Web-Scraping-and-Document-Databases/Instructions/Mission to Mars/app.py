# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 18:39:18 2019

@author: Aalok Devkota
"""

from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

#mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")
# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/craigslist_app")


@app.route("/")
def index():
    mars_info = mongo.db.mars_info.find_one()
    return render_template("index.html", mars_info=mars_info)


@app.route("/scrape")
def scraper():
    mars_info = mongo.db.mars_info
    mars_info_data = scrape_mars.scrape_mars_news()
    mars_info_data = scrape_mars.scrape_mars_image()
    mars_info_data = scrape_mars.scrape_mars_facts()
    mars_info_data = scrape_mars.scrape_mars_weather()
    mars_info_data = scrape_mars.scrape_mars_hemispheres()
    
    mars_info.update({}, mars_info_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
