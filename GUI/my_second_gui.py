import time
from pycricbuzz import Cricbuzz
from simple_colors import *
from tkinter import *
def fun():
    # url = "http://synd.cricbuzz.com/j2me/1.0/livematches.xml"
    # to extract the matches
    cric = Cricbuzz()
    details = cric.matches()
    # print(details)
    # To filter out the None objects from details
    details = filter(None, details)
    message = "No match in progress"
    for i in details:
        # traversing i
        if 'mchstate' in i:
            print('Series ==>' + i['srs'])  # List All Current Series
            # print('mchstate ==>' + i['mchstate'])  # List All Current Series
            if i['mchstate'] in ['inprogress','stump','rain'] and i['srs'] == 'Ranji Trophy 2019-20':
            # if i['mchstate'] == 'innings break':
            # if i['mchstate'] in ('inprogress','innings break'):
                id = i['id']
                main = cric.livescore(id)
                ms = main['batting']['score'][0]
                bat1 = main['batting']['batsman'][0]
                bat2 = main['batting']['batsman'][1]
                curr_bowler = main['bowling']['bowler'][0]
                # print(bat1['name'])
                # print(curr_bowler['name','overs','runs','wickets'])
                message = "\n" + i['srs'] + "      " + "\n" + "Format: " + i['type'] + "\n" + "Score: " + main['batting'][
                    'team'] + " " + ms['runs'] + '/' + ms['wickets'] + " (" + ms['overs'] + ")" + "\n" + bat1[
                              'name'] + ": " + bat1['runs'] + "(" + bat1['balls'] + ")   " + bat2['name'] + ": " + bat2[
                              'runs'] + "(" + bat2['balls'] + ")" + "\n" + curr_bowler['name'] + ": " + curr_bowler['overs'] + "-" + curr_bowler['runs'] + "-" + curr_bowler['wickets']
    # Generates the message
    print(message)
    return message
window = Tk() 				# Tk() is creating the window that you see and storing it inside the 'window' variable
window.geometry('300x400')  # This is the dimension of the window. Height and width (optional)
window.title("Vijesh's Window")		# To change the title of the window
lbl = Label(window, text = fun())
lbl.pack()
window.mainloop()			# Make sure the window stays and doesn't disappear.