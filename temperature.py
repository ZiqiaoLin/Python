Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def conver_to_celsius(fahrenheit):
	'''(number) -> number
	Return the number of Celsius degree
	>>> conver_to_celsius(32)
	0
	>>>conver_to_celsius(212)
	100
	'''
	return fahrenheit -32 * 5 / 9
