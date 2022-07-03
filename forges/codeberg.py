

from forges.gitea import Gitea


class Codeberg(Gitea):
	BASE_URL = "https://codeberg.org"
	def __init__(self):
		super().__init__()
		self.name = "Codeberg"