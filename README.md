# spaceY
## Introduction
The commercial space industry is rapidly evolving, with companies like SpaceX leading innovation through reusable rockets that dramatically lower launch costs. The Falcon 9 rocket’s first stage plays a crucial role in this cost reduction by being recoverable and reusable. Predicting whether this first stage will land successfully enables more accurate launch cost estimates, which is vital for new competitors like SpaceY. By leveraging publicly available data and machine learning techniques, this project aims to build predictive models that forecast first stage landings, helping SpaceY strategize pricing and compete effectively in the commercial space market.

## Project Goal
1. How variables like launch site, payload mass, and booster reuse affect the success of Falcon 9 launches.
2. How the success of Falcon 9 landing changes over time.
3. Which algorithm peforms best for the binary classification problem of first stage landing.

## Projects Steps
### Complete and Preprocess the Data Collection API
<code>[jupyter-labs-spacex-data-collection-api.ipynb]</code>

Make a get request to the SpaceX API. You will also do some basic data wrangling and formating.
* Request to the SpaceX API
* Clean the requested data

### Data Collection with Web Scraping
<code>[jupyter-labs-spacex-data-collection-api.ipynb]</code>

Perform web scraping to collect Falcon 9 historical launch records from a Wikipedia page titled List of Falcon 9 and Falcon Heavy launches 
https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches

### Data Wrangling
<code>[labs-jupyter-spacex-Data wrangling.ipynb]</code>

Perform some Exploratory Data Analysis (EDA) to find some patterns in the data and determine what would be the label for training supervised models.

### EDA with SQL
<code>[jupyter-labs-eda-sql-coursera_sqllite.ipynb]</code>

Determine if the first stage will land, we can determine the cost of a launch. 

### EDA with Visualization Using Pandas and Matplotlib
<code>[edadataviz.ipynb]</code>

Determine if the first stage will land, we can determine the cost of a launch. 

### Interactive Visual Analytics with Folium lab
<code>[lab_jupyter_launch_site_location.ipynb]</code>

Perform more interactive visual analytics using Folium

### Build an Interactive Dashboard with Ploty Dash
<code>[spacex-dash-app.py]</code>

<code>[helper_Plotly.py]</code>

<code>[SpaceY_Plotly_dashboard.jpg]</code>

Build a Plotly Dash application for users to perform interactive visual analytics on SpaceX launch data in
real-time

### Machine Learning Models
<code>[SpaceX_Machine Learning Prediction_Part_5.ipynb]</code>

Build, train, and evaluate a machine learning models to predict if SpaceX will reuse the first stage.

### Final Project Presentation
<code>[AM---ds-capstone-template-coursera.pdf]</code>
