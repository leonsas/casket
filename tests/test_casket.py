from casket import *
from unittest import TestCase
import time
import redis
class BasicChacheTest(TestCase):
	'''
	These tests use sleep to make sure pillow is caching the results.
	'''
	def setUp(self):
		CasketCache().r.flushall()
	def test_basic_no_args(self):
		
		@casket
		def hello_world():
			time.sleep(2)
			return "Hello, world!"

		greet = hello_world()
		start_time = time.time()
		cached_greet = hello_world()
		time_elapsed = time.time() - start_time
		self.assertEqual(greet, "Hello, world!")
		self.assertEqual(time_elapsed < 1, True)
		self.assertEqual(greet,cached_greet)

	def test_basic_args(self):
		@casket
		def hello_you(name):
			time.sleep(2)
			return "Hello %s" %name
		
		greet = hello_you("world!")
		start_time = time.time()
		cached_greet = hello_you("world!")
		time_elapsed = time.time() - start_time
		self.assertEqual(greet, "Hello world!")
		self.assertEqual(time_elapsed < 1, True)
		self.assertEqual(greet, cached_greet)	
