# ForgeFind

This is a simple, hacked-together python webapp to serve as a proof-of-concept dempnstration of a search tool similar to https://grep.app that can search multiple different code hosting platforms.

![a screenshot of the homepage](images/home.png)


![a screenshot of the results page](images/results.png)



## Setup and running
1. `pipenv install`
2. (optional) create a .env file according to the env variables below
3. `FLASK_APP=app pipenv run flask run`


### Environment variables
`GITLAB_TOKEN` - [a token appropriate for accessing the gitlab.com api](https://docs.gitlab.com/ee/api/#authentication).



## Forge support:
Currently the following forges are included in results:
- Github
- GitLab
- Gitea


## Project Limitations/intentions

Currently this project is intended to be a proof of concept.

It mostly relies on anonymously accessing public API's of various hosting providers and is therefore not able to handle the kinds of high-volume use that can result from having more than a few users. Therefore this should be considered to be "for personal use"