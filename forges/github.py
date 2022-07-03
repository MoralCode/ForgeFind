from forge import Forge
from result import Result
import json


def format_result(r, forge):
	return Result(
		r.get("id"),
		forge,
		r.get("full_name"),
		r.get("html_url"),
		r.get("description")
	)

class GitHub(Forge):

	def searchfor(self, query:str):
		results = super().searchfor(query)

		results = results.json().get('items')
		# print(results.keys())
		res = map(lambda r: format_result(r, self), results)
		return res
		# print(result)
