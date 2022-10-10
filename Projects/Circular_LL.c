#include<stdlib.h>
#include<stdio.h>
typedef struct node{
	int data;
	struct node*next;
}node;

typedef struct{
	node *last;
}LL;

int deleteBeginning(LL *l){
node *p;
if(l->last==NULL){
return -1;
}
p=l->last->next;
if(p->next==p)
l->last==NULL;
else
l->last->next=p->next;
return p->data;
}

void insertBeginning(LL *l, int ele){
	node *newrec;
	newrec=(node*)malloc(sizeof(node));
	newrec->data=ele;
	if(l->last==NULL){
		newrec->next=newrec;
		l->last=newrec;
	}
	else
	{
		newrec->next=l->last->next;
		l->last->next=newrec;
	}
}

void insertEnd(LL *l,int ele){
	node *newrec,*p;
	newrec=(node*)malloc(sizeof(node));
	newrec->data=ele;
	if(l->last==NULL){
		newrec->next=newrec;
		l->last=newrec;
	}
	else{
		newrec->next=l->last->next;
		l->last->next=newrec;
		newrec->next=l->last->next;
		l->last->next=newrec;
		l->last=newrec;
	}
}

void display(LL *l){
	node *p;
	if(l->last==NULL){
		printf("Linked Lisr is Empty\n");
		return;
	}
	p=l->last->next;
	do{
	printf("%d ",p->data);
	p=p->next;
	}
	while
	(p!=l->last->next);
	printf("\n");
}

int deleteEnd(LL *l){
	node *p,*q;
	if(l->last==NULL){
	return -1;
	}p=l->last;
	if(p->next==p)
	l->last=NULL;
	else{   
	q=l->last->next;
	while(q->next!=l->last)
	q=q->next;
	q->next=p->next;
	l->last=q;
	}
	return p->data;
}

int main(){
	LL l1;
	int ch,ele,pos;
	l1.last=NULL;
	while(1){
		printf("\n1:InsertBeginning\t2:InsertEnd\t3:DeleteBeginning\t4:DeleteEnd\n");
		printf("5:Display\t6:Exit\n");
		printf("enter choice\n");
		scanf("%d",&ch);
		if(ch==6)break;
		switch(ch)
		{
		case 1:printf(" enter element to insert at Beginning\n");
		scanf("%d",&ele);
		insertBeginning(&l1,ele);
		printf("\nupdated list\n ");
		display(&l1);
		break;
		case 2:printf(" enter element to insert at End\n");
		scanf("%d",&ele);
		insertEnd(&l1,ele);
		printf("\nupdated list\n ");
		display(&l1);
		break;
		case 3:ele=deleteBeginning(&l1);
		if(ele==-1)
		printf("Linked List is empty");
		else
		printf(" element deleted from beginning =%d\n",ele);
		printf("\nupdated list\n ");
		display(&l1);
		break;
		case 4:ele=deleteEnd(&l1);
		if(ele==-1)
		printf("Linked List is empty");
		else
		printf(" element deleted from from End =%d\n",ele);
		printf("\nupdated list\n ");
		display(&l1);
		break;
		case 5:display(&l1);
		break;
		default:printf("invalid choice\n");
	}
}
return 0;
}
