.PHONY: 'build clean'

build:
	@echo 'Building image...'
	@docker build --tag ascii-art:1.0 .

clean:
	@echo 'Deleting image...'
	@docker image rm ascii-art:1.0
