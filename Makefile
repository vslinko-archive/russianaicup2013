all: test run

local-runner: local-runner.zip
	mkdir local-runner
	cd local-runner; unzip ../local-runner.zip
	chmod a+x local-runner/*.sh

python3-cgdk: python3-cgdk.zip
	unzip python3-cgdk.zip

src/model: python3-cgdk
	cp -r python3-cgdk/model src/model

src/astar.py:
	wget -O src/astar.py "https://raw.github.com/vslinko/python-astar/patch-1/src/astar.py"

src/RemoteProcessClient.py: python3-cgdk
	cp python3-cgdk/RemoteProcessClient.py src/RemoteProcessClient.py

src/Runner.py: python3-cgdk
	cp python3-cgdk/Runner.py src/Runner.py

build.zip: src/*.py
	rm -f build.zip
	cd src; zip -9 build.zip *.py -x RemoteProcessClient.py -x Runner.py
	mv src/build.zip build.zip

local-runner.zip:
	wget -O local-runner.zip "http://russianaicup.ru/s/1384255837416/assets/local-runner/local-runner.zip?rnd"

python3-cgdk.zip:
	wget -O python3-cgdk.zip "http://russianaicup.ru/s/1384255837416/assets/cgdks/python3-cgdk.zip?rnd"

prepare: local-runner src/model src/astar.py src/RemoteProcessClient.py src/Runner.py

test: prepare
	pep8 --exclude=src/astar.py,src/RemoteProcessClient.py,src/Runner.py src/*.py

run: prepare
	cd local-runner; ./local-runner.sh
	sleep 3
	python3 src/Runner.py

clean:
	rm -rf local-runner python3-cgdk src/model src/astar.py src/RemoteProcessClient.py src/Runner.py build.zip local-runner.zip python3-cgdk.zip

.PHONY: all prepare test run clean
