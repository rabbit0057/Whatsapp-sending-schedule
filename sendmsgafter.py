import sendwhappmsg
message = "hi"  # create any message 
time_in_seconds = 10 # after how many seconds do you want the message to get triggered

# sendmsgafter(message_text, seconds)
# Open whatsapp share page after the seconds given to send given message to any contact.

sendwhappmsg.sendmsgafter(message,time_in_seconds) 