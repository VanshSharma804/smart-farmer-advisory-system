# Smart Farmer Advisory System

A simple and user-friendly agriculture advisory web application built with Python and Streamlit.

The Smart Farmer Advisory System helps farmers get basic information and guidance about crops, irrigation, fertilizers, weather, crop calendars, common pests and diseases, and approximate yield estimation.

## Features

### 1. Crop Information
Provides basic information about different crops, including:

- Growing season
- Water requirement
- Suitable soil
- Temperature
- Harvest information
- Basic farming tips

The application supports multiple crops such as Wheat, Rice, Potato, Maize, Chana, Mustard, Sugarcane, Tomato, Onion, Cotton, Soybean and more.

### 2. Irrigation Advisory
Provides basic irrigation guidance based on:

- Selected crop
- Soil condition

The farmer can select the soil condition as:

- Dry
- Normal
- Wet

The system then provides simple irrigation advice.

### 3. Fertilizer Advisory
Provides basic fertilizer guidance according to:

- Selected crop
- Crop growth stage

The available stages are:

- Sowing / Planting
- Plant Growth
- Flowering / Fruit Development

The system explains the main nutrient requirement, why it is needed, and what the farmer should do.

### 4. Weather Information
Allows the user to enter a city and view current weather information such as:

- Temperature
- Feels-like temperature
- Humidity
- Weather condition
- Wind speed

Weather information is obtained through a weather API.

### 5. Crop Calendar
Provides a simple crop calendar showing information related to:

- Sowing
- Crop growth
- Harvest
- Monthly farming activities

This helps farmers understand important activities during the crop cycle.

### 6. Pest & Disease Guide
Provides information about common pests and diseases for different crops.

It includes:

- Common problems
- Symptoms to look for
- Basic prevention methods

This feature provides general information and does not diagnose a crop from an uploaded image.

### 7. Yield Estimator
Provides an approximate yield estimate using basic farm conditions such as:

- Crop
- Farm area
- Temperature
- Rainfall
- Soil type
- Fertilizer usage

The result includes:

- Estimated yield
- Total production
- Low / Medium / High yield status
- Explanation of the factors used

**Note:** This is a basic calculation-based estimate and is not a machine-learning prediction. Actual production may vary depending on seed quality, irrigation, pests, weather conditions and farming practices.

## Language Support

The application supports two languages:

- English
- Hindi

Users can select their preferred language from the language selector.

## Technologies Used

- Python
- Streamlit
- HTML
- CSS
- Requests
- Weather API

## Project Structure

```text
smart-farmer-advisory-system/
│
├── app.py
├── requirements.txt
├── README.md


## Installation

### 1. Clone the repository

~~~bash
git clone YOUR_GITHUB_REPOSITORY_URL
~~~

### 2. Open the project folder

~~~bash
cd smart-farmer-advisory-system
~~~

### 3. Install the required libraries

~~~bash
pip install -r requirements.txt
~~~

## Run the Application

Start the Streamlit application using:

~~~bash
streamlit run app.py
~~~

## Requirements

The project requires:

~~~text
streamlit
requests
~~~

These dependencies are also included in `requirements.txt`.

## How to Use

1. Open the application.
2. Select English or Hindi.
3. Choose one of the available services from the dashboard.
4. Enter or select the required information.
5. View the farming guidance or result.
6. Use the Back to Dashboard button to return to the main dashboard.

## Important Disclaimer

This application is designed as a basic educational agriculture advisory project.

The information provided is general guidance and should not be treated as a replacement for professional agricultural advice.

Farming decisions can depend on local soil conditions, weather, crop variety, irrigation facilities, pests, diseases and other factors.

For serious crop problems or major farming decisions, farmers should consult a local agriculture expert.

## Future Improvements

Possible future improvements include:

- More detailed crop recommendations
- More weather information
- Location-based weather services
- More crop diseases and prevention methods
- Improved yield estimation using real agricultural datasets
- Machine-learning based yield prediction
- Image-based pest and disease detection
- Database integration
- User accounts and farmer profiles

## Project Purpose

The main purpose of this project is to create a simple digital platform that provides useful agricultural information in an easy-to-understand format.

The project also demonstrates the use of Python, Streamlit, APIs, conditional logic, data handling and user-friendly web application development.

## Author

Developed as a BTech Computer Science Engineering mini project.
~~~
