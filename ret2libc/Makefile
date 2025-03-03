bad:
	gcc -m32 -fno-stack-protector -z execstack bad.c -o bad

good:
	gcc -m32 -fno-stack-protector -z execstack good.c -o good

clean:
	rm bad good
