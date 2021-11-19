# External packages
import time

# Internal packages
from scraper import set_interval, pipeline

# Constants
INTERVAL = 60 * 1 # 1 minute

# Functions
def main():
    """
    Launch the data extractor.
    """
    set_interval(pipeline, INTERVAL)

# Main
if __name__ == '__main__': 
    main()