from tkinter import *
import threading
import psutil      # pip install psutil
import speedtest   # pip install speedtest-cli

BG = "#121212"
FG = "#FFFFFF"
GREEN = "#00E676"
BLUE = "#40C4FF"
FONT = "Segoe UI"

# ---------------------------------------------------------------
# LIVE SPEED MONITOR
# Every second we check how many bytes your PC has received/sent in
# total, subtract the previous reading, and convert to Mbps.
# ---------------------------------------------------------------
counters = psutil.net_io_counters()
last_recv = counters.bytes_recv
last_sent = counters.bytes_sent


def update_live_speed():
    global last_recv, last_sent

    now = psutil.net_io_counters()
    # bytes in the last second -> bits (x8) -> megabits (/10**6)
    down_mbps = (now.bytes_recv - last_recv) * 8 / 10**6
    up_mbps = (now.bytes_sent - last_sent) * 8 / 10**6
    last_recv, last_sent = now.bytes_recv, now.bytes_sent

    live_down_val.config(text=f"{down_mbps:.2f} Mbps")
    live_up_val.config(text=f"{up_mbps:.2f} Mbps")

    # Run again in 1000 ms (this is the "real time" loop)
    root.after(1000, update_live_speed)


# ---------------------------------------------------------------
# FULL SPEED TEST (runs in a background thread so the UI stays alive)
# ---------------------------------------------------------------
def run_speedtest():
    try:
        root.after(0, lambda: status_label.config(text="Finding best server...", fg=BLUE))
        sp = speedtest.Speedtest(secure=True)
        sp.get_best_server()

        root.after(0, lambda: status_label.config(text="Testing download...", fg=BLUE))
        down = round(sp.download() / 10**6, 2)

        root.after(0, lambda: status_label.config(text="Testing upload...", fg=BLUE))
        up = round(sp.upload() / 10**6, 2)

        root.after(0, lambda: test_down_val.config(text=f"{down} Mbps"))
        root.after(0, lambda: test_up_val.config(text=f"{up} Mbps"))
        root.after(0, lambda: status_label.config(text="Test complete!", fg=GREEN))
    except Exception as e:
        root.after(0, lambda: status_label.config(text=f"Error: {e}", fg="#FF5252"))
    finally:
        root.after(0, lambda: button.config(state=NORMAL))


def speedchecker():
    button.config(state=DISABLED)   # stop double clicks
    threading.Thread(target=run_speedtest, daemon=True).start()


# ---------------------------------------------------------------
# UI
# ---------------------------------------------------------------
root = Tk()
root.title("Internet Speed Test")
root.geometry("500x720")
root.config(bg=BG)


def make_label(text, y, size=20, color=FG, bold=True):
    lbl = Label(root, text=text, font=(FONT, size, "bold" if bold else "normal"),
                bg=BG, fg=color)
    lbl.place(x=40, y=y, height=45, width=420)
    return lbl


make_label("Internet Speed Test", 15, size=28)

# --- Live section ---
make_label("LIVE (updates every second)", 75, size=12, color="#9E9E9E", bold=False)
make_label("Download", 105, size=16)
live_down_val = make_label("0.00 Mbps", 145, size=26, color=GREEN)
make_label("Upload", 205, size=16)
live_up_val = make_label("0.00 Mbps", 245, size=26, color=GREEN)

# --- Speed test section ---
make_label("SPEED TEST RESULT", 320, size=12, color="#9E9E9E", bold=False)
make_label("Download", 350, size=16)
test_down_val = make_label("00", 390, size=26, color=BLUE)
make_label("Upload", 450, size=16)
test_up_val = make_label("00", 490, size=26, color=BLUE)

status_label = make_label("Ready", 550, size=12, color="#9E9E9E", bold=False)

button = Button(root, text="Click To Check Speed", font=(FONT, 18, "bold"),
                relief=RAISED, bg="red", fg="white", command=speedchecker)
button.place(x=60, y=610, height=55, width=380)

update_live_speed()   # start the live loop
root.mainloop()