import streamlit as st
import time

st.title('This is for testings(^^)/')

st.write('Progress bar')
'Start!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Loading　☺ {i+1}％')
    bar.progress(i + 1)
    time.sleep(0.03)

'Completed!!!!!'

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

text = st.sidebar.text_input('あなたの趣味は？')
condition = st.sidebar.slider('あなたの調子は', 0, 100, 50)

'Your hobby is:', text
'調子:', condition


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


input()
