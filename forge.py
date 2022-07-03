from dataclasses import dataclass
import requests

@dataclass
class Forge:
	"""a code forge
	"""
	name: str
	usersearchurl: str
	apisearchurl: str


	def searchfor(self, query:str):
		result = requests.get(self.apisearchurl.format(query=query))
		return result
		
