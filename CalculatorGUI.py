import tkinter as tk

# define a function to calculate the score
def calculate_score():
    try:
        # get input values from the entry fields
        player_name = name_entry.get()
        time_given = time_entry.get()
        progress_percent = float(progress_entry.get())
        rank = int(rank_entry.get())

        # convert time_given to seconds
        time_list = time_given.split()
        time_seconds = 0
        for i in time_list:
            if i.endswith("s"):
                time_seconds += int(i[:-1])
            elif i.endswith("m"):
                time_seconds += int(i[:-1]) * 60

        # check if time_taken is within range
        if time_seconds < 0 or time_seconds > 900:
            raise ValueError("time_taken should be between 0 and 15 minutes (900 seconds).")

        # check if progress_percent is within range
        if progress_percent < 0 or progress_percent > 100:
            raise ValueError("progress_percent should be between 0 and 100.")

        # calculate the score for the round
        if time_seconds == 0:
            score = 0
        else:
            score = int(10000.0 / time_seconds * progress_percent * (16 - rank) / 15)

        # display the score in the label
        score_label.config(text=f"The score for the round is {score}.")

    except ValueError as e:
        # display an error message in the label
        score_label.config(text=f"Error: {e}")
    except ZeroDivisionError:
        # display an error message in the label
        score_label.config(text="Error: time_taken cannot be zero.")

# create a tkinter window
window = tk.Tk()
window.title("Clash of Code Score Calculator")

# set the window size and center it on the screen
window.geometry("600x400")
window.eval('tk::PlaceWindow . center')

# create entry fields for input values
name_label = tk.Label(window, text="Player Name:")
name_label.place(relx=0.3, rely=0.1, anchor="center")
name_entry = tk.Entry(window)
name_entry.place(relx=0.7, rely=0.1, anchor="center")

time_label = tk.Label(window, text="Time Taken:")
time_label.place(relx=0.3, rely=0.2, anchor="center")
time_entry = tk.Entry(window)
time_entry.place(relx=0.7, rely=0.2, anchor="center")

progress_label = tk.Label(window, text="Progress Percent:")
progress_label.place(relx=0.3, rely=0.3, anchor="center")
progress_entry = tk.Entry(window)
progress_entry.place(relx=0.7, rely=0.3, anchor="center")

rank_label = tk.Label(window, text="Rank:")
rank_label.place(relx=0.3, rely=0.4, anchor="center")
rank_entry = tk.Entry(window)
rank_entry.place(relx=0.7, rely=0.4, anchor="center")

# create a button to calculate the score
calculate_button = tk.Button(window, text="Calculate Score", command=calculate_score)
calculate_button.place(relx=0.5, rely=0.6, anchor="center")

# create a label to display the score
score_label = tk.Label(window, text="")
score_label.place(relx=0.5, rely=0.8, anchor="center")

# run the tkinter event loop
window.mainloop()
