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

if st.checkbox('Show Earth Image🌎'):
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
