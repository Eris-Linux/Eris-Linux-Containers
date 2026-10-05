
APP = eris-api-test

OBJS =               \
  eris-api-test.o    \
  gpio-api-test.o    \
  network-api-test.o \
  sbom-api-test.o    \
  system-api-test.o  \
  time-api-test.o    \
  update-api-test.o  \
  wdog-api-test.o    \

INC = $(wildcard include/*.h)

CFLAGS  += -Wall -g -I include/ -pthread
LDLIBS  += -leris -lcurl -pthread

all: $(APP)

$(APP): $(OBJS)
	$(CC) $(CFLAGS) $(LDFLAGS)  $^ -o $@ $(LDLIBS)

%.o: %.c $(INC)
	$(CC) -c $(CFLAGS) $<

clean:
	rm -rf out *.o $(APP)
