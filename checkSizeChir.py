import os
from time import sleep
from subprocess import check_output
import psutil
import shutil
import math

found = 0

#Kills the process which is increasing the file size.
def killprocess(filename):
	print(filename)
	for proc in psutil.process_iter():
		try:
			pinfo = proc.as_dict(attrs=['pid', 'name', 'username', 'open_files'])
		except psutil.NoSuchProcess:
			pass
		else:
			if pinfo['open_files'] != None:
				# print(pinfo)
				for directory in pinfo['open_files']:
					if filename == directory[0]:
						pid = str(pinfo['pid'])
						print("Process:", pinfo['name'], " with pid :" ,pinfo['pid'], "is found to be increasing the size of file:",filename)
						proc.kill()
						print("Process killed")

					
	  
directory = 'C:\\FileScanner\\Important\\'
dictVar = {}

i=0

for i in range(100):
	if (i==0):
		for filename in os.listdir(directory):
			fp = os.path.join(directory, filename)
			size = os.path.getsize(fp)
			values = list((size,0,0))
			dictVar[fp] = values
	else : 
		for filename in os.listdir(directory):			
			
			fp = os.path.join(directory, filename)
			size = os.path.getsize(fp)
			total, used, free = shutil.disk_usage("\\")
			percentage=size/total
			fp_key = dictVar[fp]
			pre_size = fp_key[0]
			change = size - pre_size
			rate = change/(i*5)
			percentage=percentage*100
			print(percentage)

			if rate > 1 and  percentage>=0.001 and fp_key[2] != 1:
				print("Virus Detected!!")
				print(filename+" is taking more than "+ str(percentage))
				ans = input('Would you like to delete it? (y/n)')
				if ans.lower() == "y":
					print("fp is:",fp)
					killprocess(fp)
					sleep(2)
					os.remove(fp)
					print("Ending the script")
					found = 1
					break
				else:
					fp_key[2]=1
					print("cool!")	
			fp_key[1] = rate
			# print(fp)
			# print(os.path.getsize(fp))			
	if found == 1:
		break
	sleep(2)
	i=i+1


