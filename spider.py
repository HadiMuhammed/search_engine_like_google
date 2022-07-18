#Created by Hadi Muhammed
import requests
from bs4 import BeautifulSoup
import os
import re 
import string
import random

urls = []
image = ""
proc_list = []
link_dic = {}
image_dic = {}
desc_dic = {}
count = 0 
links = []
for file_name in os.listdir("./"):
    if ".json" in file_name:
        file = open(file_name,"w",encoding='utf-8') 
        file.write("")
        file.close()
start_nodes = ["https://google.com","https://facebook.com","https://twitter.com","https://yahoo.com","https://wikipedia.com"]
def crawl(url):

    global link_dic,image_dic,desc_dic,image,urls,count,links
    if len(link_dic) > 0:
        file = open("links.json","a",encoding='utf-8')
        file.write(str(link_dic)+"\n")
        file.close()
    
    if len(image_dic) >0:
        file = open("images.json","a",encoding='utf-8')
        file.write(str(image_dic)+"\n")
        file.close()
        
    if len(desc_dic) >0:
        file = open("desc.json","a",encoding='utf-8')
        file.write(str(desc_dic)+"\n")
        file.close()
        
    link_dic = {}
    image_dic = {}
    desc_dic = {}
    
    try:
        if url.split("://")[1].split("/")[0] not in urls:
            urls.append(url.split("://")[1].split("/")[0])
            resp = requests.get(url,timeout=10)
            data = BeautifulSoup(resp.text,'lxml')
            links += data.findAll("a")
            images = data.findAll("img")
            main_headings = data.findAll("h1")            
            sub_headings = data.findAll("h2")
            sub_text = data.findAll("pre")
            main_descs = data.findAll("p")
            words_in_link = url.split("://")[1].split("/")
            chars = re.escape(string.punctuation)
            words_in_link2 = re.sub(r'['+chars+']',' ',url).split(" ")
            count += 1
            os.system("cls")
            print("Got "+str(count)+" unique websites")
            if url not in desc_dic:
                desc_dic[url] = []
            for main_heading in main_headings:    
                desc_dic[url].append(main_heading.text)
            for sub_heading in sub_headings:    
                desc_dic[url].append(sub_heading.text)
            for sub_tex in sub_text:
                desc_dic[url].append(sub_tex.text)
            for main_desc in main_descs:
                desc_dic[url].append(main_desc.text)
                
                
            for word in words_in_link2:
                if word not in link_dic:
                    link_dic[word] = []
                if url not in link_dic[word]:    
                    link_dic[word].append(url)
                for img in images:
                    try:
                        img_url = img['src']
                        if word not in image_dic:
                            image_dic[word] = []
                        if img_url not in image_dic[word]:
                            if "://" not in img_url:
                                img_url = url + "/" +img_url
                            image_dic[word].append(img_url)
                        img_words = img_url.split("://")[1].split("/")
                        for img_word in img_words:
                            if img_word not in image_dic:
                                image_dic[img_word] = []
                            if img_url not in image_dic[img_word]:
                                if "://" not in img_url:
                                    img_url = url + "/" +img_url
                                image_dic[img_word].append(img_url)                            
                    except:
                        pass 
            
            for word in words_in_link:
                if word not in link_dic:
                    link_dic[word] = []
                if url not in link_dic[word]:    
                    link_dic[word].append(url)
                for img in images:
                    try:
                        img_url = img['src']
                        if word not in image_dic:
                            image_dic[word] = []
                        if img_url not in image_dic[word]:
                            if "://" not in img_url:
                                    img_url = url + "/" +img_url
                            image_dic[word].append(img_url)
                        img_words = img_url.split("://")[1].split("/")
                        for img_word in img_words:
                            if img_word not in image_dic:
                                image_dic[img_word] = []
                            if img_url not in image_dic[img_word]:
                                if "://" not in img_url:
                                    img_url = url + "/" +img_url
                                image_dic[img_word].append(img_url)                            
                    except:
                        pass            


            for h1 in main_headings:
                #print(h1.text)
                for word in h1.text.split(" "):
                    if word not in link_dic:
                        link_dic[word] = []
                    if url not in link_dic[word]:    
                        link_dic[word].append(url)
                    for img in images:
                        try:
                            img_url = img['src']
                            if word not in image_dic:
                                image_dic[word] = []
                            if img_url not in image_dic[word]:
                                if "://" not in img_url:
                                    img_url = url + "/" +img_url
                                image_dic[word].append(img_url)
                        except:
                            pass

            for h2 in sub_headings:
                #print(h1.text)
                for word in h2.text.split(" "):
                    if word not in link_dic:
                        link_dic[word] = []
                    if url not in link_dic[word]:    
                        link_dic[word].append(url)
                    for img in images:
                        try:
                            img_url = img['src']
                            if word not in image_dic:
                                image_dic[word] = []
                            if img_url not in image_dic[word]:
                                if "://" not in img_url:
                                    img_url = url + "/" +img_url
                                image_dic[word].append(img_url)
                        except:
                            pass 
            for pre in sub_text:
                #print(h1.text)
                for word in pre.text.split(" "):
                    if word not in link_dic:
                        link_dic[word] = []
                    if url not in link_dic[word]:    
                        link_dic[word].append(url)
                    for img in images:
                        try:
                            img_url = img['src']
                            if word not in image_dic:
                                image_dic[word] = []
                            if img_url not in image_dic[word]:
                                if "://" not in img_url:
                                    img_url = url + "/" +img_url                        
                                image_dic[word].append(img_url)
                        except:
                            pass                             
                            
            for p in main_descs:
                #print(p.text)
                for word in p.text.split(" "):
                    if word not in link_dic:
                        link_dic[word] = []
                    if url not in link_dic[word]:    
                        link_dic[word].append(url)                 
                    for img in images:
                        try:
                            img_url = img['src']
                            if word not in image_dic:
                                image_dic[word] = []
                            if img_url not in image_dic[word]:
                                if "://" not in img_url:
                                    img_url = url + "/" +img_url
                                image_dic[word].append(img_url)
                        except:
                            pass

            link = links.pop(0)
            print("sites left:")
            print(len(links))
            try:
                    if link:                        
                        next_url = link['href']
                        if "://" not in link['href']:
                            next_url = url+"/"+link['href']
                                                
                        #if next_url.split("://")[1].split("/")[0] not in urls:
                        print("crawling to : "+next_url)
                        crawl(next_url)

            except Exception as er:
                    pass
 
        else:

            try:
                    link = links.pop(0)
                    print("sites left :")
                    print(len(links))            
                    if link:                        
                        next_url = link['href']
                        if "://" not in link['href']:
                            next_url = url+"/"+link['href']
                                                
                        #if next_url.split("://")[1].split("/")[0] not in urls:
                        print("crawling to : "+next_url)
                        crawl(next_url)

            except Exception as er:
                    pass  
        try:
            start = start_nodes.pop(0)
            print("start nodes left:")
            print(len(start_nodes))
            crawl(start)            
        except:
            pass
    except Exception as er:
            print(er)
    if len(links) > 1000:
        while len(links) > 1000:
            random.shuffle(links)
            links.pop(0)
    while len(links) != 0:
            try:
                    link = links.pop(0)
                    print("sites left:-")
                    print(len(links))            
                    if link:                        
                        next_url = link['href']
                        if "://" not in link['href']:
                            next_url = url+"/"+link['href']
                                                
                        #if next_url.split("://")[1].split("/")[0] not in urls:
                        print("crawling to : "+next_url)
                        crawl(next_url)

            except Exception as er:
                    pass          
#start_node = input("Enter a start node : ")
urls = []
start = start_nodes.pop(0)
print("start nodes left:")
print(len(start_nodes))
crawl(start)
