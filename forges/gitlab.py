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

	def searchfor(self, query:str):
		results = session.get(self.apisearchurl.format(query=query), headers = {"PRIVATE-TOKEN": os.getenv("GITLAB_TOKEN")})

		results = results.json()
		print(results)

		res = map(lambda r: format_result(r, self), results)
		print(res)

		return res
		# print(result)
