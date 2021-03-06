1、变量的赋值
变量赋值的本质是进行了对象的传递 从使用内存的方式来划分，可以分为可变和不可变数据 
可变数据类型：
列表 list
字典 dict
优点：变量值变化不会创建新的对象，内存地址不变，内存地址中存的内容变化；或者地址进行了扩容
缺点：进行变量赋值时，传递的是列表最开头的地址，称为对象的引用 
不可变数据类型：
整型 int
浮点型 float
字符串型 string
元组 tuple
优点：内存中不管有多少个引用，引用的都是相同的对象，只占用一块内存
缺点：当对变量进行运算，改变变量引用的对象的值时，必须新创建对象。创建对象越多，内存消耗越大

2、容器序列的深浅拷贝
从类型的定义角度，可以分为序列和非序列 序列 - 容器序列：list、tuple、collections.deque 等，容器序列可以存放不同类型的数据 - 扁平序列：str、bytes、bytearray、memoryview (内存视图)、array.array 等，存放的是相同类型的数据扁平序列只能容纳一种类型。 深浅拷贝只对容器序列有效，对其他序列无效 当列表中包含子列表，如果需要拷贝列表，需要考虑是进行深拷贝(把列表中所有的值完全复制且重新占一块新内存)还是浅拷贝(只复制它的对象的引用即可)

import copy
new_list4 = copy.copy(old_list)
new_list5 = copy.deepcopy(old_list)

assert new_list4 == new_list5 #True
assert new_list4 is new_list5 #False AssertionError
非序列：
字典，hash是构成字典的基本思想，基本算法
hash是线性查找时间，查找效率高

3、函数的调用
调用函数不带括号，表示传递函数；调用函数带括号，表示执行函数 传递类，如果不带括号表示传递类对象，如果带括号表示对类进行实例化

4、变量的作用域
作用域又叫命名空间 高级语言对变量的使用：

变量声明
定义类型（分配内存空间大小）
初始化（赋值、填充内存）
引用（通过对象名称调用对象内存数据） Python 和高级语言有很大差别，在模块、类、函数中定义，才有作用域的概念。 Python 作用域遵循 LEGB 规则。 LEGB 含义解释：
L-Local(function)；函数内的名字空间
E-Enclosing function locals；外部嵌套函数的名字空间（例如closure）
G-Global(module)；函数定义所在模块（文件）的名字空间
B-Builtin(Python)；Python 内置模块的名字空间 可解决：
同名不同作用域的变量问题
变量值查找顺序问题

5、函数工具与高阶函数
位置参数 命名参数 可变长参数

*args: 传递若干个参数到函数内，并将这些参数封装到一个名为args的tuple对象中。args只是一个名字，可以替换
**kargs: 对参数进行拆解，优先获取关键字参数，把剩下参数传递给 *args 

6、闭包
解耦内外函数 设置好函数模式，执行函数时无需考虑其模式。强调函数定义态非运行态

7、装饰器介绍
增强而不改变原有函数装饰器 强调函数的定义态而不是运行态 分类

被修饰函数带参数
被修饰函数带不定长参数
被修饰函数带返回值 作用
简明代码
灵活，起到包装作用

8、被装饰函数带参数和返回值的处理
装饰器可由上至下堆叠，堆叠顺序可能影响装饰结果 包含参数的装饰器

Python内置装饰器

functools.wraps
functools.lru_cache

9、类装饰器
官方文档中的装饰器代码阅读指南 对象协议与鸭子类型 对象协议： 实现对象协议的方法叫魔术方法 鸭子类型 定义对象没有初始化类型，在运行过程中改变对象类型 正常输出时调用__str__，涉及对象间通信的时候会调用__repr__ 容器类型协议

str 打印对象时，默认输出该方法的返回值
getitem、setitem、delitem 字典索引操作
iter 迭代器
call 可调用对象协议

10、yield语句
在函数中使用 yield 关键字，可以实现生成器 2. 生成器可以让函数返回可迭代对象 3. yield 和 return 不同，return 返回后，函数状态终止，yield 保持函数的执行状态， 返回后，函数回到之前保存的状态继续执行。 4. 函数被 yield 会暂停，局部变量也会被保存。 5. 迭代器终止时，会抛出 StopIteration 异常。

11、迭代器使用的注意事项
迭代器是一个对象，一个实现了迭代器协议的对象。 迭代器协议需要包含 iter() 和 next() 两种方法 list , tuple , dict和 set 都是可迭代对象，都是可以生成迭代器的可迭代容器。这些对象都可以用 iter() 方法生成一个生成器。也可以使用 for 循环制造一个迭代器，这个迭代器通过 next() 函数遍历所有元素。

如何生成迭代器？ 为了实现一个迭代器对象/类，必须实现__iter__() 和 next() 两种方法 iter() 和 init() 扮演类似的角色，你可以进行一系列操作，但是必须返回迭代器对象本身 next() 方法允许进行一系列操作，但是必须返回序列中的下一个元素 为了防止迭代无法终止，可以通过 StopIteration 结束循环

如何使用map：

借助lamda函数
借助用户自定义函数
借助使用多个迭代对象的内置函数

12、协程简介
协程
多用于IO密集型应用，遇到IO操作时切换到其他部分程序运行，等IO操作完成后再继续
多线程
协程是异步的，线程时同步的
协程是非抢占式的，线程时抢占式的
线程是被动调度的，协程时主动调度的
协程可以暂停函数的执行，保留上一次调用时的状态，时增强性生成器
协程是用户级的任务调度，线程是内核级的任务调度
协程适用于IO密集型程序，不适用于CPU密集型程序(适合多进程/线程)的处理

13、aiohttp简介
事件循环 注册回调函数 多进程结合协程 因为GIL锁的问题，没有多线程结合协程