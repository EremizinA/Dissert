#include <stdio.h>
#include <stdlib.h>

void main()
{
char *path = "/home/alex/PycharmProjects/dis/examples/dirs/file10";
char *access = "ab+";
FILE *fp = fopen(path, access);
fclose(fp);
}

