# 	C语言

# 1.概述

## 注释

**两种格式**

1. **单行注释**：`// 描述信息` 
    - 通常放在一行代码的上方，或者一条语句的末尾，==对该行代码说明==
2. **多行注释**： `/* 描述信息 */`
    - 通常放在一段代码的上方，==对该段代码做整体说明==



## 程序框架介绍

```c
#include<stdio.h>
#include<stdlib.h>

int main() {

	printf("Hello world\n");

	system("pause");
	return 0;
}
```

**1 include头文件包含**

**头文件就是别人写好的，我们拿来直接用，和python的import一样，就是导入一个文件。**

\#include的意思是头文件包含，#include <stdio.h>代表包含stdio.h这个头文件

使用C语言库函数需要提前包含库函数对应的头文件，如这里使用了printf()函数，需要包含stdio.h头文件



**2 main函数**

*   一个完整的C语言程序，有且仅有一个main()函数 (又称主函数)
*   其他若干个函数结合而成（可选）。
*   main函数是C语言程序的入口，程序是从main函数开始执行。

 

**3  {} 括号，程序体和代码块**

*   {}叫代码块，一个代码块内部可以有一条或者多条语句
*   C语言每句可执行代码都是 ==**;**==  分号结尾
*   所有的#开头的行，都代表预编译指令，预编译指令行结尾是没有分号的
*   所有的可执行语句必须是在代码块里面

 

**4 printf函数**

printf是C语言库函数，功能是向标准输出设备输出一个字符串

printf(“Hello world\n”);    \\n  的意思是回车换行

 

**5 return语句**

*   return代表函数执行完毕，返回return代表函数的终止
*   如果main定义的时候前面是int，那么return后面就需要写一个整数；
*   在main函数中return 0代表程序执行成功

##  system函数

**功能：**在已经运行的程序中执行另外一个外部程序

最常用的

```c
#include<stdlib.h>
system("pause");
//程序运行时显示一句，请按任意键继续. . . 
//程序暂停，输入任意建后继续运行。
```

## c4996错误

**解决方案：**

*   \#define _CRT_SECURE_NO_WARNINGS  第一行写
*   \#pragma warning(disable:4996)	

*   项目配置 -> C/C++ -> 预处理器 -> 预处理定义

## 常用转义字符

**功能：**

有些字符利用printf不能直接输出，需要利用转义字符

常用转义字符如下：

| **转义字符** | **含义**                                                  |
| ------------ | --------------------------------------------------------- |
| \n           | 换行 ，将当前位置移到下一行开头                           |
| \r           | 回车 ，将当前位置移到本行开头，会将原本答应出来的覆盖掉。 |
| \t           | 水平制表（跳到下一个TAB位置                               |
| \\\\         | 代表一个反斜线字符"\\"                                    |
| \\'          | 代表一个单引号字符                                        |
| \\"          | 代表一个双引号字符                                        |

# 2.数据类型

## 变量

**作用**：给一段指定的内存空间起名，方便操作这段内存

**语法**：`数据类型 变量名 = 初始值;`

```c
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int main()
{
    // 定义变量
    int a = 10;
    printf("%d\n",a);
    a = 20;
    printf("%d\n",a);
    return 0;
}
```

注意：C在创建变量时，必须给变量一个初始值，否则会报错，默认给0

```c
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
// 一般都是声明变量在使用变量，但是要是先用在声明，就需要extern int c;告诉程序，我们有c在后面
void test01()
{
    extern int c;
    printf("%d\n", c);
}
int c = 200;

int main()
{

    test01();
    return 0;
}
```

## 常量

**作用**：用于记录程序中不可更改的数据

C语言中的常量大概有以下五种表现形式

1.  数值常量(整数型常量（整数） 、实数型常量（小数）)  
2.  字符常量  'a' 'b' 'c' '\n' '\t'
3.  字符串常量  "hello world"
4.  **\#define** 宏常量(符号常量)： `#define 常量名 常量值`
    1.  ==通常在文件上方定义==，表示一个常量
5.  **const**修饰的变量 `const 数据类型 常量名 = 常量值`
    1.  ==通常在变量定义前加关键字const==，修饰该变量为常量，不可修改

```c
#define DAY 7
#include <stdio.h>
//宏常量的定义 
int main()
{
    printf("%d\n",DAY);
    return 0;
}

```

## 关键字

**作用：**关键字是C中预先保留的单词（标识符）

* **在定义变量或者常量时候，不要用关键字**

常用的32个

| [auto]   | [break]  | [case]     | [char]   | [const]    | [continue] | [default]  | [do]     |
| -------- | -------- | ---------- | -------- | ---------- | ---------- | ---------- | -------- |
| [double] | [else]   | [enum]     | [extern] | [float]    | [for]      | [goto]     | [if]     |
| [int]    | [long]   | [register] | [return] | [short]    | [signed]   | [sizeof]   | [static] |
| [struct] | [switch] | [typedef]  | [union   | [unsigned] | [void]     | [volatile] | [while]  |

`提示：在给变量或者常量起名称时候，不要用C得关键字，否则会产生歧义。`

## 标识符命名规则

**作用**：C规定给标识符（变量、常量）命名时，有一套自己的规则

* 标识符不能是关键字
* 标识符只能由字母、数字、下划线组成
* 第一个字符必须为字母或下划线
* 标识符中字母区分大小写

> 建议：给标识符命名时，争取做到见名知意的效果，方便自己和他人的阅读

## 整型

C语言规定在创建一个变量或者常量时，必须要指定出相应的数据类型，否则无法给变量分配内存

**作用**：整型变量表示的是**整数类型**的数据

C语言中能够表示整型的类型有以下几种方式，**区别在于所占内存空间不同**：

| **数据类型**        | **占用空间**                                    | 取值范围         | 取值范围      |
| ------------------- | ----------------------------------------------- | ---------------- | ------------- |
| short(短整型)       | 2字节                                           | (-2^15 ~ 2^15-1) | -32768——32767 |
| int(整型)           | 4字节                                           | (-2^31 ~ 2^31-1) | 9位数到10位数 |
| long(长整形)        | Windows为4字节，Linux为4字节(32位)，8字节(64位) | (-2^31 ~ 2^31-1) |               |
| long long(长长整形) | 8字节                                           | (-2^63 ~ 2^63-1) |               |

**整型结论**：==short < int <= long <= long long==

```c
#include<stdio.h>


void test01()
{
    short a=10;
    int b=10;
    long c=10;
    long long d =10;
    printf("a=%hd\n",a);
    printf("a=%ld\n",c);
    printf("a=%lld\n",c);
    printf("b=%d\n",b);
    //占位符不写hd，ld，lld，也可以，直接写%d，也不会报错，为了区分就写上。
}


int main(){
    test01();
    return 0;
}
```

## sizeof关键字

**作用：**利用sizeof关键字可以==统计数据类型所占内存大小==

**语法：** `sizeof( 数据类型 / 变量)`

```c
#include<stdio.h>


void test01()
{
    short a=10;
    int b=10;
    long c=10;
    long long d =10;
    printf("a占用内存空间为: %d\n",sizeof(a));   //输出a占用内存空间为: 2
    printf("a=%hd\n",a);
    printf("a=%ld\n",c);
    printf("a=%lld\n",c);
    printf("b=%d\n",b);
   
}


int main(){
    test01();
    return 0;
}
```

## 字符型

**作用：**字符型变量用于显示单个字符

**语法：**`char ch = 'a';`

> 注意1：在显示字符型变量时，用单引号将字符括起来，不要用双引号

> 注意2：单引号内只能有一个字符，不可以是字符串



- C语言中字符型变量只占用==1个字节==。
- 字符型变量并不是把字符本身放到内存中存储，而是将对应的ASCII编码放入到存储单元

```c
#include<stdio.h>


void test01()
{
   char a ='h';
// 在次给a赋值。  a ='p';
   printf("a is %d\n",a);   //输出的ascii码种的值a is 104
   printf("a is %c\n",a);   //输出的时   a is h
}


int main(){
    test01();
    return 0;
}
```

## 浮点型

**作用**：用于==表示小数==

浮点型变量分为两种：

1. 单精度float 
2. 双精度double

两者的**区别**在于表示的有效数字范围不同。

| **数据类型** | **占用空间** | **有效数字范围** |
| ------------ | ------------ | ---------------- |
| float        | 4字节        | 7位有效数字      |
| double       | 8字节        | 15～16位有效数字 |

```c
#include<stdio.h>



void test01(){
    float b=2;
    double d=3.14;
    float e=1.222f;   			// double类型加上f变成了float
    printf("b is %lf\n",b);     // 输出b is 2.000000  默认显示后6位,显示两位就printf("b is %.2lf\n",b);
    printf("d is %lf\n",d);      // 输出d is 1374389535  
}

int main(){
    test01();
    return 0;
}
```

## 字符串

**作用**：用于表示一串字符

> 注意：字符串要用双引号括起来

```c
#include <stdio.h>

void test01()
{
    printf("%s\n", "hello，word");     // 双引号引起的内容中会带着字符串结束标志  \0
    //双引号会返回字符串的首字符的地址编号 
	//%s输出时 遇到\0 结束输出
    printf("hello\n");    // 这两个都可以。
    printf("%s\n", "hello\0word");    // 遇到\0结束。
    /* hello word
	hello
	hello  */
}

int main()
{
    test01();
    return 0;
}
```

##  数据的输入

python中的input

**作用：用于从键盘获取数据**

**语法：**scanf("格式化占位符",输入数据地址);



整型的输入

```c
#include <stdio.h>

void test01()
{
    int mun = 0;
    printf("请重新输入\n");
    scanf("%d",&mun);    // &就是拿到mun的内存地址
    printf("mun=%d\n",mun);
}

int main()
{
    test01();
    return 0;
}
```

字符串输入

```c
#include <stdio.h>

void test01()
{
    char mun = 'a';
    printf("mun= %c\n",mun);
    printf("请重新输入\n");
    scanf("%c",&mun);
    printf("mun=%c\n",mun);
}

int main()
{
    test01();
    return 0;
}
```

浮点型输入

```c
#include <stdio.h>

void test01()
{
    double mun = 3.14;
    printf("mun= %lf\n",mun);
    printf("请重新输入\n");
    scanf("%lf",&mun);
    printf("mun=%lf\n",mun);
}

int main()
{
    test01();
    return 0;
}
```

字符串的输入

```c
#include <stdio.h>

void test01()
{
    char ch[65] = "";
    printf("请重新给ch赋值\n");
    scanf("%s", ch);  //scanf("%s", &ch); 这样写也可以。
    printf("ch= %s\n", ch);
}

int main()
{
    test01();
    return 0;
}
```

# 运算符

**作用：**用于执行代码的运算

| **运算符类型** | **作用**                               |
| -------------- | -------------------------------------- |
| 算术运算符     | 用于处理四则运算                       |
| 赋值运算符     | 用于将表达式的值赋给变量               |
| 比较运算符     | 用于表达式的比较，并返回一个真值或假值 |
| 逻辑运算符     | 用于根据表达式的值返回真值或假值       |

## 算术运算符

| **运算符** | **术语**   | **示例**    | **结果**  |
| ---------- | ---------- | ----------- | --------- |
| +          | 正号       | +3          | 3         |
| -          | 负号       | -3          | -3        |
| +          | 加         | 10 + 5      | 15        |
| -          | 减         | 10 - 5      | 5         |
| *          | 乘         | 10 * 5      | 50        |
| /          | 除         | 10 / 5      | 2         |
| %          | 取模(取余) | 10 % 3      | 1         |
| ++         | 前置递增   | a=2; b=++a; | a=3; b=3; |
| ++         | 后置递增   | a=2; b=a++; | a=3; b=2; |
| --         | 前置递减   | a=2; b=--a; | a=1; b=1; |
| --         | 后置递减   | a=2; b=a--; | a=1; b=2; |

总结：在除法运算中，除数不能为0

## 赋值运算符

**作用：**用于将表达式的值赋给变量

| **运算符** | **术语** | **示例**   | **结果**  |
| ---------- | -------- | ---------- | --------- |
| =          | 赋值     | a=2; b=3;  | a=2; b=3; |
| +=         | 加等于   | a=0; a+=2; | a=2;      |
| -=         | 减等于   | a=5; a-=3; | a=2;      |
| *=         | 乘等于   | a=2; a*=2; | a=4;      |
| /=         | 除等于   | a=4; a/=2; | a=2;      |
| %=         | 模等于   | a=3; a%2;  | a=1;      |

## 比较运算符

**作用：**用于表达式的比较，并返回一个真值或假值

| **运算符** | **术语** | **示例** | **结果** |
| ---------- | -------- | -------- | -------- |
| ==         | 相等于   | 4 == 3   | 0        |
| !=         | 不等于   | 4 != 3   | 1        |
| <          | 小于     | 4 < 3    | 0        |
| \>         | 大于     | 4 > 3    | 1        |
| <=         | 小于等于 | 4 <= 3   | 0        |
| \>=        | 大于等于 | 4 >= 1   | 1        |

注意：C语言的比较运算中， ==“真”用数字“1”来表示， “假”用数字“0”来表示。==

## 逻辑运算符

**作用：**用于根据表达式的值返回真值或假值

| **运算符** | **术语** | **示例** | **结果**                                                 |
| ---------- | -------- | -------- | -------------------------------------------------------- |
| !          | 非       | !a       | 如果a为假，则!a为真；  如果a为真，则!a为假。             |
| &&         | 与       | a && b   | 如果a和b都为真，则结果为真，否则为假。                   |
| \|\|       | 或       | a \|\| b | 如果a和b有一个为真，则结果为真，二者都为假时，结果为假。 |

## 运算符优先级

*   表中优先级号越小，优先级越高
*   同一优先级中，看结合性



![image-20220314150145103](D:\笔记\C语言\assets\image-20220314150145103.png)

![image-20220314150538705](D:\笔记\C语言\assets\image-20220314150538705.png)

# 流程控制

C语言支持最基本的三种程序运行结构：==顺序结构、选择结构、循环结构==

* 顺序结构：程序按顺序执行，不发生跳转
* 选择结构：依据条件是否满足，有选择的执行相应功能
* 循环结构：依据条件是否满足，循环多次执行某段代码

## if语句

```c
#include<stdio.h>

int main(){
    printf("ok%s\n","hello");
    int a = 2;
    int b = 3;
    scanf("%d",&b);
    if(a<b){
        printf("大家好\n");
    }
    else{
        printf("我不好\n");
    }
    return 0;
}
```

注意：if条件表达式后不要加分号

多条件if

```c
#include<stdio.h>


int main(){
    printf("ok%s\n","hello");
    int a = 2;
    int b = 3;
    scanf("%d",&b);
    if(b<10){
        printf("大家好\n");
    }
    else if (b<20)
    {
        printf("我的名字事沈泽昊\n");
    }
    else if (b<30)
    {
        printf("他的问题\n");
    }
    else{
        printf("我不好\n");
    }
    return 0;
}

```

**嵌套if语句**：在if语句中，可以嵌套使用if语句，达到更精确的条件判断

案例小猪称重

```c
#include <stdio.h>

int main()
{
    int a = 0;
    int b = 0;
    int c = 0;
    printf("a的重量");
    scanf("%d", &a);
    printf("b的重量");
    scanf("%d", &b);
    printf("c的重量");
    scanf("%d", &c);
    printf("小猪a的体重事%d\n",a);
    printf("小猪b的体重事%d\n",b);
    printf("小猪c的体重事%d\n",c);
    if (a > b)
    {
        if (a > c)
        {
            printf("a最重");
        }
        else
        {
            printf("c最重");
        }
    }
    else
    {
        if (b > c)
        {
            printf("b最重");
        }
        else
        {
            printf("c最重");
        }
    }
    return 0;
}

```

## 三目运算符

**作用：** 通过三目运算符实现简单的判断

**语法：**`表达式1 ? 表达式2 ：表达式3`

**解释：**

如果表达式1的值为真，执行表达式2，并返回表达式2的结果；

如果表达式1的值为假，执行表达式3，并返回表达式3的结果。

```c
#include <stdio.h>

int main()
{
    int a = 0;
    int b = 0;
    int c = 0;
    printf("a的重量");
    scanf("%d", &a);
    printf("b的重量");
    scanf("%d", &b);

    c= a> b ?b : c;
    printf("c是%d\n",c);
    return 0;
}

```

##  switch语句

**作用：**执行多条件分支语句

```c
#include <stdio.h>

int main()
{
    // 给电影打分
    int score = 0;
    printf("请给电影打分");
    scanf("%d", &score);
    printf("你打的分数是%d\n", score);
    switch (score) // switch中的表达式类型，只能是整型或者是字符型。
    {
    case 10:
        printf("经典电影");
        break;
    case 9:
        printf("经典电影");
        break;
    case 8:
        printf("一般电影");
        break;
    default:
        printf("烂片");
        break;
    }

    return 0;
}
```

注意，如果不写break，会将switch中的所有代码全执行。

## while循环语句

**作用：**满足循环条件，执行循环语句

**语法：**` while(循环条件){ 循环语句 }`

```c
#include <stdio.h>

int main()
{

    int a = 0;
    while (a < 10)
    {   
        a++;
        printf("我的名字是沈泽昊\n");
    }

    return 0;
}

```

注意：在执行循环语句时候，程序必须提供跳出循环的出口，否则出现死循环

## do....while循环

**作用：** 满足循环条件，执行循环语句

**语法：** `do{ 循环语句 } while(循环条件);`

**注意：**与while的区别在于==do...while会先执行一次循环语句==，再判断循环条件

就是先执行一次，在进行循环

用的不多

```c
#include <stdio.h>

int main()
{

    int a = 0;
    do
    {
        printf("大家好");
    } while (a > 10);

    return 0;
}

/* 输出了大家好，后结束。*/
```

## for循环语句

**作用：** 满足循环条件，执行循环语句

**语法：**` for(起始表达式;条件表达式;末尾循环体) { 循环语句; }`

```c
#include <stdio.h>

int main()
{
    for (int i; i < 10; i++)
    {
    printf("大家好,我是i=%d\n",i);
    }
    return 0;
}
```

for循环中的3个内容可以省略的 ,分号不可以省略

```c
#include <stdio.h>

int main()
{
    int j = 0;
    for (;;)
    {
        if (j == 10)
        {
            break;
        }
        printf("%d\n", j);
        j++;
    }
    return 0;
}
```

9*9乘法表

```c
#include <stdio.h>

int main()
{
    for (int i = 1; i <= 9; i++)
    {
        for (int j = 1; j <= i; j++)
        {
            printf("%d * %d = %d", j, i, j * i);
        }
        printf("\n");
    }

    return 0;
}
```

## break语句

**作用:** 用于跳出==选择结构==或者==循环结构==

break使用的时机：

* 出现在switch条件语句中，作用是终止case并跳出switch
* 出现在循环语句中，作用是跳出当前的循环语句
* 出现在嵌套循环中，跳出最近的内层循环语句

## continue语句

**作用：**在==循环语句==中，跳过本次循环中余下尚未执行的语句，继续执行下一次循环

## goto语句

**作用：**可以无条件跳转语句

**语法：** `goto 标记;`

**解释：**如果标记的名称存在，执行到goto语句时，会跳转到标记的位置

注意：这个语句不会用，因为程序会乱。

```c
#include <stdio.h>

int main()
{

    printf("1\n");
    printf("2\n");
    printf("3\n");
    goto FALG;          //跳转到标记的地方。
    printf("4\n");
    printf("5\n");
FALG:                 // 这里写个标记，名字随便起。
    printf("6\n");
    return 0;
}


/*跳过了4和5 
输出
1
2
3
6*/
```

# 数组

所谓数组，就是一个集合，里面存放了相同类型的数据元素



**特点1：**数组中的每个==数据元素都是相同的数据类型==

**特点2：**数组是由==连续的内存==位置组成的

## 一维数组

### 数组的定义

一维数组定义的三种方式：

1. ` 数据类型  数组名[ 数组长度 ]; `
2. `数据类型  数组名[ 数组长度 ] = { 值1，值2 ...};`
3. `数据类型  数组名[ ] = { 值1，值2 ...};`

eg：

```c
#include <stdio.h>

int main()
{
    // 第一种定义的方式：
    int score[10]; // 数组名score，数组中存放最多10个元素，每个数组的数据了类型都是int
    // 一个数组定义10个数，没有定义的数全是0.
    // 给数组赋值
    // 利用下标(索引)， 从0开始计算。
    score[0] = 1;
    score[1] = 2;
    score[2] = 1;
    // printf("第一个数是%d\n",score[2]);
    // 第二种定义的方式；
    int score2[10] = {1, 2, 3, 4, 5, 6};
    for (int i = 0; i < 10; i++)
    {
        printf("%d\n", score2[i]);
    }
    // 第三种定义数组的方法；（用的很少）
    int score3[10] = {[1] = 2, [4] = 6};
    for (int i = 0; i < 10; i++)
    {
        printf("%d\n", score3[i]);
    }
    //第四种定义的，[]内不写值，但是{},里必须有数据。
    int score2[] = {1, 2, 3, 4, 5, 6};
    return 0;
}
```

总结：在定义二维数组时，如果初始化了数据，可以省略行数

### 数组名的作用

一维数组名称的**用途**：

1. 可以统计整个数组在内存中的长度
2. 可以获取数组在内存中的首地址

```c
//一维数组名称
void test02()
{
	int arr[10] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
	//1、统计整个数组占用内存空间大小
	printf("sizeof arr =  %d\n", sizeof(arr));   
	printf("每个数据占用空间大小 = %d\n", sizeof(arr[0]));
	printf("数组中元素的个数 = %d\n", sizeof (arr) / sizeof(int));

	//2、通过数组的名称，获取到数组的首地址
	printf("数组的首地址为:%d\n", arr);  //%p可以用十六进制显示  %d用十进制显示地址
	//printf("数组的首地址为:%p\n", arr);


	printf("数组中第一个元素的地址：%d\n", &arr[0]);
	printf("数组中第二个元素的地址：%d\n", &arr[1]);
	printf("数组中第三个元素的地址：%d\n", &arr[2]);

	//数组名常量，不可以赋值
	//arr = 100; error不可以给数组名赋值
}
```

> 注意：数组名是常量，不可以赋值

> 总结1：直接打印数组名，可以查看数组所占内存的首地址

>总结2：对数组名进行sizeof，可以获取整个数组占内存空间的大小

 

eg：

用代码实现，找到数组中最大的数

```c
#include <stdio.h>

int main()
{
    int a[5]={0};
    for (int i = 0; i < 5; i++)
    {
        printf("请对数组输入值");
        scanf("%d",&a[i]);
    }
    int max =0 ;
    for (int i = 0; i < 5; i++)
    {
        if (a[i]>a[max])
        {
            max=i;
        }
    }
    printf("最重的小猪的编号%d,体重为%d\n",max+1,a[max]);
    return 0;
}
```

eg：

用代码实现，数组的转置

 ```c
 #include <stdio.h>
 
 int main()
 {
     int arr[6] = {3, 2, 5, 4, 7, 9};
 	//打印转置前的数组。
     for (int i = 0; i < sizeof(arr) / sizeof(arr[0]); i++)
     {
         printf("%d", arr[i]);
     }
     printf("\n");
     // 开始转置
     int start = 0;
     int end = sizeof(arr) / sizeof(arr[0]) - 1;
     while (start < end)
     {
         // 创建一个零时的变量。
         // 开始互换元素
         int temp = arr[start];
         arr[start] = arr[end];
         arr[end] = temp;
         // 下标更新
         start++;
         end--;
     }
     
     // 打印转置后的数组。
     for (int i = 0; i < sizeof(arr) / sizeof(arr[0]); i++)
     {
         printf("%d", arr[i]);
     }
 
     return 0;
 }
 ```

## 冒泡排序

**作用：** 最常用的排序算法，对数组内元素进行排序

1. 比较相邻的元素。如果第一个比第二个大，就交换他们两个。
2. 对每一对相邻元素做同样的工作，执行完毕后，找到第一个最大值。
3. 重复以上的步骤，每次比较次数-1，直到不需要比较

![1541905327273](D:\笔记\C语言\assets\1541905327273.png)

```c
#include <stdio.h>
// 冒泡排序
/*
数据元素个数 ：9

对比轮数 ：8=9-1

对比次数 元素个数 - 对比轮数 - 1 


*/

int main()
{
    int arr[9] = {4, 2, 8, 0, 5, 7, 1, 3, 9};
    // 外层循环 循环8次就可以。作用是需要对比的轮数。
    for (int i = 0; i < sizeof(arr) / sizeof(arr[0]) - 1; i++)
    {
        // 内层循环，主要作用是相邻的两个数是否需要作对比
        for (int j = 0; j < sizeof(arr) / sizeof(arr[0]) - i - 1; j++)
        {
            if (arr[j] > arr[j + 1])
            {
                //开始换值
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }

    // 输出排序好的结果
    for (int i = 0; i < sizeof(arr) / sizeof(arr[0]); i++)
    {
        printf("%d", arr[i]);
    }
    printf("\n");
    return 0;
}
```

## 二维数组

![1541905559138](D:\笔记\C语言\assets\1541905559138.png)

### 数组的定义

二维数组定义的四种方式：

1. ` 数据类型  数组名[ 行数 ][ 列数 ]; `
2. `数据类型  数组名[ 行数 ][ 列数 ] = { {数据1，数据2 } ，{数据3，数据4 } };`
3. `数据类型  数组名[ 行数 ][ 列数 ] = { 数据1，数据2，数据3，数据4};`
4. ` 数据类型  数组名[  ][ 列数 ] = { 数据1，数据2，数据3，数据4};`

建议：以上4种定义方式，利用==第二种更加直观，提高代码的可读性==

```c
#include <stdio.h>
int main()
{

    // 数组的定义
    // 方式一
    int arr[2][3]; // 数组是两行三列的数组
    arr[0][0] = 1;
    arr[0][1] = 2;
    arr[0][2] = 3;
    arr[1][0] = 4;
    arr[1][1] = 5;
    arr[1][2] = 6;
    printf("%d\n", arr[1][2]);
    // 外层控制行
    for (int i = 0; i < 2; i++)
    {
        // 内层控制列
        for (int j = 0; j < 3; j++)
        {
            printf("%d\n", arr[i][j]);
        }
    }
    return 0;
}
```

```c
#include <stdio.h>

int main()
{

    // 数组的定义
    // 方式二
    int arr[2][3] = {
        {1, 2, 1},
        {3, 4, 2}}; // 数组是两行三列的数组

    printf("%d\n", arr[1][2]);
    // 外层控制行
    for (int i = 0; i < 2; i++)
    {
        // 内层控制列 
        for (int j = 0; j < 3; j++)
        {
            printf("%d\n", arr[i][j]);
        }
    }
    return 0;
}
```

```c
//方式3 
	//数据类型 数组名[行数][列数] = { 数据1，数据2 ,数据3，数据4  };
	int arr3[2][3] = { 1, 2, 3, 4, 5, 6 }; //本质也是一个一维数组，地址也是连续
```

```c
	//方式4 
	//数据类型 数组名[][列数] = { 数据1，数据2 ,数据3，数据4  };
	int arr4[][3] = { 1, 2, 3, 4, 5, 6 ,7};  //行数可以省略
```

### 数组名的作用

* 查看二维数组所占内存空间
* 获取二维数组首地址

```c
//二维数组数组名
void test02()
{
	int arr[2][3] = {
		{ 1, 2, 3 },
		{ 4, 5, 6 },
	};

	//可以查看整个数组占用内存空间大小
	printf("二维数组占用空间为%d\n", sizeof(arr)); //24
	printf("二维数组每行占用空间为%d\n", sizeof(arr[0])); //12
	printf("二维数组每个元素占用空间为%d\n", sizeof(arr[0][0])); // 4

	//二维数组 行数  列数
	printf("二维数组行数:%d\n", sizeof(arr) / sizeof(arr[0]));
	printf("二维数组列数:%d\n", sizeof(arr[0]) / sizeof(arr[0][0]));

	//可以查看二维数组首地址
	printf("二维数组首地址 %d\n", arr);
	printf("二维数组第一行地址 %d\n", arr[0]);
	printf("二维数组第二行地址 %d\n", arr[1]);

	printf("第一个元素的地址:%d\n", &arr[0][0]);
	printf("第二个元素的地址:%d\n", &arr[0][1]);
}
```

> 总结1：二维数组名就是这个数组的首地址

> 总结2：对二维数组名进行sizeof时，可以获取整个二维数组占用的内存空间大小

### 二维数组案例

**考试成绩统计：**

案例描述：有三名同学（张三，李四，王五），在一次考试中的成绩分别如下表，**请分别输出三名同学的总成绩**

|      | 语文 | 数学 | 英语 |
| ---- | ---- | ---- | ---- |
| 张三 | 100  | 100  | 100  |
| 李四 | 90   | 50   | 100  |
| 王五 | 60   | 70   | 80   |

```c
#include<stdio.h>
// 二维数组应用案例 求总和成绩
int main()
{
    int scores[3][3] =
        {
            {100, 100, 100}, // 第一个人考试成绩
            {90, 50, 80},    // 第二个人考试成绩
            {60, 70, 80},    // 第三个人考试成绩
        };

    int row = sizeof(scores) / sizeof(scores[0]);
    int col = sizeof(scores[0]) / sizeof(scores[0][0]);

    for (int i = 0; i < row; i++)
    {
        int sum = 0;
        for (int j = 0; j < col; j++)
        {
            sum += scores[i][j];
        }
         printf("第%d个同学总分为%d\n", i + 1, sum);
    }
    return 0;
}
```

##   字符数组

```c
#include<stdio.h>
// 二维数组应用案例 求总和成绩
int main()
{
	// char arr[5] = { 'h','e','l','l','o' };  //error，因为没有\0位置，输出乱码
	char arr[6] = { 'h','e','l','l','o' };     // \0本质就是0
	printf("sizeof = %d\n", sizeof(arr));      //sizeof = 6
	// 遍历字符数组
	for (int i = 0; i < sizeof(arr) / sizeof(char); i++)
	{
		printf("%c", arr[i]);
	}
	printf("\n");
    return 0;
}
```

###  字符串长度统计

字符串统计函数：`strlen()`

头文件：`#include<string.h>`

```c
#include<stdio.h>
#include<string.h>

int main()
{
	char arr1[32] = "hello world";

	printf("%d\n", strlen(arr1));//strlen(字符数组名) 统计字符串长度  不统计\0   输出11
	printf("%d\n", sizeof(arr1));   // 32


	char arr2[] = "hello world";
	printf("arr2 strlen = %d\n", strlen(arr2));//11    
	printf("arr2 sizeof = %d\n", sizeof(arr2));//12   sizeof会算上/0

	char arr3[] = "hello\0world";
	printf("arr3 strlen = %d\n", strlen(arr3));//5  统计到\0结束
	printf("arr3 sizeof = %d\n", sizeof(arr3));//12 
}
```

### 字符数组输入输出

输入，下面两个方法都可以，实用。

```c
#include <stdio.h>

int main()
{
    char arr[16] = "";
    printf("请输入arr的值:");
    scanf("%s", &arr);
    printf("%s\n", arr);
    return 0;
}
```

```c
#include <stdio.h>
#include<string.h>
int main()
{
    char arr[16] = "";
   // arr="hello word"  这样赋值会报错      
    strcpy(arr, "hello word");    //  需要引入 include<string.h>
    printf("%s", arr);
    return 0;
}
```

推荐     fgets

```c
#include <stdio.h>
#include <string.h>
int main()
{
    char arr[16] = "";
    printf("对arr赋值:");
    // 三个参数， arr对哪个数组赋值，sizeof(arr)数组可以接受多少值，stdin标准输入。
    fgets(arr, sizeof(arr), stdin); // stdin中文翻译就是标准输入，
    printf("%s", arr);
    return 0;
}
```

# 函数

**作用：**将一段经常使用的代码封装起来，减少重复代码

## 函数的定义

函数的定义一般主要有5个步骤：

1、返回值类型 

2、函数名

3、参数表列

4、函数体语句 

5、return 表达式

语法：

```c
返回值类型 函数名 （参数列表）
{

       函数体语句

       return表达式

}
```

* 返回值类型 ：一个函数可以返回一个值。在函数定义中
* 函数名：给函数起个名称
* 参数列表：使用该函数时，传入的数据
* 函数体语句：花括号内的代码，函数内需要执行的语句
* return表达式： 和返回值类型挂钩，函数执行完后，返回相应的数据

```c
void test01(){
    //使用void定义函数，不需要返回值，或者return; 就可以了
}
```





**示例：**定义一个加法函数，实现两个数相加

```c
//函数定义
int add(int num1, int num2)
{
	int sum = num1 + num2;
	return sum;
}
```

## 函数的调用

```c
#include <stdio.h>
#include <string.h>

// 函数定义
int add(int num1, int num2)    //num1和num2是形参。
{
    int sum = num1 + num2;
    return sum;
}

int main()   
{
    int a = 2;
    int b = 3;
    int sum = add(a, b);   //调用add函数时传入的值是实参。
    printf("%d\n", sum);
    return 0;
}
```

## 函数的声明

**作用：** 告诉编译器函数名称及如何调用函数。函数的实际主体可以单独定义。



*  函数的**声明可以多次**，但是函数的**定义只能有一次**

```c
#include <stdio.h>
#include <string.h>

// 函数定义
int add(int num1, int num2)    //num1和num2是形参。
{
    int sum = num1 + num2;
    return sum;
}

int main()   
{
    int a = 2;
    int b = 3;
    int sum = add(a, b);   //调用add函数时传入的值是实参。
    printf("%d\n", sum);
    return 0;
}

```

先定义函数，在调用，程序回自动声明函数
函数在下面，就先调用了，程序会报错，需要提前声明。

还没有运行到函数了，就已经调用了，会报错，需要提前声明，告诉程序，我有这个函数。

```c
#include <stdio.h>
#include <string.h>


// 声明函数，
int add(int num1, int num2);
int main()   
{
    int a = 2;
    int b = 3;
    int sum = add(a, b);   //调用add函数时传入的值是实参。
    printf("%d\n", sum);
    return 0;
}

int add(int num1, int num2)    //num1和num2是形参。
{
    int sum = num1 + num2;
    return sum;
}
```

## 函数的常见样式

常见的函数样式有4种

1. 无参无返
2. 有参无返
3. 无参有返
4. 有参有返

```c
#include <stdio.h>
#include <string.h>

// 函数定义

//	1、无参无返
void func1()
{
    printf("this is func1\n");
}

//	2、有参无返
void func2(int a)
{
    printf("this is func2 a = %d\n", a);
    return; // 可选添加
}

//	3、无参有返
int func3()
{
    printf("this is func3\n");
    return 1000;
}

//	4、有参有返  形参中的变量名 C语言下 必须写
int func4(int a)
{
    printf("this is func4 a = %d\n", a);
    return a;
}

void test01()
{
    // 1、无参无返
    func1();
    // 2、 有参无返
    func2(10);
    // 3、无参有返  返回值 可以在调用时候接受或者不接受
    int num = func3();
    printf("num = %d\n", num);
    // 4、有参有返
    int num2 = func4(10000);
    printf("num2 = %d\n", num2);
}
int main()
{
    test01();
    return 0;
}
```

## 值传递

* 所谓值传递，就是函数调用时实参将数值传入给形参
* 值传递时，==如果形参发生，并不会影响实参==

总结： 值传递时，形参是修饰不了实参的

## 函数的分文件编写

解耦，将不同的函数写在不同的文件中

**作用：**让代码结构更加清晰

函数分文件编写一般有4个步骤

1. 创建后缀名为.h的头文件  
2. 创建后缀名为.c的源文件
3. 在头文件中写函数的声明
4. 在源文件中写函数的定义

**示例：**

==test.h文件中==

```c
//#pragma  once  //防止头文件重复包含

#ifndef _TEST_HEAD
#define _TEST_HEAD

#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<string.h>
#include<stdlib.h>


//在头文件中 只写函数的声明，或者是变量的定义

int add(int a, int b);

int sub(int a, int b);

#endif

```

==test.c文件中==

```c
#include "test.h"  //包含 自定义 头文件

int add(int a, int b)
{
	return a + b;
}

int sub(int a, int b)
{
	return a - b;
}
```

==main.c文件中==

```c
#include "test.h" //如果用自定义的函数，需要将头文件包含到当前文件中



void test01()
{
	int a = 10;
	int b = 10;
	printf("a + b = %d\n", add(a, b));
	printf("a - b = %d\n", sub(a, b));

}



int main() {

	test01();

	system("pause");
	return EXIT_SUCCESS;
}
```

# 指针

**指针的作用：** 可以通过指针间接访问内存

* 内存编号是从0开始记录的，一般用十六进制数字表示
* 可以利用指针变量保存地址

## 指针变量的定义和使用

指针变量定义语法： `数据类型 * 变量名；`

```c
#include <stdio.h>

void test()
{
    int a = 1;
    // 定义一个指针
    int *p;
    
    // 指针和变量的关联
    p = &a;  
    
    printf("%d\n", &a);     // 输出内存地址6421988
    printf("%d\n", p);      // 6421988
    *p = 20;
    printf("%d\n", a);      // 输出变量20
    printf("%d\n", *p);     // 20

}

int main()
{
    test();
    return 0;
}
```

指针变量和普通变量的区别

* 普通变量存放的是数据,指针变量存放的是地址
* 指针变量可以通过" * "操作符，操作指针变量指向的内存空间，这个过程称为**解引用**

> 总结1： 我们可以通过 & 符号 获取变量的地址

> 总结2：利用指针可以记录地址

> 总结3：对指针变量解引用，可以操作指针指向的内存

## 指针占的内存有多大

**提问：**指针也是种数据类型，那么这种数据类型占用多少内存空间？

```c
#include <stdio.h>

void test01()
{
	printf("sizeof int * = %d\n", sizeof(int *));
	printf("sizeof char * = %d\n", sizeof(char *));
	printf("sizeof float * = %d\n", sizeof(float *));
	printf("sizeof double * = %d\n", sizeof(double *));
}
/* 输出
sizeof int * = 8
sizeof char * = 8
sizeof float * = 8
sizeof double * = 8
*/
int main()
{
    test01();
    return 0;
}
```

总结：所有指针类型在32位操作系统下是4个字节，64位操作系统下是8个字节

## 空指针和野指针

**空指针**：指针变量指向内存中编号为0的空间

**用途：**初始化指针变量

**注意：**空指针指向的内存是不可以访问的

```c
#include <stdio.h>

// 空指针
void test01()
{                  // 等需要的时候在指向变量
    int *p = NULL; // NULL本质就是 0

    // 访问空指针的存储内容 会报错
    // 内存地址编号为 0 ~ 255之间的系统占用的内存，用户不可以访问
    // printf("%d\n", *p); //error 空指针不可以访问
}
int main()
{
    test01();
    return 0;
}
```

**野指针**：指针变量指向非法的内存空间

```c
#include <stdio.h>

// 野指针
void test02()
{
    // 利用指针变量p指向非法内存空间 0x1100
    // 随便写一块内存，并且指向这个内存
    int *p = 0x1100;

    // printf("%d\n", *p); // 这个内存空间不是你的，还要访问，所以报错。
}

// 注意事项：不要操作未初始化的指针变量
void test03()
{
    int *p; // 也属于野指针,没有指向任何地址，
    *p = 100;
    printf("%d\n", *p); // error 非法访问内存
}
int main()
{
  
    test03();
    return 0;
}
```

总结：空指针和野指针都不是我们申请的空间，因此不要访问。

##  const修饰指针

const修饰指针有三种情况

1. const修饰指针   --- 常量指针
2. const修饰常量   --- 指针常量
3. const即修饰指针，又修饰常量

指针常量和常量指针是不一样的。不能搞混

`常量指针`

```c
#include <stdio.h>

void test03()
{
    int b = 20;
    int a = 10;
    printf("%d\n", &b); //  输出内存地址6421988
    const int *p = &a;    // 常量指针  p是可以修改的,但是*p不可以.
    printf("%d\n", *p); //  10
    p = &b;
    printf("%d\n", *p); //  修改后的20
    printf("%d\n", p);  //  因为修改了p的值,所以内存地址也发生了变化.内存地址6421988
    printf("%d\n", &a); //  内存地址6421984
}
/* 将b的内存地址赋值给指针p，所以原本的指向是a，现在是b。a的值和内存地址都不变。而指针指向了b的内存地址，并且值也发生了改变。*/
int main()
{

    test03();
    return 0;
}
```

`指针常量`

不可以修改定义好的内存地址，可以修改值，

```c
#include <stdio.h>

void test03()
{

    int a = 10;
     int * const p = &a;    // 指针常量  p是可以修改的,但是*p不可以.
    printf("%d\n", *p); //  10
    *p = 20;
    printf("%d\n", *p); //  修改后的20
    printf("%d\n", p);  //  因为修改了p的值,所以内存地址也发生了变化.内存地址6421988
    printf("%d\n", &a); //  内存地址6421988
    printf("%d\n", a);  // 20
    
    /* 将原本存在内存地址的值，改为20，内存地址不变*/
}

int main()
{
    test03();
    return 0;
}
```

`即修饰指针，又修饰常量`

```c
//指针的值和内存地址，都不可以改变
    
#include <stdio.h>

void test03()
{
	int a = 10;
	const int* const p = &a; //等价于 int const * const p = &a;

	//*p = 100;  报错 指针指向的值不可以改

	int b = 20;
	//p = &b; 报错 指针的指向不可以改

}

int main()
{

    test03();
    return 0;
}
```

技巧：看const右侧紧跟着的是指针还是常量, 是指针就是常量指针，是常量就是指针常量

## 指针和数组

**作用：**利用指针访问数组中元素

```c
#include <stdio.h>
//利用指针操作数组
void test01()
{
	int arr[5] = { 1, 2, 3, 4, 5 };
	//定义一个指针变量，接受数组名
	int* p = arr;

	for (int i = 0; i < 5; i++)
	{
		//printf("%d ", *(p + i));
		printf("%d ", p[i]);
	}
	printf("\n");

	//p 和arr区别
	printf("sizeof arr = %d\n", sizeof(arr)); //20
	printf("sizeof p = %d\n", sizeof(p)); //4


	int* p2 = &arr[2];
	printf("%d\n", p2[1]); // 4
	printf("%d\n", p2[-1]);// 2
}

int main()
{

    test01();
    return 0;
}
```

## 指针和函数

**作用：**利用指针作函数参数，可以修改实参的值

```c
#include <stdio.h>
// 利用指针操作数组
//1、值传递
//通过一个函数实现两个整型数字交换的函数
void mySwap(int a, int b)
{
	int temp = a;
	a = b;
	b = temp;

	printf("mySwap中的a = %d\n", a); // 20
	printf("mySwap中的b = %d\n", b); // 10
}

void test01()
{
	int a = 10;
	int b = 20;

	//值传递的 形参是改变不了实参的
	mySwap(a, b);

	printf("test01中的a = %d\n", a);
	printf("test01中的b = %d\n", b);

}


//2、地址传递
void mySwap2(int* p1, int* p2)
{
	int temp = *p1;
	*p1 = *p2;
	*p2 = temp;

	printf("mySwap2中的*p1 = %d\n", *p1);
	printf("mySwap2中的*p2 = %d\n", *p2);
}

void test02()
{
	int a = 10;
	int b = 20;
	//地址传递的形参 可以修改实参
	mySwap2(&a, &b);

	printf("test02中的a = %d\n", a);
	printf("test02中的b = %d\n", b);
}

int main()
{
    test01();
    // test02();
    return 0;
}
```

总结：如果不想修改实参，就用值传递，如果想修改实参，就用地址传递

# 结构体

**作用：**结构体属于用户==自定义的数据类型==，允许用户存储不同的数据类型

**语法：**`struct 结构体名 { 结构体成员列表 }；`

通过结构体创建变量的方式有三种：

* struct 结构体名 变量名
* struct 结构体名 变量名 = { 成员1值 ， 成员2值...}
* 定义结构体时顺便创建变量

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// 结构体定义
// 语法 : struct  结构体成员  {结构体成员列表}

struct student
{
    int id;        // 学号
    char name[64]; // 姓名
    float score;   // 分数
    int age;       // 年龄
};

void test01()
{
    // 1.struct 结构体名 变量名
    struct student s1;
    // 2. struct 结构体名 变量名 ={成员1值,成员2值}
    struct student s2 = {1, "tom", 99.9, 18};
    // 通过.符号访问结构体成员
    printf("%d\n", s2.id);
    printf("%s\n", s2.name);
    printf("%f\n", s2.score);
    printf("%d\n", s2.age);
}

int main()
{
    test01();
    return 0;
}
```

不常用

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// 结构体定义
// 语法 : struct  结构体成员  {结构体成员列表}
//在定义结构体时候，顺便创建结构体变量
struct student2
{
	int id;			//学号
	char name[64];  //姓名
	float score;	//分数
	int age;		//年龄
}s; 

void test02()
{
	s.id = 2;
	//s.name = "Jerry";  //error
	strcpy(s.name, "Jerry");
	s.score = 80;
	s.age = 19;

	
	printf("id = %d\n", s.id);
	printf("name = %s\n", s.name);
	printf("score = %f\n", s.score);
	printf("age = %d\n", s.age);
}

int main()
{
    test02();
    return 0;
}
```

第二中就常用。

> 总结1：定义结构体时的关键字是struct，不可省略

> 总结2：创建结构体变量时，关键字struct可以省略

> 总结3：结构体变量利用操作符 ''.''  访问成员

## 结构体数组

**作用：**将自定义的结构体放入到数组中方便维护



**语法：**` struct  结构体名 数组名[元素个数] = {  {} , {} , ... {} }`

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// 结构体定义
// 语法 : struct  结构体成员  {结构体成员列表}
// 在定义结构体时候，顺便创建结构体变量
struct hero
{
    int id;        // 学号
    char name[64]; // 姓名
    float height;  // 分数
    int age;       // 年龄
};

void test02()
{
    struct hero arr[5] =
        {
            {1, "刘备", 160, 30},
            {2, "张飞", 180, 31},
            {3, "关羽", 170, 32},
            {4, "赵云", 188, 34},
            {5, "吕布", 196, 33} // 最后一行的 ',' 可以省略
        };
    int num = sizeof(arr) / sizeof(struct hero); // 打印出结构体用有几个
    for (int i = 0; i < num; i++)
    {
        printf("id = %d  name = %s height = %d age = %d\n", arr[i].id, arr[i].name, arr[i].height, arr[i].age);
    }
	//求年龄的平均值
	int sum = 0;
	for (int i = 0; i < num; i++)
	{
		sum += arr[i].age;
	}
	printf("年龄平均值为:%d\n", sum / num);

}

int main()
{
    test02();
    return 0;
}
```

结构体指针

**作用：**通过指针访问结构体中的成员



* 利用操作符 `-> `可以通过结构体指针访问结构体属性

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// 结构体定义
// 语法 : struct  结构体成员  {结构体成员列表}
// 在定义结构体时候，顺便创建结构体变量
struct hero
{
    int id;        // 学号
    char name[64]; // 姓名
    float height;  // 分数
    int age;       // 年龄
};

void test02()
{
    struct hero s1 = {1, "张三", 98, 22};
    struct hero *p = &s1;
    // 这两种用的是最多的.
    printf("id = %d name = %s score = %.2f\n", p->id, p->name, p->height);
    printf("id = %d name = %s score = %.2f\n", s1.id, s1.name, s1.height);
    // 这两种用的是最多的.  上面的演变.
    printf("id = %d name = %s score = %.2f\n", (&s1)->id, (&s1)->name, (&s1)->height);
    printf("id = %d name = %s score = %.2f\n", (*p).id, (*p).name, (*p).height);
}

int main()
{
    test02();
    return 0;
}
```

总结：结构体指针可以通过 -> 操作符 来访问结构体中的成员

## 结构体嵌套结构体

**作用：** 结构体中的成员可以是另一个结构体

**例如：**每个老师辅导一个学员，一个老师的结构体中，记录一个学生的结构体

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// 结构体定义
// 语法 : struct  结构体成员  {结构体成员列表}
// 在定义结构体时候，顺便创建结构体变量
//学生结构体定义
struct student
{
	//成员列表
	char name[64];  //姓名
	int age;      //年龄
	int score;    //分数
};

//教师结构体定义
struct teacher
{
	//成员列表
	int id; //职工编号
	char name[64];  //教师姓名
	int age;   //教师年龄
	struct student stu; //子结构体 学生
};


int main() {
    // 给teacher结构体赋值
	struct teacher t1;
	t1.id = 10000;
	strcpy(t1.name, "老王");
	t1.age = 40;
    // 给student结构体赋值
	strcpy(t1.stu.name, "张三");
	t1.stu.age = 18;
	t1.stu.score = 100;

	printf("教师的职工编号： %d 姓名：%s 年龄：%d\n",t1.id,t1.name,t1.age);
	printf("辅导学员的姓名：%s 年龄： %d 分数：%d\n",t1.stu.name,t1.stu.age,t1.stu.score);

	
	system("pause");

	return 0;
}
```

**总结：**在结构体中可以定义另一个结构体作为成员，用来解决实际问题

## 结构体做函数参数 

**作用：**将结构体作为参数向函数中传递

传递方式有两种：

* 值传递
* 地址传递

`值传递`

```c
#include<stdio.h>
//学生结构体定义
struct student
{
    //成员列表
    char name[64];  //姓名
    int age;      //年龄
    int score;    //分数
};

//值传递
void printStudent(struct student stu)
{
    stu.age = 28;
    printf("子函数中 姓名:%s 年龄：%d 分数： %d\n", stu.name, stu.age, stu.score);

}

int main() {
    struct student stu = { "张三",18,100 };
    //值传递
    printStudent(stu);
    printf("主函数中 姓名:%s 年龄：%d 分数： %d\n", stu.name, stu.age, stu.score);

    return 0;
}

/* 
将结构体 传入到函数中，
输出：
子函数中 姓名:张三 年龄：28 分数： 100
主函数中 姓名:张三 年龄：18 分数： 100
这个输出也反映了子涵数是改变，不会影响主函数。
*/
```

`地址传递`

```c
#include <stdio.h>
// 学生结构体定义
struct student
{
    // 成员列表
    char name[64]; // 姓名
    int age;       // 年龄
    int score;     // 分数
};

// 地址传递
void printStudent2(struct student *stu)
{
    stu->age = 28;
    printf("子函数中 姓名:%s 年龄：%d 分数： %d\n", stu->name, stu->age, stu->score);
}

int main()
{

    struct student stu = {"张三", 18, 100};

    printf("------------------------------\n");

    // 地址传递
    printStudent2(&stu);
    printf("主函数中 姓名:%s 年龄：%d 分数： %d\n", stu.name, stu.age, stu.score);

    return 0;
}

/*
将结构体的内存地址传入函数中。
地址传递，子涵是改变了主函数中的参数也改变。
子函数中 姓名:张三 年龄：28 分数： 100
主函数中 姓名:张三 年龄：28 分数： 100
*/
```

### 结构体中 const使用场景

**作用：**用const来防止误操作

```c
#include<stdio.h>
//学生结构体定义
//学生结构体定义
struct student
{
	//成员列表
	char name[64];  //姓名
	int age;      //年龄
	int score;    //分数
};

//const使用场景
void printStudent(const struct student* stu) //加const防止函数体中的误操作
{
	// stu->age = 100; //操作失败，因为加了const修饰
	printf("姓名:%s 年龄：%d 分数： %d\n", stu->name, stu->age, stu->score);

}

int main() {

	struct student stu = { "张三",18,100 };

	printStudent(&stu);

	return 0;
}
```

## 结构体案例

**案例描述：**

设计一个英雄的结构体，包括成员姓名，年龄，性别;创建结构体数组，数组中存放5名英雄。

通过冒泡排序的算法，将数组中的英雄按照年龄进行升序排序，最终打印排序后的结果。

五名英雄信息如下：

```c
	{"刘备",23,"男"},
	{"关羽",22,"男"},
	{"张飞",20,"男"},
	{"赵云",21,"男"},
	{"貂蝉",19,"女"},
```

eg:

```c
#include<stdio.h>

//英雄结构体
struct hero
{
	char name[64];
	int age;
	char sex[32];
};
//冒泡排序
void bubbleSort(struct hero arr[], int len)
{
	for (int i = 0; i < len - 1; i++)
	{
		for (int j = 0; j < len - 1 - i; j++)
		{
			if (arr[j].age > arr[j + 1].age)
			{
				struct hero temp = arr[j];
				arr[j] = arr[j + 1];
				arr[j + 1] = temp;
			}
		}
	}
}
//打印数组
void printHeros(struct hero arr[], int len)
{
	for (int i = 0; i < len; i++)
	{
		printf("姓名:%s 年龄：%d 性别：%s\n", arr[i].name, arr[i].age, arr[i].sex);

	}
}

int main() {

	struct hero arr[5] =
	{
		{"刘备",23,"男"},
		{"关羽",22,"男"},
		{"张飞",20,"男"},
		{"赵云",21,"男"},
		{"貂蝉",19,"女"},
	};

	int len = sizeof(arr) / sizeof(struct hero); //获取数组元素个数

	bubbleSort(arr, len); //排序

	printHeros(arr, len); //打印

	return 0;
}
```

# 字符串处理

- 字符串处理函数，头文件 #include\<string.h>

## strcpy  和 strncpy

`strcpy`

```c
#include <stdio.h>
#include <string.h>

void test01()
{
	char buf[64] = { 0 };

	//buf = "hello world";  //error

	strcpy(buf, "hello world");
	printf("buf = %s\n", buf);

	//strcpy 遇到\0结束拷贝
	strcpy(buf, "hello\0world");
	printf("buf = %s\n", buf);

	//如果目标空间不足，程序出现异常终止
	char buf2[10] = { 0 };
	// strcpy(buf2, "hello world");
	// printf("buf2 = %s\n", buf2);
}

int main()
{

    test01();

    return 0;
}
```

`strcpy`

```c
#include <stdio.h>
#include <string.h>

void test02()
{
	char buf[64] = { 0 };

	strncpy(buf, "hello world", 8);   // buf只有前8个

	printf("buf = %s\n", buf);     // 输出 buf = hello wo

	char buf2[64] = { 0 };
	strncpy(buf2, "hello\0world", 8);  //遇到\0结束拷贝
	printf("buf2 = %s\n", buf2); //  输出 hello     
}


int main()
{

    test02();

    return 0;
}
```

## strcat 和 strncat

字符串拼接使用

**strcat  函数原型：**

`char *strcat(char *dest, const char *src);`

**功能：**将src字符串连接到dest的尾部，‘\0’也会追加过去

**返回值：**

​	成功：返回dest字符串的首地址

​	失败：NULL



**strncat  函数原型：**

`char *strncat(char *dest, const char *src, size_t n);`

**功能：**将src字符串前n个字符连接到dest的尾部，‘\0’也会追加过去

**返回值：**

​	成功：返回dest字符串的首地址

​	失败：NULL

```c
#include <stdio.h>
#include <string.h>

//strcat  strncat 字符串拼接
void test01()
{
	char buf1[64] = "hello";  //hello world\0
	char buf2[64] = "world";

	strcat(buf1, buf2);    //将buf2拼接到buf1的后面。
	printf("%s\n", buf1); //helloworld

	strncat(buf1, buf2, 3);  //现在的buf1已经变成了helloworld
	printf("%s\n", buf1);  //helloworldwor
}


int main()
{

    test01();

    return 0;
}
```

拼接是不能超过被拼接的大小，会报错。

## strcmp  和 strncmp

判断字符串大小的。

**strcmp  函数原型：**

`int strcmp(const char *s1, const char *s2);`

**功能：**比较 s1 和 s2 的大小，比较的是字符ASCII码大小



**返回值：**

​	相等：=0

​	大于：>0

​	小于：<0



**strncmp  函数原型：**

`char *strncmp(char *dest, const char *src, size_t n);`

**功能：**比较 s1 和 s2 前n个字符的大小，比较的是字符ASCII码大小

**返回值：**

​	相等：=0

​	大于：>0

​	小于：<0

```c
#include <stdio.h>
#include <string.h>

//strcmp     compare
void test01()
{
	char buf1[64] = "hello";

	printf("%s\n", buf1);

	char buf2[64] = "";
	fgets(buf2, sizeof(buf2), stdin);   // 接受字符串。输入的时候会回车，回车就是\n，需要将\n变成\0

	//hello\n 中的\n改为\0
	buf2[strlen(buf2) - 1] = '\0';

	if (strcmp(buf1, buf2) == 0)
	{
		printf("buf1 == buf2\n");
	}
	else if (strcmp(buf1, buf2) > 0)
	{
		printf("buf1 > buf2\n");
	}
	else
	{
		printf("buf1 < buf2\n");
	}

}


void test02()
{
	printf("请输入一个季节  spring summer autumn winter\n");

	char buf[64] = "";
	fgets(buf, 64, stdin);
	buf[strlen(buf) - 1] = '\0';

	if (strncmp(buf, "spring", 6) == 0)
	{
		printf("春天\n");
	}
	else if (strncmp(buf, "summer", 6) == 0)
	{
		printf("夏天\n");
	}
	else if (strncmp(buf, "autumn", 6) == 0)
	{
		printf("秋天\n");
	}
	else if (strncmp(buf, "winter", 6) == 0)
	{
		printf("冬天\n");
	}
}

int main()
{

    test01();

    return 0;
}
```

## sprintf

格式化字符串

**sprintf    函数原型：**

`int sprintf(char *str, const char *format, ...);`

**功能：**根据参数format字符串来转换并格式化数据，然后将结果输出到str指定的空间中



**返回值：**

​	成功：实际格式化的字符个数

​	失败： - 1

```c
#include <stdio.h>
#include <string.h>

// sprintf
void test01()
{
    char buf[64] = {0};

    // 格式化输出到字符串中
    int year = 0;
    int month = 0;
    int day = 0;
    printf("请输入年份\n");
    scanf("%d", &year);
    printf("请输入月份\n");
    scanf("%d", &month);
    printf("请输入天\n");
    scanf("%d", &day);

    sprintf(buf, "今天是%d 年 %d月 %d日", year, month, day);
    printf("buf = %s\n", buf);
}

int main()
{

    test01();

    return 0;
}
```

## sscanf

sscanf  函数原型：**

`int sscanf(const char *str, const char *format, ...);`

**功能：**从str指定的字符串读取数据，并根据参数format字符串来转换并格式化数据



**返回值：**

​	成功：成功转换的值的个数

​	失败： - 1

```c
#include <stdio.h>
#include <string.h>

//sscanf 字符串拆分
void test01()
{
	char msg[1024] = "phone:13690000000;2019/5/20;该还钱了";

	long long phone = 0;
	int year = 0;
	int month = 0;
	int day = 0;
	char content[64] = { 0 };

	int num =sscanf(msg, "phone:%lld;%d/%d/%d;%s", &phone, &year, &month, &day, content);

	printf("%llu\n", phone);
	printf("%d\n", year);
	printf("%d\n", month);
	printf("%d\n", day);
	printf("%s\n", content);
	printf("%d\n", num);
}

int main()
{

    test01();

    return 0;
}
```

sscanf扩展

格式化分割字符串的时候，可以通过一些==特殊格式==实现不同拆分



| 格式         | 作用                    |
| ------------ | ----------------------- |
| %\*s 或 %\*d | 忽略数据                |
| %[w]s        | 读n个宽度的数据         |
| %[a - z]     | 匹配a到z中任意字符      |
| %[aBc]       | 匹配指定的a、B、c       |
| %[\^a]       | 匹配非a的任意字符       |
| %[\^a-z]     | 匹配非 a - z 的所有字符 |



```c
//sscanf扩展
void test02()
{
	char str[1024] = "12345abcde";

	char buf[1024] = { 0 };

	sscanf(str, "%*d%s", buf);

	printf("buf:%s\n", buf);

}

void test03()
{
	char str[1024] = "abcde12345"; //遇到空格或者 \t 结束忽略操作

	char buf[1024] = { 0 };

	//sscanf(str, "%*s%s", buf);
	sscanf(str, "%*[a-z]%s", buf);

	printf("buf:%s\n", buf);
}


void test04()
{
	char str[1024] = "12345abcde"; 

	char buf[1024] = { 0 };

	
	sscanf(str, "%6s", buf);

	printf("buf:%s\n", buf);
}


void test05()
{
	char str[1024] = "12345abcde";
	char buf[1024] = { 0 };

	//如果匹配失败，就不在向后进行匹配
	sscanf(str, "%*d%[a-z]", buf);

	printf("buf:%s\n", buf);
}


void test06()
{
	char str[1024] = "aaBbcCde";
	char buf[1024] = { 0 };

	sscanf(str, "%[abc]", buf);

	printf("buf:%s\n", buf);
}


void test07()
{
	char str[1024] = "aaBbcCde12345";
	char buf[1024] = { 0 };

	sscanf(str, "%[^b]", buf);

	printf("buf:%s\n", buf);
}
```

## strchr

字符查找

**strchr 函数原型：**

`char *strchr(const char *s, char c);`

**功能：**在字符串s中查找字母c出现的位置

**返回值：**

​	成功：返回第一次出现的c地址

​	失败：NULL

```c
#include <stdio.h>
#include <string.h>

// sscanf 字符串拆分
void test01()
{
    char str[1024] = "zhangtao@sina.com";

    char *ret = strchr(str, '@');

    if (ret == NULL)
    {
        printf("没有@字符\n");
    }
    else
    {
        printf("有@字符，位置在 %d\n", ret - str);
    }
}

int main()
{

    test01();

    return 0;
}
```

##  strstr

**strstr 函数原型：**

`char *strstr(const char *s, const char *s2);`

**功能：**在字符串s中查找字符串s2出现的位置



**返回值：**

​	成功：返回第一次出现的s2地址

​	失败：NULL

```c
#include <stdio.h>
#include <string.h>

// sscanf 字符串拆分
void test01()
{
    char src[] = "ddddabcd123abcd333abcd";
    char *p = strstr(src, "abcd");
    if (p == NULL)
    {
        printf("没有找到目标字符串\n");
    }
    else
    {
        printf("找到了目标字符串\n");
        printf("p = %d\n",*p);
    }
}

int main()
{

    test01();

    return 0;
}
```

## strtok

**strtok 函数原型：**

`char *strtok(char *str, const char *dst);`

**功能：**

*   将字符串分割成一个个片段。
*   当strtok()在参数str的字符串中发现参数dst中包含的分割字符时, 则会将该字符改为\0 字符
*   当连续出现多个时只替换第一个为\0
*   第一次需要填入参数str，之后str中填入NULL即可



**返回值：**

​	成功：分割后字符串首地址

​	失败：NULL

```c
#include <stdio.h>
#include <string.h>

// sscanf 字符串拆分
//strtok 字符串分割
void test01()
{
	char buf[1024] = "刘备:关羽:张飞:赵云:吕布:诸葛亮";

	char* names[64] = { 0 };//将buf中的信息按照:分割，放入到字符串数组names中

	int i = 0;
	names[i] = strtok(buf, ":");

	while ( names[i] != NULL)
	{
		i++;
		names[i] = strtok(NULL, ":");
	}

	//遍历字符串数组
	i = 0;
	while (names[i] != NULL)
	{
		printf("%s\n", names[i++]);
	}
}

int main()
{

    test01();

    return 0;
}
```

## atoi

**atoi 函数原型：**

`int atoi(const char *nptr);`

**功能：**atoi()会扫描nptr字符串，跳过前面的空格字符，直到遇到数字或正负号才开始做转换，而遇到**非数字**或 **'\0'**才结束转换，并将结果返回。



**返回值：**

​	成功转换后整数



类似的函数有：

*   atof()：把一个小数形式的字符串转化为一个浮点数。

*   atol()：将一个字符串转化为long类型
*   atoll()：将一个字符串转化为long long类型

```c
void test01()
{
	char buf[1024] = "  123abc";

	int num = 0;

	num = atoi(buf);

	printf("%d\n", num);

}
```

**总结：**

| 函数      | 功能                       |
| --------- | -------------------------- |
| gets()    | 获取可带空格的字符串       |
| fgets()   | 获取可带空格的字符串(安全) |
| puts()    | 向屏幕输出字符串(自带换行) |
| fputs()   | 向屏幕输出字符串(不带换行) |
| strlen()  | 统计字符个数(\0结束统计)   |
| strcpy()  | 字符串拷贝                 |
| strncpy() | 字符串拷贝(拷贝n个字符)    |
| strcat()  | 字符串拼接                 |
| strncat() | 字符串拼接(拼接n个字符)    |
| strcmp()  | 字符串对比                 |
| strncmp() | 字符串对比(对比n个字符)    |
| sprintf() | 格式化拼接字符串           |
| sscanf()  | 格式化拆分字符串           |
| strchr()  | 查找字符                   |
| strstr()  | 查找字符串                 |
| strtok    | 分割字符串                 |
| atoi()    | 字符串转整数               |

# 文件

## 文件基本概念

数据源的一种，最主要的作用是保存数据，如word、txt、头文件、源文件、exe等

### 文件的分类

文件可以分为

* 磁盘文件
* 设备文件

**磁盘文件：** 

* 磁盘文件是计算机里的文件。存储信息不受断电的影响，存取速度相对于内存慢得多了

**设备文件：**

 * 操作系统中把每一个与主机相连的输入、输出设备看作是一个文件
 * 例如 显示器称为标准输出文件, 键盘称为标准输入文件

### 磁盘文件的分类

计算机的存储在物理上是二进制的，所以物理上所有的磁盘文件本质上都是一样的：以字节为单位进行顺序存储。

从用户或操作系统的角度，将文件分为：

* 文本文件
* 二进制文件

**文本文件：**

* 基于字符编码，常见的编码有ASCII、UNICODE等
* 一般可以使用文本编辑器直接打开
* 如数字5678的存储形式 (ASCII码)为： 00110101 00110110 00110111 00111000

 

**二进制文件：**

* 基于值编码,自己根据具体应用,指定某个值是什么意思
* 把内存中的数据按其在内存中的存储形式原样输出到磁盘上
* 如数5678的存储形式(二进制码)为：00010110  00101110

## 文件指针

*   在C语言中，操作文件之前必须先打开文件；所谓“打开文件”，就是让程序和文件建立连接的过程。
*   打开文件之后，程序可以得到文件的相关信息，例如大小、类型、权限、创建者、更新时间等。
*   操作系统为了操作文件，提供了一堆文件的**操作函数**，而函数通过**文件指针**识别不同的文件

```c
typedef struct
{
	short           level;	//缓冲区"满"或者"空"的程度 
	unsigned        flags;	//文件状态标志 
	char            fd;		//文件描述符
	unsigned char   hold;	//如无缓冲区不读取字符
	short           bsize;	//缓冲区的大小
	unsigned char   *buffer;//数据缓冲区的位置 
	unsigned        ar;	 //指针，当前的指向 
	unsigned        istemp;	//临时文件，指示器
	short           token;	//用于有效性的检查 
}FILE;
```

FILE是系统使用typedef定义出来的有关文件信息的一种结构体类型

**总结：如果我们想利用C语言操作一个文件，首先要获取到文件指针**

文件指针式专门的指针

```c
FILE *fp = NULL;
// 是FILE不是int
```



##  fopen

 fopen函数

函数原型： `FILE *fopen(char *filename, char *mode);`

功能：打开文件

参数：

​	filename - 需要打开的文件名，根据需要加上路径

​	mode - 打开文件的模式设置

返回值：

​    成功：文件指针

​	失败：NULL

| **打开模式** | **含义**                                                     |
| ------------ | ------------------------------------------------------------ |
| r或rb        | 以只读方式打开一个文本文件（不创建文件，若文件不存在则报错） |
| w或wb        | 以写方式打开文件(如果文件存在则清空文件，文件不存在则创建一个文件) |
| a或ab        | 以追加方式打开文件，在末尾添加内容，若文件不存在则创建文件   |
| r+或rb+      | 以可读、可写的方式打开文件(不创建新文件)                     |
| w+或wb+      | 以可读、可写的方式打开文件(如果文件存在则清空文件，文件不存在则创建一个文件) |
| a+或ab+      | 以添加方式打开文件，打开文件并在末尾更改文件,若文件不存在则创建文件 |

注：b是二进制模式的意思，b只是在Windows有效，在Linux用r和rb的结果是一样的

## fclose函数

函数原型：`int fclose(FILE *fp);`

* 打开的文件会占用内存资源，如果总是打开不关闭，会消耗很多内存
* 一个进程同时打开的文件数是有限制的，超过最大同时打开文件数，再次调用fopen打开文件会失败
* 如果没有明确的调用fclose关闭打开的文件，那么程序在退出的时候，操作系统会统一关闭

**打开要关闭，不关会占内存，并却打开文件是有限的。**

```c
#include <stdio.h>
#include <string.h>

// sscanf 字符串拆分
//strtok 字符串分割
void test01()
{
FILE *fp = NULL;
	fp = fopen("a.txt", "r"); 
	if (fp == NULL)
	{
		printf("打开失败\n");
		return;
	}

	printf("打开成功\n");

	fclose(fp);

}
int main()
{

    test01();

    return 0;
}
```

##  字符方式读写文件

**写文件 fputc**

​	函数原型： `int fputc(int ch, FILE *stream)`

**读文件 fgetc**

​	函数原型：`int fgetc(FILE * stream)`

`写文件`

```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void test01()
{
    // 打开文件
    FILE *fp = NULL;
    fp = fopen("a.txt", "w");
    if (fp == NULL)
    {
        printf("打开失败\n");
        return;
    }
    // 操作文件
    char buf[] = "hello word\n";
    int i = 0;
    // 定义一个i=0，循环，如果字符串最后是\0就不写了，
    while (buf[i] != '\0')
    {
        // bu[i]，i在++，将buf中的每一个字符都写入fp文件中。
        fputc(buf[i], fp);
        i++;
    }
    // 关闭文件
    fclose(fp);
}

int main()
{
    test01();
    return 0;
}
```

`读文件`

```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void test01()
{
	//打开文件
	FILE *fp = NULL;
	fp = fopen("a.txt", "r");
	if (fp == NULL)
	{
		printf("打开失败\n");
		return;
	}

	//操作文件
	char ch = 0;
    //EOF就是文件尾，读到文件尾就结束。 EOF就是end of file。
	while(  (ch = fgetc(fp)) != EOF  )
	{
		printf("%c", ch);
	}
	//关闭文件
	fclose(fp);
}


int main()
{
    test01();
    return 0;
}
```

注：==EOF==为文件结束标志，可以用来判断文件是否读取到文件尾

## 行方式读写文件

**写文件 fputs**

​	函数原型： `int fputs(const char *str, FILE *stream)`



**读文件 fgets**

​	函数原型：`char * fgets(char *str, int size, FILE *stream)`

`写文件`

```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void test01()
{

    FILE *fp = NULL;
    fp = fopen("b.txt", "w");
    if (fp == NULL)
    {
        printf("打开失败\n");
        return;
    }
    char *buf[] = {
        "床前明月光\n",
        "疑似地上霜\n",
        "举头望明月\n",
        "低头思故乡\n"};
    for (int i = 0; i < sizeof(buf) / sizeof(buf[0]); i++)
    {
        fputs(buf[i], fp);
    }

    fclose(fp);
}

int main()
{
    test01();
    return 0;
}
```



```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
// 读文件
void test01()
{

    FILE *fp = NULL;
    fp = fopen("b.txt", "r");

    if (fp == NULL)
    {
        printf("文件打开失败\n");
        return;
    }

    char buf[1024] = {0};
    // 一行一行的读，用的feof代表文件尾，!feof(fp)这个意思就是>>>没有读到fp的文件尾。
    while (!feof(fp))
    {
        fgets(buf, 1024, fp);
        //把最后的一个字符强行改为/0。将\n 改为 \0
        buf[strlen(buf) - 1] = '\0';
        // 读文件尾结束。
        if (feof(fp))
        { 
            break;
        }
        
        // 文件最后有一个换行符。
        
        printf("%s\n", buf);
    }

    // 关闭文件
    fclose(fp);
}

int main()
{
    test01();
    return 0;
}
```

## 格式化方式读写文件

**写文件 fprintf**

​	函数原型： `int fprintf(FILE * stream, const char * format, ...);`

**读文件 fscanf**

​	函数原型：`int fscanf(FILE * stream, const char * format, ...);`

```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
// 读文件
//格式化写文件
struct Hero
{
	char name[64]; //姓名
	int atk;  //攻击力
	int def;  //防御力
};

void test01()
{
	struct Hero hero[5] = {
		{ "斧头帮主",110, 200 },
		{ "紫霞仙子",150, 150 },
		{ "菩提老祖",170, 130 },
		{ "牛魔王",100, 180 },
		{ "二当家",999, 999 }
	};

	FILE* fp = NULL;
	fp = fopen("c.txt", "w");
	if (fp == NULL)
	{
		printf("文件打开失败\n");
		return;
	}

	for (int i = 0; i < sizeof(hero) / sizeof(struct Hero); i++)
	{
		//1个中文占用两个字节
		int len = fprintf(fp, "%s %d %d\n", hero[i].name, hero[i].atk, hero[i].def);
		printf("第%d行 写入字节数量为：%d\n", i + 1, len);
	}

	//关闭文件
	fclose(fp);
}

int main()
{
    test01();
    return 0;
}
```

`fscanf`

```c
void test02()
{
	struct Hero hero[5] = { 0 };
	FILE* fp = NULL;
	fp = fopen("c.txt", "r");
	if (fp == NULL)
	{
		printf("文件打开失败\n");
		return;
	}

	int i = 0; 
	while (!feof(fp))
	{
		int num = fscanf(fp, "%s %d %d\n", hero[i].name, &hero[i].atk, &hero[i].def);
		i++;
	}

	for (int j = 0; j < i; j++)
	{
		printf("姓名：%s  攻击力：%d 防御力：%d\n", hero[j].name, hero[j].atk, hero[j].def);
	}

	//关闭文件
	fclose(fp);
}
```

## 块方式读写文件

**写文件 fwrite**

​	函数原型： `size_t fwrite(const void *ptr, size_t size, size_t nmemb, FILE *stream);;`

**读文件 fread**

​	函数原型： `size_t fread(void *ptr, size_t size, size_t nmemb, FILE *stream);`

`fwrite`

```c
//按块写文件
struct Hero
{
	char name[64]; //姓名
	int age; //年龄
};

void test01()
{
	FILE* fp = NULL;
	fp = fopen("d.txt", "w");
	if (fp == NULL)
	{
		printf("文件打开失败\n");
		return;
	}

	struct Hero heros[4] = {
		{ "孙悟空", 33 },
		{ "韩信", 28 },
		{ "赵云", 45 },
		{ "亚瑟", 35 }
	};

	for (int i = 0; i < 4; i++)
	{
		//参数1 数据首地址  参数2  块大小  参数3  块数量  参数4  文件指针
		fwrite(&heros[i], sizeof(struct Hero), 1, fp);
	}

	//关闭文件
	fclose(fp);
}
```

 `fread`

```c
//按块读文件
void test02()
{
	FILE* fp = NULL;
	fp = fopen("d.txt", "r");
	if (fp == NULL)
	{
		printf("文件打开失败\n");
		return;
	}

	struct Hero heros[4] = { 0 };

	fread(&heros, sizeof(struct Hero), 4, fp);

	for (int i = 0; i < 4; i++)
	{
		printf("姓名:%s 年龄:%d\n", heros[i].name, heros[i].age);
	}

	fclose(fp);
}
```

## 文本文件与二进制文件

**文本文件与二进制文件区别**

*   换行符的处理方式不同
*   Windows下
    *   文本文件在内存中的 \n 保存到磁盘中会变为 \r\n
    *   二进制文件在内存中的 \n 保存到磁盘中依然为 \n
*   Linux下换行符没有区别

```c
void test01()
{
	FILE* fp = fopen("test1.txt", "w"); //只写  文本文件
	if (fp == NULL)
	{
		printf("文件打开失败\n");
		return;
	}

	char buf[] = "helle world\n";

	int i = 0;
	while (buf[i] != '\0')
	{
		fputc(buf[i], fp);
		i++;
	}

	fclose(fp);
}

void test02()
{
	FILE* fp = fopen("test2.txt", "wb"); //只写  二进制
	if (fp == NULL)
	{
		printf("文件打开失败\n");
		return;
	}

	char buf[] = "helle world\n";

	int i = 0;
	while (buf[i] != '\0')
	{
		fputc(buf[i], fp);
		i++;
	}

	fclose(fp);
}
```

注：打开文件时候，打开下拉框内选择打开方式，点击 二进制编辑器 打开文件

## 文件光标

文件光标移动这里主要介绍3个函数

* rewind


* fseek
* ftell      

#### rewind

函数原型：`void rewind(FILE *stream );`

功能：把文件流（文件光标）的读写位置移动到文件开头

```c
void test01()
{
	FILE* fp = fopen("rewind.txt", "w+");
	if (fp == NULL)
	{
		printf("文件打开失败\n");
		return;
	}

	fputs("hello world", fp);

	//fclose(fp);
	//fp = fopen("rewind.txt", "r");

	rewind(fp);

	char buf[32] = { 0 };
	fgets(buf, sizeof(buf),fp);
	printf("%s\n", buf);
	fclose(fp);
}
```

## fseek

函数原型： `int fseek(FILE *stream, long offset, int fromwhere);`



功能：移动文件流（文件光标）的读写位置。



fromwhere：取值如下：

*   SEEK_SET：从文件开头移动offset个字节
*   SEEK_CUR：从当前位置移动offset个字节
*   SEEK_END：从文件末尾移动offset个字节

```c
//按块写文件
struct Hero
{
	char name[64]; //姓名
	int age; //年龄
};

void test02()
{
	FILE* fp = NULL;
	fp = fopen("fseek.txt", "w");
	if (fp == NULL)
	{
		printf("文件打开失败\n");
		return;
	}

	struct Hero heros[4] = {
		{ "孙悟空", 33 },
		{ "韩信", 28 },
		{ "赵云", 45 },
		{ "亚瑟", 35 }
	};

	for (int i = 0; i < 4; i++)
	{
		//参数1 数据首地址  参数2  块大小  参数3  块数量  参数4  文件指针
		fwrite(&heros[i], sizeof(struct Hero), 1, fp);
	}

	//关闭文件
	fclose(fp);



	//fseek函数 进行随机位置读取
	FILE* fp2 = NULL;
	fp2 = fopen("fseek.txt", "r");
	if (fp2 == NULL)
	{
		printf("文件打开失败\n");
		return;
	}


	struct Hero temp;

	fseek(fp2, sizeof(struct Hero) * 2, SEEK_SET);
	fseek(fp2, sizeof(struct Hero), SEEK_CUR);
	fseek(fp2, -(long)sizeof(struct Hero)*3, SEEK_END);
	
	fread(&temp, sizeof(struct Hero), 1, fp2);

	printf("姓名：%s  年龄：%d\n", temp.name, temp.age);

	fclose(fp2);
}
```

## ftell

函数原型：`long ftell(FILE *stream);`



功能： 获取文件流（文件光标）所在的读写位置

```c
void test03()
{
	FILE *fp = fopen("ftell.txt", "w"); 
	fputs("hello,斧头帮主", fp);
	fclose(fp);

	fp = fopen("ftell.txt", "r");
	//将文件流指针定位到文件尾部
	fseek(fp, 0, SEEK_END);
	//得到文件流指针的偏移量
	int len = ftell(fp); 
	printf("len = %d\n", len); 

	fclose(fp);
}
```

