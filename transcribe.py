import os
from music21 import*

def transcribe_lstm_sheet(file):
    mf = midi.MidiFile()
    mf.open(file)
    mf.read()
    mf.close()
    len(mf.tracks)
    s = midi.translate.midiFileToStream(mf)
    s.write(fp = 'transcribed/lstm_sheet', fmt = 'lily.png')

def transcribe_cnn_sheet(file):
    mf = midi.MidiFile()
    mf.open(file)
    mf.read()
    mf.close()
    len(mf.tracks)
    s = midi.translate.midiFileToStream(mf)
    s.write(fp='transcribed/cnn_sheet', fmt='lily.png')