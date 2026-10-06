
APP = test-debug-stdio

OBJS = test-debug-stdio.o

CFLAGS += -Wall -g -O0
LDFLAGS =


all: $(APP)

$(APP): $(OBJS)
	$(CC) $(CFLAGS) $(LDFLAGS)  $^ -o $@ $(LDLIBS)
	$(CC) $(CFLAGS) -g $(LDFLAGS) $^ -o $@-debug $(LDLIBS)

%o: %c $(INC)
	$(CC) -c $(CFLAGS) $<

clean:
	rm -rf out *.o $(APP)
