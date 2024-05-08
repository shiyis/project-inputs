#!/bin/bash

# Set up the paths
SCRIPT_PATH="./script/tweet_archive.py"

# File path argument
FOLDER_PATH="$1"

if [ -z "$FOLDER_PATH" ]; then
    echo "Usage: $0 <folder_path>"
    exit 1
fi

# Check if the folder exists
if [ ! -d "$FOLDER_PATH" ]; then
    echo "Folder not found: $FOLDER_PATH"
    exit 1
fi

# Loop through files in the folder
for FILE_PATH in "$FOLDER_PATH"/*.csv
do
    echo "Processing file: $FILE_PATH"
    
    # Check if the file is empty
    if [ ! -s "$FILE_PATH" ]; then
        echo "File is empty: $FILE_PATH"
        continue
    fi
    
    echo "Extracting tweets for $FILE_PATH..."
    python3 "$SCRIPT_PATH" "$FILE_PATH" 
    echo "Tweets extracted for $FILE_PATH"

done
