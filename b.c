#include<stdio.h>
#include<stdlib.h>
struct node
{
    int a;
    struct node *b;
};
void traversal(struct node *q)
{
    struct node *Q1;
    Q1 = q;
    do
    {
        printf("%d->",Q1->a);
        Q1 = Q1->b;
    }while(Q1!=q);
    printf("\n");
};
void insertion(struct node *q,int ele,int pos)
{
    int i;
    struct node *Q,*p;
    p = q;
    Q = (struct node*)malloc(sizeof(struct node));
    Q->a = ele;
    for (i = 1; i<pos;i++)
    {
        p = p->b;
    };
    p->b = Q;
    Q->b = q;
    traversal(q);
};
void deletion(struct node *q,int pos)
{
    int i;
    struct node *Q1,*Q2;
    Q1 = q;
    Q2 = Q1->b;
    for (i= 1;i<pos;i++)
    {
        Q1 = Q2;
        Q2 = Q1->b;
    };
    Q1->b = Q2->b;
    traversal(q);
};
int main()
{
    int cho,ele1,pos1,pos2,cont = 0;
    struct node *head;
    head = (struct node*)malloc(sizeof(struct node));
    head->a = 1;
    head->b = head;
    while(cont == 0)
    {
    printf("enter 1) for insertion\n,2)for deletion of node\n,3)traversal of node\n");
    scanf("%d",&cho);
    switch(cho)
    {
        case 1:printf("Enter the position.\n");
        scanf("%d",&pos1);
        printf("Enter value\n");
        scanf("%d",&ele1);
        insertion(head,ele1,pos1);
        break;
        case 2:printf("Enter the node\n");
        scanf("%d",&pos2);
        deletion(head,pos2);
        break;
        case 3:traversal(head);
        break;
        default: printf("invalid input!");
        break;
    };
    printf("Enter 0 to continue.\n");
    scanf("%d",&cont);
    };
}
