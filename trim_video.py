from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
ffmpeg_extract_subclip("cartoon.mp4", 0, 20, targetname="test.mp4")