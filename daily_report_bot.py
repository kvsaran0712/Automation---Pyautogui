
# daily_report_bot.py

import pyautogui
import subprocess
import time
from datetime import datetime

# Safety pause
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

# Generate date/time
now = datetime.now()
current_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
current_date = now.strftime("%Y-%m-%d")

excel_file = f"daily_report_{current_date}.xlsx"
screenshot_file = f"daily_report_{current_date}.png"

# -----------------------------------------
# Step 1: Open Chrome
# -----------------------------------------
subprocess.Popen("start chrome", shell=True)
time.sleep(5)

# Open a public website
pyautogui.hotkey("ctrl", "l")
pyautogui.write("https://finance.yahoo.com", interval=0.05)
pyautogui.press("enter")
time.sleep(8)

# Example fetched value
fetched_data = "Yahoo Finance Opened"

# -----------------------------------------
# Step 2: Open Excel
# -----------------------------------------
subprocess.Popen("start excel", shell=True)
time.sleep(10)

# Create headers
pyautogui.write("Date & Time")
pyautogui.press("tab")
pyautogui.write("Data")
pyautogui.press("tab")
pyautogui.write("Comment")

# Move to next row
pyautogui.press("enter")

# Data row
pyautogui.write(current_datetime)
pyautogui.press("tab")

pyautogui.write(fetched_data)
pyautogui.press("tab")

pyautogui.write("Daily information captured successfully")

# -----------------------------------------
# Step 3: Save workbook
# -----------------------------------------
pyautogui.hotkey("ctrl", "s")
time.sleep(3)

pyautogui.write(excel_file)
time.sleep(1)

pyautogui.press("enter")
time.sleep(3)

# -----------------------------------------
# Step 4: Screenshot final sheet
# -----------------------------------------
screenshot = pyautogui.screenshot()
screenshot.save(screenshot_file)

print(f"Excel File Saved: {excel_file}")
print(f"Screenshot Saved: {screenshot_file}")