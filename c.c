#include <stdio.h>
#include <stdlib.h>
struct node
{
    int data;
    struct node *address1;
    struct node *address2;
};
// int lenn(struct node *top)
// {
//     int a = 0;
//     struct node *p;
//     p = top;
//     do
//     {
//         a = a + 1;
//         p = p ->address2;
//     }while(p!=NULL);
//     return a;
// };
void traversal(struct node *top)
{
    struct node *Q;
    Q = top;
    do
    {
        printf("%d->", Q->data);
        Q = Q->address2;
    } while (Q != NULL);
};
void insertion(struct node *top, int ele, int pos)
{
    int i;
    struct node *Q1, *p;
    p = top;
    Q1 = (struct node *)malloc(sizeof(struct node *));
    Q1->data = ele;
    for (i = 1; i < pos; i++)
    {
        p = p->address2;
    };
    Q1->address1 = p;
    Q1->address2 = NULL;
    p->address2 = Q1;
    traversal(top);
};
void deletion(struct node *top)
{
    int i;
    struct node *p;
    p = top;
    while(p->address2->address2!=NULL)
    {
        p = p->address2;
    }
    p->address2 = NULL;
    traversal(top);
};
int main()
{
    int a, ele1, pos1, pos2, cont = 0;
    struct node *top;
    top = (struct node *)malloc(sizeof(struct node));
    top->data = 1;
    top->address1 = NULL;
    top->address2 = NULL;
    while (cont == 0)
    {
        printf("Enter 1)for traversal\n2)deletion\n3)for insertion\n");
        scanf("%d", &a);
        switch (a)
        {
        case 1:
            traversal(top);
            break;

        case 2:
            deletion(top);
            break;
        case 3:
            printf("Enter the value\n");
            scanf("%d", &ele1);
            printf("enter the postion\n");
            scanf("%d", &pos1);
            insertion(top, ele1, pos1);
            break;
        default:
            printf("Ivalid option!\n");
            break;
        };
        printf("Enter 0 to continue\n");
        scanf("%d", &cont);
    };
}