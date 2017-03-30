# birthday calculator
from datetime import date

class Birthday():
	def __init__(self, year, month, day):
		self._year = year
		self._month = month
		self._day = day
		self._birthday = date(year, month, day)

	def daysRemaining(self):
		today = date.today()
		if self._birthday < today:
			self._birthday = self._birthday.replace(year=today.year + 1)
		remaining = abs(self._birthday - today) 
		return remaining.days 

	def getOutput(self):
		days = self.daysRemaining()
		returnStr = "It looks like you were born on {day}/{mo}/{year}\n".format(day=self._day,
			mo=self._month, year=self._year)
		returnStr += "Looks like your birthday is in {days} days.\n".format(days=self.daysRemaining())
		returnStr += "Hope you're looking forward to it!"
		return returnStr


if __name__ == '__main__':
	print ('-'*40)
	print ("\t\tBIRTHDAY APP")
	print ('-'*40)
	year = int(input("What year were you born [YYYY]? "))
	month = int(input("What month were you born [MM]? "))
	day = int(input("What day were you born [DD]? "))
	print()
	bday = Birthday(year, month, day)
	print(bday.getOutput())