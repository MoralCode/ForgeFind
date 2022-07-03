from dataclasses import dataclass
# import requests
import requests_cache


session = requests_cache.CachedSession('forge-cache')

@dataclass
class Forge:
	"""a code forge
	"""
	name: str
	usersearchurl: str
	apisearchurl: str


	def searchfor(self, query:str):
		result = session.get(self.apisearchurl.format(query=query))
		return result
		
