# Import dependencies
import numpy as np 

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Import Flask
from flask import Flask, jsonify




# Create an app
app = Flask(__name__)  

# Define routes
################
# Define route for Home Page and list all routes available
@app.route("/")
def home():
    """List all available api routes. """
    return(
        f"Available Routes:<br/>"
        f"/api.v1.0/precipitation<br/>"
        f"/api.v1.0/stations<br/>"
        f"/api.v1.0/tobs<br/>"
        f"/api/v1.0/<start>"
    )




@app.route("/api.v1.0/precipitation")






@app.route("/api/v1.0/stations")



@app.route("/api/v1.0/tobs")



@app.route("/api/v1.0/<start>")

