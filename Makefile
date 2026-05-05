
PYTHON = python3
VENV = venv
SCRIPT = send_weather_update.py
DOCKER_IMAGE = weather-bot

venv:
	$(PYTHON) -m venv $(VENV)


install:
	$(VENV)/bin/pip install -r requirements.txt

#run locally
run:
	$(VENV)/bin/python $(SCRIPT)

# Run scheduler version (uncomment main() first and comment send_weather_update())
run-schedule:
	$(VENV)/bin/python $(SCRIPT)

clean:
	rm -rf $(VENV)

setup: venv install

docker-build:
	docker build -t $(DOCKER_IMAGE) .

docker-run:
	docker run --env-file .env $(DOCKER_IMAGE)

docker-stop:
	docker ps -q --filter ancestor=$(DOCKER_IMAGE) | xargs -r docker stop

docker-clean:
	docker rmi -f $(DOCKER_IMAGE)