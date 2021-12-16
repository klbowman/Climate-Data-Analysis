# Climate Analysis and Exploration 

Basic climate analysis and data exploration using Python and SQLAlchemy with a Flask application to display data.

## Description

This repository is designed to explore and analyze climate data from Hawaii using Python and SQLAlchemy. The **goal** is to analyze previous weather conditions to select ideal vacation dates. Climate data is imported into Jupyter Notebook (climate_starter.ipynb) from a SQL database using sqlite. A SQLAlchemy engine is created to connect to the sqlite database (hawaii.sqlite) in the Resources directory, and a Base is used to reflect the tables into classes. Pandas and Matplotlib are used to analyze and visualize precipitation and temperature data from the past 12 months. 

<p align="center">
  <img src="https://user-images.githubusercontent.com/74067302/146426590-1af40c96-2eb9-41bf-8c24-91a2f3255091.png" alt="Bar Chart: Precipitation" width="400"/>
  <img src="https://user-images.githubusercontent.com/74067302/146426600-9f1b4237-d2d7-42b4-bedd-50bd08b6a4d5.png" alt="Bar Chart: Temperature" width="400"/>
</p>

A [Flask](https://flask.palletsprojects.com/en/2.0.x/) API application is designed to create and display dictionaries of each query developed in the Juptyer Notebook file (climate_starter.ipynb). Flask application routes display JSON lists of precipitation, station ID, and observed temperature. 

Additional data analysis using SciPy statistical applications (t-test) revealed that temperatures are significantly higher in June compared to December (temp_analysis_bonus_1_starter.ipynb). Minimum, maximum, and average temperatures are plotted for popular vacation periods (Feb. 28 - March 5) in 2012 (temp_analysis_bonus_2_starter) to furthur investigate ideal vacation dates.


## Getting Started

### Technologies Used 

* Jupyter Notebook
* Python
* Pandas
* Matplotlib
* NumPy
* SciPy
* SQLAlchemy
* Flask

### Installing

* Clone this repository to your desktop.
* Navitage to the home directory and open index.html in your browser.

### Data Sources

* Menne, M.J., I. Durre, R.S. Vose, B.E. Gleason, and T.G. Houston, 2012: An overview of the Global Historical Climatology Network-Daily Database. Journal of Atmospheric and Oceanic Technology, 29, 897-910, https://doi.org/10.1175/JTECH-D-11-00103.1


## Author

Katlin Bowman, PhD

E: klbowman@ucsc.edu

[LinkedIn](https://www.linkedin.com/in/katlin-bowman/)
