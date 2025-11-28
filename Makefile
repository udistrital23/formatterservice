PACKAGE_NAME=formatterservice

build:
	docker build -t $(PACKAGE_NAME) -f Dockerfile .
run:
	docker run -it --rm -p 8001:8001 -v $(shell pwd):/app $(PACKAGE_NAME)


