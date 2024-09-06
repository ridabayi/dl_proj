import os
from pathlib import Path
import logging 
""" Logging module provides a flexible event logging system. This can include tasks such as:
Logging events or errors in an application
Configuring logging levels, handlers, and formatters
Creating custom logging classes or functions """

#logging string
# Configure the basic logging settings
logging.basicConfig(
    # Set the logging level to INFO
    level=logging.INFO,
    
    # Set the format of the log messages
    format='%(asctime)s - %(levelname)s - %(message)s'
    # 
    # The format string uses placeholders to include information about the log event:
    #   %(asctime)s: The timestamp of the log event
    #   %(levelname)s: The logging level of the event (e.g., INFO, WARNING, etc.)
    #   %(message)s: The actual log message
)

# Define the project name
project_name = 'cnnClassifier'

# Define a list of files required for the project structure
list_of_files = [
    # GitHub workflows directory with a .gitkeep file to maintain the directory
    ".github/workflows/.gitkeep",
    
    # Project source directory with an __init__.py file to make it a package
    f"src/{project_name}/__init__.py",
    
    # Components directory within the project source with an __init__.py file
    f"src/{project_name}/components/__init__.py",
    
    # Utilities directory within the project source with an __init__.py file
    f"src/{project_name}/utils/__init__.py",
    
    # Configuration directory within the project source with an __init__.py file
    f"src/{project_name}/config/__init__.py",
    
    # Configuration file within the configuration directory
    f"src/{project_name}/config/configuration.py",
    
    # Pipeline directory within the project source with an __init__.py file
    f"src/{project_name}/pipeline/__init__.py",
    
    #
    f"src/{project_name}/entity/__init__.py",

    # Constants directory within the project source with an __init__.py file
    f"src/{project_name}/constants/__init__.py",
    
    # Project configuration file in YAML format
    "config/config.yaml",
    
    # Data Version Control (DVC) configuration file
    "dvc.yaml",
    
    # Parameters file in YAML format
    "params.yaml",
    
    # Requirements file for dependencies
    "requirements.txt",
    
    # Setup file for the project
    "setup.py",
    
    # Jupyter Notebook for trials and research
    "research/trials.ipynb",
    
    # Index HTML template
    "templates/index.html"
]

# Iterate over each file path in the list of files
for filepath in list_of_files:
    # Convert the file path to a Path object for easier manipulation
    filepath = Path(filepath)
    
    # Split the file path into the directory path and the file name
    filedir, filename = os.path.split(filepath)

    # If the directory path is not empty, create the directory if it doesn't exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        # Log the creation of the directory
        logging.info(f"Creating directory: {filedir} for the file: {filename}")
    
    # If the file does not exist or is empty, create a new empty file
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            # Create an empty file
            pass
            # Log the creation of the empty file
            logging.info(f"Creating empty file: {filepath}")

    # If the file already exists, log a message indicating that
    else:
        logging.info(f"{filename} already exists")

