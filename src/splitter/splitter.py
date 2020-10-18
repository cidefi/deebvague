#!/usr/bin/python

from pydub import AudioSegment
from pydub.silence import split_on_silence

def match_target_amplitude(aChunk, target_dBFS):
    ''' Normalize given audio chunk '''
    change_in_dBFS = target_dBFS - aChunk.dBFS
    return aChunk.apply_gain(change_in_dBFS)

inputFile = AudioSegment.from_mp3("demo.mp3")
audioChunks = split_on_silence (
    inputFile, 
    min_silence_len = 500,  # measured in ms
    silence_thresh = -40    # measured in dBFS
)

for i, chunk in enumerate(audioChunks):
    padding = AudioSegment.silent(duration=500)
    rawSegment = padding + chunk + padding
    normalizedSegment = match_target_amplitude(rawSegment, -20.0)

    # Export the audio chunk with new bitrate.
    print("Exporting segment{0}.mp3.".format(i))
    normalizedSegment.export(
        "./output/segment{0}.mp3".format(i),
        bitrate = "192k",
        format = "mp3"
    )
