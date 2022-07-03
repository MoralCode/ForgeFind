from forge import Forge

class GitLab(Forge):

	def searchfor(self, query:str):
		result = super().searchfor(query)

		result = result.json()
		print(result)
