"""
8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. Write a
function called send_messages() that prints each text message and moves each message
to a new list called sent_messages as it is printed. After calling the function, print both of
your lists to make sure the messages were moved correctly.
"""
# old funcation
def show_messages(mesg):
    for mesgs in mesg:
        mesg_ = f"{mesgs.title()}!"
        print(mesg_)

# This is the new funcion that has 2 parmeter And pops the messages sent into the array
def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print("Sending message:", current_message)
        sent_messages.append(current_message)

message = ["Hello how are you", "Hows your Day going", "Welcome!"]
sent_messages = []

print("Messages:")
show_messages(message)
send_messages(message, sent_messages)
print("\nSent Messages:")
show_messages(sent_messages)