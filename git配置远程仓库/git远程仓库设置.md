# 连接仓库

# git连接gitee

第一步在gitee是建立一个仓库

![image-20231208212805983](D:\笔记\git配置远程仓库\assets\image-20231208212805983.png)



```
ssh-keygen -t rsa -C "XXXXX@XXX.com"
```

![img](D:\笔记\git配置远程仓库\assets\1745115-20200222170622669-1668407453.png)

## win系统中

在C:\Users\Lenovo\.ssh可以找到，

在在记事本中打开id_rsa.pub复制，在github或者gitee中创建ssh

在输入

```
yes
```

将密钥添加到gitee中

![image-20231208213036277](D:\笔记\git配置远程仓库\assets\image-20231208213036277.png)

没有写完

## ubuntu系统中

在gitee已经有仓库了

```python
git init
git config user.name "shenzehao"
git config user.email "3145315473@qq.com"
# 将代码上传到仓库的地址。下面的代码修改成，自己的仓库
git remote add origin git@gitee.com:shenzehao/yingmingapi.git
ssh-keygen -C "3145315473@qq.com"
cat ~/.ssh/id_rsa.pub  # 把公钥复制到gitee 「个人设置」->「安全设置」->「SSH公钥」->「添加公钥」
rm -rf .idea
git add .
git commit -m "fix: crate app instance"
git push -u origin master
```











