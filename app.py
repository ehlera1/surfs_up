# Set up the Flask Weather App

# Initial dependencies 
import datetime as dt
import numpy as np
import pandas as pd


# Improt sqlalchemy dependencies 
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


# Import Flask dependencies
from flask import Flask, jsonify


# Set up the database 
engine = create_engine("sqlite:///hawaii.sqlite")

# Reflect the database into our classes 
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save referenecs to each table - create a variable for each of the classes 
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session link from Python to our database
session = Session(engine)

# Define our app
# Set up Flask
app = Flask(__name__)

#Define Welcome route
@app.route("/")

# Create function and additional routes
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API! 
    <br>Available Routes:
    <br>/api/v1.0/precipitation
    <br>/api/v1.0/stations
    <br>/api/v1.0/tobs
    <br>/api/v1.0/temp/start/end
    ''')


# Creating new route for precipitation 
@app.route("/api/v1.0/precipitation")


# Precipitaiton Function 
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

# Creating new route for stations
@app.route("/api/v1.0/stations")

# Stations Function
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

# Creating new route for monthly temperature 
@app.route("/api/v1.0/tobs")

# Function for monthly temperature
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

# Creating Statistics Route
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

# Function for stats
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)









if __name__=="__main__":
    app.run(debug=True)

