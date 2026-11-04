import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title="Time To Wake Up",
            message="The nightmare is over, and the darkness has lost its grip. It is time to wake up, stand tall, and conquer your day.",
            app_icon="timetowakeup.ico",
            timeout=6
        )

        time.sleep(10)