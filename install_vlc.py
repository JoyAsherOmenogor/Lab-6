import requests
import hashlib
import subprocess
import os

def main():
    # Get the expected SHA-256 hash value of the VLC installer
    expected_sha256 = get_expected_sha256()

    # Download (but don't save) the VLC installer from the VLC website
    installer_data = download_installer()

    # Verify the integrity of the downloaded VLC installer by comparing the
    # expected and computed SHA-256 hash values
    if installer_ok(installer_data, expected_sha256):
        # Save the downloaded VLC installer to disk
        installer_path = save_installer(installer_data)

        # Silently run the VLC installer
        run_installer(installer_path)

        # Delete the VLC installer from disk
        delete_installer(installer_path)

def get_expected_sha256():
    """Downloads the text file containing the expected SHA-256 value for the VLC installer file from the
    videolan.org website and extracts the expected SHA-256 value from it.
    Returns:
        str: Expected SHA-256 hash value of VLC installer
    """
    # TODO: Step 1
    # Use the requests library to download the text file from the videolan.org website
    file_url = 'http://download.videolan.org/pub/videolan/vlc/3.0.17.4/win64/SHA256SUMS'
    response = requests.get(file_url)

    if response.status_code == requests.codes.ok:
        file_content = response.text
        # TODO: Extract the expected SHA-256 value from the text file content
        expected_sha256 =  = extract_file_value(file_content)
        return expected_sha256

def download_installer():
    """Downloads, but does not save, the .exe VLC installer file for 64-bit Windows.
    Returns:
        bytes: VLC installer file binary data
    """
    # TODO: Step 2
    # Use the requests library to download the VLC installer file
    file_url = resp_msg.text
    response = requests.get(file_url)

    if response.status_code == requests.codes.ok:
        installer_data = response.content
        return installer_data

def installer_ok(installer_data, expected_sha256):
    """Verifies the integrity of the downloaded VLC installer file by calculating its SHA-256 hash value
    and comparing it against the expected SHA-256 hash value.
    Args:
        installer_data (bytes): VLC installer file binary data
        expected_sha256 (str): Expected SHA-256 of the VLC installer
    Returns:
        bool: True if SHA-256 of VLC installer matches expected SHA-256. False if not.
    """
    # TODO: Step 3
    # Use the hashlib library to calculate the SHA-256 hash value of the installer_data
    computed_sha256 = hashlib.sha256(installer_data).hexdigest()

    # Compare the computed SHA-256 with the expected SHA-256
    return computed_sha256 == expected_sha256

def save_installer(installer_data):
    """Saves the VLC installer to a local directory.
    Args:
        installer_data (bytes): VLC installer file binary data
    Returns:
        str: Full path of the saved VLC installer file
    """
    # TODO: Step 4
    # Specify the path where you want to save the VLC installer file
    installer_path =  os.path.join(os.getenv('TEMP'), 'vlc-3.0.17.4-win64.exe')
    with open(installer_path, 'wb') as file:
        file.write(installer_data)
    return installer_path

def run_installer(installer_path):
    subprocess.run([installer_path, '/silent'])

def delete_installer(installer_path):
    os.remove(installer_path)

if __name__ == '__main__':
    main() 















    

