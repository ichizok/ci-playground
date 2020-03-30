#include <netinet/in.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netdb.h>
#include <arpa/inet.h>
#include <string.h>
void use_gethostbyname(const char *name)
{
    struct hostent *host = gethostbyname(name);
    char **p;
    if (host == NULL) {
        fprintf(stderr, "gethostbyname: %s\n", strerror(h_errno));
        return;
    }
    for (p = host->h_addr_list; *p != NULL; ++p) {
        struct in_addr inaddr = {0};
        memcpy(&inaddr, *p, host->h_length);
        printf("gethostbyname:\n %s is %s\n", name, inet_ntoa(inaddr));
    }
}
void use_getaddrinfo(const char *name)
{
    int err;
    struct addrinfo hints = {0};
    struct addrinfo *res = NULL;
    struct addrinfo *r = NULL;
    hints.ai_family = AF_INET;
    hints.ai_socktype = SOCK_STREAM;
    if ((err = getaddrinfo(name, NULL, &hints, &res)) != 0) {
        fprintf(stderr, "getaddrinfo: %s\n", gai_strerror(err));
        return;
    }
    for (r = res; r != NULL; r = r->ai_next) {
        printf("getaddrinfo:\n %s is %s\n", name, inet_ntoa(((struct sockaddr_in *)r->ai_addr)->sin_addr));
    }
    freeaddrinfo(res);
}
int main(int argc, char *argv[])
{
    if (argc > 1)
    {
        use_gethostbyname(argv[1]);
        use_getaddrinfo(argv[1]);
    }
    return 0;
}
