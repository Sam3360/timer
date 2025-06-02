import time
import math
import winsound # Import winsound for Windows specific sounds

def timer(total_seconds_float):
    """
    Counts down from a specified number of seconds, printing each second on a new line.
    Handles fractional total seconds by rounding up for display.
    Makes a 'buzz' sound at the end using winsound (Windows only).
    """
    total_seconds_int = math.ceil(total_seconds_float)

    while total_seconds_int > 0:
        mins, secs = divmod(total_seconds_int, 60)
        timer_display = f"{int(mins):02d}:{int(secs):02d}"
        print(timer_display)
        time.sleep(1)
        total_seconds_int -= 1
    
    print("Time's up!")

    try:
        winsound.Beep(2500, 500) # Play a 2500 Hz beep for 0.5 seconds
        time.sleep(0.1) # Short pause
        winsound.Beep(2500, 500) # Play it again
        time.sleep(0.1) # Short pause
        winsound.Beep(2500, 500) # Play it again
        time.sleep(0.1) # Short pause
        winsound.Beep(2500, 500) # Play it again
        time.sleep(0.1) # Short pause
    except AttributeError:
        # winsound is Windows-specific, so it will fail on other OSes.
        print('\a') 
        print('\a')
        print(" (Note: winsound is only available on Windows. Falling back to console bell.)")

if __name__ == "__main__":
    try:
        duration_minutes_float = float(input("Enter the duration of the timer in minutes (e.g., 0.5 for 30 seconds): "))
        
        if duration_minutes_float <= 0:
            print("Please enter a positive number of minutes.")
        else:
            total_seconds_calculated = duration_minutes_float * 60
            timer(total_seconds_calculated)
    except ValueError:
        print("Invalid input. Please enter a number (e.g., 5, 0.5, 10.75).")
