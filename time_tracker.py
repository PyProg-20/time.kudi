import datetime
import time
import csv
time_task_started = '11:00'
time_task_completed = '12:00'
current_time = '10:00'
time_n = (2020, 7, 30, 23, 30, 4, 3, 212, 0)
time_hour_started = 0
time_minute_started = 0
time_hour_completed = 0
time_minute_completed = 0
response = "Waiting"
task = "Waiting"
time_task_continue = 0
time_hour_continue = 0
time_minute_continue = 0
hour_used_before_break = 0
minute_used_after_break = 0
minute_used_before_break = 0
world_start = ""
world_end = ""

def taskInput():
    #Function to take the name of the task and if the user is ready to start the task
    global task, response
    task = input("Type the description(name) of the task you want to track: ").capitalize().strip()
    print("Ready to get started with the task? Yes or No?")
    response = input("Answer: ")
    if response.strip().capitalize() == "Yes":
        now_start = datetime.datetime.now()
        date_task_started = now_start.strftime('%Y-%m-%d')
        #global world_start = date_task_started
        tell_time()
        global time_hour_started
        global time_minute_started
        time_hour_started = int(time.strftime("%I", time_n))
        time_minute_started = int(time.strftime("%M", time_n))
        print(f"You are beginning this task on {date_task_started} at {current_time}")
        completed_Task()
    while response.strip().capitalize() == "No":
        print("Come back when you are ready to start the task")
        print("Ready to get started with the task? Yes or No?")
        response = input("Answer: ")
        if response.strip().capitalize() == "Yes":
          now_start = datetime.datetime.now()
          date_task_started = now_start.strftime('%Y-%m-%d')
          tell_time()
          time_hour_started
          time_minute_started
          time_hour_started = int(time.strftime("%I", time_n))
          time_minute_started = int(time.strftime("%M", time_n))
          print(f"You are beginning this task on {date_task_started} at {current_time}")
          completed_Task()

def completed_Task():
    print("Type Break if you want to go on a break or Done when you are completely done with the task.")
    global response
    response = input("Your response: ")
    if response.strip().capitalize() == "Done":
        now_done = datetime.datetime.now()
        global date_time_task_completed
        #global time_task_completed
        date_task_completed = now_done.strftime('%Y-%m-%d')
        tell_time()
        global time_hour_completed, time_minute_completed
        time_hour_completed = int(time.strftime("%I", time_n))
        time_minute_completed = int(time.strftime("%M", time_n))
        print(f"You completed the task on {date_task_completed} at {current_time}")
        time_task_lasted_calculator()
    if response.capitalize().strip() == "Break":
        breakTask()

def time_task_lasted_calculator():
    global time_task_started, time_task_completed, time_hour_completed
    global time_minute_completed, time_minute_started, time_hour_started
    now_done = datetime.datetime.now()
    time_task_completed = now_done.strftime('%H:%M')
    tell_time()
    total_hours_for_task = abs(time_hour_completed - time_hour_started)
    total_minutes_for_task = abs(time_minute_completed - time_minute_started)
    total_time_spent_on_task = (total_minutes_for_task/60) + total_hours_for_task
    money_to_be_paid = 5*total_time_spent_on_task
    print(f"Hours taken for completion of the task was {total_hours_for_task}")
    print(f"Minutes taken for completion of the task was {total_minutes_for_task}")
    print("Based on the total time you spent on the task, your pay is %.2f" %money_to_be_paid)

def tell_time():
    #This function tells the current time
    global current_time, time_n
    time_n = time.gmtime()
    current_time = time.strftime("%I:%M %p", time_n)  # %I= prints the hour, %M= gives the minutes, %P= prints AM or PM
    time_hour = int(time.strftime("%I", time_n))
    time_minute = int(time.strftime("%M", time_n))

def breakTask():
    global response, time_hour_started, time_minute_started, task
    global time_task_continue, time_minute_continue, time_hour_continue
    global hour_used_before_break, minute_used_before_break
    response = input("Your response: ")
    tell_time()
    breakFunction()

def breakFunction():
    global response, time_task_continue, time_minute_continue
    global time_hour_continue, hour_used_before_break, minute_used_before_break
    now_break = datetime.datetime.now()
    tell_time()
    number_of_breaks = 0
    while response.capitalize().strip() == "Break":
        break_date = now_break.strftime('%Y-%m-%d')
        break_time = current_time
        time_hour_break = int(time.strftime("%I", time_n))
        time_minute_break = int(time.strftime("%M", time_n))
        print(f"You are going on a break from your ongoing task on {break_date} at {break_time}")
        hour_used_before_break = time_hour_break - time_hour_started
        minute_used_before_break = time_minute_break - time_minute_started
        print(
            f"You worked on the project for {hour_used_before_break} hours, {minute_used_before_break} minute before going on a break at {break_time}")
        print("Are you ready to continue with your uncompleted task? Yes? or No?")
        response = input("Your response: ")
        if response.capitalize().strip() == "Yes":
            responseYes()
            response = input("Your response: ")
            whenDone()
        while response.strip().capitalize() == "No":
            print("Come back another time when you are ready to finish your uncompleted task.")
            print("Ready to continue the uncompleted task? Yes or No?")
            response = input("Your response: ")
            number_of_breaks += 1
            if response.capitalize().strip() == "Yes":
                responseYes()
                response = input("Your response: ")
                whenDone()

def responseYes():
    global response, time_task_continue, time_minute_continue
    global time_hour_continue, hour_used_before_break, minute_used_before_break
    tell_time()
    now_continue = datetime.datetime.now()
    date_task_continue = now_continue.strftime('%Y-%m-%d')
    time_task_continue = current_time
    time_hour_continue = int(time.strftime("%I", time_n))
    time_minute_continue = int(time.strftime("%M", time_n))
    print(f"You are continuing at {date_task_continue} on {time_task_continue}")
    print("Type Done if you are Done with the task completely or Break if you want to go on a break.")

def whenDone():
    global response, time_task_continue, time_minute_continue
    global time_hour_continue, hour_used_before_break, minute_used_before_break
    tell_time()
    if response.strip().capitalize() == "Done":
        now_done_break = datetime.datetime.now()
        date_task_done = now_done_break.strftime('%Y-%m-%d')
        time_task_done = current_time
        time_hour_done = int(time.strftime("%I", time_n))
        time_minute_done = int(time.strftime("%M", time_n))
        print(f"You completed the task {task} on {date_task_done} at {time_task_done}")
        hour_used_after_break = time_hour_done - time_hour_continue
        minute_used_after_break = time_minute_done - time_minute_continue
        total_hours_used_for_task = hour_used_before_break + hour_used_after_break
        total_minutes_used_for_task = minute_used_before_break + minute_used_after_break
        total_time_spent_on_task = (total_minutes_used_for_task / 60) + total_hours_used_for_task
        money_to_be_paid = 5 * total_time_spent_on_task
        print(f"You are to be paid $%.2f" %money_to_be_paid)

def whenBreakAgain():
    global response, time_task_continue, time_minute_continue
    global time_hour_continue, hour_used_before_break, minute_used_before_break
    tell_time()
    if response.strip().capitalize() == "Break":
        breakTask()

if __name__ == '__main__':
    with open('time_tracking_details.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Task", "Date_Started", "Time_Started", "Date_Completed", "Time_Completed"])
        try:
            while True:
                world_start = datetime.datetime.now().strftime("%d/%m/%Y")
                world_start_time = datetime.datetime.now().strftime("%H:%M")
                taskInput()
                writer.writerow([task, world_start, world_start_time, datetime.datetime.now().strftime("%d/%m/%Y"), datetime.datetime.now().strftime("%H:%M")])
        except Exception:
            file.close()