from tkinter import *
from tkinter import ttk  
import requests  


def data_get():
    city = city_name.get()  
    data = requests.get(
        "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=6d9728d107cce7518f2bc406685fa336"
    ).json()
    w1_label.config(text=data["weather"][0]["main"])  
    wd1_label.config(text=data["weather"][0]["description"])
    temp_in_kelvin = data["main"]["temp"]
    temp_in_celsius = float(temp_in_kelvin) - 273.15
    wt_label1.config(text=str(temp_in_celsius))
    wp_label1.config(text=data["main"]["pressure"])


win = Tk()
win.title("Weather app")
win.config(bg="#87CEEB")  
win.geometry("600x600")
name_label = Label(win, text="Weather app", font=("Times New Roman", 30, "bold"))
name_label.place(x=25, y=50, height=50, width=550)  

list_name = [
    "Andhra Pradesh", "Arunachal Pradesh ", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana",
    "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra",
    "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu",
    "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal", "Andaman and Nicobar Islands",
    "Chandigarh", "Dadra and Nagar Haveli", "Daman and Diu", "Lakshadweep", "National Capital Territory of Delhi",
    "Puducherry"
]  

city_name = StringVar()  
com = ttk.Combobox(
    win, text="Weather app", values=list_name, font=("Times New Roman", 20, "bold"), textvariable=city_name
)  
com.place(x=25, y=125, height=50, width=550)  


done_button = Button(win, text="Done", font=("Times New Roman", 20, "bold"), command=data_get) 
done_button.place(x=250, y=190, height=50, width=100)

w_label = Label(win, text="Weather Climate", font=("Times New Roman", 20))
w_label.place(x=25, y=260, height=50, width=250)  


w1_label = Label(win, text="", font=("Times New Roman", 20))
w1_label.place(x=300, y=260, height=50, width=250) 


wd_label = Label(win, text="Description", font=("Times New Roman", 19))
wd_label.place(x=25, y=330, height=50, width=250)  

wd1_label = Label(win, text="", font=("Times New Roman", 19))
wd1_label.place(x=300, y=330, height=50, width=250)  


wt_label = Label(win, text="Temparature", font=("Times New Roman", 20))
wt_label.place(x=25, y=398, height=50, width=250)  


wt_label1 = Label(win, text="", font=("Times New Roman", 20))
wt_label1.place(x=300, y=398, height=50, width=250)  


wp_label = Label(win, text="Pressure", font=("Times New Roman", 20))
wp_label.place(x=25, y=470, height=50, width=250)  


wp_label1 = Label(win, text="", font=("Times New Roman", 20))
wp_label1.place(x=300, y=470, height=50, width=250)  

win.mainloop()
