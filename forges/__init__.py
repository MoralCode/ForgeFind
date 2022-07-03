from forge import Forge

from forges.github import GitHub
from forges.gitlab import GitLab
from forges.gitea import Gitea

github = GitHub()

# sourcehut = Forge("SourceHut", "https://sr.ht/projects?search={query}&sort=recently-updated")

# notabug = Forge("Notabug", "https://notabug.org/explore/repos?q={query}", apisearchurl)

# codeberg = Forge("Codeberg", "https://codeberg.org/explore/repos?tab=&sort=recentupdate&q={query}")

gitea = Gitea()
codeberg = Codeberg()


gitlab = GitLab()

all_forges = [github, gitlab, gitea]