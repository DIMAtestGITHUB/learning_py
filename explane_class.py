class Calculate:
	def __init__(self):
		pass
	def calc(self, exp):
		try:
			temp = exp.split(" ")
			print(f"ok-{temp}")
		except AttributeError:
			print("AttributeError - its mean you put in enter bar number when program wait string!")

			
		
	#def calc(self, number1, calculant, number2):
		#res =  {"+":lambda a,b: a+b
			#}
		#print(res[calculant](number1, number2))
n = Calculate()
#n.calc(1,"+", 1)
n.calc(1)			
