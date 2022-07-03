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

class Gitea(Forge):

	BASE_URL = "https://gitea.com"

	def __init__(self):
		super().__init__("Gitea", "", self.BASE_URL + "/api/v1/repos/search?q={query}")

	# https://try.gitea.io/api/swagger#/repository/repoSearch
	def searchfor(self, query:str):
		results = super().searchfor(query)

		results = results.json().get('data')
		# print(results.keys())
		res = map(lambda r: format_result(r, self), results)
		return res
		# print(result)
