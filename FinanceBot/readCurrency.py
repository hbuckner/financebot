class readCurrency():

	def currencyGet(self,filename):
		f=open(filename,'r')
		Line=[]

		with open(filename) as f:
			for line in f:
				line =line.replace("\n","")
				Line.append(line)
				#print(Line)

		return Line
