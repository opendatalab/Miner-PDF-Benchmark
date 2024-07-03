浙江大学 $2013-2014$ 学年夏季学期<br>《C 程序设计专题》 课程期末考试试卷<br>课程号: $211 Z 0050$, 开课学院: 计算机学院<br>考试试卷: $\sqrt{ } \mathrm{A}$ 卷、B卷（请在选定项上打 $\sqrt{ }$ )<br>考试形式: $\sqrt{ }$ 闭、开卷（请在选定项上打 $\sqrt{ }$ )，允许带上入场<br>考试日期: 2014 年 06 月 $\underline{27}$ 日, 考试时间: 120 分钟<br>诚信考试, 沉着应考, 杜绝违纪.

考生姓名:学号:所属院系:

# (注意: 答题内容必须写在答题卷上, 写在本试题卷上无效) 

## Section 1: single Choice(2 marks for each item, total 26 marks)

1. Suppose that five characters are pushed into a stack in the order of $\mathbf{a}, \boldsymbol{b}, \boldsymbol{c}, \boldsymbol{d}, \boldsymbol{e}$. The impossible popping sequence is
A. $\mathrm{abcde}$
B. e d cb a
$\overline{\text { C. }}$ d ceab
D. decba
2. When using a stack to evaluate the postfix expression $235+6 *+84 /+$, what symbols are inside the stack when " 9 " is read?
A. $+^{*}+$
B. ++
C. 235684
D. 5084
3. To insert a node pointed by $\boldsymbol{s}$ after the node pointed by $\boldsymbol{p}$ in a linked list, we should do the following statements
A. s->next=p; p->next=s;
B. s->next=p->next; p->next=s;
C. $s->$ next=p->next; $p=s ;$
D. p->next=s; s->next $=$ p;
4. Assume that two structures are defined as following:

## struct data \{

 int day, month, year; \} below can set the year of the second student's birthday to 1995 correctly.A. $(p+1)->$ birthday.year $=1995$;
B. $*(p+1)->$ birthday.year $=1995$
C. $(p+1)->$ birthday $->$ year $=1995$;
D. $(p+1) \cdot$ birthday->year $=1995$;

5. About the function pointer, the statement _ below is WRONG.

A. The function pointer can be passed to a function as an actual argument.

B. The function pointer can be used to call a function.

C. Can't pass argument to a function when a function pointer is used to call the function.

D. The function name is a pointer value which can be assigned to a function pointer variable.

6. About \#include, the statement below is correct.

A. \#include "xx.h" means that search the file xx.h in the current directory ONLY.

B. \#include <stdio.h> means that the stdio library is included in the program.

C. \#include $<x x . h>$ means that search the file xx.h ONLY in the directory which be appointed by the compiler.

D. \#include $<x x>$ is NOT correct because of missing the postfix. $\boldsymbol{h}$

7. Given the variables declaration char s[5];If we convert the integer variable $\boldsymbol{i}$ to the corresponding character string, the statement
A. sprintf( $4,40 d ", i)$
B. sprintf(s, "\%5d", i):
C. sprintf(s, " $\% 4 \mathrm{~d} "$, i);
D. None of the above. below is correct.
8. For the graphics library of our course, the statement about the function printf below is correct.

A. Printf can NOT output anything.

B. Printf can output the content in the current position of the graphics window.

C. Printf can open a text window and output the content automatically.

D. If calling the function InitConsole(), printf will output the content in the special console window, otherwise nothing will be output.

9. Use typedef to define a function pointer type PunPtr which points to a function void func(int $x$ ). The correct expression is
A. typedef FunPtr fun(int x);
B. typedef void FunPtr(int $x$ );
C. typedef void ( $F$ FunPtr)();
D. typedef void ( ${ }^{*} F u n P$ trr)(int);
10. The complexity(复杂度) of sort algorithm below is $\mathrm{O}\left(\mathrm{N} * \log _{2} \mathrm{~N}\right)$.
A. Selection sort algorithm
B. Bubble sort algorithm
C. Insertion sort algorithm
D. Merge sort algorithm
11. In the selection sort function SelectionSort(int a】,int $\boldsymbol{n}$ ), a function swap is used to exchange two variables' values. The correct swap function which can fulfill(实现) the function(功能) is
A. $\operatorname{void} \operatorname{swap}($ int $a$, int b) \{ int $t$; $\mathrm{t}=\mathrm{a} ; \mathrm{a}=\mathrm{b} ; \mathrm{b}=\mathrm{t} ;$
\}
C. void swap(int a[, int i, int j) \{ int $t$; $\mathrm{t}=\mathrm{a}[i] ; \mathrm{a}[\mathrm{i}=\mathrm{a}[\mathrm{j}] ; a[]=\mathrm{t} ;$
B. $\operatorname{void}$ swap(int $* a$, int ${ }^{*}$ ) \{
} int ${ }^{*}$;
}
t=a;a=b;b=t;
D. void swap(int *a, int *b) {
int *t;

![](https://cdn.mathpix.com/cropped/2024_05_06_9e975176ac259165fda2g-2.jpg?height=49&width=291&top_left_y=1643&top_left_x=1028)
}

12. About the recursive function, the statement _ below is WRONG.

A. The recursive function must call the function itself DIRECTLY.

B. The recursion must have an EXIT(出口).

C. The sub-problems in a recursive solution have the same form as the original problem.

D. The $\mathrm{C}$ systems use the STACK strategy to implement the recursion.

13. Given the following definitions, the scanf statement $\qquad$ below is NOT correct. struct pupil \{ char name[20]; int age; int sex; 3 pup [5], *p=pup;
A. $\operatorname{scanf}(4 \% s=$ "pup $[0]$. name);
B. $\operatorname{scanf(“\% d",\& pup[0].age);}$
C. $\operatorname{scanf}(“ \% d ", p->a g e) ;$
D. $\operatorname{scanf}(“ d ", \&(p->s e x)) ;$

## Section 2: Read the following problems and answer questions (5 marks for each item, total 30 marks)

1. Given the polynomial(多项式) definition of a linked list and a practical example (linked list $\boldsymbol{h}$ ), and the function $\boldsymbol{f}$ which is a mathematical operation(数学运算) on the
polynomial. Please draw up(画出) the result ( a new polynomial) of the linked list $\boldsymbol{h}$ after calling the function $f(h)$.

struct ListNode \{

int fact; / /

int exp; / / exponent(指数) $)^{*}$ struct ListNode $*$ next;

\}

![](https://cdn.mathpix.com/cropped/2024_05_06_9e975176ac259165fda2g-3.jpg?height=194&width=1491&top_left_y=537&top_left_x=317)

```
void \(f(\) struct ListNode *head)
\{
    struct ListNode HEAD;
    struct ListNode *cur = head, *pre = \&HEAD;
    HEAD.next = head;
    If (!head) return;
    while(cur) \{
        if(cur->exp) \{
            cur->fact \(=\) cur->fact \(*\) cur->exp;
            cur->exp = cur->exp - 1 ;
        \} else \{
            free(cur);
            pre->next \(=\) NULL;
            break;
        \}
        pre \(=\) cur;
        cur \(=\) cur->next;
        \}
    \}
```

2. Given the definition of a linked list and a practical example (list $\boldsymbol{h}$ ), please write out the result of the linked list after calling the function $f(h, 3)$.

struct ListNode \{

int val;

struct ListNode $*$ next;

};

struct ListNode *f(struct ListNode *head, int x)

{

struct ListNode *root = (struct ListNode *)malloc(sizeof(struct ListNode));

struct ListNode *pivot = (struct ListNode *)malloc(sizeof(struct ListNode));

struct ListNode *root_last = root;

struct ListNode *pivot_last = pivot;

struct ListNode *current = head;

memset(root, 0, sizeof(struct ListNode)); /*nitial root spaces as zeroes*/

memset(pivot, 0, sizeof(struct ListNode)); /* Initial pivot spaces as zeroes */

while (current!= NULL){

if (current->val <x) {

root_last->next = current;

root last = current;

} else {

pivot_last->next = current;

pivot_last = current;

}

```
current = current->next;
    }
    root_last->next = pivot->next;
    pivot_last->next = NULL;
    return root->next;
}
```

The input linked list $\boldsymbol{h}$ is:

$1->4->3->2->5->2$ and $x=3$.

3. The following program will output

\#include <stdio.h>

int f(int $\mathrm{x}$, int $\mathrm{n}$, char $\mathrm{s}[$ )

\{

int count;

```
if (x<9) {
        s[n]=x + '0';
        s[n+1] = '00';
        return n+1;
    }
    count = f(x/9, n,s);
    count = f(x%9, count, s );
    return count;
main()
    int a = 159;
    char s[100];
    f(a, 0, s);
    puts(s);
```

}

{

}

4. Write down the declaration of the function pointer variable $\boldsymbol{p}$ which points to a procedure(过程) $\boldsymbol{f}$ with two formal parameters: the first is an integer variable, the other is an integer pointer array.
5. Xiao Ming wrote a C program to call the library function printf("helloln") in the main function, but he forgot to write down \#include <stdio.h> in the beginning of the source file. However his program was be compiled and executed correctly. Why? Give a more example to explain that in what situation the program can be compiled but can NOT be executed correctly if the related head files are not be included.
6. Please describe the linear search algorithm(线性查找算法) and the binary search algorithm(二分查找算法). Evaluate their efficiencies(效率) and explain their use conditions(使用条件) respectively.

## Section 3: According to the specification, complete each program (2 marks for each blank, total 24 marks)

1. Given a sorted linked list in ascending order (升序) , delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,

Given $1->2->3->3->4->4->5$, return $1->2->5$.

Given 1->1->1->2->3, return 2->3.

```
typedef struct _ListNode {
    int val;
    struct _ListNode *next;
} ListNode;
```

ListNode *insert(ListNode *target, ListNode *head, ListNode *tail)

/*insert a node target after the tail of list which has a head node */

{

if(!head->next) /*Null list - only head node.*/

head->next = target; /*insert after head, as the first node */

else

tail->next = target; /*insert after the tail */

tail = target

tail->next = _(1)_;

return tail;

}

ListNode *deleteDuplicates(ListNode *head)

/* head is the sorted linked list which has no head node */

{

ListNode result_head, *result_tail, *pre = head, *cur;

if(!head || !head->next) return head;

result_head.next = NULL;

cur = head->next;

while(pre) {

while (cur \&\& cur->val == pre->val)

cur = cur->next;

if (cur ==__(2) __)

result_tail = insert(pre, \&result_head, result_tail);

pre = cur;

if (cur) cur = cur->next;

}

return __(3)

}

2. Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing(拼接) together the nodes of the first two lists. The sorted list is in ascending order.

typedef struct _ListNode \{ int val; struct _ListNode *next;

\} ListNode;

ListNode *mergeTwoLists(ListNode *|1, ListNode *|2)

\{

ListNode HEAD, ${ }^{*} p$

ListNode ${ }^{*}$ cur $=\& H E A D$

while ( 11 \& \& | 2 ) \{

```
if( (4) _ ) {
    cur->next = |1;
    |1=|1->next;
} else {
```

```
cur->next = |2;
        12 =__(5) __;
    }
        cur = cur->next;
    }
    p= = (6)
    cur->next = p;
    return HEAD.next;
```

3. The graphics library of our course uses a timer(定时器) strategy which contains three functions:

- void RegisterTimerEvent(TimerEventCallback callback); /*register the callback function*/
- void starttimer(int timerID, int timeinterval); /*start the timer*/
- void canceltimer(int timerID); $/ *$ close the timer*/

Now we wants to implement a single timer task(单次定时任务) that outputs a string "Hello World" in the console window after $1000 \mathrm{~ms}$, then the display will not occur again. Please complete the following program fragment.

NOTE: If you think that some places don't need to be filled in anything, you can leave them blanks. Don't care about the codes which create the window.

```
void timerCallBack(int timelD)
{
    printf("Hello World\n");
    (7) _;
}
void Main()
{
    RegisterTimerEvent(__(8) ___(B)
    starttimer(__(9)__(_);
    ....
}
```

4. The following program uses the recursive quick sort algorithm to sort the character strings in ascending order (升序) according to the compare strategy in the function numcmp. The program will output:

22

111

Complete the program.

\#include <stdio.h>

\#include <stdlib.h>

/* numcmp: compare s1 and s2 numerically */

int numcmp(char *s1, char *s2)

\{

int v1, v2;

$\mathrm{v} 1=$ atoi(s1);

v2 = atoi(s2);

if $(\mathrm{v} 1<\mathrm{v} 2)$

return -1

else if $(v 1>v 2)$

```
return 1;
    else
        return 0;
}
void swap(char *v[, int i, int j)
{
    char *temp;
    temp = v[i];
    v[i] = v[j];
    v[j] = temp;
}
/* qsort: sort v[left]..v[right] into increasing order */
void qsort(char *v[], int left, int right, int (*comp)(char *, char *))
{
    int i, last;
    void swap(char *v[], int, int);
    if (left >= right) /* do nothing if array contains nothing*/
        return;
    swap(v, left, (left + right)/2);
    last = left;
    for (i = left+1; ; <= right; i++)
        if((*comp)(v[i], v[left])<0)
            swap(v, ++last, i);
    swap(v, left, last);
    qsort(v,
    (10)
    qsort(v, (11)
}
main()
{

```

![](https://cdn.mathpix.com/cropped/2024_05_06_9e975176ac259165fda2g-7.jpg?height=52&width=440&top_left_y=1670&top_left_x=431)

```
    int i;
    qsort( _(12) <ref (_)
    for(i=0;i<3;i++) printf("%s\n",str[i]);
}
```


## Section 4: Algorithms design (10 marks for each item, total 20 marks)

1. Given a linked list (no cycle in the list), remove the $n t h$ node from the end of list and return its head. Please (1) describe your algorithm of this problem, and (2) give your function ListNode *removeNthFromEnd(ListNode *head, int n).

For example,

Given linked list: 1->2->3->4->5, and $n=2$.

After removing the second node from the end, the linked list becomes 1->2->3->5.

You must travel the linked list only once.

Definition of the linked list:

typedef struct_ListNode \{

int val;

struct_ListNode next;

\} ListNode;

2. On a standard telephone keypad, the digits are mapped onto the alphabet (minus the letters $\mathrm{Q}$ and $\mathrm{Z}$ ) as shown in this diagram. In order to make their phone numbers more memorable, service providers like to find numbers that spell out some word appropriate to their business that makes that phone number easier to remember. Such words that help you remember some other data are called mnemonics. In the following program, The function ListMnemonics will generate all possible letter combinations that correspond to a given number, represented as a string of digits.

![](https://cdn.mathpix.com/cropped/2024_05_06_9e975176ac259165fda2g-8.jpg?height=386&width=437&top_left_y=612&top_left_x=1295)

Write down the definition of recursive function

ListMnemonics to complete the program.

\#include <stdio.h>

\#include "genlib.h"

\#include "strlib.h"

\#include "simpio.h"

/* Private function prototypes $* /$

static void ListMnemonics(string str);

/*data structure/

static string dialpad $[=\{/ *$ map table from dial-pad to their letters $* /$

"0", "1", "ABC", "DEF", "GHI", "JKL", "MNO", "PRS", "TUV", "WXY"

};

static char Mnemonics[100]={'0'}; /*Store the mnemonics string */

static int index = 0; /*Record the current letter position of the mnemonics */

main()

{

string str;

printf("This program lists all Mnemonics of a telephone number.\n");

prinf("Enter a telephone number string: ");

str = GetLine();

ListMnemonics(str);

}

static void ListMnemonics(string str)

{

}

