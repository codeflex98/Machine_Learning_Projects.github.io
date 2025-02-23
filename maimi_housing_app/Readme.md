# Miami Housing Prediction App

This project is an interactive web app that predicts the price of a property in Miami based on various features such as location, area, and other property details. The app is built using Streamlit, making it easy to use for anyone interested in estimating housing prices in Miami.

## Files

- **miami_housing_model**: This file contains the trained machine learning model used to predict the price of the property.
- **maimi_housing_app.py**: This file is the main Streamlit application that connects to the model and provides a user interface for input and prediction.
- **Miami_price_prediction_model.ipynb**: A Jupyter notebook containing the development of the housing price prediction model.
- **requirements.txt**: This file lists the required dependencies to run the app.

## Installation

To set up and run the app locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/miami-housing-prediction.git
   cd miami-housing-prediction
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## How to Run

1. Make sure that all dependencies are installed.
2. Run the Streamlit app:

   ```bash
   streamlit run maimi_housing_app.py
   ```

3. Open your browser and go to `http://localhost:8501` to access the app.

## Usage

The app allows you to enter various features related to the property you wish to estimate the price for. These features include:

- **Latitude** and **Longitude**: The location of the property.
- **Land Size**, **Living Area**, **Structure Quality**: Various details about the property.
- **Distances to key locations**: Like rail stations, the ocean, water bodies, and highways.
- **Other Property Attributes**: Including age of the property, month sold, and more.

After entering the values, click the "Awsome Price" button to get an estimated price for the property in US dollars.

## Example Inputs

- **Latitude**: Enter a value between -90.0 and 90.0.
- **Longitude**: Enter a value between -180.0 and 180.0.
- **Land Size** and **Living Area**: Enter the area values as numeric values (square feet).
- **Structure Quality**: Input the quality rating of the structure.

## Model Details

- The machine learning model is trained on housing data specific to Miami, predicting the price based on features like location, size, and property condition.
- The model is saved and loaded using `joblib` from the `miami_housing_model` file.

## Requirements

To run the app, you need the following Python packages:

- `streamlit`
- `joblib==1.3.2`
- `scikit-learn==1.3.1`

These dependencies are listed in the `requirements.txt` file.

## Contributing

Feel free to fork the repository and submit pull requests with any improvements or features.

## License

This project is open-source and available under the MIT License.
