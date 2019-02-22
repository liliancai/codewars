import os,unittest
from unittest import skip
import cheapest2

class CheapestTest(unittest.TestCase):
	with open('input.test','w+') as f:
		f.write("test")

	def test_empty_string_error(self):
		self.assertEqual(cheapest2.Routing(""),None)
	
	@skip
	def test_if_txt_file_does_not_exist(self):
		try:
			#remove input.test if exist
			os.remove("input.test")
		except FileNotFoundError:
			pass
		#check if 404error raised in Routing
		self.assertRaises(FileNotFoundError,cheapest2.Routing,'123')

	def test_routing_result(self):
		self.assertEqual(cheapest2.Routing("1"),(0.9,'A'))
		self.assertEqual(cheapest2.Routing("46732"),(1.1,'A'))
		self.assertEqual(cheapest2.Routing("44"),(0.5,'B'))
		self.assertEqual(cheapest2.Routing("22"),None)
			
if __name__=="__main__":
	unittest.main()
