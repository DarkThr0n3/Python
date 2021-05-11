import random

------------------------Easy warmup-------------------


s = "race ! ee=car"							Palindrom ? Ignore punc
Life is much bigger than tikki

while

	while

	while







-------------------------Med Q------------------------
tasks = [1,1,2,2]
cooldown = 2
steps ?

1 _ _ 1 2 _ _ 2

tasks = [1,2,3,1,2,3]
cooldown = 3
  0 0 _ 2 3
1 2 3 _ 1 2 3



def task_fn(tasks, cooldown):

	steps = 0
	d = {}

	for task_no in tasks:
		if task_no in d:
			steps+= d[task_no]+1

			for key in d:
				if key==task_no:						########  1
					d[key] -= d[task_no]	     		########  2

					if d[task_no]==0:					########  3
						del d[task_no]
			d[task_no] = cooldown
		else:
			steps+=1
			for key in d:
				if key==task_no:
					d[task_no]-= 1


	return steps

s= """

tasks = [1,2,3,1,2,3]
cooldown = 3








"""
