import os,unittest
import cheapest
class CheapestTest(unittest.TestCase):
	with open('input.test','w+') as f:
		f.write("test")

	def test_empty_string_error(self):
		print("test")
		self.assertEqual(cheapest.routing(""),False)
	
	def test_if_txt_file_does_not_exist(self):
		try:
			#remove input.test if exist
			os.remove("input.test")
		except FileNotFoundError:
			pass
		#check if 404error raised in routing
		self.assertRaises(FileNotFoundError,cheapest.routing,123)

if __name__=="__main__":
	unittest.main()
