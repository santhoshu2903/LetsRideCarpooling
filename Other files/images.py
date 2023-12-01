
from PIL import Image
import customtkinter

app = customtkinter.CTk()  # create a CTk window

#window size
app.geometry("1050x600")

my_image = customtkinter.CTkImage(light_image=Image.open("images/welcome.jpg"),
                                  dark_image=Image.open("images/welcome.jpg"),
                                  size=(1050,650))

image_label = customtkinter.CTkLabel(app, image=my_image, text="")  # display image with a CTkLabel

image_label.pack()

#button upon image
button = customtkinter.CTkButton(app, text="Login", command=lambda: app.change_theme("dark"))
button.place(x=500, y=500)


app.mainloop()  # start the app