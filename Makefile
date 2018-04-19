all: connectback

connectback: connectback.o
	arm-linux-androideabi-ld $< -o $@

%.o: %.s
	arm-linux-androideabi-as $< -o $@

clean:
	rm -f *.o connectback
