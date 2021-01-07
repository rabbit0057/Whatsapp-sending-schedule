import sendwhappmsg
mobile_number =       #Enter a vaild mobile number with country code # provide a vaild whatapp mobile number 
message = "hi"  # create any message 
time_in_seconds = 10 # after how many seconds do you want the message to get triggered

# sendmsgafter(message_text, seconds)
# Open whatsapp share page after the seconds given to send given message to any contact.

sendwhappmsg.sendmsgtoafter(mobile_number,message,time_in_seconds) 