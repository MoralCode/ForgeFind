from forge import Forge, session
from result import Result
import os
import json

def format_result(r, forge):
	return Result(
		r.get("id"),
		forge,
		r.get("namespace").get("name") + "/" + r.get("name"),
		r.get("http_url_to_repo"),
		r.get("description")
	)

class GitLab(Forge):

	def __init__(self):
		super().__init__("GitLab", "https://gitlab.com/search?search={query}", "https://gitlab.com/api/v4/search?scope=projects&search={query}")

	# https://docs.gitlab.com/ee/api/search.html
	def searchfor(self, query:str):
		token = os.getenv("GITLAB_TOKEN")
		if token != None:
			results = session.get(self.apisearchurl.format(query=query), headers = {"PRIVATE-TOKEN": token})

			results = results.json()
			print(results)

			res = map(lambda r: format_result(r, self), results)
			print(res)

			return res
		return []
		# print(result)
