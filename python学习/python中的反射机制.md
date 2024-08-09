[TOC]



# python中的反射机制(2022.2.11)

## 1.什么是反射

指的是程序运行过程中可以"动态"获取对象信息

### 反射的内置函数（通过字符串来操作属性值）

也可以通过dir获取属性，如

```python
print(dir(object1))
print((object1.__dict__[dir(object1)[-2]]))
```

#### 1.hasattr()  

判断有无属性

> ```python
> hasattr(obj,'name')   #  判断有无属性
> # hasattr(obj,'name')  # 如果对象obj中有name这个属性，就输出True走否则输出False
> ```

#### 2.getattr() 

运行obj下的属性

```python
getattr(obj,'name',None) # 等同于obj.name,不存在该属性则返回默认值None，
print(getattr(obj,'name',None)) # 如果有obj.name就运行，对象obj中没有name这个属性，就输出None，print(getattr(obj,'name'))没有写None，又没有属性报错。（如果None,写成别的，如果没有就name，就会返回写成的那个。）
```

#### 3.setattr() 

修改obj下的某个属性

```python
setattr(obj,'name','value') # 将对象obj中的name值修改成value
print(setattr(object1,'name','cao'))  # 将name=xxx 修个成name=cao
```

#### 4.delattr()  

删除obj下的某个属性

```python
delattr(obj,'name')
print(delattr(obj,'name')) # 将obj下的name属性删除
```

##### 练习的反射机制例子

```python
class Ftp:
    def put(self, file):
        print('正在上传{file}'.format(file=file))

    def get(self, file):
        print('正在下载{file}'.format(file=file))

    def core(self):
        while True:
            cmd = input('请输入get或者put').strip()
            if cmd == 'get' or cmd == 'put':
                pass
            else:
                print('请重新输入cmd')
                continue
            file = input('请输入想要上传或者下载的文件').strip()
            if hasattr(self, cmd):
                func = getattr(self, cmd)
                func(file)
                break
object2 = Ftp()
object2.core()
```



