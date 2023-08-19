"""
8-9. Messages: Make a list containing a series of short text messages. Pass the list to a
function called show_messages(), which prints each text message.
"""
#This funcation make a parmenter and Passing a List
def show_messages(mesg):
    for mesgs in mesg:
        mesg_ = f"{mesgs.title()}!"
        print(mesg_)
#This is an list with a list of message
message = ["Hello how are you", "Hows your Day going", "Welcome!"]
#This prints out the list from message variable.
show_messages(message)