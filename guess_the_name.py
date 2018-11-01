from Tkinter import *
import ttk
import random

words = ["virat kohli","ms dhoni","rohit sharma","ravindra jadeja","ajinkya rahane","suresh raina","kl rahul","shikhar dhawan"]
no_of_guess = 5
word = random.choice(words)
display_word = ''
for i in word:
	if i == ' ':
		display_word = display_word + ' '
	else:
		display_word = display_word + '-'


class Window(Frame):
	global words, no_of_guess, word, display_word
	global letter,no_ofguess,alertmess,display_wrd

	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.master = master
		self.init_window()

	#Creation of init_window
	def init_window(self):
		# changing the title of our master widget
		global words, no_of_guess, word, display_word
		global letter,no_ofguess,alertmess,display_wrd
		self.master.title("Guess the name")

		# allowing the widget to take the full space of the root window
		self.pack(fill=BOTH, expand=1)
		frame = Frame(self, relief=RAISED, borderwidth=1)
		frame.pack(fill=BOTH, expand=True)

		############ creating and placing label:
		guessname = Label(self, text="Guess the name :")
		guessname.place(x=5,y=10)
		display_wrd = StringVar()
		displayword = Label(self,textvariable=display_wrd)
		displayword.place(x=150,y=10)
				
		lettertext = Label(self, text="Letter :") 
		lettertext.place(x=5,y=35)
		letter = StringVar()
		letter_entry = Entry(width=1,textvariable=letter)
		letter_entry.place(x=150,y=35)

		numberlifetext = Label(self, text="No. of guess left :")
		numberlifetext.place(x=5,y=60)
		no_ofguess = StringVar()
		noofguess = Label(self,textvariable=no_ofguess)
		noofguess.place(x=150,y=60)

		alertmess = StringVar()
		alertmessage = Label(self, textvariable=alertmess, fg="red")
		alertmessage.place(x=5,y=85)

		############ creating buttons instance
		newButton = Button(self, text="New Name", command=self.new_word)
		checkButton = Button(self, text="Check", command=self.check_letter)
		quitButton = Button(self, text="Quit",command=self.client_exit)

		############ placing the new wrord button on my window
		checkButton.pack(side=TOP,padx=5,pady=5)
		newButton.pack(side=LEFT,padx=5,pady=5)
		quitButton.pack(side=RIGHT,padx=5,pady=5)

		##### seting the default value of lablels:
		display_wrd.set(display_word)
		no_ofguess.set(no_of_guess)
		# alertmess.set('Y')

	def check_letter(self):
		global words, no_of_guess, word, display_word
		global letter,no_ofguess,alertmess,display_wrd

		ch = str(letter.get())
		if no_of_guess >= 1:
			if word.count(ch) == 0:
				no_of_guess = no_of_guess - 1
				alertmessshow = ch+" is not present in the word"
				no_ofguess.set(no_of_guess)
				alertmess.set(alertmessshow)
			else:
				foo = ( [pos for pos, char in enumerate(word) if char == ch])
				l1 = list(display_word)
				for r in foo:
					l1[r] = ch
				display_word = "".join(l1)
				if display_word.count('-') == 0:
					#no_of_guess = 0
					alertmessshow = "You won"
				else:
					alertmessshow = ch+" is present in the word"
				display_wrd.set(display_word)
				alertmess.set(alertmessshow)
		else:
			alertmessshow = "You lost. The name was " + word
			alertmess.set(alertmessshow)
		if no_of_guess == 0:
			alertmessshow = "You lost. The name was " + word
			alertmess.set(alertmessshow)
		letter.set('')

	def new_word(self):
		global words, no_of_guess, word, display_word
		global letter,no_ofguess,alertmess,display_wrd
		no_of_guess = 5
		word = random.choice(words)
		display_word = ''
		for i in word:
			if i == ' ':
				display_word = display_word + ' '
			else:
				display_word = display_word + '-'
		no_ofguess.set(no_of_guess)
		alertmess.set("")
		display_wrd.set(display_word)

	def client_exit(self):
	 	exit()


root = Tk()

#size of the window
root.geometry("400x200")
app = Window(root)

root.mainloop()	