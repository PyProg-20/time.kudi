# Time.kudi
Time. kudi outlines python codes that is intended to calculate the time Nana spent on a task and how much Nana earns from the task. The program already has its own defined time and all Nana has to do is tell the program if he has started, taken a break, resumed from break and if he is done with the task.

## Implementation process and Design
1. Entering task description:
The task description is to help assign name to the task for easy identification and tracking. The name takes on any data types (string, integer, boolean, etc) in a way that task can easily be traced. User can define exactly define any extensions  if the task is under a particular project. For example, user can type Azubi.Lab_1 to indicate he’s working on Azubi project and the task under that project is Lab_1

2. Ready to begin?
After user has entered the task name, the system requires the user to enter Yes or No to the question “Ready to start with task? Yes or No?. 
Yes allows the system to start count of time that it automatically embedded. In this case, the user doesn’t need to input the time he started work. He only types Yes and the system automatically starts counting the time. The Yes or No is not case sensitive, that is, type yes / no instead of Yes / No does not change a thing. 

When the user types No, the system does not start counting, but indicates “ Come back when you are ready to start the task” and initiates “Ready to get started with the task? Yes or No?

When user finally starts, the system returns the the name of the task user has entered, the date (yyyy-mm-dd format) and time (hh:mm format)

3. Taking a break
 After completing step 1 and step 2 above, the user is promoted to “Type Break if you want to go on a break or Done when you are completely done with the task”. When you type Break, which is not case sensitive, the system automatically informs the user the date and time of task so far, how many hours and minutes he has spent on the task so far before going on break and the time user is going on break.
There is a prompting to continue with task when ready to continue. The user can take as many breaks as possible when working on a particular task

4. Done with the project
There is a prompting to type done when user is finally done with the project. This ends the time and date of the project and user cannot make any changes. The system then generates the following details to the user
	. Description of task and time of completion
	. How much user is to be paid. This part is divides hours (in this 60 minutes) per the hourly rate of $5. 
5. Saving in csv
All information pertain to the task are saved in a csv file which the user can make reference to later in life. The csv contains 1) the task name, 2) date started, 3) time started, 4) date completed, 5) time completed, 6) hours spent on the project and 7) amount paid

## Program dependencies
The program depends on the user to initiate. 
  
