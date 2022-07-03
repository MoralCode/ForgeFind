from forge import Forge

from forges.github import GitHub
from forges.gitlab import GitLab

github = GitHub("GitHub", "https://github.com/search?q={query}", "https://api.github.com/search/repositories?q={query}")

# sourcehut = Forge("SourceHut", "https://sr.ht/projects?search={query}&sort=recently-updated")

# notabug = Forge("Notabug", "https://notabug.org/explore/repos?q={query}", apisearchurl)

# codeberg = Forge("Codeberg", "https://codeberg.org/explore/repos?tab=&sort=recentupdate&q={query}")

# gitea = Forge("Gitea", "")


gitlab = GitLab("GitLab", "https://gitlab.com/search?search={query}", "https://gitlab.com/api/v4/search?scope=projects?search={query}")

all_forges = [github, gitlab]