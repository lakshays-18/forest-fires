Algerian Forest Fire Prediction
This project aims to predict the occurrence of forest fires in the Bejaia region of Algeria using various meteorological and environmental features. The dataset contains information on forest fire occurrences along with different factors that influence fire behavior.

Dataset Overview
The dataset consists of 247 entries (rows) with multiple features (columns). The primary column, labeled "Bejaia Region Dataset", contains the key data used for analysis and predictions. The features include:

Date Information:

day: Day of the month.
month: Month of the year.
year: Year of the observation.
Weather Conditions:

Temperature: Temperature recorded on the given day (in °C).
RH (Relative Humidity): The percentage of relative humidity.
Ws (Wind Speed): Wind speed on the day of observation (in km/h or m/s).
Rain: Rainfall measured in millimeters (mm).
Fire Indicators:

FFMC (Fine Fuel Moisture Code): Moisture content of fine fuels like twigs and leaves.
DMC (Duff Moisture Code): Moisture content of decomposing organic matter.
DC (Drought Code): Moisture content of deep, compact organic layers.
ISI (Initial Spread Index): Indicates the potential for fire spread.
BUI (Build-Up Index): Measures the total amount of fuel available for combustion.
FWI (Fire Weather Index): A composite index indicating fire severity based on weather conditions.
Classes:

Classes: Labels representing whether a fire occurred, e.g., "fire" or "not fire."
Objective
The primary objective of this project is to predict the occurrence of forest fires based on the FWI (Fire Weather Index) value. The FWI is a critical indicator of fire severity and spread potential, which is used as a key feature for forecasting fire outbreaks.

Issues with the Dataset
The dataset contains some formatting issues that need to be addressed before analysis:

Columns might not be properly separated into a tabular format.
The dataset appears to have multi-indexing, which needs correction for easier analysis.
The data cleaning and reformatting process will be performed to ensure that the dataset is ready for use in predictive modeling.