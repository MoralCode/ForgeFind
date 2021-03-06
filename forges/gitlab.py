from forge import Forge, session
from result import Result
import os
import json
from constants import USER_AGENT

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
			results = session.get(self.apisearchurl.format(query=query), headers = USER_AGENT.update({"PRIVATE-TOKEN": token}))

			if results.status_code != 200:
				print("Gitlab error: " + results.text)
				return []
			else:
				results = results.json()
				res = map(lambda r: format_result(r, self), results)
				return res
		return []
		# print(result)
