#! /usr/bin/env python

from Tkinter import *
import Tkinter
import interpreter


class mainFrame(Frame):
	def __init__(self, master = None):
		Frame.__init__(self, master)
		self.grid()
		self.createWidgets()

	def createWidgets(self):
		self.quitButton = Button(self, text='Click Here!', command=self.interpret)
		self.quitButton.grid()

		self.rawText = Text(self)
		self.rawText.grid()

		self.showText = Text(self)
		self.showText.grid()

	def interpret(self):
		rawstr = self.rawText.get('1.0', 'end')
		result = interpreter.interMarkdown(rawstr)
		self.showText.delete('1.0', 'end')
		self.showText.insert('1.0', result)

main = mainFrame()
fi = open('readme', 'r')
main.rawText.insert('1.0', fi.read())
main.interpret()
main.master.title('This is a interpreter for markdown!')

main.mainloop()




















