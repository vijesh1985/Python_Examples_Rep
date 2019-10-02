import baloontip
# ICON_PATH = "C:\Users\vijes\PycharmProjects\Python_Rep\icons\cricbuzz_icon.png"
# initialise baloontip.py
baloontip.__init__('Test App')
# create Notification object
n = baloontip.balloon_tip("Hi There","This is Just a Test Message!!!")
n.show()