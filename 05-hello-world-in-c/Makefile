
APP = hello-world-in-c

OBJS = hello-world-in-c.o

CFLAGS += -Wall -g
LDFLAGS =


all: $(APP)

$(APP): $(OBJS)
	$(CC) $(CFLAGS) $(LDFLAGS)  $^ -o $@ $(LDLIBS)

%o: %c $(INC)
	$(CC) -c $(CFLAGS) $<

clean:
	rm -rf out *.o $(APP)
