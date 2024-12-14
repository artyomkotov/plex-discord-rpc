# Plex Discord Rich Presence

This script updates your Discord Rich Presence with the currently playing media from your Plex server. It shows the track title, artist, album, and the platform you are using (e.g., Windows, Android).

## Setup

### Prerequisites

- Python 3.x
- Plex server
- Discord application with Rich Presence enabled

### Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/artyomkotov/plex-discord-rpc.git
    cd plex-discord-rpc
    ```

2. Install the required Python packages:

    ```bash
    pip install plexapi pypresence
    ```

3. Upload the necessary images to your Discord application's assets:
    - `windows`: An image representing the Windows platform.
    - `macos`: An image representing the macOS platform.
    - `linux`: An image representing the Linux platform.
    - `ios`: An image representing the iOS platform.
    - `android`: An image representing the Android platform.
    - `plexamp`: An image representing the plexamp application.
    - `default`: A default image for other platforms.

### Configuration

1. Open the rpc.py file in a text editor.

2. Replace the placeholder values with your actual Plex server details and Discord Client ID:

    ```python
    # Plex server details
    PLEX_URL = 'http://your-plex-server-url:32400'  # Replace with your Plex server URL
    PLEX_TOKEN = 'your-plex-token'  # Replace with your Plex token

    # Discord RPC details
    CLIENT_ID = 'your-discord-client-id'  # Replace with your Discord Client ID
    ```

### Running the Script

Run the script using Python:

```bash
python rpc.py
