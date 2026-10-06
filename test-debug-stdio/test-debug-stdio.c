
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(void)
{
	int i = 0;
	for (;;) {
		fprintf(stderr, "This message goes to stderr (%d)\n", i);
		fprintf(stdout, "This message goes to stdout (%d)\n", i);
		sleep(1);
		if (++i > 5) {
			fflush(stdout);
			i = 0;
		}
	}
	return 0;
}
