import sys
import os

path = sys.argv[1]

# Check if path exits
if os.path.exists(path):
    print("File exists")

    # Get filename
    print("filename : " + path.split("/")[-1])
