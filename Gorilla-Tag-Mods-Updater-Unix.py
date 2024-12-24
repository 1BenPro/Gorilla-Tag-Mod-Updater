import os
import requests
import zipfile
import shutil
from getch import getch

def download_file(url, dest_path):
    response = requests.get(url, stream=True)
    with open(dest_path, "wb") as file:
        shutil.copyfileobj(response.raw, file)
    print(f"Downloaded: {dest_path}")

def extract_zip(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"Extracted: {zip_path} to {extract_to}")

def create_directories(game_path):
    dirs = [
        f"{game_path}/BepInEx/config",
        f"{game_path}/BepInEx/plugins",
        f"{game_path}/BepInEx/plugins/Utilla"
    ]
    for dir in dirs:
        os.makedirs(dir, exist_ok=True)
    print(f"Created directories: {', '.join(dirs)}")

def get_latest_plugin_url(api_url):
    response = requests.get(api_url)
    response.raise_for_status()  # Ensure we handle HTTP errors
    data = response.json()

    # Find the "assets" field in the API response
    if isinstance(data, dict) and "assets" in data:
        for asset in data["assets"]:
            if asset.get("name", "").endswith(".dll"):
                return asset.get("browser_download_url", "")
    return ""

def main():
    game_path = "C:/Program Files (x86)/Steam/steamapps/common/Gorilla Tag"

    # Step 1: Download BepInEx
    print("Downloading BepInEx...")
    download_file("https://github.com/BepInEx/BepInEx/releases/download/v5.4.23.2/BepInEx_win_x64_5.4.23.2.zip", "BPNX54232.zip")
    extract_zip("BPNX54232.zip", game_path)

    # Step 2: Create directories
    create_directories(game_path)

    # Step 3: Download BepInEx configuration
    print("Downloading BepInEx config...")
    download_file("https://pastebin.com/raw/rhr2Tani", f"{game_path}/BepInEx/config/BepInEx.cfg")

    # Step 5: Download Utilla.dll
    print("Downloading Utilla.dll...")
    plugin_url = get_latest_plugin_url(
        "https://api.github.com/repos/legoandmars/Utilla/releases/latest"
    )
    if plugin_url:
        download_file(plugin_url, f"Utilla.zip")
        extract_zip("Utilla.zip", game_path)
    else:
        print("Failed to get latest release of Utilla.")
        return
    return

# Downloading Legal Mod Menu #1
    print("Downloading Grate.dll...")
    plugin_url = get_latest_plugin_url(
        "https://api.github.com/repos/The-Graze/Grate/releases/latest"
    )
    if plugin_url:
        download_file(plugin_url, f"{game_path}/BepInEx/plugins/Grate.dll")
    else:
        print("Failed to get latest release of Grate.dll.")
        return

# Downloading Newtilla
    print("Downloading Newtilla.dll...")
    plugin_url = get_latest_plugin_url(
        "https://api.github.com/repos/Loafiat/Newtilla/releases/latest"
    )
    if plugin_url:
        download_file(plugin_url, f"{game_path}/BepInEx/plugins/Newtilla.dll")
    else:
        print("Failed to get latest release of Newtilla.dll.")
        return

    print("Finished downloading all plugins.")

    # Cleanup
    if os.path.exists("BPNX54232.zip"):
        os.remove("BPNX54232.zip")
        print("Deleted BPNX54232.zip")
    if os.path.exists("Utilla.zip")
        os.remove("Utilla.zip")
        print("Deleted Utilla.zip")

if __name__ == "__main__":
    main()


# For debugging in a workspace (DO NOT UNCOMMENT THE CODE BELOW AND RUN IT ON YOUR PHYSICAL COMPUTER)
# If you want to see what it does, you can uncomment it and run it in a controlled environment like "https://replit.com/" instead of a physical computer.
'''
kd = input("Delete installed files? (y/n): ")
if kd == "y":
    game_path = "C:/Program Files (x86)/Steam/steamapps/common/Gorilla Tag"
    shutil.rmtree(f"{game_path}/BepInEx/")
    print("Deleted folder 'BepInEx'")
    os.remove(f"{game_path}/.doorstop_version")
    print("Deleted '.doorstop_version'")
    os.remove(f"{game_path}/changelog.txt")
    print("Deleted 'changelog.txt'")
    os.remove(f"{game_path}/doorstop_config.ini")
    print("Deleted 'doorstop_config.ini'")
    os.remove(f"{game_path}/winhttp.dll")
    print("Deleted 'winhttp.dll'")
    print("Done!")
'''

print("Press any key to exit...")
getch()