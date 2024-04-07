# Load necessary libraries
library(mongolite)
library(reticulate)
library(lubridate)

source_python("./functions/scrape_gas_prices.py")



scrape_gas_prices()
print("reloaded app")
# accessing Mongo DB database
conf <- config::get()

# Connect to MongoDB database and collection
gas_prices_collection <- mongo(collection = conf$table, db = conf$database, url = conf$connection_string)

# Retrieve all documents from the "gas_prices" collection
gas_prices_df <- gas_prices_collection$find('{}')

# Convert to R dataframe
today_dat <- today()
global_dat <- distinct(subset(as.data.frame(gas_prices_df), date == today_dat))
