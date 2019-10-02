dependencies:
	@pip install -U pip
	@pip install pipenv --upgrade
	@pipenv install --dev --skip-lock

update:
	@pipenv clean
	@pipenv lock --clear
	@pipenv sync

check:
	@pipenv check


.PHONY: dependencies update check
