import os
import openai
import io
#from PIL import Image
import PIL.Image
from tkinter import *
import urllib.request


def submit():
    label2 = Label(root, text="please wait while image is being generated")
    label2.pack()
    global prompt_data
    prompt_data = prompt_input.get()

    openai.api_key = 'put your API key here'    #put your API key inside quotes
    response = openai.Image.create(prompt=prompt_data,n=1,size="1024x1024")
    image_url = response['data'][0]['url']
   # image_url="https://media.istockphoto.com/id/1307189136/photo/gateway-of-india-mumbai-maharashtra-monument-landmark-famous-place-magnificent-view-without.jpg?b=1&s=170667a&w=0&k=20&c=BLP7ZQkbok5etYvEF3obeqaG-5Sv06_kaqPfS8z9CS4="
    urllib.request.urlretrieve(image_url,"new.jpeg")
    img = PIL.Image.open("new.jpeg")
    img.show()
    prompt_input.delete(0, END)                      #clears the input field


root = Tk()
label1=Label(root,text="Text to Image Generation Program ",bg="#d5e1df")
label1.pack()


prompt_input=Entry(root,width=69)
prompt_input.pack()


button1=Button(root,text="submit",padx=6,pady=3,command=submit,bg="#d5e1df")
button1.pack()

root.mainloop()
#second commit





