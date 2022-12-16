#!/bin/bash

# Set the URL of the zip file to download
zip_url="http://example.com/path/to/zip/file.zip"

# Set the name of the subdirectory to unzip the file into
subdir_name="unzipped_files"

# Download the zip file
wget "$zip_url"

# Extract the zip file into the specified subdirectory
unzip -d "$subdir_name" "file.zip"

# Remove the zip file
rm "file.zip"
