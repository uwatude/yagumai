from ast import increment_lineno
import streamlit as st
import time
from PIL import Image

st.title('This is for testings(^^)/')

st.write('Progress bar')
'Start!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Loading　☺ {i+1}％')
    bar.progress(i + 1)
    time.sleep(0.019)

'Completed!!!!!'

if st.checkbox('🌎Show Earth Image🌎'):
    img = Image.open('earth.jpg')
    st.image(img, caption='EARTH', use_column_width=True)

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字表示')
if button:
    right_column.write('ここは右カラム')

expander= st.expander('せんだ')
expander.write('ミツオ')
expander1= st.expander('那覇')
expander1.write('那覇！')


#df = pd.DataFrame({
#    '1列目': [1,2,3,4],
#    '2列目': [10,20,30,40]
#})



text = st.sidebar.text_input('What is your hobby？')
condition = st.sidebar.slider('あなたの調子は(%)', 0, 100, 50)


'← Answers from the left sidebar.'
'☺Your hobby is:', text
'調子:', condition, '%'

#option = st.selectbox(
#    'Your favorite number?',
#     list (range(1,11))
#)
#'Your favorite number is ', option, 'です。'

#if st.checkbox('Show Image'):
#   img = Image.open('PH.jpg')
#   st.image(img, caption='test', use_column_width=True)

#st.table(df.style.highlight_min(axis=0))
##最小数にハイライト##

#ef = pd.DataFrame(
#    np.random.rand(50,4),
#    columns=['a','b','c','d']
#)
#st.bar_chart(ef) 

##種類として、st.bar_chart,line_chart,area_chartがある＃＃


import os
from google.cloud import texttospeech

import io
import streamlit as st

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:\\Users\\Shota Uwabo\\secret.json'

def synthesize_speech(text, lang='English', gender='Neutral'):
  gender_type = {
      'Male':texttospeech.SsmlVoiceGender.MALE,
      'Female':texttospeech.SsmlVoiceGender.FEMALE,
      'Neutral':texttospeech.SsmlVoiceGender.NEUTRAL
  }
  
  lang_code = {
      'English': 'en-US',
      '日本語': 'ja-JP'
  }
  
  #lang = 'English'
  #gender = 'Neutral'
  #text = "Hello I'm John Thirdfield junior from Jacksonville Florida. Oh That' my super hero"
  
  client = texttospeech.TextToSpeechClient()
  
  
  synthesis_input = texttospeech.SynthesisInput(text=text)
      
  
  voice = texttospeech.VoiceSelectionParams(
      language_code=lang_code[lang], ssml_gender=gender_type[gender]
  )
  
  audio_config = texttospeech.AudioConfig(
      audio_encoding=texttospeech.AudioEncoding.MP3
  )
  
  response = client.synthesize_speech(
      input=synthesis_input, voice=voice, audio_config=audio_config
  )
  return response

st.title('Audio Output App')

st.markdown('### データ準備')

input_option = st.selectbox(
    'Select input data',
    ('Input directly', 'Text file')
)
input_data = None

if input_option == 'Input directly':
    input_data = st.text_area('Please input text here.', 'Hello, this is for testing.')
else:
    uploaded_file = st.file_uploader('Please upload a text file.', ['txt'])
    if uploaded_file is not None:
        content = uploaded_file.read()
        input_data = content.decode() 
        
if input_data is not None:
    st.write('入力されたデータ')
    st.write(input_data)
    st.markdown('### パラーメータ設定')
    st.subheader('Language & Speaker setting')

    lang = st.selectbox(
        'Please select the language',
        ('日本語','English')
    )
    gender = st.selectbox(
        'Please select the speaker',
        ('Neutral', 'Male', 'Female')
    )
    st.markdown('### 音声合成')
    st.write('Okay to proceed?')
    if st.button('Play♪'):
        comment = st.empty()
        comment.write('Start Playing')
        response = synthesize_speech(input_data, lang=lang, gender=gender)
        ##音声再生↓
        st.audio(response.audio_content)
        comment.write('Completed!!')



