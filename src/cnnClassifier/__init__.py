# Import necessary modules
import os  # for interacting with the operating system (e.g., creating directories)
import sys  # for accessing system-specific variables and functions (e.g., sys.stdout)
import logging  # for setting up the logging system

# Define a string format for logging messages
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
# This format includes:
#   %(asctime)s: the timestamp of the log message
#   %(levelname)s: the log level (e.g., INFO, WARNING, ERROR)
#   %(module)s: the name of the module that generated the log message
#   %(message)s: the actual log message

# Define the log directory and log file path
log_dir = "logs"  # directory where log files will be stored
log_filepath = os.path.join(log_dir, "running_logs.log")  # path to the log file
# Create the log directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)

# Configure the logging system
logging.basicConfig(
    # Set the log level to INFO
    level=logging.INFO,
    # Use the previously defined logging_str format for log messages
    format=logging_str,
    # Specify two handlers: one for writing to a file and one for writing to the console
    handlers=[
        # Write log messages to the file specified by log_filepath
        logging.FileHandler(log_filepath),
        # Write log messages to the console (sys.stdout)
        logging.StreamHandler(sys.stdout)
    ]
)

# Create a logger instance with the name cnnClassifierLogger
logger = logging.getLogger("cnnClassifierLogger")
# This logger can be used throughout the application to log messages