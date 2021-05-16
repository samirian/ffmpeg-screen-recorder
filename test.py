from ffmpeg_screen_recorder import Screen_recorder
import time
from screeninfo import get_monitors


desktop_screen = get_monitors()[0]
resolution = f'{desktop_screen.width}x{desktop_screen.height}'
print(resolution)
# the resolution should match the input screen resolution
screen_recorder = Screen_recorder(resolution=resolution, input_screen='0', output_filename='record.mp4')
screen_recorder.start()
time.sleep(5)
screen_recorder.stop()