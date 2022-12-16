#!/bin/bash
  
# Set the URL of the zip file to download
zip_url="https://github.com/stho32/LocalNetAppChat/releases/download/v1.6/lnac-server-linux-x64.zip"

# Set the name of the subdirectory to unzip the file into
subdir_name="lnac-server"

rm -rf $subdir_name

# Download the zip file
wget "$zip_url"

# Extract the zip file into the specified subdirectory
unzip -d "$subdir_name" "lnac-server-linux-x64.zip"

# Remove the zip file
rm "lnac-server-linux-x64.zip"

cd $subdir_name

chmod +x LocalNetAppChat.Server

ip_address=$(ip -4 addr show scope global | grep inet | awk '{print $2}' | cut -d/ -f1)

./LocalNetAppChat.Server --listenOn $ip_address --https --key somePassword
