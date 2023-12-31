.PHONY : local-run

local-run: build
	@echo "Running the Docker compose up..."
	docker compose --file examples/docker-compose.yaml up --detach

docker-clean:
	@echo "Running docker clean..."
	docker compose --file examples/docker-compose.yaml down
	docker system prune --all --force

local-docker-login:
	@echo "Logging into $(DOCKER_REPO)..."
	echo $$GITHUB_TOKEN | docker login $(DOCKER_REPO) --username USERNAME --password-stdin
