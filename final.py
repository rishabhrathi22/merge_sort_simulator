import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

k=0
p=1
global elements
global x1

def main():

	def home():
		
	    def reset():
	        master.destroy()
	        home()
	       
	    def best():

	        list1=[]
	        b1.configure ( state = DISABLED )
	        b2.configure ( state = DISABLED )
	        b3.configure ( state = DISABLED )
	        
	        x1 = n.get()
	        for i in range ( 1, int( x1 )+1 ):
	            Button ( f , text = i , width = 8 , font = "Helvetica 10 bold" , bg = "powder blue" ,relief=SUNKEN,
	                     fg = "black" ).grid(row=0,column=i,padx=10)
	            list1.append(i)
	        mergesort(list1)    	

	    def worst():
	        list2=[]
	        b1.configure ( state = DISABLED )
	        b2.configure ( state = DISABLED )
	        b3.configure ( state = DISABLED )
	        
	        x1 = n.get()
	        for i in range (int( x1 ), 0, -1 ):
	            Button ( f , text = i , width = 8 , font = "Helvetica 10 bold" , bg = "powder blue" ,relief=SUNKEN,
	                     fg = "black" ).grid(row=0,column=10-i,padx=10)
	            list2.append(i)
	        mergesort(list2)            
	            
	    def average():     
	        b1.configure ( state = DISABLED )
	        b2.configure ( state = DISABLED )
	        b3.configure ( state = DISABLED )
	         
	        global z
	        
	        x1 = n.get ()
	        z=[]
	        for i in range (0,int(x1)):
	            z.append(Entry ( f , width = 7 , bd = 10 , bg = "powder blue" , fg = "black" , font = "lucida 10 bold" ,justify="center"))
	            z[i].grid (row=0,column=i,padx=6 )

	        Button ( f , text = "INSERT" , width = 7 ,font = "Helvetica 15 bold" ,bg = "red" , fg = "White" , padx = 2 , pady = 3, command=create_array ).grid(row=1,column=int(x1)//2)

	    def create_array():
	    	elements=[]
	    	x1=n.get()
	    	for i in range (0,int(x1)):
	    		elements.append(z[i].get())
	    	print("elements",elements)
	    	elements=mergesort(elements)
	    	print("elements",elements)

	    def display(arr):
	    	global k
	    	global p

	    	Button ( f5 , text = "Pass "+str(p) , width = 8 , font = "Helvetica 10 bold" , bg = "green" , fg = "black" , padx=2 , pady=2).grid(row=k,column=1)

	    	for i in range(len(arr)):
	    		Button ( f5 , text = arr[i] , width = 8 , font = "Helvetica 10 bold" , bg = "powder blue" , fg = "black" , padx=2 , pady=2).grid(row=k,column=i+2)
	    	k+=1    	
	    	p+=1
	    	
	    def merge(left, right):
	    	global k
	    	if not len(left) or not len(right):
	    		print("merge",left,right)
	    		return left or right
	    	print("merge",left,right)
	    	#if len(left)>1 and len(right)>1:
	    	Button ( f5 , text = "Left" , width = 8 , font = "Helvetica 10 bold" , bg = "powder blue" , fg = "black" , padx=2 , pady=2).grid(row=k,column=0)
	    	display(left)
	    	Button ( f5 , text = "Right" , width = 8 , font = "Helvetica 10 bold" , bg = "powder blue" , fg = "black" , padx=2 , pady=2).grid(row=k,column=0)
	    	display(right)
	    	result = []
	    	i, j = 0, 0
	    	while (len(result) < len(left) + len(right)):
	    		if left[i] < right[j]:
	    			result.append(left[i])
	    			i+= 1
	    		else:
	    			result.append(right[j])
	    			j+= 1
	    		if i == len(left) or j == len(right):
	    			result.extend(left[i:] or right[j:])
	    			break
	    	print("result",result)
	    	Button ( f5 , text = "Merged array" , font = "Helvetica 10 bold" , bg = "powder blue" , fg = "black" , padx=2 , pady=2).grid(row=k,column=0)
	    	display(result)
	    	k+=1
	    	return result

	    def mergesort(list):
        	if len(list) < 2:
        		print(list)
        		return list
        	print("list",list)
        	display(list)
        	middle = len(list)//2
        	left = mergesort(list[:middle])
        	right = mergesort(list[middle:])

        	return merge(left, right)


	    #Simulation home window     
	        
	    master = Tk()
	    master.title('Merge Sort Simulator')  
	    master.geometry("1000x900") 
	    #master.resizable(0,0)
	    

	    menubar = Menu (master)

	    Home = Menu(menubar, tearoff=0)
	    menubar.add_cascade(label ='Options', menu = Home)
	    Home.add_command(label ='Simulate', command = home)
	    Home.add_command(label ='About', command = about)
	    Home.add_command(label ='Pseudocode', command = pseudocode)
	    Home.add_command(label ='Example', command = example)
	    Home.add_command(label ='Analysis', command = analysis)
	    Home.add_command(label ='Exit', command = master.destroy)
	    master.config(menu = menubar)

	 
	    f2 = Frame ( master ,bg = "blue")
	    f2.pack ( side = TOP , fill = "x" )

	    l = Label ( f2 , text = "Merge Sort Simulation" , font = "Helvetica 30 bold" , fg = "white" , bg = "blue", pady = 10)
	    l.pack ()
	    
	    f3 = Frame ( master ,bg = "white")
	    f3.pack ( side = TOP , fill = "x" )
	    
	    l2 = Label ( f3 , text = "Enter number of elements." , font = "Helvetica 20 bold" , fg = "black" , bg = "white").grid(row=0,column=0)
	    
	    n = Spinbox( f3, from_=0, to=10,width=17,font = "Helvetica 20 bold")
	    n.grid(row=0,column=1)

	    b5=Button ( f3, text = "Reset" , width = 18 , font = "Helvetica 20 bold", fg = "red" , bg = "powder blue", command=reset )
	    b5.grid(row=0,column=2,sticky="e",padx=25)

	    f4 = Frame ( master ,bg = "white")
	    f4.pack ( side = TOP , fill = "x" )
	    b1=Button ( f4, text = "Best Case" , width = 25 , font = "Helvetica 15" , bg = "green" ,command=best, fg = "white"  ,activebackground="yellow")
	    b1.grid ( row=1 , column=0 , padx=20, pady=15)
	    b2=Button ( f4 , text = "Worst Case" , width = 25 , font = "Helvetica 15" , bg = "green"  ,command=worst , fg = "white" , activebackground="yellow")
	    b2.grid( row=1 , column=1 , padx=20, pady=15)
	    b3=Button (f4 , text = "Average Case" , width = 25 , font = "Helvetica 15" , bg = "green" ,command=average , fg = "white"  ,activebackground="yellow")
	    b3.grid( row=1 , column=2 , padx=20, pady=15)
	    
	    f = Frame ( master ,bg = "white")
	    f.pack ( side = TOP , fill = "x" )

	    f5 = Frame ( master ,bg = "white")
	    f5.pack ( side = TOP , fill = "both" )
	    global p
	    p=1
	    master.mainloop()



	def about():
		"""try:
			master.destroy()
			home.destroy()
		except:
			pass	"""
		about=Tk()
		about.title ( "About" )
		about.geometry ( "1200x700" )

		# Creating Menubar 
		menubar = Menu(about) 

		# Adding File Menu and commands 
		Home = Menu(menubar, tearoff = 0) 
		menubar.add_cascade(label ='Menu', menu = Home) 
		Home.add_command(label ='Exit', command = about.destroy) 
		about.config(menu = menubar) 

		f2 = Frame ( about ,bg = "blue")
		f2.pack ( side = TOP , fill = "x" )

		l = Label ( f2 , text = "About Merge Sort" , font = "Helvetica 30 bold" , fg = "white" , bg = "blue", pady = 10)
		l.pack ()

		f3 = Frame ( about , bg = "powder blue")
		f3.pack ( side = TOP, fill = "both" )

		l1 = Label ( f3 , text = "1.Merge sort is an efficient, general-purpose, \ncomparison-based sorting algorithm. \n\n2.Merge sort is a divide and conquer algorithm\nthat was invented by John von Neumann in 1945.\n\n3.Conceptually, a merge sort works as follows:\n\t (i)Divide the unsorted list into n sublists,\n\t each containing one element \n\t (a list of one element is considered sorted).\n\t (ii)Repeatedly merge sublists to produce new sorted sublists\n\t until there is only one sublist remaining.\nThis will be the sorted list.", justify=LEFT , font = "Helvetica 24 bold" , bg = "powder blue" , fg = "black", pady=100)
		l1.pack ()

		about.mainloop()


	def pseudocode():
		"""try:
			master.destroy()
			home.destroy()
		except:
			pass	"""
		pseudocode=Tk()
		pseudocode.title ( "Pseudocode" )
		pseudocode.geometry ( "1000x700" )

		# Creating Menubar 
		menubar = Menu(pseudocode) 

		# Adding File Menu and commands 
		Home = Menu(menubar, tearoff = 0) 
		menubar.add_cascade(label ='Menu', menu = Home) 
		Home.add_command(label ='Exit', command = pseudocode.destroy) 
		pseudocode.config(menu = menubar) 

		f2 = Frame ( pseudocode ,bg = "blue")
		f2.pack ( side = TOP , fill = "x" )

		l = Label ( f2 , text = "Pseudocode\n(For Merge Sort)" , font = "Helvetica 30 bold" , fg = "white" , bg="blue", pady = 10 )
		l.pack ()

		f3 = Frame ( pseudocode ,bg = "powder blue")
		f3.pack ( side = TOP , fill = "both")

		l1=Label(f3,text="\t\t MergeSort(arr[], l,  r)\n If r > l\n 1. Find the middle point to divide the array into two halves:\n\t middle m = (l+r)/2\n 2. Call mergeSort for first half:\n\t Call mergeSort(arr, l, m)\n 3. Call mergeSort for second half:\n\t Call mergeSort(arr, m+1, r)\n 4. Merge the two halves sorted in step 2 and 3:\n\t Call merge(arr, l, m, r)", font = "Helvetica 24 bold",bg="powder blue",justify=LEFT,fg="black",pady=100)
		l1.pack()

		pseudocode.mainloop()


	def example():
		"""try:
			master.destroy()
			home.destroy()
		except:
			pass	"""
		example=Toplevel()
		example.title ( "Example" )
		example.geometry ( "1000x700" )

		# Creating Menubar 
		menubar = Menu(example) 

		# Adding File Menu and commands 
		Home = Menu(menubar, tearoff = 0) 
		menubar.add_cascade(label ='Menu', menu = Home) 
		Home.add_command(label ='Exit', command = example.destroy) 
		example.config(menu = menubar) 

		f2 = Frame ( example ,bg = "blue")
		f2.pack ( side = TOP , fill = "x" )

		l = Label ( f2 , text = "Example-Merge Sort" , font = "Helvetica 30 bold" , fg = "white" , bg="blue", pady = 10 )
		l.pack ()

		img = ImageTk.PhotoImage(Image.open("merge_sort.png"))
		panel = Label(example, image = img)
		panel.pack(side = TOP, fill = "both", pady=15)

		example.mainloop()



	def analysis():
		"""try:
			master.destroy()
			home.destroy()
		except:
			pass	"""
		analysis = Tk()
		analysis.title ("Analysis of merge sort")
		analysis.geometry ("1000x450")

		# Creating Menubar 
		menubar = Menu(analysis) 

		# Adding File Menu and commands 
		Home = Menu(menubar, tearoff = 0) 
		menubar.add_cascade(label ='Menu', menu = Home) 
		Home.add_command(label ='Exit', command = analysis.destroy) 
		analysis.config(menu = menubar) 

		f2 = Frame ( analysis ,bg = "blue")
		f2.pack ( side = TOP , fill = "x" )

		l = Label ( f2 , text = "Analysis of Merge Sort" , font = "Helvetica 30 bold" , fg = "white" , bg = "blue", pady = 10)
		l.pack ()

		f3 = Frame ( analysis , bg = "powder blue")
		f3.pack ( side = TOP, fill = "x" )

		l1 = Label ( f3 , text = "1.Time complexity: O(nLogn)\n2.Auxiliary Space: O(n)\n3.Algorithmic Paradigm: Divide and Conquer\n4.Sorting In Place: No in a typical implementation\n5.Stable: Yes", justify=LEFT , font = "Helvetica 24" , bg = "powder blue" , fg = "black", pady=100)
		l1.pack ()

		analysis.mainloop()    


	master = Tk()
	master.title('Merge Sort Simulator')  
	master.geometry("1000x570") 

	# Creating Menubar 
	menubar = Menu(master) 

	# Adding File Menu and commands 
	Home = Menu(menubar, tearoff = 0) 
	menubar.add_cascade(label ='Options', menu = Home) 
	Home.add_command(label ='Simulate', command = home) 
	Home.add_command(label ='About', command = about)
	Home.add_command(label ='Pseudocode', command = pseudocode)
	Home.add_command(label ='Example', command = example)
	Home.add_command(label ='Analysis', command = analysis)
	Home.add_command(label ='Exit', command = master.destroy) 
	master.config(menu = menubar) 


	f=Frame(master,bg="powder blue", relief="solid")
	f.pack(side=TOP,fill="x")

	l=Label(f,text="Merge Sort Simulator",font="Helvetica 35 bold",fg="black",bg="powder blue",pady=35, borderwidth=2)
	l.pack()

	f2=Frame(master,bg="white")
	f2.pack(side=LEFT,fill="y")

	Button(f2,text="About",width=20,font="Helvetica 20 bold",bg="green",fg="white",command=about,pady=10).pack()
	Button(f2,text="Pseudocode",width=20,font="Helvetica 20 bold",bg="green",fg="white",command=pseudocode,pady=10).pack()
	Button(f2,text="Example",width=20,font="Helvetica 20 bold",bg="green",fg="white",command=example,pady=10).pack()
	Button(f2,text="Analysis",width=20,font="Helvetica 20 bold",bg="green",fg="white",command=analysis,pady=10).pack()
	Button(f2,text="Simulate",width=20,font="Helvetica 20 bold",bg="green",fg="white",command=home,pady=10).pack()
	Button(f2,text="Exit",width=20,font="Helvetica 20 bold",bg="green",fg="white",command=master.destroy,pady=10).pack()

	f3 = Frame(master,bg="powder blue")
	f3.pack(fill="x")

	img2 = ImageTk.PhotoImage(Image.open("images.png"))
	panel2 = Label(f3, image = img2)
	panel2.pack(fill = "both")

	#side = TOP, fill = "both", pady=15
	l2=Label(f3,text="Developed by:\nRishabh Rathi.\nPrince Varshney.\nGuided by: \nProf. S.G. Mundhada.",font="Helvetica 20 bold",fg="black",bg="powder blue",pady=35, borderwidth=2,justify=LEFT)
	l2.pack(side=BOTTOM,fill="both")

	l3=Label(f3,text="This is a merge sort simulator \ndeveloped in python using tkinter.",font="Helvetica 20 bold",fg="black",bg="powder blue",pady=35, borderwidth=2,justify=LEFT)
	l3.pack(side=BOTTOM,fill="x")

	master.mainloop()

main()

