# -*- coding: utf-8 -*-
"""


@author: Aalok Devkota
"""

# Import dependencies
import pandas as pd
import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from flask import Flask, jsonify

# Set up Flask
app = Flask(__name__)


engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)


Station = Base.classes.station


Measurement = Base.classes.measurement


session = Session(engine)

@app.route("/")
def homepage():

    return (
        f"HomePage<br/>"
        
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"       
        f"/api/v1.0/2016-08-23/2017-08-23<br/>"
    )
    
last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
one_year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=3)
prcp = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= one_year_ago).all()
    
    
prcp_dict = dict(prcp)
prcp_dict
    

@app.route("/api/v1.0/precipitation")
def precipitation():
    last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    one_year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=3)
    prcp = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= one_year_ago).all()
    
    
    prcp_dict = dict(prcp)
    prcp_dict
  
    return (jsonify(prcp_dict))
   

@app.route("/api/v1.0/stations")
def stations():
    all_stations = session.query(Station.station).all()
    all_stations= list(np.ravel(stations))
    all_stations

  
    return (jsonify(all_stations))
    
@app.route("/api/v1.0/tobs")
def temp_year():
    today = datetime.datetime.today()
    today = today.date()
    last_year = today - datetime.timedelta(365)
    temp_year = session.query(Measurement.date, Measurement.tobs).filter(and_(Measurement.date <= today, Measurement.date >= last_year)).all()

    return jasonify(temp_year)


@app.route("/api/v1.0/<start>")
def start_temp(start):
   
    temp_data = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).all()
    
    return jsonify(temp_data)

    

@app.route("/api/v1.0/<start>/<end>")
def range_temp(start, end):

    temp_data = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(and_(Measurement.date >= start, Measurement.date <= end)).all()
    
    return jsonify(temp_data)

if __name__ == '__main__':
    app.run(debug=False)