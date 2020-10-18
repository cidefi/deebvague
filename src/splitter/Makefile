install:
	sudo apt-get -y install ffmpeg
	pip install pydub
	mkdir ./output/
	echo "installation might be complete? lol. try running 'make split'"

split:
	python ./splitter.py

clean:
	rm ./output/*
