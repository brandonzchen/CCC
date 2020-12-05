speedlimit=40
actualspeed=90
if speedlimit>actualspeed:
    print("Congradulations, you are within the speed limit!")
elif actualspeed-speedlimit<=20:
    print("You are speeding and your fine is $100")
elif actualspeed-speedlimit>=21 and actualspeed-speedlimit<=30:
    print("You are speeding and your fine is $270")
else:
    print("You are speeding and your fine is $500")
