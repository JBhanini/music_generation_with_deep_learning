import streamlit as st
import os
import base64
from lstm_generate import lstm_generate
from cnn_generate import cnn_generate

main_bg = 'images/beach.jpg'
main_bg_ext = ".jpg"

st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
    }}
   
    </style>
    """,
    unsafe_allow_html=True
)

def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
    return href

st.title("Music Generation with Deep Learning")
st.header("“If I were not a physicist, I would probably be a musician. I often think in music. I live my daydreams in music. I see my life in terms of music.” 〰 Albert Einstein")
#st.image('images/email-composer.jpg')

col1, col2 = st.beta_columns(2)

with col1:
    st.header("Long Short Term Memory")
    LSTM = st.button('Generate Music with LSTM model')

with col2:
    st.header("WaveNet Architecture")
    CNN = st.button('Generate Music with WaveNet')


with st.beta_container():
    if LSTM :
        st.header('Your generating using LSTM')
        st.write('Deets. for Geeks :)')
        st.write("LSTMs are a variation of Recurrent Neural Networks. Traditionally, RNNs are used to learn temporal dependencies in the data.  The general topology of a recurrent network is such that the output of the previous time step is fed as input to the next, allowing the network to learn the sequential dependencies in the data. With the help of their added memory (internal state), RNNs can process sequences of inputs. This makes them a great fit to tasks such as handwriting recognition or speech recognition")
        lstm_generate()
        st.image('transcribed/lstm_sheet.png')
        st.markdown(get_binary_file_downloader_html('transcribed/lstm_sheet.png', 'LSTM-sheet'), unsafe_allow_html=True)
        st.markdown(get_binary_file_downloader_html('lstm_generated.mid', 'LSTM-midi'), unsafe_allow_html=True)


with st.beta_container():
    if CNN:
        st.header('Your generating using CNN')
        st.write('Deets. for Geeks :)')
        st.write ('WaveNet is a variant of Convolutional Neural Networks which in turn are variants of Artificial Neural Networks. Defining a CNN is one or more convolutional layers called a convolution or convolutions   . In the context of a convolutional neural network, a convolution defines multiplying the input with a set of weights in this case called the Kernel or the filter.')
        cnn_generate()
        st.image('transcribed/cnn_sheet.png')
        st.markdown(get_binary_file_downloader_html('transcribed/cnn_sheet.png', 'CNN-sheet'), unsafe_allow_html=True)
        st.markdown(get_binary_file_downloader_html('cnn_generated.mid', 'CNN-midi'), unsafe_allow_html=True)


def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
    return href