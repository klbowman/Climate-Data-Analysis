# Climate Analysis and Exploration 

Basic climate analysis and data exploration using Python and SQLAlchemy...flask app

## Description

This repository is designed to explore and analyze climate data using Python and SQLAlchemy. Climate data is imported into Jupyter Notebook (climate_starter.ipynb) from a SQL database using sqlite. A SQLAlchemy engine is created to connect to the sqlite database (hawaii.sqlite) in the Resources directory, and a Base is used to reflect the tables into classes. Pandas and Matplotlib are used to analyze and visualize precipitation and temperature data from the past 12 months. 

<p align="center">
  <img src="https://user-images.githubusercontent.com/74067302/146426590-1af40c96-2eb9-41bf-8c24-91a2f3255091.png" alt="Bar Chart: Precipitation" width="400"/>
  <img src="https://user-images.githubusercontent.com/74067302/146426600-9f1b4237-d2d7-42b4-bedd-50bd08b6a4d5.png" alt="Bar Chart: Temperature" width="400"/>
</p>


visualize taxonomic data using charts, and display metadata in an organized panel. The [data](http://robdunnlab.com/projects/belly-button-biodiversity/results-and-data/) comes from a study that sequenced the microbiome of 153 human belly buttons (Hulcr et al., 2012), and is stored in the samples.json file. Individual samples are identified by a numerical code and accompanied by metadata including age, gender, ethnicity, etc. Operational taxonomic units (OTUs) id numbers and counts are provided for each sample.

The dashboard includes a drop-down menu that displays the numerical code for each individual sample. When a sample is selected, the “Demographic Info” panel is populated with metadata and the following three charts are populated with data:
* Bar graph displaying the top 10 OTUs by count
* Gauge plot showing the belly button scrubs per week
* Bubble plot displaying OTU counts for the entire sample

<p align="center">
  <img src="https://user-images.githubusercontent.com/74067302/145615550-98e49162-44c9-4e39-9050-ba837dc42863.png" alt="Dashboard Image"/>
</p>
<p align="center">
  <img src="https://user-images.githubusercontent.com/74067302/145615561-5fc19f35-646b-47aa-9f63-4a93a495efe5.png" alt="Dashboard Image"/>
</p>

## Getting Started

### Technologies Used 

* Jupyter Notebook
* Python
* Pandas
* Matplotlib
* NumPy
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
