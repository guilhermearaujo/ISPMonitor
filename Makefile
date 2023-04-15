install:
ifeq (, $(shell command -v speedtest))
	@echo "IMPORTANT!\n"
	@echo "Speedtest CLI tool must be installed."
	@echo "Follow instructions for your platform at https://www.speedtest.net/apps/cli\n\n"
else
	@echo "Speedtest CLI tool is installed"
endif
	@poetry install

update:
	@poetry update

lint:
	@poetry run black .

lint-check:
	@poetry run black . --check

run:
	@poetry run python main.py

.PHONY: install update lint lint-check run
