import requests
import pandas as pd

# API endpoints
leipzig_url = "https://opendata.leipzig.de/api/3/action/package_list"
chemnitz_url = "https://hub.arcgis.com/api/search/v1/collections/all/items?filter=((group%20IN%20(69e2759993d642a4a39cfa7985863b50)))%20AND%20((tags%20IN%20(allgemein)))"

# Fetch data from Leipzig
leipzig_response = requests.get(leipzig_url)
leipzig_data = leipzig_response.json()

# Fetch data from Chemnitz
chemnitz_response = requests.get(chemnitz_url)
chemnitz_data = chemnitz_response.json()

# Print data to inspect the structure
print("Leipzig Data:", leipzig_data)
print("Chemnitz Data:", chemnitz_data)

