# import os
# import yt_dlp as youtube_dl
# from config import VIDEO_DIR
# from utils import sanitize_filename

# def download_video(url, format="video"):
#     """Download a YouTube video or audio."""
#     try:
#         with youtube_dl.YoutubeDL({"quiet": True}) as ydl:
#             info = ydl.extract_info(url, download=False)
#             title = sanitize_filename(info.get("title", "video"))
#             output_file = f"{title}.mp4" if format == "video" else f"{title}.mp3"
#             output_path = os.path.join(VIDEO_DIR, output_file)

#         ydl_opts = {
#             "format": "best" if format == "video" else "bestaudio",
#             "outtmpl": output_path,
#             "quiet": False,
#         }

#         with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#             ydl.download([url])

#         return output_path, None  # No error

#     except Exception as e:
#         return None, str(e)  # Return error message


import os
import yt_dlp as youtube_dl
from config import VIDEO_DIR
from utils import sanitize_filename

def download_video(url, format="video"):
    """Download a YouTube video or audio while preserving the original title."""
    try:
        # Extract video info
        ydl_opts = {"quiet": True}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            title = info.get("title", "video")  # Get original title
            sanitized_title = sanitize_filename(title)  # Remove unsafe characters
            
            # Define file extensions
            file_ext = "mp4" if format == "video" else "mp3"
            output_file = f"{sanitized_title}.{file_ext}"
            output_path = os.path.join(VIDEO_DIR, output_file)

        # Download options
        ydl_opts = {
            "format": "best" if format == "video" else "bestaudio",
            "outtmpl": output_path,  # Save file with original title
            "quiet": False,
        }

        # Download video
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        return output_path, None  # No error

    except Exception as e:
        return None, str(e)  # Return error message
