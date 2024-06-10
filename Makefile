curr_dir= ../..
tetris_dir= game/tetris
tc_dir= game/trivial_compute

# auto-install the neccesary packages
setup_tetris: ${tetris_dir}/requirements.txt
	pip install -r ${tetris_dir}/requirements.txt

# package all directory files for release
release_tetris:
	@cd ${tetris_dir}; \
	pyinstaller -F --noconsole --windowed \
	tetris_main.py; \
	mkdir -p ${curr_dir}/release; \
	cp -rf assets ${curr_dir}/release/; \
	mv dist/tetris_main ${curr_dir}/release/; \
	cd ${curr_dir}; zip -r tetris.zip release/*; \
	mv tetris.zip release

# run your release
test_tetris:
	@cd release; ./tetris_main

# clean all unneeded files from your repository
clean_tetris:
	rm -rf ${tetris_dir}/__pycache__ \
	${tetris_dir}/build ${tetris_dir}/dist \
	${tetris_dir}/*.spec \
	release

# run tetris
tetris: tetris_main

tetris_main: ${tetris_dir}/tetris_main.py
	@cd ${tetris_dir}; \
	./$@.py;

# run trivial compute
run_tc: main

main: ${tc_dir}/main.py
	@cd ${tc_dir}; \
	./$@.py;
