from pystyle import *
print(Box.Lines("[+] This program for login page"))

# Print a message with purple-to-red gradient color
Write.Print("Write user name and password: \n\n", Colors.purple_to_red, interval=0.2)

print(Box.DoubleCube("Example [1]"))

while True:
    # Input for username and password with blue-to-green gradient color
    username = Write.Input("Enter your username:", Colors.blue_to_green, interval=0.4)
    password = Write.Input("Enter your password:", Colors.blue_to_green, interval=0.4)

    if username == "admin" and password == "admin123":
        # Print a welcome message for successful login with green color
        Write.Print("[+] welcome admin [+]\n", Colors.green, interval=0.1)
        input("press any key to exit...")
    else:
        # Print an error message for failed login attempt with red color
        Write.Print("[-] Error try again [-] \n\n", Colors.red, interval=0.1)
