# 第一周：数据结构的概念与分类

## 1. 本周目标
理解数据结构的基本概念与分类，熟悉与数据结构相关的基本术语；了解数据的逻辑结构与存储结构的区别，掌握常见数据结构（线性表、栈、队列、树、图、集合、字典等）的定义和基本操作，并学会用 C 语言描述数据结构的基本操作原型。

## 2. 基本概念与术语
- 数据（Data）：能反映事物属性和状态的符号记录。
- 数据元素（Element）：数据的最小单位。
- 数据对象（Data Object）：相互之间存在某种关系的数据元素的集合。
- 数据项（Data Item）：数据对象中的一个独立属性。
- 数据结构（Data Structure）：数据元素之间相互关系的集合，以及对这些数据元素进行操作的一组算法的统称。
- 算法（Algorithm）：为解决特定问题而规定的有限步骤序列。

## 3. 逻辑结构与存储结构
- 逻辑结构（Logical Structure）：数据元素之间的抽象关系，常见的有集合、线性结构、树形结构、图形结构等。
- 存储结构（Physical/Storage Structure）：数据在计算机内存中的表示方式。主要有：
  - 顺序存储（数组）
  - 链式存储（链表）
  - 索引/散列等扩展方式

### 逻辑结构与存储结构的对应
- 线性结构可以用顺序或链式存储；
- 树形结构通常用链式存储（孩子-兄弟表示法也常用）或顺序存储（完全二叉树）;
- 图常用邻接矩阵或邻接表表示。

## 4. 数据结构的分类（按逻辑结构）
- 线性结构：线性表、栈、队列、串等。特点：元素之间存在一对一的相邻关系。
- 树形结构：树、二叉树、堆等。特点：呈层次关系，一对多。
- 图结构：有向图、无向图、带权图。特点：复杂的多对多关系。
- 集合与字典（映射）：集合、散列表（哈希表），用于快速查找。

## 5. 常见数据结构及基本操作
下面列出常见数据结构与常见操作（抽象数据类型 ADT 的视角）：

### 5.1 线性表（Linear List / Sequence）
抽象定义：具有零个或多个元素的有限序列。
常见操作：
- InitList(&L)：初始化线性表
- ListEmpty(L)：判断是否为空
- ListLength(L)：返回长度
- GetElem(L, i, &e)：取第 i 个元素
- LocateElem(L, e)：按值查找，返回位置
- ListInsert(L, i, e)：在第 i 个位置插入元素
- ListDelete(L, i, &e)：删除第 i 个元素并返回

存储实现：
- 顺序表（数组实现）
- 链表（单链表、双向链表、循环链表）

### 5.2 栈（Stack）
- 抽象：后进先出（LIFO）
- 主要操作：InitStack, Push, Pop, GetTop, StackEmpty
- 应用：函数调用、表达式求值、括号匹配、回溯等

### 5.3 队列（Queue）
- 抽象：先进先出（FIFO）
- 主要操作：InitQueue, EnQueue, DeQueue, GetHead, QueueEmpty
- 常见变体：循环队列、优先队列、双端队列

### 5.4 树（Tree）与二叉树（Binary Tree）
- 抽象：节点的层次性结构
- 术语：根节点、叶子节点、父节点、子节点、层次（深度）、高度等
- 二叉树特殊性质：每个节点度≤2，常有前序/中序/后序/层序遍历
- 常见操作：创建、遍历（递归与非递归）、插入、删除、查找

### 5.5 图（Graph）
- 抽象：顶点与边的集合，可带权或不带权
- 表示：邻接矩阵、邻接表
- 常见算法：深度优先搜索（DFS）、广度优先搜索（BFS）、最短路径（Dijkstra）、最小生成树（Prim、Kruskal）

### 5.6 哈希表（Hash Table）
- 抽象：基于关键字的直接访问结构，用于快速查找
- 处理冲突的方法：开放地址法（线性探测、二次探测）、链地址法（拉链法）

## 6. 在 C 语言中描述数据结构
下面给出若干常见数据结构在 C 语言中的基本描述与操作原型（示例代码注重概念清晰，非完整工程代码）。

### 6.1 顺序表（数组实现）的结构定义与简单操作
```c
#define MAXSIZE 100
typedef int ElemType;

typedef struct {
    ElemType data[MAXSIZE];
    int length;
} SqList;

void InitList(SqList *L) {
    L->length = 0;
}

int ListEmpty(SqList L) {
    return L.length == 0;
}

int ListLength(SqList L) {
    return L.length;
}

int GetElem(SqList L, int i, ElemType *e) {
    if (i < 1 || i > L.length) return 0; // 失败
    *e = L.data[i-1];
    return 1; // 成功
}

int ListInsert(SqList *L, int i, ElemType e) {
    if (i < 1 || i > L->length + 1 || L->length == MAXSIZE) return 0;
    for (int j = L->length; j >= i; j--) L->data[j] = L->data[j-1];
    L->data[i-1] = e;
    L->length++;
    return 1;
}
```

### 6.2 单链表的定义与插入（在第 i 个位置插入）
```c
typedef struct Node {
    ElemType data;
    struct Node *next;
} Node, *LinkList;

// 在第 i 个位置前插入元素 e（假设带头结点）
int ListInsert_Link(LinkList L, int i, ElemType e) {
    LinkList p = L; // 指向头结点
    int j = 0;
    while (p && j < i-1) { p = p->next; j++; }
    if (!p || j > i-1) return 0; // 位置不存在
    LinkList s = (LinkList)malloc(sizeof(Node));
    s->data = e; s->next = p->next; p->next = s;
    return 1;
}
```

### 6.3 栈（顺序栈）示例
```c
#define MAXSIZE 100
typedef struct {
    ElemType data[MAXSIZE];
    int top; // 指向栈顶元素的下标，空栈时 top = -1
} SqStack;

void InitStack(SqStack *S) { S->top = -1; }
int StackEmpty(SqStack S) { return S.top == -1; }
int Push(SqStack *S, ElemType e) {
    if (S->top == MAXSIZE-1) return 0;
    S->data[++(S->top)] = e;
    return 1;
}
int Pop(SqStack *S, ElemType *e) {
    if (S->top == -1) return 0;
    *e = S->data[(S->top)--];
    return 1;
}
```

### 6.4 队列（循环队列）示例
```c
#define MAXQSIZE 100
typedef struct {
    ElemType data[MAXQSIZE];
    int front, rear; // 队头、队尾指针
} SqQueue;

void InitQueue(SqQueue *Q) { Q->front = Q->rear = 0; }
int QueueEmpty(SqQueue Q) { return Q.front == Q.rear; }
int EnQueue(SqQueue *Q, ElemType e) {
    if ((Q->rear + 1) % MAXQSIZE == Q->front) return 0; // 队满
    Q->data[Q->rear] = e;
    Q->rear = (Q->rear + 1) % MAXQSIZE;
    return 1;
}
int DeQueue(SqQueue *Q, ElemType *e) {
    if (Q->front == Q->rear) return 0; // 队空
    *e = Q->data[Q->front];
    Q->front = (Q->front + 1) % MAXQSIZE;
    return 1;
}
```

## 7. 常见操作与复杂度（简要）
- 访问第 i 个元素（顺序表）：O(1)
- 插入/删除（顺序表中间位置）：O(n)
- 插入/删除（链表指定节点后）：O(1)
- 查找（平均）：线性查找 O(n)，哈希表 O(1) 平均
- 栈/队列的 Push/Pop 或 EnQueue/DeQueue：O(1)

## 8. 例题与练习（含答案）

1. 用数组实现顺序表并完成插入操作：初始数组为 [1,2,4,5]，在第3位插入 3，结果为？
   - 答： [1,2,3,4,5]

2. 在带头结点的单链表 L 中插入元素 7 到第2位，原链表为头->3->9->null，插入后为？
   - 答：头->3->7->9->null

3. 给出一个栈的 Push 顺序：1,2,3，随后 Pop 两次，最终栈中剩余元素为？
   - 答：栈中只剩元素 1

4. 写出用邻接表表示的简单无向图的存储结构示例（示意说明），并写出 BFS 的思想。
   - 答：邻接表为每个顶点维护一个链表，链表存储相邻顶点；BFS 使用队列，先访问起始顶点并入队，依次出队并访问其尚未访问的邻居，入队，直至队空。

## 9. 学习建议与后续计划
- 先熟悉线性表、栈、队列的实现与应用，再学习树与图的概念与常见算法。
- 多做编程实现练习：把每个数据结构用 C 语言实现一遍，并写测试用例。建议使用小型样例逐步调试。