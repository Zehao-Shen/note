# 版本控制

# 一.开始管理

想让git去管理一个目录，需要几步

- 进入要管理的文件夹

- 执行初始化命令(让git帮助我们管理当前文件夹)

```
git init
```

注：执行完这个代码会在文件夹下生成一个`.git`的文件，不要删啊，删了就离职了

- 管理目录下的文件状态

```
git status    # 查看状态
git status –s # 简约显示

红色：新增文件/修改了原来的老文件
绿色：git已经管理起来了，
```

- 管理指定文件（红变绿）（将文件放到暂存区）

```
git add 文件名   指定文件
git add .      管理全部文件
```

这里需要配置个人信息（第一次下载需要）

```
 git config --global user.email "you@example.com"
 git config --global user.name "Your Name"
```

- 生成版本

```
git commit -m '版本名字' 
```

- 查看版本记录

```
git log
```

###########################下面的很重要##########################

> **记住每次修改完文件后都需要让git管理起来**
> git add .
> git status    
> git commit -m '版本名字' 
>
> 查看是否变绿

###########################上面的很重要##########################

# 2.git三大区域

<img src="D:\笔记\git\assets\6756c73e5e99a486c76b250c24a4826.png" alt="6756c73e5e99a486c76b250c24a4826"  />

# 3.扩展新功能

将新功能交给git，并生成版本

```
git add 文件名        

git commit -m '版本名字'
```

# 4.回滚

- 回滚到之前的版本

```
git log
git reset --hard 版本号
```

- 回滚到之后功能

```
git reflog     # 忘记了生成版本，可以用这个
git reset --hard 版本号    
# 注意是版本号， 不是版本名字
```

# 5.分支

> 分支：就是c1版本(c1有100个文件)，c2版本(c2修改了其中的10个，又增加了20个文件)，c2只是存了修改的和增加的，不变的文件还在c1，c2在使用时是去c1中拿不动的文件，和自己的文件，
>
> 分支：可以分成几个不同的版本，之后在合并。 eg:c3分成c4和c5两个还可以在合并

**分支可以给使用者提供多个环境的使用，意味着你可以把你的工作从开发主线上分离出来，以免影响开发主线。**



![384af9d65430a799d90a6aa50206a1e](D:\笔记\git\assets\384af9d65430a799d90a6aa50206a1e.png)

> 出现bug后该怎么办：
>
> 创建一个新的分支，修复好后在合并到下一个版本。

主线名称：master
其他分支：随便起名，一般就是dev分支和bug分支

- 查看分支

```
git branch
```

- 创建分支

```
git branch 分支名称 
eg：git branch dev  (创建新的分支)
```

- 切换分支

```
git checkout 分支名称
eg：git checkout dev  (创建新的分支)
```

创建分支，并进入分支

```
git checkout -b 分支名称
eg：git checkout -b develop
```



**注：在哪个分支，哪个就是绿色的**

- 分支合并(可能产生冲突)

> 产生冲突手动修改，在执行`git add .` 和`git commit -m '版本名字'`
>
> **注意：合并前没有`git add .` 和`git commit -m '版本名字'`会出现像自动合并的感觉，**

```
git merge 要合并的分支
git merge <分支名称>       # 重点把指定分支下的代码合并当前所在分支，
注意：切换分支在合并（切换到主分支合并其他分支）
```

- 删除分支

```
git branch -d 分支名称
```





# 6.gitee仓库和git的共同使用



- 给远程仓库起名字

```
git remote add origin 远程仓库地址
eg：git remote add origin https://gitee.com/shenzehao/gitpro.git
远程仓库地址    https://gitee.com/shenzehao/gitpro.git
仓库名字       origin
```

- 向远程仓库推送

```
git push -u origin 分支
eg：git push -u origin master
eg: git push -u origin dev
```

从仓库拿代码

- 新建一个文件夹，打开git命令行
- 克隆远程仓库代码

```
git clone 远程仓库地址
eg:  git clone  https://gitee.com/shenzehao/gitpro.git
```

- 却换分支

```
git checkout 分支
eg：git checkout dev
```

- 删除和这个仓库的联系。

```
 git remote rm origin
```

- 更新本地代码

```
git pull origin dev  
eg: git pull origin dev  (和上面的git clone 不一样，clone是将全部的文件都下载下来，git pull origin dev是就dev分支上本地没有的文件下载下来。)
```

- 

```
git pull origin dev  
就等同于
git fetch origin dev   把代码拉到本地
git merge origin dev   合并    

一般不用，直接git pull
```



每次工作前都是（哪个分支的代码更新过，拉哪个分支的代码）

> 1.切换到dev分支
> git  checkout   dev 
>
> 2. 拉代码
> git pull origin dev
>
> 3.写完
> git add .
> git status    
> git commit -m '版本名字' 
>
> 4.传代码
> git push -u origin dev

第二天上班依然

> 1.切换到dev分支
> git  checkout   dev 
>
> 2. 拉代码
>     git pull origin dev
>
> 3.写完
> git add .
> git status    
> git commit -m '版本名字' 
>
> 4.传代码
> git push -u origin dev

- 记录图形展示

```
git log --graph --pretty=format:"%h %s"
```



![159bb0291a5a1f628da430c90b794ff](D:\笔记\git\assets\159bb0291a5a1f628da430c90b794ff.png)

# rebase的使用

rebase可以保持提交记录简洁，不交叉

rebase(变基)

解决冲突

# 7.多人协同开发

> 你们公司如何做到多人开发？
>
> 答：我们公司每个人有自己的分支







