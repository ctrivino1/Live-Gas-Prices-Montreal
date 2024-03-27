#source("renv/activate.R")
env_name <- "mongo_db_py"

#Create the virtual environment 
reticulate::virtualenv_create(envname = env_name)

reticulate::virtualenv_install(env_name,
                                packages = c("numpy","pandas",'bs4','requests','pymongo'))  # <- Add other packages here, if needed
#
# Install the required Python packages within the virtual environment
reticulate::use_virtualenv(env_name, required = TRUE)

