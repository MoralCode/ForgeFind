from dataclasses import dataclass
from forge import Forge
@dataclass
class Result:
	"""a normalized search result from a forge
	"""
	identifier:str
	forge:Forge
	name:str
	url:str
	description:str