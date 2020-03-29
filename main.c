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
    if (host != NULL) {
        struct in_addr inaddr = {0};
        memcpy(&inaddr, host->h_addr_list[0], host->h_length);
        printf("gethostbyname:\n %s is %s\n", name, inet_ntoa(inaddr));
    }
}
void use_getaddrinfo(const char *name)
{
    int err;
    struct addrinfo hints = {0};
    struct addrinfo *res = NULL;
    hints.ai_family = AF_INET;
    hints.ai_socktype = SOCK_STREAM;
    if ((err = getaddrinfo(name, NULL, &hints, &res)) != 0) {
        fprintf(stderr, "getaddrinfo: %s\n", gai_strerror(err));
        return;
    }
    printf("getaddrinfo:\n %s is %s\n", name, inet_ntoa(((struct sockaddr_in *)res->ai_addr)->sin_addr));
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
