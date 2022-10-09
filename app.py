from tkinter import Y
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time

subscription_key = '4e909ea77e6d4d2f802b3c602f9cbd45'
endpoint = 'https://2022-yagumai.cognitiveservices.azure.com/'

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

def get_tags(filepath):
    local_image = open(filepath, "rb")

    # Call API with remote image
    tags_result = computervision_client.tag_image_in_stream(local_image)
    tags = tags_result.tags
    tags_name = []
    for tag in tags:
        tags_name.append(tag.name)
        
    return tags_name
    
def detect_objects(filepath):
    local_image = open(filepath, "rb")

    detect_objects_results = computervision_client.detect_objects_in_stream(local_image)
    objects = detect_objects_results.objects
    return objects

import streamlit as st
from PIL import ImageDraw
from PIL import ImageFont

st.title("物体検出App")

uploaded_file = st.file_uploader('Please choose an image...', type={'jpg','png'})
if uploaded_file is not None:
    img = Image.open(uploaded_file)
    #img_path = f'img/{uploaded_file.name}'
    #img.save(img_path)
    #objects = detect_objects(img_path)

    # 描画
    draw = ImageDraw.Draw(img)
    for object in objects:
        x = object.rectangle.x
        y = object.rectangle.y
        w = object.rectangle.w
        h = object.rectangle.h
        caption = object.object_property

    

        draw.rectangle([(x,y), (x+w, y+h)], fill=None, outline='orange', width=9)

    
    st.image(img)
    
    tags_name = get_tags(img_path)
    ptags_name = (', '.join(tags_name))
    st.markdown('**Detected content tag(s)**')
    st.markdown(f'> {tags_name}')
    
#############test

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
