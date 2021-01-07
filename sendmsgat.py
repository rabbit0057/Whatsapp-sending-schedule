import sendwhappmsg
message = "hi"  # create any message 
time_in_hours = 1 #after how many hours do you want the message to get triggered
time_in_minutes = 10 #after how many minutes do you want the message to get triggered
time_in_seconds = 30 # after how many seconds do you want the message to get triggered

# sendmsgat(message_text, hour, minutes, seconds='00')
# Open whatsapp share page at a given time to send given message to any contact.

sendwhappmsg.sendmsgat(message,time_in_hours,time_in_minutes,time_in_seconds) 