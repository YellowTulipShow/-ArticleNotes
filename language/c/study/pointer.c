#include <stdio.h>

int main()
{
    int num = 20; /* 实际变量的声明 */
    int *ip;      /* 指针变量的声明 */

    ip = &num; /* 在指针变量中存储 var 的地址 */

    printf("num 变量的地址: %p\n", &num);

    /* 在指针变量中存储的地址 */
    printf("ip 变量存储的地址: %p\n", ip);

    /* 使用指针访问值 */
    printf("*ip 变量的值: %d\n", *ip);

    return 0;
}
