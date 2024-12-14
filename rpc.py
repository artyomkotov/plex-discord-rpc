from plexapi.server import PlexServer
from pypresence import Presence
import time

# Plex server details
PLEX_URL = 'http://your-plex-server-url:32400'  # Replace with your Plex server URL
PLEX_TOKEN = 'your-plex-token'  # Replace with your Plex token

# Discord RPC details
CLIENT_ID = 'your-discord-client-id'  # Replace with your Discord Client ID
RPC = Presence(CLIENT_ID)
RPC.connect()

# Initialize Plex server connection
plex = PlexServer(PLEX_URL, PLEX_TOKEN)

# Variable to keep track of the current track ID
current_track_id = None

def update_discord_rpc():
    """
    Updates the Discord Rich Presence (RPC) with the currently playing media
    from the Plex server. Clears the RPC if no media is playing or if media is paused.
    """
    global current_track_id
    sessions = plex.sessions()
    
    # Find the active session (the one that is currently playing)
    active_session = None
    for session in sessions:
        if session.players[0].state == 'playing':
            active_session = session
            break
    
    if active_session:
        media = active_session
        if media:
            # Check if track changed
            if current_track_id != media.ratingKey:
                current_track_id = media.ratingKey
                
                title = media.title
                artist = media.grandparentTitle or ''
                album = media.parentTitle or ''
                platform = media.players[0].platform or 'Unknown'
                
                # Determine the appropriate small image based on the platform
                platform_lower = platform.lower()
                if platform_lower == 'windows':
                    small_image = 'windows'
                elif platform_lower == 'android':
                    small_image = 'android'
                elif platform_lower == 'macos':
                    small_image = 'macos'
                elif platform_lower == 'linux':
                    small_image = 'linux'
                elif platform_lower == 'ios':
                    small_image = 'ios'
                else:
                    small_image = 'default'
                
                # Update Discord RPC
                RPC.update(
                    state=f"by {artist}",
                    details=title,
                    large_image="plexamp",
                    large_text=album,
                    small_image=small_image,
                    small_text=platform
                )
    else:
        # Clear the RPC if no media is playing or if media is paused
        if current_track_id is not None:
            RPC.clear()
            current_track_id = None

if __name__ == '__main__':
    while True:
        update_discord_rpc()
        time.sleep(5)  # Update every 5 seconds
