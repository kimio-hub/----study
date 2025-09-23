# 第二周：时空复杂度与线性表（详细版）

## 一、 算法的时空复杂度分析（概述）
在计算机科学中，评估算法性能通常从时间（Time）和空间（Space）两个维度进行。复杂度分析不考虑具体硬件与实现细节，只关注随输入规模 n 增长时资源消耗的增长率，常用大 O 表示法（Big O）。

### 1. 时间复杂度（Time Complexity）
时间复杂度描述算法执行基本操作次数随输入规模 n 的增长趋势。常见复杂度（按增长快慢）：
- O(1)：常数时间（例如：按下标访问数组元素）
- O(log n)：对数时间（例如：二分查找）
- O(n)：线性时间（例如：遍历数组）
- O(n log n)：线性对数时间（例如：归并排序、快速排序平均）
- O(n^2)：平方时间（例如：冒泡、选择、插入排序最坏情况）

常用步骤简化求大 O：
1. 用常数 1 代替运行次数中的加法常数；
2. 保留最高阶项；
3. 去掉该项前的常数系数。

示例：二分查找（迭代版）
    int binarySearch(int arr[], int n, int target) {
        int left = 0, right = n - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (arr[mid] == target) return mid;
            else if (arr[mid] < target) left = mid + 1;
            else right = mid - 1;
        }
        return -1;
    }

示例：遍历求和（O(n)）
    int sumArray(int arr[], int n) {
        int sum = 0;
        for (int i = 0; i < n; ++i) sum += arr[i];
        return sum;
    }

### 2. 空间复杂度（Space Complexity）
空间复杂度衡量算法运行时额外使用的内存（不含输入本身所占空间）。常见量级：
- O(1)：常数额外空间（例如：原地排序的辅助变量）
- O(log n)：递归调用栈为对数级（例如：平衡递归分治）
- O(n)：需要与输入大小相同的额外结构（例如：复制数组、辅助数组）

示例：冒泡排序额外空间 O(1)；归并排序典型实现需要 O(n) 额外数组用于合并。

---

## 二、 线性表（Linear List）

### 1. 定义与特点
线性表是由 n (n ≥ 0) 个类型相同的数据元素按线性顺序排列的有限序列，记作 (a1, a2, ..., an)。

主要特点：
- 有序性：元素之间存在一对一的相邻关系；
- 有限性：元素个数有限；
- 同质性：元素类型相同；
- 唯一首尾：存在第一个（无前驱）和最后一个（无后继）元素；
- 直接前驱与后继：除首尾外，每个元素有且仅有一个直接前驱和后继。

### 2. 抽象数据类型（ADT）——线性表的基本操作
- InitList(&L)：初始化线性表 L（建立空表）
- DestroyList(&L)：销毁线性表，释放资源
- ListEmpty(L)：判断是否为空
- ListLength(L)：返回元素个数
- GetElem(L, i, &e)：按位查找第 i 个元素并返回其值
- LocateElem(L, e)：按值查找，返回位置（首次出现）
- ListInsert(&L, i, e)：在第 i 个位置插入元素 e
- ListDelete(&L, i, &e)：删除第 i 个位置元素并返回其值

---

## 三、 顺序表（Sequential List / SqList）
顺序表是线性表的一种顺序存储方式，使用地址连续的存储单元（数组）依次存放元素，支持 O(1) 的按下标访问，但插入/删除（非尾部）需要移动元素，平均 O(n)。

### 1. 存储方式
a) 静态分配（编译时确定容量）
- 优点：实现简单、开销小
- 缺点：容量固定，可能浪费或溢出

静态顺序表示例（C++ 风格，示意）：
    #define MAXSIZE 50
    typedef struct {
        int data[MAXSIZE];
        int length;
    } SqList;

    void InitList_Static(SqList &L) { L.length = 0; }

b) 动态分配（运行时按需申请）
- 优点：容量可扩展，空间利用灵活
- 缺点：需手动管理内存，扩容时有开销（可能导致拷贝）

动态顺序表示例（C 风格）：
    #include <stdlib.h>
    #define INIT_SIZE 10
    typedef struct {
        int *data;
        int MaxSize;
        int length;
    } SeqList;

    void InitList_Dynamic(SeqList &L) {
        L.data = (int *)malloc(INIT_SIZE * sizeof(int));
        if (!L.data) exit(EXIT_FAILURE);
        L.length = 0; L.MaxSize = INIT_SIZE;
    }

    void IncreaseSize(SeqList &L, int len) {
        L.data = (int *)realloc(L.data, (L.MaxSize + len) * sizeof(int));
        if (!L.data) exit(EXIT_FAILURE);
        L.MaxSize += len;
    }

### 2. 插入操作（ListInsert）
逻辑：在位置 i 插入元素 e（位序从 1 开始），需将原第 i..n 元素后移一位，然后将 e 放入 data[i-1]。

时间复杂度：
- 最好：O(1)（在表尾插入）
- 最坏：O(n)（在表头插入，移动 n 个元素）
- 平均：O(n)

示例实现（伪 C++）：
// 在 L 的第 i 个位置插入元素 e（i 从 1 开始）
    bool ListInsert(SeqList &L, int i, int e) {
        if (i < 1 || i > L.length + 1) return false;
        if (L.length >= L.MaxSize) return false; // 或者先扩容
        for (int j = L.length; j >= i; --j) L.data[j] = L.data[j - 1];
        L.data[i - 1] = e;
        ++L.length;
        return true;
    }

（如果实现自动扩容，应在满时调用 IncreaseSize 并处理 realloc 失败）

### 3. 删除操作（ListDelete）
逻辑：删除第 i 个元素，将第 i+1..n 元素前移一位覆盖被删元素，长度减 1。

时间复杂度：
- 最好：O(1)（删除表尾）
- 最坏：O(n)（删除表头，移动 n−1 个元素）
- 平均：O(n)

示例实现（伪 C++）：
    bool ListDelete(SeqList &L, int i, int &e) {
        if (i < 1 || i > L.length) return false;
        e = L.data[i - 1];
        for (int j = i; j < L.length; ++j) L.data[j - 1] = L.data[j];
        --L.length;
        return true;
    }

### 4. 插入/删除的优化思路（常见技巧）
- 若对顺序表插入/删除频繁且位置随机，考虑使用链表或平衡树等结构。
- 对于尾部频繁插入，顺序表表现良好（O(1) 摊销，如果带动态扩容策略）。
- 批量插入可一次性扩容后再移动/拷贝，减少 realloc 次数。

---

## 四、 顺序表的应用场景
- 随机访问频繁且元素数目近似稳定：数组（顺序表）优先。
- 实现其他线性结构：顺序栈、顺序队列（循环队列）均基于数组实现。
- 小规模数据集合、矩阵（二维数组）、函数参数传递等。
- 某些哈希表的冲突处理链可使用动态数组存放冲突项（拉链中使用顺序表）。

---

## 五、 小结与练习建议
- 掌握大 O 表示法及常见复杂度的推导方法。
- 理解顺序表的优缺点：随机访问 O(1)，插入删除（中间）O(n)。
- 能用 C/C++ 实现静态和动态顺序表，并实现插入/删除、扩容等基本操作。
- 练习：
  1. 实现带自动扩容的动态顺序表（以倍增策略扩容），测试插入、删除、随机访问性能。
  2. 比较顺序表与单/双链表在不同操作（随机访问、插入/删除不同位置）上的耗时。
  3. 用顺序表实现栈和循环队列，并验证复杂度。