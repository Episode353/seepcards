import os
import shutil
import urllib.request

def main():
    if os.path.exists("seepcards"):
        print("You already have seepcards!")
        print("Please delete the 'seepcards' folder before updating.")
        input("Press Enter to exit...")  # Wait for user confirmation before closing
    else:
        download_repo()
        input("Press Enter to exit...")  # Wait for user confirmation before closing

def download_repo():
    print("Downloading seepcards...")
    url = "https://github.com/Episode353/seepcards/archive/main.zip"
    zip_file = "seepcards-main.zip"
    urllib.request.urlretrieve(url, zip_file)

    print("Extracting seepcards...")
    shutil.unpack_archive(zip_file, ".")  # Extract directly into the current directory


    os.remove(zip_file)
    # Rename the extracted folder to "seepcards"
    os.rename("seepcards-main", "seepcards")
    print("seepcards downloaded successfully.")



if __name__ == "__main__":
    main()
# pyinstaller --onefile seepcard-updater.py