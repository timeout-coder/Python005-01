1、类属性与对象属性
class Human(object):
    # 静态字段
    live = True

    def __init__(self, name):
        # 普通字段
        self.name = name

man = Human('Adam')
woman = Human('Eve')

# 有静态字段，live 属性
Human.__dict__
# 有普通字段， name 属性
man.__dict__

# 实例可以使用普通字段也可以使用静态字段
man.name
man.live = False # 不会改变类的静态字段的值

# 查看实例属性
man.__dict__ # 普通字段有 live 变量
man.live # False
woman.live # True

# 类可以使用静态字段
Human.live

# 可以为类添加静态字段
Human.newattr = 1

2、类的属性作用域
作用域：
• _name 人为约定不可修改
• __name 私有属性
• __name__ 魔术方法
魔术方法：
• 双下划线开头和结尾的方法，实现了类的特殊成员，这类称作魔术方法
• 不是所有的双下划线开头和结尾的方法都是魔术方法
• 魔术方法类似其他语言的接口
私有属性是可以访问到的，Python 通过改名机制隐藏了变量名称
• class.__dict__

3、类方法描述器
普通方法：至少一个 self 参数，表示该方法的对象
类方法：至少一个 cls 参数，表示该方法的类
静态方法：由类调用，无参数

4、描述器
描述器高级应用 getattribute
属性的处理
在类中，需要对实例获取属性这一行为进行操作，可以使用：

__getattribute__()
__getattr__()
异同：

都可以对实例属性进行获取拦截
__getattr__() 适用于未定义的属性
__getattribute__() 对所有属性的访问都会调用该方法

描述器高级应用 getattr

4、属性描述符 property
实现特定协议（描述符）的类 property 类需要实现以下方法

__get__
__set__
__delete__
class Teacher:
	def __init__(self, name):
		self.name = name

	def __get__(self):
		return self.name

	def __set__(self, value):
		self.name = value

pythonteacher = Teacher('yin')
pythonteacher.name = 'wilson'
print(pythonteacher.name)

5、面向对象编程 —— 继承
特性
封装
将内容封装到某处
从某处调用被封装的内容
继承
基本继承
多重继承
重载
Python 无法在语法层面实现数据类型重载，需要在代码逻辑上实现
Python 可以实现参数个数重载
多态
Pyhon 不支持 Java 和 C# 这一类强类型语言中多态的写法，
Python 使用“鸭子类型”
新式类
新式类和经典类的区别
当前类或者父类继承了 object 类，那么该类便是新式类，否则便是经典类

object 和 type 的关系
object 和 type 都属于 type 类 (class 'type')
type 类由 type 元类自身创建的。object 类是由元类 type 创建
object 的父类为空，没有继承任何类
type 的父类为 object 类 (class 'object')
类的继承
单一继承
多重继承
菱形继承（钻石继承）
继承机制 MRO
MRO 的 C3 算法

6、SOLID 设计原则与设计模式 & 单例模式
SOLID 设计原则
单一责任原则 The Single Responsibility Principle
开放封闭原则 The Open Closed Principle
里氏替换原则 The Liskov Substitution Principle
依赖倒置原则 The Dependency Inversion Principle
接口分离原则 The Interface Segregation Principle
设计模式
设计模式用于解决普遍性问题
设计模式保证结构的完整性
单例模式
对象只存在一个实例
init 和 new 的区别：
new 是实例创建之前被调用，返回该实例对象，是静态方法
init 是实例对象创建完成后被调用，是实例方法
new 先被调用，init 后被调用
new 的返回值（实例）将传递给 init 方法的第一个参数，init 给这个 实例设置相关参数

7、元类
元类是关于类的类，是类的模板。
元类是用来控制如何创建类的，正如类是创建对象的模板一样。
元类的实例为类，正如类的实例为对象
创建元类的两种方法
type
type（类名，父类的元组（根据继承的需要，可以为空），包含属性的字典（名字和值））
class

8、mixin 模式
抽象基类
抽象基类（abstract base class，ABC）用来确保派生类实现了基类中的特定方法。 使用抽象基类的好处：
避免继承错误，使类层次易于理解和维护
无法实例化基类
如果忘记在其中一个子类中实现接口方法，会尽早报错。

在程序运行过程中，重定义类的继承，即动态继承。好处：
可以在不修改已有类源代码的情况下，对已有类进行扩展
进行组件的划分。








