#Imports
import numpy as np
import pandas as pd
import datetime as dt
import matplotlib.dates as mdates
from flask import Flask, jsonify

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# create engine to hawaii.sqlite
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
# Declare a Base using `automap_base()`
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

# Calculate the date one year from the last date in data set.
query_date = dt.date(2017, 8,23) - dt.timedelta(days=365)
print("Query Date: ", query_date)

# Perform a query to retrieve the date and precipitation scores

year = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= query_date).all()
year

# Save the query results as a Pandas DataFrame and set the index to the date column
df = pd.DataFrame(year, columns=['Date', 'Prcp'])

#Create dictionary of PRECIP query for flask
df = df.dropna()
df = df.reset_index()
precip_dic = df.to_dict('records')


#Query the dates and temperature observations of the most active station for the last year of data.
results = session.query(Measurement.station, Measurement.date, Measurement.tobs).\
    filter(Measurement.station == 'USC00519281').all()

#Create dictionary of STATIONS for flask
stations = session.query(Station.station, Station.name).all()
stations_df = pd.DataFrame(stations, columns=['Station', 'Name'])

station_dic = stations_df.to_dict('records')
print(station_dic)

# Create dictionary of TEMPERATURE OBSERVATIONS for flask
tobs_df = pd.DataFrame(results, columns=['Station','Date','Temperature'])
tobs_dic = tobs_df.to_dict('records')


# Create app
app = Flask(__name__)

# Create Home Page
@app.route("/")
def home():
    return (
        f"Welcome to the home page!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
    )

# Define /api/v1.0/precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return the precipitation data as json"""
    return jsonify(precip_dic)

# Define /api/v1.0/stations route
@app.route("/api/v1.0/stations")
def stations():
    """Return the station data as json"""
    return jsonify(station_dic)

# Define /api/v1.0/tobs route
@app.route("/api/v1.0/tobs")
def tobs():
    """Return the tobs data as json"""
    return jsonify(tobs_dic)

# Define /api/v1.0/<start> route
@app.route("/api/v1.0/<date>")
def start(date):
    """Return the min, max, ave temps as json"""
    session = Session(engine)
    date = dt.datetime.strptime(date,'%Y-%m-%d')
    start_results = session.query(func.ave(Measurement.tobs),func.min(Measurement.tobs),func.max(Measurement.tobs)).filter(Measurement.date >= date).all()
    print(start_results)
    session.close()

    start = list(np.ravel(start_results))
    return jsonify(start)

if __name__ == "__main__":
    app.run(debug=True)

# start_results = session.query(Measurement.date, func.ave(Measurement.tobs),func.min(Measurement.tobs),func.max(Measurement.tobs)).filter(Measurement.date >= date).all()