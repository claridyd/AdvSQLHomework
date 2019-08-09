#####################
# Import dependencies
#####################
import numpy as np 
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Import Flask
from flask import Flask, jsonify

#####################
# Database Setup
#####################
engine = create_engine("sqlite:///Resources/hawaii.sqlite", connect_args={'check_same_thread': False})
# Reflect an existing database into a new model
Base = automap_base()
# Reflect the tables
Base.prepare(engine, reflect=True)
# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station
# Create our session from Python to the db to query it
session = Session(engine)


#####################
# Create an app
#####################
app = Flask(__name__)  

################
# Define routes
################
# Define route for Home Page and list all routes available
@app.route("/")
def home():
    """List all available api routes. """
    return(
        f"Available Routes:<br/>"
        f" <br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    # query the date and precip
    results = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date > '2016-08-23').all()

    # create dictionary
    rain = []
    for result in results:
        prcp_dict = {}
        prcp_dict["date"] = result[0]
        prcp_dict["prcp"] = result[1]
        rain.append(prcp_dict)

    return jsonify(rain)    
    
   


@app.route("/api/v1.0/stations")
def stations():
    # get list of stations
    results = session.query(Station.station).all()
    all_stations = list(np.ravel(results))

    return jsonify(all_stations)


@app.route("/api/v1.0/tobs")
def tobs():
    results = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.date > '2016-08-23').all()

    tobs_list = list(np.ravel(results))
    return jsonify(tobs_list)



@app.route("/api/v1.0/<start_date>")
@app.route("/api/v1.0/<start_date>/<end_date>")
def calc_temps(start_date=None, end_date=None):
    """TMIN, TAVG, TMAX for a list of dates"""
    if not end_date:
        results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs),func.max(Measurement.tobs)).\
            filter(Measurement.date>= start_date).all()
        start_list = list(np.ravel(results))
        return jsonify(start_list)

    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()
    all_list = list(np.ravel(results))
    return jsonify(all_list)

if __name__ == '__main__':
    app.run(debug=True)
