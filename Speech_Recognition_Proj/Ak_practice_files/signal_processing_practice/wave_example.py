#Audio File formats
#.mp3
#.flac
#.wav

import wave

# Audio signal parameters:
# - number of channels
# - sample width
# - framerate/ sample_rate
# - number of frames
# - values of a frame

obj = wave.open("basic_output.wav","rb")
print("Number of channels: ", obj.getnchannels())
print("Sample Width: ", obj.getsampwidth())
print("Frame rate: ", obj.getframerate())
print("Number of frames: ", obj.getnframes())
print("Parameters: ", obj.getparams())

audio_duration = obj.getnframes() / obj.getframerate()
print("audio_duration: ", audio_duration)

frames = obj.readframes(-1)  # This line reads all frames from the audio file 
                             # into a bytes object and assigns it to the variable frames. The argument -1 
                             # indicates that it should read all frames until the end of the file.
print(type(frames), type(frames[0]))
print("Length of total frames: ", len(frames)," bytes")   #It's the total size of the audio data in bytes - 2 bytes each frame

# In digital audio, a sample refers to a single data point that represents the amplitude (loudness) of the
# audio signal at a specific point in time. It's a discrete measurement of the audio waveform at a particular moment.
# Sample width refers to the number of bits used to represent each sample in the digital audio file. 
# It determines the precision or resolution of each sample.

obj.close()

new_obj = wave.open("basic_output.wav","wb")
new_obj.setnchannels(1)
new_obj.setsampwidth(2)
new_obj.setframerate(18000.0)

new_obj.writeframes(frames)

new_obj.close()