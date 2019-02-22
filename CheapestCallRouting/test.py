import os,unittest
from unittest import skip
import cheapest

class CheapestTest(unittest.TestCase):
	with open('input.test','w+') as f:
		f.write("test")

	def test_empty_string_error(self):
		self.assertEqual(cheapest.Routing(""),None)
	
	@skip
	def test_if_txt_file_does_not_exist(self):
		try:
			#remove input.test if exist
			os.remove("input.test")
		except FileNotFoundError:
			pass
		#check if 404error raised in Routing
		self.assertRaises(FileNotFoundError,cheapest.Routing,'123')

	def test_routing_result(self):
		self.assertEqual(cheapest.Routing("1"),('0.9','Operator A'))
		self.assertEqual(cheapest.Routing("46732"),('1.1','Operator A'))
		self.assertEqual(cheapest.Routing("44"),('0.5','Operator B'))
		self.assertEqual(cheapest.Routing("22"),None)
			
if __name__=="__main__":
	unittest.main()
