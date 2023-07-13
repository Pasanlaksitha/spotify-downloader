# Spotify Playlist Music Downloader
This script allows you to download music from a Spotify playlist by searching for the songs on YouTube and saving them as .mp3 files on your computer. It utilizes the following libraries: 
+ spotipy 
+ youtube_dl
+ youtubesearchpython.

## Prerequisites
Before using the script, you need to set up a Spotify developer account and obtain your client ID and client secret. Follow the steps below:

1. Go to Spotify Developer Dashboard and log in with your Spotify account.
2. Create a new application and fill in the required information.
3. Once your application is created, note down the Client ID and Client Secret.
## Installation
1. Clone this repository to your local machine or download the script file directly.
2. Install the required dependencies by running the following command: ```
```
pip install -r requirments.txt
```
## Configuration
when first luanch you can save your client id and clien secret with giving therminl input but if you need to update it Open the `configuration.ini` file and enter your Spotify `client ID` and `client secret` obtained from the Spotify Developer Dashboard.
Save and close the `configuration.ini` file.
## Usage
Run the script by executing the command 
```
python main.py
```
 in your terminal or command prompt.
The script will prompt you to enter the Spotify playlist link you want to download music from.
Provide the playlist link and press Enter.
The script will start searching for each track on YouTube, downloading the songs, and saving them as .mp3 files in the music folder.
Upon completion, a log file will be generated in the log folder, containing information about the downloaded files.
Note: The script assumes that you have valid internet connectivity and the required dependencies are installed.

Disclaimer
Please ensure that you have the necessary rights and permissions to download and use the music files. Downloading copyrighted material may infringe upon the rights of the content creators and may be illegal in some jurisdictions. Use this script responsibly and for personal use only.



__Feel free to customize and modify the script as per your requirements. Happy downloading!__