#include <stdio.h>
#include <stdlib.h>

#define MAXSIZE 100
typedef int ElemType;

typedef struct {
    ElemType data[MAXSIZE];
    int length;
} SqList;

void InitList(SqList *L) {
    L->length = 0;
}

int ListInsert(SqList *L, int i, ElemType e) {
    if (i < 1 || i > L->length + 1 || L->length == MAXSIZE) return 0;
    for (int j = L->length; j >= i; j--) L->data[j] = L->data[j-1];
    L->data[i-1] = e;
    L->length++;
    return 1;
}

void PrintList(SqList L) {
    printf("[");
    for (int i = 0; i < L.length; i++) {
        printf("%d", L.data[i]);
        if (i < L.length - 1) printf(", ");
    }
    printf("]\n");
}

int main() {
    SqList L;
    InitList(&L);
    // 初始数据 [1,2,4,5]
    ListInsert(&L,1,1);
    ListInsert(&L,2,2);
    ListInsert(&L,3,4);
    ListInsert(&L,4,5);
    printf("初始顺序表："); PrintList(L);
    // 在第3位插入3
    if (ListInsert(&L,3,3)) {
        printf("插入后顺序表："); PrintList(L);
    } else {
        printf("插入失败\n");
    }
    return 0;
}
