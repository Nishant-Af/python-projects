from tkinter import * 
import speedtest 

def speedchecker(): 
    # Initialize the client
    sp = speedtest.Speedtest(secure=True) 
    
    # Getting the server
    sp.get_best_server() 
    
    # (10**6 converts bits to Megabits) 
    down_speed = round(sp.download() / (10**6), 2) 
    up_speed = round(sp.upload() / (10**6), 2) 
    down_str = f"{down_speed} Mbps" 
    up_str = f"{up_speed} Mbps" 
    
    # Update your Tkinter Label widgets 
    # BUG FIX: Target the specific 'lab_down_val' and 'lab_up_val' widgets
    lab_down_val.config(text=down_str) 
    lab_up_val.config(text=up_str) 

root = Tk() 
root.title("Internet Speed Test") 
root.geometry("500x600") 
root.config(bg="#121212") 

lab = Label(root, text="Internet Speed Test", font=("Segoe UI", 30, "bold")) 
lab.place(x = 60, y = 40, height=50, width=380) 

lab_download = Label(root, text="Download Speed", font=("Segoe UI", 30, "bold")) 
lab_download.place(x = 60, y = 130, height=50, width=380) 

# BUG FIX: Named this uniquely so it doesn't get overwritten by the next 'lab' variable
lab_down_val = Label(root, text="00", font=("Segoe UI", 30, "bold")) 
lab_down_val.place(x = 60, y = 200, height=50, width=380) 

lab_upload = Label(root, text="Upload Speed", font=("Segoe UI", 30, "bold")) 
lab_upload.place(x = 60, y = 290, height=50, width=380) 

# BUG FIX: Named this uniquely so it doesn't get overwritten by the button's 'lab' variable
lab_up_val = Label(root, text="00", font=("Segoe UI", 30, "bold")) 
lab_up_val.place(x = 60, y = 360, height=50, width=380) 

# BUG FIX: Changed command from the module name 'speedtest' to your function name 'speedchecker'
button = Button(root, text="Click To Check Speed", font=("Segoe UI", 20, "bold"), relief=RAISED, bg="red", command=speedchecker) 
button.place(x = 60, y = 450, height=50, width=380) 

root.mainloop()
