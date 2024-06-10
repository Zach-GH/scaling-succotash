currDir= ../..
tetrisDir= game/tetris

# auto-install the neccesary packages
setup_tetris: ${tetrisDir}/requirements.txt
	pip install -r ${tetrisDir}/requirements.txt

# package all directory files for release
release_tetris:
	@cd ${tetrisDir}; \
	pyinstaller -F --noconsole --windowed \
	tetrisMain.py; \
	mkdir -p ${currDir}/release; \
	cp -rf assets ${currDir}/release/; \
	mv dist/tetrisMain ${currDir}/release/; \
	cd ${currDir}; zip -r tetris.zip release/*; \
	mv tetris.zip release

# run your release
test_tetris:
	@cd release; ./tetrisMain

# clean all unneeded files from your repository
clean_tetris:
	rm -rf ${tetrisDir}/__pycache__ \
	${tetrisDir}/build ${tetrisDir}/dist \
	${tetrisDir}/*.spec \
	release

# run tetris
tetris: tetrisMain

tetrisMain: ${tetrisDir}/tetrisMain.py
	@cd ${tetrisDir}; \
	./$@.py;
