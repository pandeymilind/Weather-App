from import_ import *
root=Tk()
root.title("Weather App")
root.geometry("890x470+300+200")
root.configure(bg="#57adff")
root.resizable(False,False)

image_icon=PhotoImage(file="image/sun.png")
root.iconphoto(False,image_icon)

def image_(url,size):
    img=Image.open(url)
    resized_image= img.resize(size)
    img= ImageTk.PhotoImage(resized_image)
    return img


def getweather():
    city=search_text.get()
    geolocator=Nominatim(user_agent="geoapiExercises")
    location=geolocator.geocode(city)
    obj=TimezoneFinder()
    result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
    timezone.config(text=result)
    lat=location.latitude
    lon=location.longitude
    long_lat.config(text=f"{round(lat)} °N   {round(lon)} °E")

    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M %p")
    clock.config(text=current_time)

    #weather
    #api_key from mpandey.org@gmail.com
    api_key="f0a6af23e1a11d3601a0eff6a6938f15"
    api_url=f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units=metric&exclude=hourly&appid={api_key}"
    json_data=requests.get(api_url).json()
    temp=json_data["current"]["temp"]
    humidity = json_data["current"]["humidity"]
    pressure = json_data["current"]["pressure"]
    wind = json_data["current"]["wind_speed"]
    description = json_data["current"]["weather"][0]["description"]
    temp_detail.config(text=(round(temp),"°C"))
    humidity_detail.config(text=(humidity,"%"))
    pressure_detail.config(text=(pressure,"hpa"))
    wind_speed_detail.config(text=(wind,"m/s"))
    description_detail.config(text=(description))
    #weather image for cell
    img1=json_data["daily"][0]["weather"][0]['icon']
    photo1=ImageTk.PhotoImage(file=f"weather_icon/{img1}@2x.png")
    firstimage.config(image=photo1)
    firstimage.image=photo1

    tempd1=json_data['daily'][0]["temp"]['day']
    tempn1=json_data['daily'][0]["temp"]['night']
    day1temp.config(text=f"Day : {tempd1}\n Night : {tempn1}")

    
    img2=json_data["daily"][1]["weather"][0]['icon']
    photo2=image_(f"weather_icon/{img2}@2x.png",(50,50))
    secondimage.config(image=photo2)
    secondimage.image=photo2
    
    tempd2=json_data['daily'][0]["temp"]['day']
    tempn2=json_data['daily'][0]["temp"]['night']
    day2temp.config(text=f"Day:{tempd2}\nNight:{tempn2}")

    
    img3=json_data["daily"][2]["weather"][0]['icon']
    photo3=image_(f"weather_icon/{img3}@2x.png",(50,50))
    thirdimage.config(image=photo3)
    thirdimage.image=photo3
    
    tempd3=json_data['daily'][0]["temp"]['day']
    tempn3=json_data['daily'][0]["temp"]['night']
    day3temp.config(text=f"Day:{tempd3}\nNight:{tempn3}")

    
    img4=json_data["daily"][3]["weather"][0]['icon']
    photo4=image_(f"weather_icon/{img4}@2x.png",(50,50))
    fouthimage.config(image=photo4)
    fouthimage.image=photo4
    
    tempd4=json_data['daily'][0]["temp"]['day']
    tempn4=json_data['daily'][0]["temp"]['night']
    day4temp.config(text=f"Day:{tempd4}\nNight:{tempn4}")

    
    img5=json_data["daily"][4]["weather"][0]['icon']
    photo5=image_(f"weather_icon/{img5}@2x.png",(50,50))
    fifthimage.config(image=photo5)
    fifthimage.image=photo5
    
    tempd5=json_data['daily'][0]["temp"]['day']
    tempn5=json_data['daily'][0]["temp"]['night']
    day5temp.config(text=f"Day:{tempd5}\nNight:{tempn5}")

    
    img6=json_data["daily"][5]["weather"][0]['icon']
    photo6=image_(f"weather_icon/{img6}@2x.png",(50,50))
    sixthimage.config(image=photo6)
    sixthimage.image=photo6
    
    tempd6=json_data['daily'][0]["temp"]['day']
    tempn6=json_data['daily'][0]["temp"]['night']
    day6temp.config(text=f"Day:{tempd6}\nNight:{tempn6}")

    
    img7=json_data["daily"][6]["weather"][0]['icon']
    photo7=image_(f"weather_icon/{img7}@2x.png",(50,50))
    seventhimage.config(image=photo7)
    seventhimage.image=photo7
    
    tempd7=json_data['daily'][0]["temp"]['day']
    tempn7=json_data['daily'][0]["temp"]['night']
    day7temp.config(text=f"Day:{tempd7}\nNight:{tempn7}")

    
    #days
    first=datetime.now()
    day1.config(text=first.strftime("%A"))
    second = first+timedelta(days=1)
    day2.config(text=second.strftime("%A"))

    third = first+timedelta(days=2)
    day3.config(text=third.strftime("%A"))

    fouth = first+timedelta(days=3)
    day4.config(text=fouth.strftime("%A"))

    fifth = first+timedelta(days=4)
    day5.config(text=fifth.strftime("%A"))

    sixth = first+timedelta(days=5)
    day6.config(text=sixth.strftime("%A"))

    seventh = first+timedelta(days=6)
    day7.config(text=seventh.strftime("%A"))



#search bar
search_image=image_("image/search bar_1.png",(300,50))
search_=Label(image=search_image,bg="#57adff")
search_.place(x=270,y=20)
#search text
search_text=Entry(root,justify="right",width=15,font=("poppins",20,"bold"),bg="#203652",border=0,fg="white")
search_text.place(x=300,y=30)
search_text.focus()
#Search bar style image
search_style_image=image_("image/sun.png",(40,40))
search_style=Label(root,image=search_style_image,bg="#203652")
search_style.place(x=280,y=25)
#search button
search_icon_=image_("image/Search_icon_.png",(50,50))
search_button=Button(image=search_icon_,borderwidth=0,cursor="hand2",bg="#57adff",command=getweather)
search_button.place(x=530,y=21)
#Weather detail
img=image_("image/rectangle_2_.png",(260,154))
Label(root,image=img,bg="#57adff").place(x=30,y=110)

temp=Label(root,text="Temperature",font=("Helvetica",11),fg="white",bg="black")
temp.place(x=50,y=120)

humidity=Label(root,text="Humidity",font=("Helvetica",11),fg="white",bg="black")
humidity.place(x=50,y=150)

pressure=Label(root,text="Pressure",font=("Helvetica",11),fg="white",bg="black")
pressure.place(x=50,y=180)

wind_speed=Label(root,text="Wind Speed",font=("Helvetica",11),fg="white",bg="black")
wind_speed.place(x=50,y=210)

description=Label(root,text="Description",font=("Helvetica",11),fg="white",bg="black")
description.place(x=50,y=240)


#botom box
frame=Frame(root,width=900,height=180,bg="#212120")
frame.pack(side=BOTTOM)

#bottom boxes
#3e3e3e
firstbox=image_("image/rectangle_3_.png",(250,154))
Label(frame,image=firstbox,bg="#212120").place(x=30,y=13)
secondbox = image_("image/Rectangle_5.png",(90,130))
Label(frame,image=secondbox,bg="#212120").place(x=295,y=24)
Label(frame,image=secondbox,bg="#212120").place(x=395,y=24)
Label(frame,image=secondbox,bg="#212120").place(x=495,y=24)
Label(frame,image=secondbox,bg="#212120").place(x=595,y=24)
Label(frame,image=secondbox,bg="#212120").place(x=695,y=24)
Label(frame,image=secondbox,bg="#212120").place(x=795,y=24)
#clock
clock=Label(root,font=("Helvetica",30,"bold"),fg="white",bg="#57adff")
clock.place(x=30,y=20)
#timeZOne
timezone=Label(root,font=("Helvetica",15,"bold"),fg="white",bg="#57adff")
timezone.place(x=700,y=20)
long_lat=Label(root,font=("Helvetica",10,"bold"),fg="white",bg="#57adff")
long_lat.place(x=700,y=50)

#thpwd
temp_detail=Label(root,font=("Helvetica",11),fg="white",bg="black")
temp_detail.place(x=150,y=120)

humidity_detail=Label(root,font=("Helvetica",11),fg="white",bg="black")
humidity_detail.place(x=150,y=150)

pressure_detail=Label(root,font=("Helvetica",11),fg="white",bg="black")
pressure_detail.place(x=150,y=180)
wind_speed_detail=Label(root,font=("Helvetica",11),fg="white",bg="black")
wind_speed_detail.place(x=150,y=210)
description_detail=Label(root,font=("Helvetica",11),fg="white",bg="black")
description_detail.place(x=150,y=240)


#first cell
firstframe=Frame(frame,width=235,height=146,bg='#3e3e3e')
firstframe.place(x=40,y=19)

day1=Label(firstframe,font="arial 18",fg="white",bg="#3e3e3e")
day1.place(x=100,y=5)

firstimage=Label(firstframe,bg="#3e3e3e")
firstimage.place(x=1,y=15)

day1temp=Label(firstframe,bg="#3e3e3e",fg="#57adff",font="arial 15 bold")
day1temp.place(x=100,y=50)

#second cell
secondframe=Frame(frame,width=77,height=117,bg='#3e3e3e')
secondframe.place(x=304,y=33)

day2=Label(secondframe,bg="#3e3e3e",fg="white")
day2.place(x=10,y=5)

secondimage=Label(secondframe,bg="#3e3e3e")
secondimage.place(x=7,y=23)

day2temp=Label(secondframe,bg="#3e3e3e",fg="#57adff")
day2temp.place(x=10,y=70)
#third cell
thirdframe=Frame(frame,width=77,height=117,bg='#3e3e3e')
thirdframe.place(x=404,y=33)

day3=Label(thirdframe,bg="#3e3e3e",fg="white")
day3.place(x=10,y=5)

thirdimage=Label(thirdframe,bg="#3e3e3e")
thirdimage.place(x=7,y=23)

day3temp=Label(thirdframe,bg="#3e3e3e",fg="#57adff")
day3temp.place(x=10,y=70)
##fouth cell
fouthframe=Frame(frame,width=77,height=117,bg='#3e3e3e')
fouthframe.place(x=504,y=33)

day4=Label(fouthframe,bg="#3e3e3e",fg="white")
day4.place(x=10,y=5)

fouthimage=Label(fouthframe,bg="#3e3e3e")
fouthimage.place(x=9,y=23)

day4temp=Label(fouthframe,bg="#3e3e3e",fg="#57adff")
day4temp.place(x=10,y=70)

##fifth cell
fifthframe=Frame(frame,width=77,height=117,bg='#3e3e3e')
fifthframe.place(x=604,y=33)

day5=Label(fifthframe,bg="#3e3e3e",fg="white")
day5.place(x=10,y=5)

fifthimage=Label(fifthframe,bg="#3e3e3e")
fifthimage.place(x=7,y=23)

day5temp=Label(fifthframe,bg="#3e3e3e",fg="#57adff")
day5temp.place(x=10,y=70)
##sixth cell
sixthframe=Frame(frame,width=77,height=117,bg='#3e3e3e')
sixthframe.place(x=704,y=33)

day6=Label(sixthframe,bg="#3e3e3e",fg="white")
day6.place(x=10,y=5)

sixthimage=Label(sixthframe,bg="#3e3e3e")
sixthimage.place(x=9,y=23)

day6temp=Label(sixthframe,bg="#3e3e3e",fg="#57adff")
day6temp.place(x=10,y=70)
##seventh cell
seventhframe=Frame(frame,width=77,height=117,bg='#3e3e3e')
seventhframe.place(x=804,y=33)
day7=Label(seventhframe,bg="#3e3e3e",fg="white")
day7.place(x=10,y=5)

seventhimage=Label(seventhframe,bg="#3e3e3e")
seventhimage.place(x=9,y=23)

day7temp=Label(seventhframe,bg="#3e3e3e",fg="#57adff")
day7temp.place(x=10,y=70)
##test
##day1.config(text="Wednesday")
##day2.config(text="Wednesday")
##day3.config(text="Wednesday")
##day4.config(text="Wednesday")
##day5.config(text="Wednesday")
##day6.config(text="Wednesday")
##day7.config(text="Wednesday")
root.mainloop()
