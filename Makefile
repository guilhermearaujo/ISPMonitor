dependencies:
ifeq (, $(shell command -v speedtest))
	@echo "IMPORTANT!\n"
	@echo "Speedtest CLI tool must be installed."
	@echo "Follow instructions for your platform at https://www.speedtest.net/apps/cli\n\n"
else
	@echo "Speedtest CLI tool is installed"
endif
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
