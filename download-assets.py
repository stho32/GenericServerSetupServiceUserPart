import argparse
import os
import requests
import zipfile

# Parse the repository URL from the command line
parser = argparse.ArgumentParser()
parser.add_argument('repository_url', help='The URL of the repository')
args = parser.parse_args()
repository_url = args.repository_url

# Get the latest release information from the GitHub API
response = requests.get(f'{repository_url}/releases/latest')
release_info = response.json()

# Create a subdirectory for the attachments
attachment_dir = 'attachments'
os.makedirs(attachment_dir, exist_ok=True)

# Download each attachment and extract zip files
for asset in release_info['assets']:
    asset_url = asset['browser_download_url']
    asset_name = asset['name']
    print(f'Downloading {asset_name}...')

    # Download the asset
    response = requests.get(asset_url)
    open(f'{attachment_dir}/{asset_name}', 'wb').write(response.content)

    # Extract zip files
    if asset_name.endswith('.zip'):
        zip_file = zipfile.ZipFile(f'{attachment_dir}/{asset_name}')
        zip_dir = asset_name[:-4]
        os.makedirs(f'{attachment_dir}/{zip_dir}', exist_ok=True)
        zip_file.extractall(f'{attachment_dir}/{zip_dir}')
        zip_file.close()

print('Done!')
