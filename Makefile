build-dev:
	docker build -t translator-dev -f Dockerfile.dev .
run-dev:
	docker run -it -d -v .:/code translator-dev
build:
	docker build -t translator .
run:
	docker run -v .:/code translator