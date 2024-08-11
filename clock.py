# imports
import os
import time
from datetime import datetime

# clear terminal for show the new time
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# show the clock
def digital_clock():
    while True:
        clear_terminal()
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"""
         ██████╗██╗      ██████╗  ██████╗██╗  ██╗
        ██╔════╝██║     ██╔═══██╗██╔════╝██║ ██╔╝
        ██║     ██║     ██║   ██║██║     █████╔╝ 
        ██║     ██║     ██║   ██║██║     ██╔═██╗ 
        ╚██████╗███████╗╚██████╔╝╚██████╗██║  ██╗
         ╚═════╝╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝
        
        Current Time: {current_time}
        """)
        time.sleep(1)

if __name__ == "__main__":
    digital_clock()
