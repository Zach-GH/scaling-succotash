curr_dir= ../..
tc_dir= game/trivial_compute

# run trivial compute
run_tc: main

main: ${tc_dir}/main.py
	@cd ${tc_dir}; \
	./$@.py;
