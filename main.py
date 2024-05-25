import datetime
import ctypes
import pandas as pd

# 'use cols' to read specific columns
df = pd.read_csv('data.csv', usecols=['date', 'name'])  # Successfully read the file

# d = datetime.datetime.now()  # Today's date
# dateTimeStr = str(d)            # Make it a string, so we can slice it to take only month and day

# today = dateTimeStr[5:10]       # Month and day only

today = datetime.date.today().strftime('%m-%d')


# Iterate over the 'date' column and check if it matches today's date
def main():
    for index, row in df.iterrows():
        if row['date'] == today:
            WS_EX_TOPMOST = 0x40000
            windowTitle = "Birthday Reminder"
            message = f"Today is {row['name']}'s birthday, don't forget to call him/her ;)"

            ctypes.windll.user32.MessageBoxExW(None, message, windowTitle, WS_EX_TOPMOST)

        # print(f"Today is {row['name']}'s birthday")


# And finally display a message in the user's desktop (only if there's a birthday) every time the computer starts

if __name__ == "__main__":
    main()
