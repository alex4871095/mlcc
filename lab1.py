#!/usr/bin/env python

import pandas as pd

city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
population = pd.Series([852469, 1015785, 485199])
square_miles = pd.Series([46.87, 176.53, 97.92])
cities = pd.DataFrame({ 'City name': city_names, 'Population': population, 'Square': square_miles})
cities['San_50'] = cities['City name'].str.startswith('San') & (cities['Square'] > 50)
cities

