import numpy as np
import os
from music21 import converter, instrument, note, chord
from collections import Counter
from sklearn.model_selection import train_test_split


def read_midi(file):

    notes = []
    notes_to_parse = None

    midi = converter.parse(file)

    s2 = instrument.partitionByInstrument(midi)

    for part in s2.parts:

        if 'Piano' in str(part):

            notes_to_parse = part.recurse()

            # finding whether a particular element is note or a chord
            for element in notes_to_parse:
                if isinstance(element, note.Note):
                    notes.append(str(element.pitch))
                elif isinstance(element, chord.Chord):
                    notes.append('.'.join(str(n) for n in element.normalOrder))

    return np.array(notes)


path='data/medium_midi_dataset/'

#Reading each midi file and adding the notes to an array

files=[i for i in os.listdir(path) if i.endswith(".mid")]
notes_array = np.array([read_midi(path+i) for i in files])

#Getting only the unique notes and their frequencies

notes_ = [element for note_ in notes_array for element in note_]

unique_notes = list(set(notes_))

freq = dict(Counter(notes_))
frequent_notes = [note_ for note_, count in freq.items() if count>=50]

#Seggregating the most frequent notes

new_music = []

for notes in notes_array:
    temp = []
    for note_ in notes:
        if note_ in frequent_notes:
            temp.append(note_)
    new_music.append(temp)

new_music = np.array(new_music)

#Preaparing the input and output sequences for the network

no_of_timesteps = 32
x = []
y = []

for note_ in new_music:
    for i in range(0, len(note_) - no_of_timesteps, 1):
        # preparing input and output sequences
        input_ = note_[i:i + no_of_timesteps]
        output = note_[i + no_of_timesteps]

        x.append(input_)
        y.append(output)

x = np.array(x)
y = np.array(y)

#mapping notes to integers

unique_x = list(set(x.ravel()))
x_note_to_int = dict((note_, number) for number, note_ in enumerate(unique_x))

x_seq = []
for i in x:
    temp = []
    for j in i:
        temp.append(x_note_to_int[j])
    x_seq.append(temp)

x_seq = np.array(x_seq)

unique_y = list(set(y))
y_note_to_int = dict((note_, number) for number, note_ in enumerate(unique_y))

y_seq=np.array([y_note_to_int[i] for i in y])

#Splitting the data into test, train, and evaluation sets

x_tr, x_val, y_tr, y_val = train_test_split(x_seq,y_seq,test_size=0.2,random_state=0)

network_input = np.array(x_tr)
network_output = np.array(y_tr)
validation_data = (np.array(x_val), np.array(y_val))