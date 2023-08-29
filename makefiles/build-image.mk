build-image-test:
	@echo "Building the Docker image (test)..."
	docker build --tag $(DOCKER_IMAGE_URL)-test:$(BUILD_VERSION) --file Dockerfile.testenv .

build-image-app:
	@echo "Building the Docker image (app)..."
	docker build --tag $(DOCKER_IMAGE_URL):$(BUILD_VERSION) --build-arg APP_VERSION=$(BUILD_VERSION) .