import streamlit as st
from PIL import Image
import ast
import string
import re
import random

html_string = "<center><h1><span style='color:red'>2</span><span style='color:black'>0</span><span style='color:red'>2</span><span style='color:red'>2</span></h1>"
st.markdown(html_string, unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,10,1])

text_input = ""
search_button = ""
list_links = []
list_images = []
list_desc = []
with col2:
    text_input = st.text_input(" ")
    
    
if text_input:
     links = {}
     images = {}
     try:
         file = open("links.json","r",encoding='utf-8')
         list_links = file.readlines()
         file.close()
         file = open("images.json","r",encoding='utf-8')
         list_images = file.readlines()
         file.close()
         file = open("desc.json","r",encoding='utf-8')
         list_desc = file.readlines()
         file.close()         
     except Exception as er:
        st.warning("Database is empty")
        st.error(str(er))
     random.shuffle(list_desc)
     random.shuffle(list_images)
     random.shuffle(list_links)     
     chars = re.escape(string.punctuation)
     search_text_1 = re.sub(r'['+chars+']',' ',text_input)  
     search_text_2 = text_input
     results = []
     img_results = []
     for img in list_images:
        img_link = ast.literal_eval(img)
        for key in search_text_1.split(" "):
            if key in img_link:
                for result in img_link[key]:
                    count = 0
                    if result not in img_results:
                        img_results.append(result)
                    if count > 3:
                        break
                    count += 1    
        for key in search_text_2.split(" "):
            if key in img_link:
                for result in img_link[key]:
                    count = 0 
                    if result not in img_results:
                        img_results.append(result)  
                    if count > 3:
                        break
                    count += 1    
     for link in list_links:
         links = ast.literal_eval(link)
         for key in search_text_1.split(" "):
            if key in links:
                for result in links[key]:
                    count = 0
                    if result not in results:
                        results.append(result)
                    if count > 3:
                        break
                    count += 1    
         for key in search_text_2.split(" "):
            if key in links:
                for result in links[key]:
                    count = 0
                    if result not in results:
                        results.append(result)
                    if count > 3:
                        break
                    count += 1    
     result_cache = []           
     with col2:
         count = 0
         html_string = ""
         col_cnt = 0
         for result in img_results: 
            html_string += "<img width='160px' height='160px' src='"+result+"'>"
            col_cnt += 1
            if col_cnt == 3:
                html_string += "<br>"
                col_cnt = 0            
            if count > 10:
                break
            count += 1 
         st.markdown(html_string,unsafe_allow_html=True)   
         cnt = 0    
         for result in results:
                result = result.replace(" ","")                
                if cnt > 10:
                    break
                cnt += 1    
                if result not in result_cache:
                    result_cache.append(result)
                    st.markdown("<h3><a href='"+result+"'>"+result+"</a><h3>",unsafe_allow_html=True)
                    for descs in list_desc:
                        count = 0
                        desc = ast.literal_eval(descs)
                        if result in desc:                        
                            for text in desc[result]:
                                st.markdown(" "+text+" ",unsafe_allow_html=True)
                                count += 1
                                if count > 3:
                                    break
                        if count > 3:
                            break

   
     if len(results) == 0:
        st.info("No results found")