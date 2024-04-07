library(tidyverse)
library(mongolite)

# Replace 'your_database_name' with the name of your MongoDB database
# Replace 'your_collection_name' with the name of your MongoDB collection
connection_string <- 'mongodb+srv://trivinochris124:Ihavethepower1!@cluster0.yl5qyo0.mongodb.net/sample_mflix?retryWrites=true&w=majority'

# Connect to MongoDB database and collection
gas_prices_collection <- mongo(collection = "gas_prices", db = "gas_prices_db", url = connection_string)

# Retrieve all documents from the "gas_prices" collection
gas_prices_df <- gas_prices_collection$find('{}')

# Convert to R dataframe
gas_prices <- as.data.frame(gas_prices_df)


