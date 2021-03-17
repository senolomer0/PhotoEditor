import cv2
import time
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
import tkinter as tk
from tkinter import messagebox,filedialog
from tkinter.ttk import Combobox
import time
from PIL import ImageTk,Image
import os
from win32api import GetSystemMetrics
import turtle

class Editor():
    def __init__(self):
        super().__init__()
        self.main_screen = tk.Tk()
        self.main_screen.title("Photo Editor")
        self.main_screen.resizable(False,False)
        self.main_screen.config(bg="white")
        self.cal = 0
        self.screen_width = GetSystemMetrics(0)
        self.screen_height = GetSystemMetrics(1)
        self.sign = 0
        self.page()

    def get_image(self):
        if self.sign==0:
            self.turtle()
            self.sign += 1
            
        self.filename = filedialog.askopenfilename(initialdir="/Desktop", title="Select An Image", filetypes=(("image files", "*.jpg;*.png"),("image files", "*.jpeg")))
        if(len(self.filename)!=0):
            self.show_photo(self.filename)
        try:os.remove("modified_photo.jpg")
        except:pass

    def show_control(self):
        try:
            img = cv2.imread(self.filename)
            img.shape
            self.show_photo(self.filename)
            try:os.remove("modified_photo.jpg")
            except:pass
        except:
            try:self.warning.destroy()
            except:pass
            self.add_main_widget()
            self.warning = tk.Label(text="Please upload a photo first.",bg="white",fg="black",font="Arial 14")
            self.warning.place(x=520,y=380)

    def upload_control(self):
        try:
            img = cv2.imread(self.filename)
            img.shape
            try:os.remove("modified_photo.jpg")
            except:pass
            return 1
        except:
            try:self.warning.destroy()
            except:pass
            self.add_main_widget()
            self.warning = tk.Label(text="Please upload a photo first.",bg="white",fg="black",font="Arial 14")
            self.warning.place(x=520,y=380)
            return 0

    def delete_all_widget(self):
        try:self.signature.destroy()
        except:pass
        try:self.warning.destroy()
        except:pass
        try:self.image2_label.destroy()
        except:pass
        try:self.function_text.destroy()
        except:pass
        try:self.recommend.destroy()
        except:pass
        try:self.button1.destroy()
        except:pass
        try:self.button2.destroy()
        except:pass
        try:self.button3.destroy()
        except:pass
        try:self.button4.destroy()
        except:pass
        try:self.button5.destroy()
        except:pass
        try:self.title1.destroy()
        except:pass
        try:self.title2.destroy()
        except:pass
        try:self.title3.destroy()
        except:pass
        try:self.title4.destroy()
        except:pass
        try:self.title5.destroy()
        except:pass
        try:self.input1.destroy()
        except:pass
        try:self.input2.destroy()
        except:pass
        try:self.input3.destroy()
        except:pass
        try:self.input4.destroy()
        except:pass
        try:self.input5.destroy()
        except:pass
        try:self.combo1.destroy()
        except:pass
        try:self.combo2.destroy()
        except:pass
        try:self.combo3.destroy()
        except:pass
        try:self.radio1.destroy()
        except:pass
        try:self.radio2.destroy()
        except:pass
        try:self.radio3.destroy()
        except:pass
        try:self.radio4.destroy()
        except:pass

    def add_main_widget(self):
        self.delete_all_widget()
        self.title1 = tk.Label(text="Welcome",bg="white",fg="dark slate gray",font="Times 60")
        self.title1.place(x=485,y=70)

        self.title2 = tk.Label(text="To Photo Editor",bg="white",fg="black",font="Arial 20")
        self.title2.place(x=550,y=150)

        self.title3 = tk.Label(text="Please Upload First Photo",bg="white",fg="black",font="Arial 16")
        self.title3.place(x=520,y=300)

        self.button1 = tk.Button(text="Upload Photo",bg="dark slate gray",fg="white",font="Arial 12",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=self.get_image)
        self.button1.place(x=570,y=340,width =140,height=34)
        
        self.title4 = tk.Label(text="Ömer Şenol",bg="white",fg="gray",font="Arial 7")
        self.title4.place(x=935,y=587)

    def show_photo(self,image_url,function=0):
        def save_photo():
            if function==1:
                cv2.imwrite("resized_photo.jpg",img)
            elif function==2:
                cv2.imwrite("edited_photo.jpg",img)
            elif function==3:
                cv2.imwrite("combined_photo.jpg",img)
            elif function==4:
                cv2.imwrite("mixed_photos.jpg",img)
            elif function==5:
                cv2.imwrite("thresholding_photo.jpg",img)
            elif function==6:
                cv2.imwrite("blurring_photo.jpg",img)
            elif function==7:
                cv2.imwrite("noised_photo.jpg",img)
            elif function==8:
                cv2.imwrite("edited_photo.jpg",img)
            elif function==9:
                cv2.imwrite("gradient_photo.jpg",img)
            elif function==10:
                cv2.imwrite("gray_photo.jpg",img)
            elif function==11:
                cv2.imwrite("contrast_photo.jpg",img)
            
            self.warning = tk.Label(text="Photo saved.",bg="white",fg="red",font="Arial 16")
            self.warning.place(x=650,y=560)
        
        def back_to_function():
            if function==1:
                self.resize_image()
            elif function==2:
                self.add_figure_text()
            elif function==3:
                self.combine_image()
            elif function==4:
                self.mix_images()
            elif function==5:
                self.apply_threshold()
            elif function==6:
                self.blur_image()
            elif function==7:
                self.add_noise_image()
            elif function==8:
                self.morph_transform()
            elif function==9:
                self.gradient_detection()

        try:
            img = cv2.imread(image_url)
            original_size = img.shape
            self.delete_all_widget()

            if(function==0):
                if(original_size[0]<=490 and original_size[1]<=490) and (original_size[0]>=400 and original_size[1]>=400) and (original_size[0]!= original_size[1]):
                    self.main_screen.geometry("1000x605+"+str(int((self.screen_width-1000)/2))+"+"+str(int((self.screen_height-605)/2)))
                    load = Image.open(image_url)
                    self.img = ImageTk.PhotoImage(load)   
                    self.image_label = tk.Label(image=self.img,bg="white")
                    self.image_label.place(x=410,y=20)

                elif((original_size[0]<=400 or original_size[1]<=400) and (original_size[0]!= original_size[1])):
                    self.main_screen.geometry("1000x605+"+str(int((self.screen_width-1000)/2))+"+"+str(int((self.screen_height-605)/2)))
                    if(original_size[0]>original_size[1]):
                        ratio = original_size[0]/490
                        img_resized = cv2.resize(img,(int(img.shape[1]/ratio),490))
                        cv2.imwrite("modified_photo.jpg",img_resized)
                        load = Image.open("modified_photo.jpg")
                        self.img = ImageTk.PhotoImage(load)   
                        self.image_label = tk.Label(image=self.img,bg="white")
                        self.image_label.place(x=410,y=20)
                    else:
                        ratio = original_size[1]/490
                        img_resized = cv2.resize(img,(490,int(img.shape[0]/ratio)))
                        cv2.imwrite("modified_photo.jpg",img_resized)
                        load = Image.open("modified_photo.jpg")
                        self.img = ImageTk.PhotoImage(load)   
                        self.image_label = tk.Label(image=self.img,bg="white")
                        self.image_label.place(x=410,y=20)

                elif((original_size[0]>490 or original_size[1]>490) and (original_size[1]>original_size[0]) and (original_size[0]!= original_size[1])):
                    self.main_screen.geometry("1300x605+"+str(int((self.screen_width-1300)/2))+"+"+str(int((self.screen_height-605)/2)))
                    ratio = original_size[1]/800
                    img_resized = cv2.resize(img,(800,int(original_size[0]/ratio)))
                    if(img_resized.shape[0]>490):
                        img_resized = cv2.resize(img,(800,490))
                    cv2.imwrite("modified_photo.jpg",img_resized)
                    load = Image.open("modified_photo.jpg")
                    self.img = ImageTk.PhotoImage(load)   
                    self.image_label = tk.Label(image=self.img,bg="white")
                    self.image_label.place(x=410,y=20)

                elif((original_size[0]>490 or original_size[1]>490) and (original_size[1]<original_size[0]) and (original_size[0]!= original_size[1])):
                    self.main_screen.geometry("1000x605+"+str(int((self.screen_width-1000)/2))+"+"+str(int((self.screen_height-605)/2)))
                    ratio = original_size[0]/490
                    img_resized = cv2.resize(img,(int(original_size[1]/ratio),490))
                    if(img_resized.shape[1]>490):
                        img_resized = cv2.resize(img,(490,490))
                    cv2.imwrite("modified_photo.jpg",img_resized)
                    load = Image.open("modified_photo.jpg")
                    self.img = ImageTk.PhotoImage(load)   
                    self.image_label = tk.Label(image=self.img,bg="white")
                    self.image_label.place(x=410,y=20)

                elif(original_size[0] == original_size[1]):
                    self.main_screen.geometry("1000x605+"+str(int((self.screen_width-1000)/2))+"+"+str(int((self.screen_height-605)/2)))
                    img_resized = cv2.resize(img,(490,490))
                    cv2.imwrite("modified_photo.jpg",img_resized)
                    load = Image.open("modified_photo.jpg")
                    self.img = ImageTk.PhotoImage(load)   
                    self.image_label = tk.Label(image=self.img,bg="white")
                    self.image_label.place(x=410,y=20)

            if(function==1):
                if(original_size[0]<=490 and original_size[1]<=490):
                    self.main_screen.geometry("1000x605+"+str(int((self.screen_width-1000)/2))+"+"+str(int((self.screen_height-605)/2)))
                    load = Image.open(image_url)
                    self.img = ImageTk.PhotoImage(load)   
                    self.image_label = tk.Label(image=self.img,bg="white")
                    self.image_label.place(x=410,y=20)

                elif((original_size[0]>490 or original_size[1]>490) and (original_size[1]>original_size[0]) and (original_size[0]!= original_size[1])):
                    self.main_screen.geometry("1300x605+"+str(int((self.screen_width-1300)/2))+"+"+str(int((self.screen_height-605)/2)))
                    ratio = original_size[1]/800
                    img_resized = cv2.resize(img,(800,int(original_size[0]/ratio)))
                    if(img_resized.shape[0]>490):
                        img_resized = cv2.resize(img,(800,490))
                    cv2.imwrite("modified_photo.jpg",img_resized)
                    load = Image.open("modified_photo.jpg")
                    self.img = ImageTk.PhotoImage(load)   
                    self.image_label = tk.Label(image=self.img,bg="white")
                    self.image_label.place(x=410,y=20)

                elif((original_size[0]>490 or original_size[1]>490) and (original_size[1]<original_size[0]) and (original_size[0]!= original_size[1])):
                    self.main_screen.geometry("1000x605+"+str(int((self.screen_width-1000)/2))+"+"+str(int((self.screen_height-605)/2)))
                    ratio = original_size[0]/490
                    img_resized = cv2.resize(img,(int(original_size[1]/ratio),490))
                    if(img_resized.shape[1]>490):
                        img_resized = cv2.resize(img,(490,490))
                    cv2.imwrite("modified_photo.jpg",img_resized)
                    load = Image.open("modified_photo.jpg")
                    self.img = ImageTk.PhotoImage(load)   
                    self.image_label = tk.Label(image=self.img,bg="white")
                    self.image_label.place(x=410,y=20)

                elif(original_size[0] == original_size[1]):
                    self.main_screen.geometry("1000x605+"+str(int((self.screen_width-1000)/2))+"+"+str(int((self.screen_height-605)/2)))
                    img_resized = cv2.resize(img,(490,490))
                    cv2.imwrite("modified_photo.jpg",img_resized)
                    load = Image.open("modified_photo.jpg")
                    self.img = ImageTk.PhotoImage(load)   
                    self.image_label = tk.Label(image=self.img,bg="white")
                    self.image_label.place(x=410,y=20)

                if "1300" in str(self.main_screen.geometry()):
                    self.button1 = tk.Button(text="Save Photo",bg="dark slate gray",fg="white",font="Arial 14",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=save_photo)
                    self.button1.place(x=1100,y=560,width =180,height=37)
                    self.button2 = tk.Button(text="Back",bg="dark slate gray",fg="white",font="Arial 14",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=back_to_function)
                    self.button2.place(x=1100,y=518,width =180,height=37)

                elif "1000" in str(self.main_screen.geometry()):
                    self.button1 = tk.Button(text="Save Photo",bg="dark slate gray",fg="white",font="Arial 14",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=save_photo)
                    self.button1.place(x=800,y=560,width =180,height=37)
                    self.button2 = tk.Button(text="Back",bg="dark slate gray",fg="white",font="Arial 14",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=back_to_function)
                    self.button2.place(x=800,y=518,width =180,height=37)
            
            if(function==2 or function==3 or function==4 or function==5 or function==6 or function==7 or function==8 or function==9):
                if(original_size[0]<=490 and original_size[1]<=490) and (original_size[0]>=400 and original_size[1]>=400) and (original_size[0]!= original_size[1]):
                    self.main_screen.geometry("1000x605+"+str(int((self.screen_width-1000)/2))+"+"+str(int((self.screen_height-605)/2)))
                    load = Image.open(image_url)
                    self.img = ImageTk.PhotoImage(load)   
                    self.image_label = tk.Label(image=self.img,bg="white")
                    self.image_label.place(x=410,y=20)

                elif((original_size[0]<=400 or original_size[1]<=400) and (original_size[0]!= original_size[1])):
                    self.main_screen.geometry("1000x605+"+str(int((self.screen_width-1000)/2))+"+"+str(int((self.screen_height-605)/2)))
                    if(original_size[0]>original_size[1]):
                        ratio = original_size[0]/490
                        img_resized = cv2.resize(img,(int(img.shape[1]/ratio),490))
                        cv2.imwrite("modified_photo.jpg",img_resized)
                        load = Image.open("modified_photo.jpg")
                        self.img = ImageTk.PhotoImage(load)   
                        self.image_label = tk.Label(image=self.img,bg="white")
                        self.image_label.place(x=410,y=20)
                    else:
                        ratio = original_size[1]/490
                        img_resized = cv2.resize(img,(490,int(img.shape[0]/ratio)))
                        cv2.imwrite("modified_photo.jpg",img_resized)
                        load = Image.open("modified_photo.jpg")
                        self.img = ImageTk.PhotoImage(load)   
                        self.image_label = tk.Label(image=self.img,bg="white")
                        self.image_label.place(x=410,y=20)

                elif((original_size[0]>490 or original_size[1]>490) and (original_size[1]>original_size[0]) and (original_size[0]!= original_size[1])):
                    self.main_screen.geometry("1300x605+"+str(int((self.screen_width-1300)/2))+"+"+str(int((self.screen_height-605)/2)))
                    ratio = original_size[1]/800
                    img_resized = cv2.resize(img,(800,int(original_size[0]/ratio)))
                    if(img_resized.shape[0]>490):
                        img_resized = cv2.resize(img,(800,490))
                    cv2.imwrite("modified_photo.jpg",img_resized)
                    load = Image.open("modified_photo.jpg")
                    self.img = ImageTk.PhotoImage(load)   
                    self.image_label = tk.Label(image=self.img,bg="white")
                    self.image_label.place(x=410,y=20)

                elif((original_size[0]>490 or original_size[1]>490) and (original_size[1]<original_size[0]) and (original_size[0]!= original_size[1])):
                    self.main_screen.geometry("1000x605+"+str(int((self.screen_width-1000)/2))+"+"+str(int((self.screen_height-605)/2)))
                    ratio = original_size[0]/490
                    img_resized = cv2.resize(img,(int(original_size[1]/ratio),490))
                    if(img_resized.shape[1]>490):
                        img_resized = cv2.resize(img,(490,490))
                    cv2.imwrite("modified_photo.jpg",img_resized)
                    load = Image.open("modified_photo.jpg")
                    self.img = ImageTk.PhotoImage(load)   
                    self.image_label = tk.Label(image=self.img,bg="white")
                    self.image_label.place(x=410,y=20)

                elif(original_size[0] == original_size[1]):
                    self.main_screen.geometry("1000x605+"+str(int((self.screen_width-1000)/2))+"+"+str(int((self.screen_height-605)/2)))
                    img_resized = cv2.resize(img,(490,490))
                    cv2.imwrite("modified_photo.jpg",img_resized)
                    load = Image.open("modified_photo.jpg")
                    self.img = ImageTk.PhotoImage(load)   
                    self.image_label = tk.Label(image=self.img,bg="white")
                    self.image_label.place(x=410,y=20)

                if "1300" in str(self.main_screen.geometry()):
                    self.button1 = tk.Button(text="Save Photo",bg="dark slate gray",fg="white",font="Arial 14",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=save_photo)
                    self.button1.place(x=1100,y=560,width =180,height=37)
                    self.button2 = tk.Button(text="Back",bg="dark slate gray",fg="white",font="Arial 14",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=back_to_function)
                    self.button2.place(x=1100,y=518,width =180,height=37)

                elif "1000" in str(self.main_screen.geometry()):
                    self.button1 = tk.Button(text="Save Photo",bg="dark slate gray",fg="white",font="Arial 14",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=save_photo)
                    self.button1.place(x=800,y=560,width =180,height=37)
                    self.button2 = tk.Button(text="Back",bg="dark slate gray",fg="white",font="Arial 14",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=back_to_function)
                    self.button2.place(x=800,y=518,width =180,height=37)

            if(function==10 or function==11):
                if(original_size[0]<=490 and original_size[1]<=490) and (original_size[0]>=400 and original_size[1]>=400) and (original_size[0]!= original_size[1]):
                    self.main_screen.geometry("1000x605+"+str(int((self.screen_width-1000)/2))+"+"+str(int((self.screen_height-605)/2)))
                    load = Image.open(image_url)
                    self.img = ImageTk.PhotoImage(load)   
                    self.image_label = tk.Label(image=self.img,bg="white")
                    self.image_label.place(x=410,y=20)

                elif((original_size[0]<=400 or original_size[1]<=400) and (original_size[0]!= original_size[1])):
                    self.main_screen.geometry("1000x605+"+str(int((self.screen_width-1000)/2))+"+"+str(int((self.screen_height-605)/2)))
                    if(original_size[0]>original_size[1]):
                        ratio = original_size[0]/490
                        img_resized = cv2.resize(img,(int(img.shape[1]/ratio),490))
                        cv2.imwrite("modified_photo.jpg",img_resized)
                        load = Image.open("modified_photo.jpg")
                        self.img = ImageTk.PhotoImage(load)   
                        self.image_label = tk.Label(image=self.img,bg="white")
                        self.image_label.place(x=410,y=20)
                    else:
                        ratio = original_size[1]/490
                        img_resized = cv2.resize(img,(490,int(img.shape[0]/ratio)))
                        cv2.imwrite("modified_photo.jpg",img_resized)
                        load = Image.open("modified_photo.jpg")
                        self.img = ImageTk.PhotoImage(load)   
                        self.image_label = tk.Label(image=self.img,bg="white")
                        self.image_label.place(x=410,y=20)

                elif((original_size[0]>490 or original_size[1]>490) and (original_size[1]>original_size[0]) and (original_size[0]!= original_size[1])):
                    self.main_screen.geometry("1300x605+"+str(int((self.screen_width-1300)/2))+"+"+str(int((self.screen_height-605)/2)))
                    ratio = original_size[1]/800
                    img_resized = cv2.resize(img,(800,int(original_size[0]/ratio)))
                    if(img_resized.shape[0]>490):
                        img_resized = cv2.resize(img,(800,490))
                    cv2.imwrite("modified_photo.jpg",img_resized)
                    load = Image.open("modified_photo.jpg")
                    self.img = ImageTk.PhotoImage(load)   
                    self.image_label = tk.Label(image=self.img,bg="white")
                    self.image_label.place(x=410,y=20)

                elif((original_size[0]>490 or original_size[1]>490) and (original_size[1]<original_size[0]) and (original_size[0]!= original_size[1])):
                    self.main_screen.geometry("1000x605+"+str(int((self.screen_width-1000)/2))+"+"+str(int((self.screen_height-605)/2)))
                    ratio = original_size[0]/490
                    img_resized = cv2.resize(img,(int(original_size[1]/ratio),490))
                    if(img_resized.shape[1]>490):
                        img_resized = cv2.resize(img,(490,490))
                    cv2.imwrite("modified_photo.jpg",img_resized)
                    load = Image.open("modified_photo.jpg")
                    self.img = ImageTk.PhotoImage(load)   
                    self.image_label = tk.Label(image=self.img,bg="white")
                    self.image_label.place(x=410,y=20)

                elif(original_size[0] == original_size[1]):
                    self.main_screen.geometry("1000x605+"+str(int((self.screen_width-1000)/2))+"+"+str(int((self.screen_height-605)/2)))
                    img_resized = cv2.resize(img,(490,490))
                    cv2.imwrite("modified_photo.jpg",img_resized)
                    load = Image.open("modified_photo.jpg")
                    self.img = ImageTk.PhotoImage(load)   
                    self.image_label = tk.Label(image=self.img,bg="white")
                    self.image_label.place(x=410,y=20)
        
                if "1300" in str(self.main_screen.geometry()):
                    self.button1 = tk.Button(text="Save Photo",bg="dark slate gray",fg="white",font="Arial 14",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=save_photo)
                    self.button1.place(x=1100,y=560,width =180,height=37)

                elif "1000" in str(self.main_screen.geometry()):
                    self.button1 = tk.Button(text="Save Photo",bg="dark slate gray",fg="white",font="Arial 14",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=save_photo)
                    self.button1.place(x=800,y=560,width =180,height=37)

            try:
                self.title1 = tk.Label(text="Original Size: ({},{})\nShown Size: ({},{})".format(original_size[1],original_size[0],img_resized.shape[1],img_resized.shape[0]),bg="white",fg="black",font="Arial 16")
                self.title1.place(x=350,y=520)
            except:
                self.title1 = tk.Label(text="Original Size: ({},{})\nShown Size: ({},{})".format(original_size[1],original_size[0],img.shape[1],img.shape[0]),bg="white",fg="black",font="Arial 16")
                self.title1.place(x=350,y=520)
                    
        except:
            try:
                self.image_label
                try:self.button1.destroy()
                except:pass
                if "1300" in self.main_screen.geometry():
                    self.warning = tk.Label(text="Photo could not be uploaded.\nPlease try again.",bg="white",fg="black",font="Arial 16")
                    self.warning.place(x=800,y=520)  
                elif "1000" in self.main_screen.geometry(): 
                    self.warning = tk.Label(text="Photo could not be uploaded.\nPlease try again.",bg="white",fg="black",font="Arial 16")
                    self.warning.place(x=630,y=520)
            except:
                self.warning = tk.Label(text="Photo could not be uploaded.\nPlease try again.",bg="white",fg="black",font="Arial 14")
                self.warning.place(x=520,y=380) 

        try:os.remove("modified_photo.jpg")
        except:pass

    def black_and_white(self):
        control = self.upload_control()
        if control ==1: 
            self.delete_all_widget()
            self.img = cv2.imread(self.filename,0)
            cv2.imwrite("modified_photo.jpg",self.img)
            self.show_photo("modified_photo.jpg",10)

    def resize_image(self):
        self.cal =0

        def calculate():
            try:
                if(int(self.old_width) != int(self.width.get())):
                    self.height.set(str(int(int(self.width.get())/self.ratio)))
                    self.old_width = int(self.width.get())
                    self.old_height = int(self.height.get())
                elif(int(self.old_height) != int(self.height.get())):
                    pass
            except:
                if(len(self.width.get())==0 and len(self.height.get())==0):
                    self.height.set("0")
                    self.width.set("0")
            if(self.cal==0):
                self.main_screen.after(100,calculate)

        def apply():
            self.warning.config(text="")
            self.cal +=1
            if(int(self.width.get())>3840 or int(self.height.get())>3840):
                self.warning.config(text="The maximum value can be\n (3840x3840)")
                self.cal =0
                calculate()
            elif(int(self.width.get())<10 or int(self.height.get())<10):
                self.warning.config(text="The minimum value can be\n (10x10)")
                self.cal =0
                calculate()
            else:
                self.warning.config(text="")
                img_resized = cv2.resize(self.img,(int(self.width.get()),int(self.height.get())))
                cv2.imwrite("modified_photo.jpg",img_resized)
                self.show_photo("modified_photo.jpg",1)

        def reset():
            self.height.set(str(original_size[0]))
            self.width.set(str(original_size[1]))

        control = self.upload_control()
        if control ==1: 
            self.delete_all_widget()
            self.main_screen.geometry("1000x605+"+str(int((self.screen_width-1000)/2))+"+"+str(int((self.screen_height-605)/2)))
            self.function_text = tk.Label(text="Image Resize",bg="white",fg="dark slate gray",font="Times 50")
            self.function_text.place(x=420,y=80)
            self.img = cv2.imread(self.filename)
            original_size = self.img.shape
            self.old_width = original_size[1]
            self.old_height = original_size[0]
            self.ratio = original_size[1]/original_size[0]
            self.title1 = tk.Label(text="Original Size = ({},{})".format(original_size[1],original_size[0]),bg="white",fg="black",font="Arial 16")
            self.title1.place(x=470,y=220)
            self.title2 = tk.Label(text="""\n\nNew Size =            x""",bg="white",fg="black",font="Arial 16")
            self.title2.place(x=470,y=250)
            
            self.width = tk.StringVar(value=original_size[1])
            self.height = tk.StringVar(value=original_size[0])

            self.input1 = tk.Entry(fg ="black",bg="white",textvariable=self.width,font="Times 15")
            self.input1.place(x=593,y=300,width=52) 
            self.input2 = tk.Entry(fg ="black",bg="white",textvariable=self.height,font="Times 15")
            self.input2.place(x=667,y=300,width=52)

            self.button1 = tk.Button(text="Reset",bg="dark slate gray",fg="white",font="Arial 13",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=reset)
            self.button1.place(x=490,y=350,width =100,height=30)
            self.button2 = tk.Button(text="Apply",bg="dark slate gray",fg="white",font="Arial 13",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=apply)
            self.button2.place(x=610,y=350,width =100,height=30)

            self.warning = tk.Label(text="",bg="white",fg="black",font="Arial 14")
            self.warning.place(x=470,y=400)

            calculate()

    def add_figure_text(self):
        def color_rgb_code(selected_color):
            if(selected_color == "Black"):
                return (0,0,0)
            elif(selected_color == "Gray"):
                return (128,128,128)
            elif(selected_color == "White"):
                return (255,255,255)
            elif(selected_color == "Red"):
                return (0,0,255)
            elif(selected_color == "Orange"):
                return (0,165,255)
            elif(selected_color == "Yellow"):
                return (0,255,255)
            elif(selected_color == "Green"):
                return (0,255,0)
            elif(selected_color == "Blue"):
                return (255,0,0)
            elif(selected_color == "Purple"):
                return (128,0,128)
            elif(selected_color == "Pink"):
                return (203,192,255)

        def font_code(selected_font): 
            if(selected_font == "SIMPLEX"):
                return cv2.FONT_HERSHEY_SIMPLEX
            elif(selected_font == "PLAIN"):
                return cv2.FONT_HERSHEY_PLAIN
            elif(selected_font == "DUPLEX"):
                return cv2.FONT_HERSHEY_DUPLEX
            elif(selected_font == "COMPLEX"):
                return cv2.FONT_HERSHEY_COMPLEX
            elif(selected_font == "COMPLEX SMALL"):
                return cv2.FONT_HERSHEY_COMPLEX_SMALL
            elif(selected_font == "TRIPLEX"):
                return cv2.FONT_HERSHEY_TRIPLEX
            elif(selected_font == "SCRIPT SIMPLEX"):
                return cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
            elif(selected_font == "SCRIPT COMPLEX"):
                return cv2.FONT_HERSHEY_SCRIPT_COMPLEX

        def back():
            self.add_figure_text()

        def add_line():
            def apply_line():
                rgb = color_rgb_code(self.line_color.get())

                try:
                    x_start = int(self.x_start.get())
                    y_start = int(self.y_start.get())
                    x_end = int(self.x_end.get())
                    y_end = int(self.y_end.get())

                    try:
                        thickness = int(self.thickness.get())                    
                    except:
                        if(len(self.thickness.get())== 0):
                            self.warning.config(text="Thickness should not be empty.\nDefault = 1.")
                        else:
                            self.warning.config(text="Just enter numbers.")
                    
                    if(x_start<0 or y_start<0 or x_end<0 or y_end<0 or thickness<0):
                        self.warning.config(text="Please enter positive number.")

                    else:
                        img_add_line = cv2.line(self.img,(x_start,y_start),(x_end,y_end),rgb,thickness)
                        cv2.imwrite("modified_photo.jpg",img_add_line)
                        self.show_photo("modified_photo.jpg",2)

                except:
                    self.warning.config(text="Just enter numbers.")

            self.delete_all_widget()
            self.function_text = tk.Label(text="Add Line To Photo",bg="white",fg="dark slate gray",font="Times 45")
            self.function_text.place(x=420,y=80)

            self.title1 = tk.Label(text="""Start Point : (           ,           )""",bg="white",fg="dark slate gray",font="Arial 16")
            self.title1.place(x=510,y=200)

            self.title2 = tk.Label(text="""End Point  : (            ,           )""",bg="white",fg="dark slate gray",font="Arial 16")
            self.title2.place(x=510,y=250)

            self.title3 = tk.Label(text="""Color         :""",bg="white",fg="dark slate gray",font="Arial 16")
            self.title3.place(x=510,y=300)

            self.title4 = tk.Label(text="""Thickness  :""",bg="white",fg="dark slate gray",font="Arial 16")
            self.title4.place(x=510,y=350)

            self.x_start = tk.StringVar(value=0)
            self.y_start = tk.StringVar(value=0)
            self.x_end = tk.StringVar(value=original_size[1])
            self.y_end = tk.StringVar(value=original_size[0])
            self.line_color = tk.StringVar()
            self.thickness = tk.StringVar()        

            self.input1 = tk.Entry(fg ="black",bg="white",textvariable=self.x_start,font="Arial 15")
            self.input1.place(x=640,y=204,width=62) 
            self.input2 = tk.Entry(fg ="black",bg="white",textvariable=self.y_start,font="Arial 15")
            self.input2.place(x=712,y=204,width=62)

            self.input3 = tk.Entry(fg ="black",bg="white",textvariable=self.x_end,font="Arial 15")
            self.input3.place(x=640,y=254,width=62) 
            self.input4 = tk.Entry(fg ="black",bg="white",textvariable=self.y_end,font="Arial 15")
            self.input4.place(x=714,y=254,width=62)

            self.input5 = tk.Entry(fg ="black",bg="white",textvariable=self.thickness,font="Arial 15")
            self.input5.place(x=640,y=354,width=134)

            color_list = ["Black","Gray","White","Red","Orange","Yellow","Green","Blue","Purple","Pink"]
            self.combo1 = Combobox(values=color_list,font="Arial 13",height=6,state="readonly",textvariable=self.line_color)
            self.combo1.current(0)
            self.combo1.place(x=640,y=304,width=134)

            self.button1 = tk.Button(text="Back",bg="dark slate gray",fg="white",font="Arial 13",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=back)
            self.button1.place(x=510,y=420,width =128,height=35)

            self.button2 = tk.Button(text="Apply",bg="dark slate gray",fg="white",font="Arial 13",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=apply_line)
            self.button2.place(x=648,y=420,width =128,height=35)

            self.warning = tk.Label(text="",bg="white",fg="red",font="Arial 16")
            self.warning.place(x=510,y=470)

        def add_text():
            def apply_text():
                rgb = color_rgb_code(self.text_color.get())
                font = font_code(self.text_font.get())

                try:
                    x_start = int(self.x_start.get())
                    y_start = int(self.y_start.get())
                    text = self.write_text.get()

                    try:
                        thickness = float(self.thickness.get())

                        if(x_start<0 or y_start<0 or thickness<0):
                            self.warning.config(text="Please enter positive number.")

                        else:
                            img_add_text = cv2.putText(self.img,text,(x_start,y_start),font,thickness,rgb)
                            cv2.imwrite("modified_photo.jpg",img_add_text)
                            self.show_photo("modified_photo.jpg",2)                  

                    except:
                        if(len(self.thickness.get())== 0):
                            self.warning.config(text="Thickness should not be empty.\nDefault = 1.")
                        else:
                            self.warning.config(text="Just enter numbers.")                   

                except:
                    self.warning.config(text="Just enter numbers.")

            self.delete_all_widget()
            self.function_text = tk.Label(text="Add Text To Photo",bg="white",fg="dark slate gray",font="Times 45")
            self.function_text.place(x=420,y=80)

            self.title1 = tk.Label(text="""Text           :""",bg="white",fg="dark slate gray",font="Arial 16")
            self.title1.place(x=510,y=200)

            self.title2 = tk.Label(text="""Start Point : (           ,           )""",bg="white",fg="dark slate gray",font="Arial 16")
            self.title2.place(x=510,y=250)

            self.title3 = tk.Label(text="""Font           : """,bg="white",fg="dark slate gray",font="Arial 16")
            self.title3.place(x=510,y=300)

            self.title4 = tk.Label(text="""Color         :""",bg="white",fg="dark slate gray",font="Arial 16")
            self.title4.place(x=510,y=350)

            self.title5 = tk.Label(text="""Thickness  :""",bg="white",fg="dark slate gray",font="Arial 16")
            self.title5.place(x=510,y=400)

            self.write_text = tk.StringVar()
            self.x_start = tk.StringVar(value=0)
            self.y_start = tk.StringVar(value=0)
            self.text_font = tk.StringVar()
            self.text_color = tk.StringVar()
            self.thickness = tk.StringVar()

            self.input1 = tk.Entry(fg ="black",bg="white",textvariable=self.write_text,font="Arial 15")
            self.input1.place(x=640,y=204,width=134) 

            self.input2 = tk.Entry(fg ="black",bg="white",textvariable=self.x_start,font="Arial 15")
            self.input2.place(x=640,y=254,width=62) 
            self.input3 = tk.Entry(fg ="black",bg="white",textvariable=self.y_start,font="Arial 15")
            self.input3.place(x=712,y=254,width=62)

            self.input4 = tk.Entry(fg ="black",bg="white",textvariable=self.thickness,font="Arial 15")
            self.input4.place(x=640,y=404,width=134)

            font_list = ["SIMPLEX","PLAIN","DUPLEX","COMPLEX","COMPLEX SMALL","TRIPLEX","SCRIPT SIMPLEX","SCRIPT COMPLEX"]
            self.combo1 = Combobox(values=font_list,font="Arial 13",height=6,state="readonly",textvariable=self.text_font)
            self.combo1.current(0)
            self.combo1.place(x=640,y=304,width=134)

            color_list = ["Black","Gray","White","Red","Orange","Yellow","Green","Blue","Purple","Pink"]
            self.combo2 = Combobox(values=color_list,font="Arial 13",height=6,state="readonly",textvariable=self.text_color)
            self.combo2.current(0)
            self.combo2.place(x=640,y=354,width=134)

            self.button1 = tk.Button(text="Back",bg="dark slate gray",fg="white",font="Arial 13",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=back)
            self.button1.place(x=510,y=470,width =128,height=35)

            self.button2 = tk.Button(text="Apply",bg="dark slate gray",fg="white",font="Arial 13",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=apply_text)
            self.button2.place(x=648,y=470,width =128,height=35)

            self.warning = tk.Label(text="",bg="white",fg="red",font="Arial 16")
            self.warning.place(x=510,y=520)

        def add_rectangle():
            def apply_rectangle():
                rgb = color_rgb_code(self.rect_color.get())

                try:
                    x_start = int(self.x_start.get())
                    y_start = int(self.y_start.get())
                    x_end = int(self.x_end.get())
                    y_end = int(self.y_end.get())
                    fill = self.rectangle_radio.get()
                        
                    try:
                        thickness = int(self.thickness.get())   

                        if(x_start<0 or y_start<0 or x_end<0 or y_end<0 or thickness<0):
                            self.warning.config(text="Please enter positive number.")

                        elif(fill == "Y"):
                            img_add_rect = cv2.rectangle(self.img,(x_start,y_start),(x_end,y_end),rgb,cv2.FILLED)
                            cv2.imwrite("modified_photo.jpg",img_add_rect)
                            self.show_photo("modified_photo.jpg",2)

                        elif(fill == "N"):
                            img_add_rect = cv2.rectangle(self.img,(x_start,y_start),(x_end,y_end),rgb,thickness)
                            cv2.imwrite("modified_photo.jpg",img_add_rect)
                            self.show_photo("modified_photo.jpg",2)
                        
                        else:
                            self.warning.config(text="Please select fill attribute.")             

                    except:
                        print(len(self.thickness.get()))
                        if(len(self.thickness.get())== 0):
                            self.warning.config(text="Thickness should not be empty.\nDefault = 1.")
                        else:
                            self.warning.config(text="Just enter numbers.")

                except:
                    self.warning.config(text="Just enter numbers.")

            self.delete_all_widget()
            self.function_text = tk.Label(text="Add Rectangle To Photo",bg="white",fg="dark slate gray",font="Times 40")
            self.function_text.place(x=400,y=80)

            self.title1 = tk.Label(text="""Start Point : (           ,           )""",bg="white",fg="dark slate gray",font="Arial 16")
            self.title1.place(x=510,y=200)

            self.title2 = tk.Label(text="""End Point  : (            ,           )""",bg="white",fg="dark slate gray",font="Arial 16")
            self.title2.place(x=510,y=250)

            self.title3 = tk.Label(text="""Color         :""",bg="white",fg="dark slate gray",font="Arial 16")
            self.title3.place(x=510,y=300)

            self.title4 = tk.Label(text="""Thickness  :""",bg="white",fg="dark slate gray",font="Arial 16")
            self.title4.place(x=510,y=350)

            self.title5 = tk.Label(text="""Fill             :""",bg="white",fg="dark slate gray",font="Arial 16")
            self.title5.place(x=510,y=400)

            self.x_start = tk.StringVar(value=0)
            self.y_start = tk.StringVar(value=0)
            self.x_end = tk.StringVar(value=original_size[1])
            self.y_end = tk.StringVar(value=original_size[0])
            self.rect_color = tk.StringVar()
            self.thickness = tk.StringVar()
            self.rectangle_radio = tk.StringVar(value=0)

            self.input1 = tk.Entry(fg ="black",bg="white",textvariable=self.x_start,font="Arial 15")
            self.input1.place(x=640,y=204,width=62) 
            self.input2 = tk.Entry(fg ="black",bg="white",textvariable=self.y_start,font="Arial 15")
            self.input2.place(x=712,y=204,width=62)

            self.input3 = tk.Entry(fg ="black",bg="white",textvariable=self.x_end,font="Arial 15")
            self.input3.place(x=640,y=254,width=62) 
            self.input4 = tk.Entry(fg ="black",bg="white",textvariable=self.y_end,font="Arial 15")
            self.input4.place(x=714,y=254,width=62)

            self.input5 = tk.Entry(fg ="black",bg="white",textvariable=self.thickness,font="Arial 15")
            self.input5.place(x=640,y=354,width=134)         

            color_list = ["Black","Gray","White","Red","Orange","Yellow","Green","Blue","Purple","Pink"]
            self.combo1 = Combobox(values=color_list,font="Arial 15",height=6,state="readonly",textvariable=self.rect_color)
            self.combo1.current(0)
            self.combo1.place(x=640,y=304,width=134)            

            self.radio1 = tk.Radiobutton(text="Yes",bg="white",value="Y",font="Arial 15",activebackground="white",variable=self.rectangle_radio)
            self.radio1.place(x=640,y=400)
            self.radio2 = tk.Radiobutton(text="No",bg="white",value="N",font="Arial 15",activebackground="white",variable=self.rectangle_radio)
            self.radio2.place(x=710,y=400)

            self.button1 = tk.Button(text="Back",bg="dark slate gray",fg="white",font="Arial 13",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=back)
            self.button1.place(x=510,y=450,width =128,height=35)

            self.button2 = tk.Button(text="Apply",bg="dark slate gray",fg="white",font="Arial 13",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=apply_rectangle)
            self.button2.place(x=648,y=450,width =128,height=35)

            self.warning = tk.Label(text="",bg="white",fg="red",font="Arial 16")
            self.warning.place(x=510,y=500)

        def add_circle():
            def apply_circle():
                rgb = color_rgb_code(self.circle_color.get())

                try:
                    x_start = int(self.x_start.get())
                    y_start = int(self.y_start.get())
                    radius = int(self.radius.get())
                    fill = self.circle_radio.get()
                        
                    try:
                        thickness = int(self.thickness.get())  

                        if(x_start<0 or y_start<0 or radius<0 or thickness<0):
                            self.warning.config(text="Please enter positive number.")

                        elif(fill == "Y"):
                            img_add_circ = cv2.circle(self.img,(x_start,y_start),radius,rgb,cv2.FILLED)
                            cv2.imwrite("modified_photo.jpg",img_add_circ)
                            self.show_photo("modified_photo.jpg",2)

                        elif(fill == "N"):
                            img_add_circ = cv2.circle(self.img,(x_start,y_start),radius,rgb,thickness)
                            cv2.imwrite("modified_photo.jpg",img_add_circ)
                            self.show_photo("modified_photo.jpg",2)
                        
                        else:
                            self.warning.config(text="Please select fill attribute.")      

                    except:
                        if(len(self.thickness.get())== 0):
                            self.warning.config(text="Thickness should not be empty.\nDefault = 1.")
                        else:
                            self.warning.config(text="Just enter numbers.")      

                except:
                    self.warning.config(text="Just enter numbers.")

            self.delete_all_widget()
            self.function_text = tk.Label(text="Add Circle To Photo",bg="white",fg="dark slate gray",font="Times 40")
            self.function_text.place(x=420,y=80)

            self.title1 = tk.Label(text="""Start Point : (           ,           )""",bg="white",fg="dark slate gray",font="Arial 16")
            self.title1.place(x=510,y=200)

            self.title2 = tk.Label(text="""Radius       : """,bg="white",fg="dark slate gray",font="Arial 16")
            self.title2.place(x=510,y=250)

            self.title3 = tk.Label(text="""Color         :""",bg="white",fg="dark slate gray",font="Arial 16")
            self.title3.place(x=510,y=300)

            self.title4 = tk.Label(text="""Thickness  :""",bg="white",fg="dark slate gray",font="Arial 16")
            self.title4.place(x=510,y=350)

            self.title5 = tk.Label(text="""Fill             :""",bg="white",fg="dark slate gray",font="Arial 16")
            self.title5.place(x=510,y=400)

            self.x_start = tk.StringVar(value=0)
            self.y_start = tk.StringVar(value=0)
            self.radius = tk.StringVar()
            self.circle_color = tk.StringVar()
            self.thickness = tk.StringVar()
            self.circle_radio = tk.StringVar(value=0)

            self.input1 = tk.Entry(fg ="black",bg="white",textvariable=self.x_start,font="Arial 15")
            self.input1.place(x=640,y=204,width=62) 
            self.input2 = tk.Entry(fg ="black",bg="white",textvariable=self.y_start,font="Arial 15")
            self.input2.place(x=712,y=204,width=62)

            self.input3 = tk.Entry(fg ="black",bg="white",textvariable=self.radius,font="Arial 15")
            self.input3.place(x=640,y=254,width=134)

            self.input4 = tk.Entry(fg ="black",bg="white",textvariable=self.thickness,font="Arial 15")
            self.input4.place(x=640,y=354,width=134)

            color_list = ["Black","Gray","White","Red","Orange","Yellow","Green","Blue","Purple","Pink"]
            self.combo1 = Combobox(values=color_list,font="Arial 13",height=6,state="readonly",textvariable=self.circle_color)
            self.combo1.current(0)
            self.combo1.place(x=640,y=304,width=134)     

            self.radio1 = tk.Radiobutton(text="Yes",bg="white",value="Y",font="Arial 15",activebackground="white",variable=self.circle_radio)
            self.radio1.place(x=640,y=400)
            self.radio2 = tk.Radiobutton(text="No",bg="white",value="N",font="Arial 15",activebackground="white",variable=self.circle_radio)
            self.radio2.place(x=710,y=400)

            self.button1 = tk.Button(text="Back",bg="dark slate gray",fg="white",font="Arial 13",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=back)
            self.button1.place(x=510,y=470,width =128,height=35)

            self.button2 = tk.Button(text="Apply",bg="dark slate gray",fg="white",font="Arial 13",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=apply_circle)
            self.button2.place(x=648,y=470,width =128,height=35)

            self.warning = tk.Label(text="",bg="white",fg="red",font="Arial 16")
            self.warning.place(x=510,y=520)
            
        control = self.upload_control()
        if control ==1: 
            self.delete_all_widget()
            self.img = cv2.imread(self.filename)
            original_size = self.img.shape
            self.main_screen.geometry("1000x605+"+str(int((self.screen_width-1000)/2))+"+"+str(int((self.screen_height-605)/2)))
            self.function_text = tk.Label(text="Choose what you want to add\nto the photo.",bg="white",fg="dark slate gray",font="Times 20")
            self.function_text.place(x=500,y=80)

            self.button1 = tk.Button(text="Line",bg="dark slate gray",fg="white",font="Arial 14",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=add_line)
            self.button1.place(x=520,y=200,width =300,height=38)

            self.button2 = tk.Button(text="Text",bg="dark slate gray",fg="white",font="Arial 14",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=add_text)
            self.button2.place(x=520,y=250,width =300,height=38)

            self.button3 = tk.Button(text="Rectangle",bg="dark slate gray",fg="white",font="Arial 14",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=add_rectangle)
            self.button3.place(x=520,y=300,width =300,height=38)

            self.button4 = tk.Button(text="Circle",bg="dark slate gray",fg="white",font="Arial 14",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=add_circle)
            self.button4.place(x=520,y=350,width =300,height=38)

    def combine_image(self):
        def ver_combine():
            ver = np.vstack((self.img,self.img))
            cv2.imwrite("modified_photo.jpg",ver)
            self.show_photo("modified_photo.jpg",3)

        def hor_combine():
            hor = np.hstack((self.img,self.img))
            cv2.imwrite("modified_photo.jpg",hor)
            self.show_photo("modified_photo.jpg",3)

        control = self.upload_control()
        if control ==1: 
            self.delete_all_widget()
            self.img = cv2.imread(self.filename)
            original_size = self.img.shape
            self.main_screen.geometry("1000x605+"+str(int((self.screen_width-1000)/2))+"+"+str(int((self.screen_height-605)/2)))
            self.function_text = tk.Label(text="Choose how you want to combine\nthe photos.",bg="white",fg="dark slate gray",font="Times 20")
            self.function_text.place(x=470,y=150)

            self.button1 = tk.Button(text="Horizontal",bg="dark slate gray",fg="white",font="Arial 14",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=hor_combine)
            self.button1.place(x=520,y=270,width =300,height=38)

            self.button2 = tk.Button(text="Vertical",bg="dark slate gray",fg="white",font="Arial 14",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=ver_combine)
            self.button2.place(x=520,y=350,width =300,height=38)

    def mix_images(self):
        self.cal =0

        def calculate():
            try:
                first = self.first_image_ratio.get()
                second = self.second_image_ratio.get()

                try:
                    int(first)
                    int(second)
                except:
                    self.second_image_ratio.set(str(self.old_second_ratio))
                    self.first_image_ratio.set(str(self.old_first_ratio))

                if(int(first)>100 or int(second)>100):
                    self.second_image_ratio.set(str(self.old_second_ratio))
                    self.first_image_ratio.set(str(self.old_first_ratio))

                if(int(first) != self.old_first_ratio):
                    self.second_image_ratio.set(str(100-int(first)))
                    self.old_first_ratio = int(first)
                    self.old_second_ratio = int(second)
                elif(int(second) != self.old_second_ratio):
                    self.first_image_ratio.set(str(100-int(second)))
                    self.old_first_ratio = int(first)
                    self.old_second_ratio = int(second)
                else:
                    pass
            except ValueError:
                if(len(first)==0):
                    self.first_image_ratio.set("0")
                    self.second_image_ratio.set("100")
                elif(len(second)==0):
                    self.first_image_ratio.set("100")
                    self.second_image_ratio.set("0")

            if(self.cal==0):
                self.main_screen.after(100,calculate)

        def get_image(func):
            self.filename2 = filedialog.askopenfilename(initialdir="/Desktop", title="Select An Image", filetypes=(("image files", "*.jpg;*.png"),("image files", "*.jpeg")))
            if(len(self.filename2)!=0):
                if func==1:
                    self.mix_image1 = cv2.imread(self.filename2)
                    show(self.filename2,1)
                elif func==2:
                    self.mix_image2 = cv2.imread(self.filename2)
                    show(self.filename2,2)

        def show(image_url,image_no):
            if image_no==1:
                img = cv2.imread(image_url)
                original_size = img.shape

                if(original_size[0]<=490 and original_size[1]<=490) and (original_size[0]>=400 and original_size[1]>=400) and (original_size[0]!= original_size[1]):
                    load = Image.open(image_url)
                    self.img = ImageTk.PhotoImage(load)   
                    self.image_label = tk.Label(image=self.img,bg="white")
                    self.image_label.place(x=410,y=20)

                elif((original_size[0]<=400 or original_size[1]<=400) and (original_size[0]!= original_size[1])):
                    if(original_size[0]>original_size[1]):
                        ratio = original_size[0]/245
                        img_resized = cv2.resize(img,(int(img.shape[1]/ratio),245))
                        cv2.imwrite("modified_photo.jpg",img_resized)
                        load = Image.open("modified_photo.jpg")
                        self.img = ImageTk.PhotoImage(load)   
                        self.image_label = tk.Label(image=self.img,bg="white")
                        self.image_label.place(x=410,y=20)
                    else:
                        ratio = original_size[1]/245
                        img_resized = cv2.resize(img,(245,int(img.shape[0]/ratio)))
                        cv2.imwrite("modified_photo.jpg",img_resized)
                        load = Image.open("modified_photo.jpg")
                        self.img = ImageTk.PhotoImage(load)   
                        self.image_label = tk.Label(image=self.img,bg="white")
                        self.image_label.place(x=410,y=20)

                elif((original_size[0]>490 or original_size[1]>490) and (original_size[1]>original_size[0]) and (original_size[0]!= original_size[1])):
                    ratio = original_size[1]/400
                    img_resized = cv2.resize(img,(400,int(original_size[0]/ratio)))
                    if(img_resized.shape[0]>245):
                        img_resized = cv2.resize(img,(400,245))
                    cv2.imwrite("modified_photo.jpg",img_resized)
                    load = Image.open("modified_photo.jpg")
                    self.img = ImageTk.PhotoImage(load)   
                    self.image_label = tk.Label(image=self.img,bg="white")
                    self.image_label.place(x=410,y=20)

                elif((original_size[0]>490 or original_size[1]>490) and (original_size[1]<original_size[0]) and (original_size[0]!= original_size[1])):
                    ratio = original_size[0]/245
                    img_resized = cv2.resize(img,(int(original_size[1]/ratio),245))
                    if(img_resized.shape[1]>245):
                        img_resized = cv2.resize(img,(245,245))
                    cv2.imwrite("modified_photo.jpg",img_resized)
                    load = Image.open("modified_photo.jpg")
                    self.img = ImageTk.PhotoImage(load)   
                    self.image_label = tk.Label(image=self.img,bg="white")
                    self.image_label.place(x=410,y=20)

                elif(original_size[0] == original_size[1]):
                    img_resized = cv2.resize(img,(245,245))
                    cv2.imwrite("modified_photo.jpg",img_resized)
                    load = Image.open("modified_photo.jpg")
                    self.img = ImageTk.PhotoImage(load)   
                    self.image_label = tk.Label(image=self.img,bg="white")
                    self.image_label.place(x=410,y=20)
            
            elif image_no==2:
                self.button1.destroy()
                img2 = cv2.imread(image_url)
                original_size2 = img2.shape

                if(original_size2[0]<=490 and original_size2[1]<=490) and (original_size2[0]>=400 and original_size2[1]>=400) and (original_size2[0]!= original_size2[1]):
                    load2 = Image.open(image_url)
                    self.img2 = ImageTk.PhotoImage(load2)   
                    self.image2_label = tk.Label(image=self.img2,bg="white")
                    self.image2_label.place(x=850,y=20)

                elif((original_size2[0]<=400 or original_size2[1]<=400) and (original_size2[0]!= original_size2[1])):
                    if(original_size2[0]>original_size2[1]):
                        ratio = original_size2[0]/245
                        img_resized2 = cv2.resize(img2,(int(img2.shape[1]/ratio),245))
                        cv2.imwrite("modified_photo.jpg",img_resized2)
                        load2 = Image.open("modified_photo.jpg")
                        self.img2 = ImageTk.PhotoImage(load2)   
                        self.image2_label = tk.Label(image=self.img2,bg="white")
                        self.image2_label.place(x=850,y=20)
                    else:
                        ratio = original_size2[1]/245
                        img_resized2 = cv2.resize(img2,(245,int(img2.shape[0]/ratio)))
                        cv2.imwrite("modified_photo.jpg",img_resized2)
                        load2 = Image.open("modified_photo.jpg")
                        self.img2 = ImageTk.PhotoImage(load2)   
                        self.image2_label = tk.Label(image=self.img2,bg="white")
                        self.image2_label.place(x=850,y=20)

                elif((original_size2[0]>490 or original_size2[1]>490) and (original_size2[1]>original_size2[0]) and (original_size2[0]!= original_size2[1])):
                    ratio = original_size2[1]/400
                    img_resized2 = cv2.resize(img2,(400,int(original_size2[0]/ratio)))
                    if(img_resized2.shape[0]>245):
                        img_resized2 = cv2.resize(img2,(400,245))
                    cv2.imwrite("modified_photo.jpg",img_resized2)
                    load2 = Image.open("modified_photo.jpg")
                    self.img2 = ImageTk.PhotoImage(load2)   
                    self.image2_label = tk.Label(image=self.img2,bg="white")
                    self.image2_label.place(x=850,y=20)

                elif((original_size2[0]>490 or original_size2[1]>490) and (original_size2[1]<original_size2[0]) and (original_size2[0]!= original_size2[1])):
                    ratio = original_size2[0]/245
                    img_resized2 = cv2.resize(img2,(int(original_size2[1]/ratio),245))
                    if(img_resized2.shape[1]>245):
                        img_resized2 = cv2.resize(img2,(245,245))
                    cv2.imwrite("modified_photo.jpg",img_resized2)
                    load2 = Image.open("modified_photo.jpg")
                    self.img2 = ImageTk.PhotoImage(load2)   
                    self.image2_label = tk.Label(image=self.img2,bg="white")
                    self.image2_label.place(x=850,y=20)

                elif(original_size2[0] == original_size2[1]):
                    img_resized2 = cv2.resize(img2,(245,245))
                    cv2.imwrite("modified_photo.jpg",img_resized2)
                    load2 = Image.open("modified_photo.jpg")
                    self.img2 = ImageTk.PhotoImage(load2)   
                    self.image2_label = tk.Label(image=self.img2,bg="white")
                    self.image2_label.place(x=850,y=20)

                main()

            try:os.remove("modified_photo.jpg")
            except:pass

        def main():
            self.button1 = tk.Button(text="Select New\nFirst Image",bg="dark slate gray",fg="white",font="Arial 11",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=lambda: get_image(1))
            self.button1.place(x=520,y=300,width =150,height=40)

            self.button2 = tk.Button(text="Select New\nSecond Image",bg="dark slate gray",fg="white",font="Arial 11",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=lambda: get_image(2))
            self.button2.place(x=980,y=300,width =150,height=40)

            self.title1 = tk.Label(text="Mix Ratio",bg="white",fg="dark slate gray",font="Arial 24")
            self.title1.place(x=760,y=340)
            self.title2 = tk.Label(text="First Image",bg="white",fg="black",font="Arial 16")
            self.title2.place(x=660,y=400)
            self.title3 = tk.Label(text="Second Image",bg="white",fg="black",font="Arial 16")
            self.title3.place(x=860,y=400)

            self.first_image_ratio = tk.StringVar(value=50)
            self.second_image_ratio = tk.StringVar(value=50)
            self.old_first_ratio = 50
            self.old_second_ratio = 50

            self.input1 = tk.Entry(fg ="black",bg="white",textvariable=self.first_image_ratio,font="Times 15")
            self.input1.place(x=680,y=440,width=80) 
            self.input2 = tk.Entry(fg ="black",bg="white",textvariable=self.second_image_ratio,font="Times 15")
            self.input2.place(x=890,y=440,width=80)

            self.button3 = tk.Button(text="Apply",bg="dark slate gray",fg="white",font="Arial 13",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=apply)
            self.button3.place(x=730,y=485,width =180,height=40)

            self.warning = tk.Label(text="The sum of the ratios should be 100.",bg="white",fg="red",font="Arial 12")
            self.warning.place(x=690,y=530)

            calculate()

        def apply():
            self.cal+=1
            size = self.mix_image1.shape
            self.mix_image2 = cv2.resize(self.mix_image2,(size[1],size[0]))

            img_mix = cv2.addWeighted(src1=self.mix_image1,src2=self.mix_image2,alpha=int(self.first_image_ratio.get())/100,beta=int(self.second_image_ratio.get())/100,gamma=0)
            cv2.imwrite("modified_photo.jpg",img_mix)
            self.show_photo("modified_photo.jpg",4)
        
        control = self.upload_control()
        if control ==1: 
            self.delete_all_widget()
            self.mix_image1 = cv2.imread(self.filename)
            self.main_screen.geometry("1300x605+"+str(int((self.screen_width-1300)/2))+"+"+str(int((self.screen_height-605)/2)))
            self.button1 = tk.Button(text="Import Second\nImage",bg="dark slate gray",fg="white",font="Arial 11",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=lambda: get_image(2))
            self.button1.place(x=980,y=150,width =150,height=40)
            show(self.filename,1)

    def apply_threshold(self):
        def method_code(selected_method):  
            if(selected_method == "Binary"):
                return cv2.THRESH_BINARY
            elif(selected_method == "Binary Inverse"):
                return cv2.THRESH_BINARY_INV
            elif(selected_method == "Trunc"):
                return cv2.THRESH_TRUNC
            elif(selected_method == "To Zero"):
                return cv2.THRESH_TOZERO
            elif(selected_method == "To Zero Inverse"):
                return cv2.THRESH_TOZERO_INV

        def adaptive():
            adaptive_thresh = cv2.adaptiveThreshold(self.img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,8)
            cv2.imwrite("modified_photo.jpg",adaptive_thresh)
            self.show_photo("modified_photo.jpg",5)

        def apply():
            method = method_code(self.thresh_method.get())
            try:
                thresh_val = int(self.thresh_value.get())

                if(thresh_val<0 or thresh_val>255):
                    self.warning.config(text="Thresh value should be between 0-255.")
                else:
                    _,thresh_img = cv2.threshold(self.img,thresh=thresh_val,maxval=255,type=method)
                    cv2.imwrite("modified_photo.jpg",thresh_img)
                    self.show_photo("modified_photo.jpg",5)

            except:
                self.warning.config(text="Just enter numbers.")

        def examine():
            plt.figure(),plt.imshow(self.img,cmap="gray"),plt.axis("off"),plt.show()

        control = self.upload_control()
        if control ==1: 
            self.delete_all_widget()
            self.main_screen.geometry("1000x605+"+str(int((self.screen_width-1000)/2))+"+"+str(int((self.screen_height-605)/2)))
            self.function_text = tk.Label(text="Thresholding",bg="white",fg="dark slate gray",font="Times 50")
            self.function_text.place(x=460,y=50)
            self.img = cv2.imread(self.filename,0)

            self.button1 = tk.Button(text="Adaptive Thresholding",bg="dark slate gray",fg="white",font="Arial 13",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=adaptive)
            self.button1.place(x=520,y=170,width =250,height=40)

            self.title1 = tk.Label(text="""Thresh Value =                          (0-255)""",bg="white",fg="black",font="Arial 16")
            self.title1.place(x=470,y=260)
            self.title2 = tk.Label(text="Method =",bg="white",fg="black",font="Arial 16")
            self.title2.place(x=470,y=320)
            
            self.thresh_value = tk.StringVar()
            self.thresh_method = tk.StringVar(value=0)

            self.input1 = tk.Entry(fg ="black",bg="white",textvariable=self.thresh_value,font="Times 15")
            self.input1.place(x=620,y=262,width=140) 

            method_list = ["Binary","Binary Inverse","Trunc","To Zero","To Zero Inverse"]
            self.combo1 = Combobox(values=method_list,font="Arial 14",height=6,state="readonly",textvariable=self.thresh_method)
            self.combo1.current(0)
            self.combo1.place(x=568,y=322,width=194)  

            self.button2 = tk.Button(text="Apply",bg="dark slate gray",fg="white",font="Arial 13",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=apply)
            self.button2.place(x=650,y=382,width =120,height=40)
            self.button3 = tk.Button(text="Examine",bg="dark slate gray",fg="white",font="Arial 13",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=examine)
            self.button3.place(x=520,y=382,width =120,height=40)

            self.warning = tk.Label(text="",bg="white",fg="red",font="Arial 14")
            self.warning.place(x=470,y=450)

    def blur_image(self):
        def back():
            self.blur_image()

        def average_blur():
            def apply():
                try:
                    k1 = int(self.k_size1.get())
                    k2 = int(self.k_size2.get())
                    
                    if(k1>0 and k2>0):
                        self.warning.config(text="")
                        img_blur = cv2.blur(self.img,ksize=(k1,k2))
                        cv2.imwrite("modified_photo.jpg",img_blur)
                        self.show_photo("modified_photo.jpg",6)
                    else:
                        self.warning.config(text="The value '0' cannot be written.")

                except:
                    self.warning.config(text="Just enter numbers.")

            self.delete_all_widget()
            self.recommend = tk.Label(text="*Recommended values ​​are typed automatically.",bg="white",fg="red",font="Arial 9")
            self.recommend.place(x=730,y=10)

            self.function_text = tk.Label(text="Averaging",bg="white",fg="dark slate gray",font="Times 50")
            self.function_text.place(x=500,y=150)

            self.title1 = tk.Label(text="Ksize =",bg="white",fg="black",font="Arial 16")
            self.title1.place(x=510,y=300)
            
            self.k_size1 = tk.StringVar(value=3)
            self.k_size2 = tk.StringVar(value=3)

            self.input1 = tk.Entry(fg ="black",bg="white",textvariable=self.k_size1,font="Times 15")
            self.input1.place(x=595,y=302,width=85) 
            self.input2 = tk.Entry(fg ="black",bg="white",textvariable=self.k_size2,font="Times 15")
            self.input2.place(x=695,y=302,width=85) 

            self.button1 = tk.Button(text="Back",bg="dark slate gray",fg="white",font="Arial 13",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=back)
            self.button1.place(x=500,y=380,width =140,height=40)
            self.button2 = tk.Button(text="Apply",bg="dark slate gray",fg="white",font="Arial 13",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=apply)
            self.button2.place(x=645,y=380,width =140,height=40)

            self.warning = tk.Label(text="",bg="white",fg="red",font="Arial 14")
            self.warning.place(x=500,y=440)
        
        def gaussian_blur():
            def apply():
                try:
                    k1 = int(self.k_size1.get())
                    k2 = int(self.k_size2.get())
                    sigma = int(self.sigma.get())
                    
                    if(k1>0 and k1<8 and k2<8 and k2>0 and sigma>0):
                        self.warning.config(text="")
                        img_blur = cv2.GaussianBlur(self.img,ksize=(k1,k2),sigmaX=sigma)
                        cv2.imwrite("modified_photo.jpg",img_blur)
                        self.show_photo("modified_photo.jpg",6)
                    else:
                        self.warning.config(text="The ksize value can be between 1-7.\nSigmaX value must be greater than 0.")

                except:
                    self.warning.config(text="Just enter numbers.")
                    
            self.delete_all_widget()
            self.recommend = tk.Label(text="*Recommended values ​​are typed automatically.",bg="white",fg="red",font="Arial 9")
            self.recommend.place(x=730,y=10)

            self.function_text = tk.Label(text="Gaussian Blurring",bg="white",fg="dark slate gray",font="Times 40")
            self.function_text.place(x=450,y=120)

            self.title1 = tk.Label(text="Thresh Value =",bg="white",fg="black",font="Arial 16")
            self.title1.place(x=500,y=230)
            self.title2 = tk.Label(text="SigmaX =",bg="white",fg="black",font="Arial 16")
            self.title2.place(x=500,y=300)
            
            self.k_size1 = tk.StringVar(value=3)
            self.k_size2 = tk.StringVar(value=3)
            self.sigma = tk.StringVar(value=7)

            self.input1 = tk.Entry(fg ="black",bg="white",textvariable=self.k_size1,font="Times 15")
            self.input1.place(x=650,y=232,width=65) 
            self.input2 = tk.Entry(fg ="black",bg="white",textvariable=self.k_size2,font="Times 15")
            self.input2.place(x=720,y=232,width=65) 
            self.input3 = tk.Entry(fg ="black",bg="white",textvariable=self.sigma,font="Times 15")
            self.input3.place(x=600,y=302,width=186) 

            self.button1 = tk.Button(text="Back",bg="dark slate gray",fg="white",font="Arial 13",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=back)
            self.button1.place(x=500,y=380,width =140,height=40)
            self.button2 = tk.Button(text="Apply",bg="dark slate gray",fg="white",font="Arial 13",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=apply)
            self.button2.place(x=645,y=380,width =140,height=40)

            self.warning = tk.Label(text="",bg="white",fg="red",font="Arial 14")
            self.warning.place(x=500,y=440)

        def median_blur():
            def apply():
                try:
                    k1 = int(self.k_size1.get())
                    
                    if(k1>0 and k1<8):
                        self.warning.config(text="")
                        img_blur = cv2.medianBlur(self.img,ksize=k1)
                        cv2.imwrite("modified_photo.jpg",img_blur)
                        self.show_photo("modified_photo.jpg",6)
                    else:
                        self.warning.config(text="The ksize value can be between 1-7.")

                except:
                    self.warning.config(text="Just enter numbers.")

            self.delete_all_widget()
            self.recommend = tk.Label(text="*Recommended values ​​are typed automatically.",bg="white",fg="red",font="Arial 9")
            self.recommend.place(x=730,y=10)

            self.function_text = tk.Label(text="Median Blurring",bg="white",fg="dark slate gray",font="Times 40")
            self.function_text.place(x=470,y=150)

            self.title1 = tk.Label(text="Ksize =",bg="white",fg="black",font="Arial 16")
            self.title1.place(x=530,y=280)
            
            self.k_size1 = tk.StringVar(value=3)

            self.input1 = tk.Entry(fg ="black",bg="white",textvariable=self.k_size1,font="Times 15")
            self.input1.place(x=615,y=282,width=130) 

            self.button1 = tk.Button(text="Back",bg="dark slate gray",fg="white",font="Arial 13",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=back)
            self.button1.place(x=500,y=380,width =140,height=40)
            self.button2 = tk.Button(text="Apply",bg="dark slate gray",fg="white",font="Arial 13",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=apply)
            self.button2.place(x=645,y=380,width =140,height=40)

            self.warning = tk.Label(text="",bg="white",fg="red",font="Arial 14")
            self.warning.place(x=500,y=440)

        control = self.upload_control()
        if control ==1: 
            self.delete_all_widget()
            self.img = cv2.imread(self.filename)
            self.main_screen.geometry("1000x605+"+str(int((self.screen_width-1000)/2))+"+"+str(int((self.screen_height-605)/2)))
            self.function_text = tk.Label(text="Choose which method you will use to\napply blur to the image.",bg="white",fg="dark slate gray",font="Times 20")
            self.function_text.place(x=460,y=110)

            self.button1 = tk.Button(text="Averaging",bg="dark slate gray",fg="white",font="Arial 14",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=average_blur)
            self.button1.place(x=520,y=230,width =300,height=38)

            self.button2 = tk.Button(text="Gaussian Blurring",bg="dark slate gray",fg="white",font="Arial 14",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=gaussian_blur)
            self.button2.place(x=520,y=280,width =300,height=38)

            self.button3 = tk.Button(text="Median Blurring",bg="dark slate gray",fg="white",font="Arial 14",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=median_blur)
            self.button3.place(x=520,y=330,width =300,height=38)

    def add_noise_image(self):
        def back():
            self.add_noise_image()

        def gaussian_noise():
            def apply():
                try:
                    mean = float(self.mean.get())
                    sigma = float(self.sigma.get())
                            
                    if(sigma>1):
                        self.warning.config(text="The sigma value must be between 0-1.")

                    elif(mean>=0 and sigma>=0):
                        self.warning.config(text="")
                        self.img = self.img/255
                        noisy_img = self.img + np.random.normal(mean,sigma, self.img.shape)
                        noisy_img_clipped = np.clip(noisy_img, 0, 255)
                        noisy_img_clipped = noisy_img_clipped*255
                        cv2.imwrite("modified_photo.jpg",noisy_img_clipped)
                        self.show_photo("modified_photo.jpg",7)
                    
                    else:
                        self.warning.config(text="Parameter values ​​must be positive.")

                except:
                   self.warning.config(text="Just enter numbers.")

            self.delete_all_widget()
            self.recommend = tk.Label(text="*Recommended values ​​are typed automatically.",bg="white",fg="red",font="Arial 9")
            self.recommend.place(x=730,y=10)
            
            self.function_text = tk.Label(text="Gaussian Noise",bg="white",fg="dark slate gray",font="Times 40")
            self.function_text.place(x=480,y=120)

            self.title1 = tk.Label(text="Mean Value =",bg="white",fg="black",font="Arial 16")
            self.title1.place(x=500,y=230)
            self.title2 = tk.Label(text="Sigma Value =",bg="white",fg="black",font="Arial 16")
            self.title2.place(x=500,y=300)
            
            self.mean = tk.StringVar(value=0)
            self.sigma = tk.StringVar(value=(0.223))

            self.input1 = tk.Entry(fg ="black",bg="white",textvariable=self.mean,font="Times 15")
            self.input1.place(x=650,y=232,width=100) 
            self.input2 = tk.Entry(fg ="black",bg="white",textvariable=self.sigma,font="Times 15")
            self.input2.place(x=650,y=302,width=100) 

            self.button1 = tk.Button(text="Back",bg="dark slate gray",fg="white",font="Arial 13",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=back)
            self.button1.place(x=500,y=380,width =140,height=40)
            self.button2 = tk.Button(text="Apply",bg="dark slate gray",fg="white",font="Arial 13",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=apply)
            self.button2.place(x=645,y=380,width =140,height=40)

            self.warning = tk.Label(text="",bg="white",fg="red",font="Arial 14")
            self.warning.place(x=500,y=440)

        def s_p_noise():
            self.cal =0

            def calculate():
                try:
                    if(len(str(self.whitedot.get()))==1):
                        self.old_white = int(self.whitedot.get())
                        self.old_black = int(self.blackdot.get())

                    if(float(self.whitedot.get()) == 0.5):
                        self.blackdot.set(0.5)
                        self.whitedot.set(0.5)

                    if(float(self.whitedot.get()) > 1):
                        self.blackdot.set(0.0)
                        self.whitedot.set(1.0)

                    if(float(self.blackdot.get()) > 1):
                        self.blackdot.set(1.0)
                        self.whitedot.set(0.0)

                    if(float(self.old_white) != float(self.whitedot.get())):
                        self.blackdot.set(1-float(self.whitedot.get()))
                        self.old_white = int(self.whitedot.get())
                        self.old_black = int(self.blackdot.get())

                    if(float(self.old_black) != float(self.blackdot.get())):
                        self.whitedot.set(1-float(self.blackdot.get()))
                        self.old_white = int(self.whitedot.get())
                        self.old_black = int(self.blackdot.get())

                except:
                    pass

                if(self.cal==0):
                    self.main_screen.after(100,calculate)

            def apply():
                self.cal +=1
                
                try:
                    amount = float(self.amount.get())
                    white_dot = float(self.whitedot.get())
                    black_dot = float(self.blackdot.get())
                        
                    if(amount>0):
                        self.warning.config(text="")

                        num_salt = int(np.ceil(amount*self.img.size*white_dot))
                        corrds = [np.random.randint(0,i-1,num_salt) for i in self.img.shape]
                        self.img[corrds] = 1

                        num_pep = int(np.ceil(amount*self.img.size*black_dot))
                        corrds = [np.random.randint(0,i-1,num_pep) for i in self.img.shape]
                        self.img[corrds] = 0

                        cv2.imwrite("modified_photo.jpg",self.img)
                        self.show_photo("modified_photo.jpg",7)
                    
                    else:
                        self.warning.config(text="Parameter values ​​must be positive.")

                except:
                   self.warning.config(text="Just enter numbers.")
                

            self.delete_all_widget()
            self.recommend = tk.Label(text="*Recommended values ​​are typed automatically.",bg="white",fg="red",font="Arial 9")
            self.recommend.place(x=730,y=10)
            
            self.function_text = tk.Label(text="Salt&Pepper Noise",bg="white",fg="dark slate gray",font="Times 40")
            self.function_text.place(x=440,y=120)

            self.title1 = tk.Label(text="Amount Value =",bg="white",fg="black",font="Arial 16")
            self.title1.place(x=500,y=230)
            self.title2 = tk.Label(text="White Dot Ratio =",bg="white",fg="black",font="Arial 16")
            self.title2.place(x=500,y=300)
            self.title3 = tk.Label(text="Black Dot Ratio =",bg="white",fg="black",font="Arial 16")
            self.title3.place(x=500,y=370)
            
            self.amount = tk.StringVar(value=0.004)
            self.whitedot = tk.StringVar(value=(0.5))
            self.blackdot = tk.StringVar(value=(0.5))

            self.old_white = float(self.whitedot.get())
            self.old_black = float(self.blackdot.get())

            self.input1 = tk.Entry(fg ="black",bg="white",textvariable=self.amount,font="Times 15")
            self.input1.place(x=655,y=232,width=120) 
            self.input2 = tk.Entry(fg ="black",bg="white",textvariable=self.whitedot,font="Times 15")
            self.input2.place(x=675,y=302,width=100)
            self.input3 = tk.Entry(fg ="black",bg="white",textvariable=self.blackdot,font="Times 15")
            self.input3.place(x=675,y=372,width=100) 

            self.button1 = tk.Button(text="Back",bg="dark slate gray",fg="white",font="Arial 13",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=back)
            self.button1.place(x=500,y=450,width =140,height=40)
            self.button2 = tk.Button(text="Apply",bg="dark slate gray",fg="white",font="Arial 13",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=apply)
            self.button2.place(x=645,y=450,width =140,height=40)

            self.warning = tk.Label(text="",bg="white",fg="red",font="Arial 14")
            self.warning.place(x=500,y=520)

            calculate()

        control = self.upload_control()
        if control ==1: 
            self.delete_all_widget()
            self.img = cv2.imread(self.filename)
            self.main_screen.geometry("1000x605+"+str(int((self.screen_width-1000)/2))+"+"+str(int((self.screen_height-605)/2)))
            self.function_text = tk.Label(text="Choose which method you will use to\napply noise to the image.",bg="white",fg="dark slate gray",font="Times 20")
            self.function_text.place(x=460,y=130)

            self.button1 = tk.Button(text="Gaussian Noise",bg="dark slate gray",fg="white",font="Arial 14",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=gaussian_noise)
            self.button1.place(x=520,y=260,width =300,height=38)

            self.button2 = tk.Button(text="Salt-Pepper Noise",bg="dark slate gray",fg="white",font="Arial 14",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=s_p_noise)
            self.button2.place(x=520,y=330,width =300,height=38)

    def morph_transform(self):
        def back():
            self.morph_transform()

        def erosion():
            def apply():
                try:
                    iteration = int(self.iter.get())
                    
                    if(iteration>=1):
                        self.warning.config(text="")
                        kernel = np.ones((5,5),dtype=np.uint8)
                        result = cv2.erode(self.img,kernel,iterations=iteration)
                        cv2.imwrite("modified_photo.jpg",result)
                        self.show_photo("modified_photo.jpg",8)
                    else:
                        self.warning.config(text="The iteration number must be greater than 1.")

                except:
                    self.warning.config(text="Just enter numbers.")

            self.delete_all_widget()
            self.recommend = tk.Label(text="*Recommended values ​​are typed automatically.",bg="white",fg="red",font="Arial 9")
            self.recommend.place(x=730,y=10)

            self.function_text = tk.Label(text="Erosion",bg="white",fg="dark slate gray",font="Times 50")
            self.function_text.place(x=530,y=120)

            self.title1 = tk.Label(text="Number Of Iteration =",bg="white",fg="black",font="Arial 16")
            self.title1.place(x=500,y=260)
            
            self.iter = tk.StringVar(value=1)

            self.input1 = tk.Entry(fg ="black",bg="white",textvariable=self.iter,font="Times 15")
            self.input1.place(x=720,y=262,width=65) 

            self.button1 = tk.Button(text="Back",bg="dark slate gray",fg="white",font="Arial 13",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=back)
            self.button1.place(x=500,y=340,width =140,height=40)
            self.button2 = tk.Button(text="Apply",bg="dark slate gray",fg="white",font="Arial 13",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=apply)
            self.button2.place(x=645,y=340,width =140,height=40)

            self.warning = tk.Label(text="",bg="white",fg="red",font="Arial 14")
            self.warning.place(x=500,y=400)

        def dilation():
            def apply():
                try:
                    iteration = int(self.iter.get())
                    
                    if(iteration>=1):
                        self.warning.config(text="")
                        kernel = np.ones((5,5),dtype=np.uint8)
                        result = cv2.dilate(self.img,kernel,iterations=iteration)
                        cv2.imwrite("modified_photo.jpg",result)
                        self.show_photo("modified_photo.jpg",8)
                    else:
                        self.warning.config(text="The iteration number must be greater than 1.")

                except:
                    self.warning.config(text="Just enter numbers.")

            self.delete_all_widget()
            self.recommend = tk.Label(text="*Recommended values ​​are typed automatically.",bg="white",fg="red",font="Arial 9")
            self.recommend.place(x=730,y=10)

            self.function_text = tk.Label(text="Dilation",bg="white",fg="dark slate gray",font="Times 50")
            self.function_text.place(x=530,y=120)

            self.title1 = tk.Label(text="Number Of Iteration =",bg="white",fg="black",font="Arial 16")
            self.title1.place(x=500,y=260)
            
            self.iter = tk.StringVar(value=1)

            self.input1 = tk.Entry(fg ="black",bg="white",textvariable=self.iter,font="Times 15")
            self.input1.place(x=720,y=262,width=65) 

            self.button1 = tk.Button(text="Back",bg="dark slate gray",fg="white",font="Arial 13",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=back)
            self.button1.place(x=500,y=340,width =140,height=40)
            self.button2 = tk.Button(text="Apply",bg="dark slate gray",fg="white",font="Arial 13",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=apply)
            self.button2.place(x=645,y=340,width =140,height=40)

            self.warning = tk.Label(text="",bg="white",fg="red",font="Arial 14")
            self.warning.place(x=500,y=400)

        def opening():
            kernel = np.ones((5,5),dtype=np.uint8)
            result = cv2.morphologyEx(self.img.astype(np.float32),cv2.MORPH_OPEN,kernel)
            cv2.imwrite("modified_photo.jpg",result)
            self.show_photo("modified_photo.jpg",8)

        def closing():
            kernel = np.ones((5,5),dtype=np.uint8)
            result = cv2.morphologyEx(self.img.astype(np.float32),cv2.MORPH_CLOSE,kernel)
            cv2.imwrite("modified_photo.jpg",result)
            self.show_photo("modified_photo.jpg",8)

        def gradient():
            kernel = np.ones((5,5),dtype=np.uint8)
            result = cv2.morphologyEx(self.img,cv2.MORPH_GRADIENT,kernel)
            cv2.imwrite("modified_photo.jpg",result)
            self.show_photo("modified_photo.jpg",8)

        control = self.upload_control()
        if control ==1: 
            self.delete_all_widget()
            self.img = cv2.imread(self.filename)
            self.main_screen.geometry("1000x605+"+str(int((self.screen_width-1000)/2))+"+"+str(int((self.screen_height-605)/2)))
            self.function_text = tk.Label(text="""Morphological\n                           Transformations""",bg="white",fg="dark slate gray",font="Times 30")
            self.function_text.place(x=340,y=60)

            self.button1 = tk.Button(text="Erosion",bg="dark slate gray",fg="white",font="Arial 14",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=erosion)
            self.button1.place(x=530,y=180,width =300,height=38)

            self.button2 = tk.Button(text="Dilation",bg="dark slate gray",fg="white",font="Arial 14",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=dilation)
            self.button2.place(x=530,y=240,width =300,height=38)

            self.button3 = tk.Button(text="Opening",bg="dark slate gray",fg="white",font="Arial 14",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=opening)
            self.button3.place(x=530,y=300,width =300,height=38)

            self.button4 = tk.Button(text="Closing",bg="dark slate gray",fg="white",font="Arial 14",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=closing)
            self.button4.place(x=530,y=360,width =300,height=38)

            self.button5 = tk.Button(text="Morphological Gradient",bg="dark slate gray",fg="white",font="Arial 14",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=gradient)
            self.button5.place(x=530,y=420,width =300,height=38)

    def gradient_detection(self):
        def horizontal():
            sobely = cv2.Sobel(self.img,ddepth=cv2.CV_16S,dx=0,dy=1,ksize=5)
            cv2.imwrite("modified_photo.jpg",sobely)
            self.show_photo("modified_photo.jpg",9)

        def vertical():
            sobelx = cv2.Sobel(self.img,ddepth=cv2.CV_16S,dx=1,dy=0,ksize=5)
            cv2.imwrite("modified_photo.jpg",sobelx)
            self.show_photo("modified_photo.jpg",9)

        def both():
            sobel_both = cv2.Laplacian(self.img,ddepth=cv2.CV_16S)
            cv2.imwrite("modified_photo.jpg",sobel_both)
            self.show_photo("modified_photo.jpg",9)

        control = self.upload_control()
        if control ==1: 
            self.delete_all_widget()
            self.img = cv2.imread(self.filename)
            self.main_screen.geometry("1000x605+"+str(int((self.screen_width-1000)/2))+"+"+str(int((self.screen_height-605)/2)))
            self.function_text = tk.Label(text="Choose what type to do the\ngradient detection.",bg="white",fg="dark slate gray",font="Times 24")
            self.function_text.place(x=500,y=110)

            self.button1 = tk.Button(text="Horizontal Direction",bg="dark slate gray",fg="white",font="Arial 14",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=horizontal)
            self.button1.place(x=530,y=230,width =300,height=38)

            self.button2 = tk.Button(text="Vertical Direction",bg="dark slate gray",fg="white",font="Arial 14",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=vertical)
            self.button2.place(x=530,y=290,width =300,height=38)

            self.button3 = tk.Button(text="Both Directions",bg="dark slate gray",fg="white",font="Arial 14",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=both)
            self.button3.place(x=530,y=350,width =300,height=38)

    def increase_contrast(self):
        control = self.upload_control()
        if control ==1: 
            self.delete_all_widget()
            self.img = cv2.imread(self.filename,0)

            eq_hist = cv2.equalizeHist(self.img)
            cv2.imwrite("modified_photo.jpg",eq_hist)
            self.show_photo("modified_photo.jpg",11)

    def turtle(self):
        turt = turtle.RawTurtle(self.signature)
        turt.speed(15)
        turt.penup();turt.goto(-80,35);turt.pendown();turt.right(90);turt.forward(20);turt.left(90);turt.forward(20);turt.left(90);turt.forward(20);turt.left(90);turt.forward(20);turt.left(90);turt.penup();turt.forward(20);turt.left(90);turt.forward(30);turt.left(90);turt.pendown();turt.forward(20);turt.right(135);turt.forward(20);turt.left(90);turt.forward(20);turt.right(135);turt.forward(20);turt.left(90);turt.penup();turt.forward(30);turt.pendown();turt.left(180);turt.forward(20);turt.right(90);turt.forward(10);turt.right(90);turt.forward(10);turt.right(180);turt.forward(10);turt.right(90);turt.forward(10);turt.right(90);turt.forward(20);turt.penup();turt.right(90);turt.forward(20);turt.left(90);turt.forward(10);turt.pendown();turt.left(90);turt.forward(20);turt.right(90);turt.forward(15);turt.right(90);turt.forward(10);turt.right(90);turt.forward(15);turt.left(150);turt.forward(18)

        turt.penup();turt.right(140);turt.forward(60);turt.pendown();turt.right(10);turt.forward(20);turt.left(90);turt.forward(10);turt.left(90);turt.forward(20);turt.right(90);turt.forward(10);turt.right(90);turt.forward(20);turt.right(180);turt.penup();turt.forward(50);turt.pendown();turt.right(180);turt.forward(20);turt.right(90);turt.forward(10);turt.right(90);turt.forward(10);turt.right(180);turt.forward(10);turt.right(90);turt.forward(10);turt.right(90);turt.forward(20);turt.penup();turt.right(90);turt.forward(20);turt.left(90);turt.forward(10);turt.pendown();turt.left(90);turt.forward(20);turt.right(135);turt.forward(20);turt.right(45);turt.forward(5);turt.left(180);turt.forward(20);turt.right(90);turt.penup();turt.forward(10);turt.pendown();turt.forward(20);turt.right(90);turt.forward(20);turt.right(90);turt.forward(20);turt.right(90);turt.forward(20);turt.penup();turt.right(90);turt.forward(30);turt.pendown();turt.right(90);turt.forward(20);turt.left(90);turt.forward(20);turt.penup();turt.forward(100)
 
    def page(self):
        self.signature = tk.Canvas(self.main_screen,width=200,height=80,bd=0,highlightthickness=0,relief='ridge',bg="white") 
        self.signature.place(x=790,y=530)
        self.signature.update()        

        self.main_screen.geometry("1000x605+"+str(int((self.screen_width-1000)/2))+"+"+str(int((self.screen_height-605)/2)))
        self.import_photo = tk.Button(text="Upload New Photo",bg="dark slate gray",fg="white",font="Arial 14",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=self.get_image)
        self.import_photo.place(x=10,y=10,width =300,height=38)

        self.show = tk.Button(text="Show Original Photo",bg="dark slate gray",fg="white",font="Arial 14",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=self.show_control)
        self.show.place(x=10,y=53,width =300,height=38)

        self.black_white = tk.Button(text="Black & White",bg="dark slate gray",fg="white",font="Arial 14",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=self.black_and_white)
        self.black_white.place(x=10,y=96,width =300,height=38)

        self.resize = tk.Button(text="Resize",bg="dark slate gray",fg="white",font="Arial 14",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=self.resize_image)
        self.resize.place(x=10,y=139,width =300,height=38)

        self.figure_text = tk.Button(text="Add Figure Or Text",bg="dark slate gray",fg="white",font="Arial 14",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=self.add_figure_text)
        self.figure_text.place(x=10,y=182,width =300,height=38)

        self.combine = tk.Button(text="Combine Pictures",bg="dark slate gray",fg="white",font="Arial 14",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command = self.combine_image)
        self.combine.place(x=10,y=225,width =300,height=38)

        self.mix = tk.Button(text="Mix Pictures",bg="dark slate gray",fg="white",font="Arial 14",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=self.mix_images)
        self.mix.place(x=10,y=268,width =300,height=38)

        self.thresholding = tk.Button(text="Thresholding",bg="dark slate gray",fg="white",font="Arial 14",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command = self.apply_threshold)
        self.thresholding.place(x=10,y=311,width =300,height=38)

        self.blurring = tk.Button(text="Blurring",bg="dark slate gray",fg="white",font="Arial 14",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command = self.blur_image)
        self.blurring.place(x=10,y=354,width =300,height=38)

        self.noise = tk.Button(text="Add Noise",bg="dark slate gray",fg="white",font="Arial 14",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command = self.add_noise_image)
        self.noise.place(x=10,y=397,width =300,height=38)

        self.morphological = tk.Button(text="Morphological Transformations",bg="dark slate gray",fg="white",font="Arial 14",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=self.morph_transform)
        self.morphological.place(x=10,y=440,width =300,height=38)

        self.gradient = tk.Button(text="Gradient",bg="dark slate gray",fg="white",font="Arial 14",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=self.gradient_detection)
        self.gradient.place(x=10,y=483,width =300,height=38)

        self.contrast = tk.Button(text="Increase Contrast Of \nThe Black And White Photo",bg="dark slate gray",fg="white",font="Arial 14",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=self.increase_contrast)
        self.contrast.place(x=10,y=526,width =300,height=58)

        self.button1 = tk.Button(text="Upload Photo",bg="dark slate gray",fg="white",font="Arial 12",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=self.turtle)
        self.button1.place(x=570,y=340,width =140,height=34)

        self.title1 = tk.Label(text="Welcome",bg="white",fg="dark slate gray",font="Times 60")
        self.title1.place(x=485,y=70)

        self.title2 = tk.Label(text="To Photo Editor",bg="white",fg="black",font="Arial 20")
        self.title2.place(x=550,y=150)

        self.title3 = tk.Label(text="Please Upload First Photo",bg="white",fg="black",font="Arial 16")
        self.title3.place(x=520,y=300)

        self.button1 = tk.Button(text="Upload Photo",bg="dark slate gray",fg="white",font="Arial 12",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=self.get_image)
        self.button1.place(x=570,y=340,width =140,height=34)

        self.main_screen.mainloop()

photo_editor = Editor()