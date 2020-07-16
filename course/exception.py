
# try this block
try:
  number=123
  # this will not work: text + number ist invalid
  print("Hello" + number)
# do this, if the try-block did not work
except:    
  print("Something went wrong")
# clean up (optional)
finally:
  print("Call this always at the end")

