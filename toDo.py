import datetime
import time
import json
	
def task(name = time.strftime("%d/%m/%y"), due = time.strftime("%d/%m/%y"), rep = 0, desc = "", sub = None, stat = 0, dur = 0.5):
	# Default task name vaule is today's date.
	# Default due date is tomorrow
	# The repeat vaule will be stored as an integer.
	# The event will repeat after this number of days.
	# A description of the task.
	# Any sub-tasks that make up this task.  These values will be stored as a Task object.
	# The status of the task as a percentage. Incomplete tasks are 0%, and complete tasks are 100%.
	# The value of duration can be stored as any time unit. 
	# As default, it is stored in hours, and defaults to 0.5 hours.
	current = {"name" : name, "due" : due, "repeat" : rep, "description" : desc, "sub-task" : sub, "status" : stat, "duration" : dur}
	return(current)

def createList(tasks, filename = time.strftime("%d_%b_%y")+".txt"):
	print(tasks)
	jsontasks = json.dumps(tasks)
	l = open(filename, "w")
	l.write(jsontasks)
	l.close()

def loadList(filename):
	comp = "comp"+filename
	completed = open(comp, "r+")
	l = open(filename, "r+")
	tasks = json.loads(l)
	l.truncate()
	for task in tasks:
		if task["repeat"] != 0 & task["due"] < time.strftime("%d/%m/%y"):
			duedate = task["due"]
			due = datetime.datetime.strptime(duedate, "%d/%m/%y") + timedelta(days=task["repeat"])
			t = json.dumps(task)
			l.write(t)
		if task["status"] == 1:
			t = json.dumps(task)
			completed.write(t)
		else:
			t = json.dumps(task)
			l.write(t)
	## return(tasks)
	l.close()
	completed.close()

# def toDo(filename):
#	urgency = []
#	for task in tasks:
#		timeleft = task["dur"]
#
# def doTask(task, comp):
	
