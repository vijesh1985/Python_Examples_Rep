from tkinter import * 		# Importing the Tkinter package
# import live_score as ls
window = Tk() 				# Tk() is creating the window that you see and storing it inside the 'window' variable
window.geometry('300x400')  # This is the dimension of the window. Height and width (optional)
window.title("Vijesh's Window")		# To change the title of the window
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)
window.mainloop()			# Make sure the window stays and doesn't disappear.