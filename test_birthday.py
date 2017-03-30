#tests for birthday app
import birthday as bd
from datetime import date, timedelta

def test_birthday_calculates_remaining_days_for_1_day_left():
	testBday = bd.Birthday(date.today().year, date.today().month, date.today().day + 1)
	assert testBday.daysRemaining() == 1 

def test_birthday_calculates_remaining_days_for_30_days_left():
	daysMinus30 = date.today() + timedelta(days = 30)
	testBday = bd.Birthday(daysMinus30.year, daysMinus30.month, daysMinus30.day)
	assert testBday.daysRemaining() == 30 

def test_birthday_calculates_remaining_days_for_364_days_left():
	daysMinus364 = date.today() + timedelta(days = 364)
	testBday = bd.Birthday(daysMinus364.year, daysMinus364.month, daysMinus364.day)
	assert testBday.daysRemaining() == 364 

def test_birthday_returns_correct_string():
	days = abs(date(date.today().year+1, 1, 1) - date.today())
	result = "It looks like you were born on 1/1/2001\n"
	result += "Looks like your birthday is in {d} days.\n".format(d=days.days)
	result += "Hope you're looking forward to it!"
	testBday = bd.Birthday(2001, 1, 1)
	assert testBday.getOutput() == result