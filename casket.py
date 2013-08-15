import redis
from hashlib import md5
import pickle
class CasketCache():
	
	def __init__(self):
		self.r =  redis.StrictRedis(host='localhost', port=6379, db=0)	
	
def casket(fn):
	'''
	Key based on function name and pickled args & kwargs.
	'''
	cache = CasketCache()
	def wrapped(*args, **kwargs):
		funname = fn.__name__
		m = md5(pickle.dumps(args) + pickle.dumps(kwargs)).digest()
		key = "%s:%s" % (funname,m)

		value = cache.r.get(key)
		if value is None:
			value = fn(*args,**kwargs)
			cache.r.set(key,value)

		return value
	return wrapped
