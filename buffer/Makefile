bad:
	python3 localpayload.py > localinput
	python3 virtualpayload.py > virtualinput
	gcc -m32 -fno-stack-protector -z execstack -no-pie bad.c -o bad

good:
	python3 localpayload.py > localinput
	python3 virtualpayload.py > virtualinput
	gcc -m32 -fno-stack-protector -z execstack -no-pie good.c -o good
