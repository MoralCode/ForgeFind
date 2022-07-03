from dataclasses import dataclass
import requests
import requests_cache
import os
from constants import USER_AGENT

session = None
if os.getenv("FLASK_ENV") == 'development':
	session = requests_cache.CachedSession('forge-cache')
else:
	 session = requests.Session()

@dataclass
class Forge:
	"""a code forge
	"""
	name: str
	usersearchurl: str
	apisearchurl: str


	def searchfor(self, query:str):
		result = session.get(self.apisearchurl.format(query=query), headers=USER_AGENT)
		return result
		
