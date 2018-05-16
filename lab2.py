#!/usr/bin/env python

import numpy as np
import pandas as pd

city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
population = pd.Series([852469, 1015785, 485199])
square_miles = pd.Series([46.87, 176.53, 97.92])
cities = pd.DataFrame({ 'City name': city_names, 'Population': population, 'Square': square_miles})
#cities
#cities.reindex([2, 0, 1])
cities.reindex(np.random.permutation(cities.index))

