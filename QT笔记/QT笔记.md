QWidget 是一个预定义的窗口，

QDialog  是一个对话窗口  需要打开文件，等等

QMainWindow 

![窗口类继承关系](D:\笔记\QT笔记\assets\image-20201009170432819-420ab17b1be841bb9fb2a976e79ea591.png)

## 信号

```c++
 connect()  //第一个参数是信号对的发出者，第二个参数是信号的指针，
            //第三个参数接受信号的接收者，第四个参数接受信号的接收者的处理方法，还有第五个参数。

```

设置信号的三种方式

第一种使用宏

```c++
connect(ui->spinBox,SIGNAL(valueChanged(int)),this,SLOT(onPinBoxValueChaneged(int)));
```

第二种使用指针

```c++
connect(ui->spinBox,&QSpinBox::valueChanged,this,&helloco::onPinBoxValueChaneged);
```

第三种使用函数

自动有的信号

```c#
// 声明信号 通过emit发送信号。
signals:
    void numChanged(int value);
```

### 自定义信号

在头文件中写写在类中。

```c++
// 信号声明不需要实现，槽需要声明并需要实现。
signals:
    void go();
```

在cpp文件中的实现

```c++
    connect(ui->lineEdit,SIGNAL(QLineEdit::returnPressed()),this,SLOT(on_pushButton_2_clicked()));
    connect(this,SIGNAL(go()),this,SLOT(on_pushButton_clicked()));
// 运行on_pushButton_2_clicked函数发送 go()信号，后执行on_pushButton_clicked函数


void testDialog::on_pushButton_clicked()
{
    qDebug("点击了");
}

void testDialog::on_pushButton_2_clicked()
{
    emit go();
}
```



信号

```c++
accept();   // accept会发出一个信号。
代码运行到accept()会发出一个信号，写connect时写accepted
connect(m_loginDialog,&loginDialog::accepted,this,&uimain::show);
```

## 槽

槽需要提前在头文件中定义

```c#
private slots:
    void onNumChanged(int value);
    void onPinBoxValueChaneged(int value);
    void on_spinBox_valueChanged(int arg1);
```

发起信号，运行接受信号者的处理方法。（connect函数的第第四个参数）。

## 信号槽和信号

在单线程下emit还是相当于函数的调用。

```c++
 connect(this,SIGNAL(dowmloadFile()),this,SLOT(on_pushButton_clicked1()));
 connect(this,SIGNAL(dowmloadFile()),this,SLOT(on_pushButton_clicked2()));
 connect(this,SIGNAL(dowmloadFile()),this,SLOT(on_pushButton_clicked3()));




// 槽函数。
void xiazaiDialog::on_pushButton_clicked()
{

    renameFile();
    emit dowmloadFile();
    
    //原理
    on_pushButton_clicked1();
    on_pushButton_clicked2();
    on_pushButton_clicked3();
    
}

void xiazaiDialog::on_pushButton_clicked1()
{
    qDebug()<<"on_pushButton_clicked1";
}

void xiazaiDialog::on_pushButton_clicked2()
{
    qDebug()<<"on_pushButton_clicked2";
}

void xiazaiDialog::on_pushButton_clicked3()
{
    qDebug()<<"on_pushButton_clicked3";
}


void xiazaiDialog::renameFile(){
    qDebug()<<"点击了";
}


```

上面代码的执行结果。

```c++
点击了
on_pushButton_clicked1
on_pushButton_clicked2
on_pushButton_clicked3
```

和信号绑定的顺序有关。在单线程下emit还是相当于函数的调用。

## sender或者文本

```c++
// 获取点击的是哪一个按钮
void xiazaiDialog::on_pushButton_clicked()
{

    renameFile();
    // 获取按钮的文本
    QPushButton* btn = dynamic_cast<QPushButton*>(sender());
    qDebug()<<btn->text();
    emit dowmloadFile();
}

```

## 信号断开连

![image-20240703193410119](D:\笔记\QT笔记\assets\image-20240703193410119.png)

```c++
#include "dialog.h"
#include "ui_dialog.h"

Dialog::Dialog(QWidget *parent)
    : QDialog(parent)
    , ui(new Ui::Dialog)
{
    ui->setupUi(this);

    connect(ui->spinBox,SIGNAL(valueChanged(int)),ui->progressBar,SLOT(setValue(int)));
    connect(ui->spinBox,SIGNAL(valueChanged(QString)),ui->progressBar,SLOT(setWindowTitle(QString)));
    connect(ui->spinBox,SIGNAL(valueChanged(int)),ui->label,SLOT(setNum(int)));
}

Dialog::~Dialog()
{
    delete ui;
}

void Dialog::on_pushButton_clicked()
{
    //1
    //断开ui->spinBox的所有链接
    // disconnect(ui->spinBox,nullptr,nullptr,nullptr);
    //ui->spinBox->disconnect(ui->spinBox,nullptr,nullptr,nullptr);
    // 这两个写法不同，但是功能是一样的，

    // 2
    //断开其中一个信号的所有链接(断开valueChanged(int))
    //ui->spinBox->disconnect(ui->spinBox,SIGNAL(valueChanged(QString)),nullptr,nullptr);

    // 3
    // 断开接收者ui->progressBar所有的链接。
   // ui->spinBox->disconnect(ui->spinBox,nullptr,ui->progressBar,nullptr);

    //4
    // 断开接收者的某个槽函数（ui->label）的链接
    ui->spinBox->disconnect(ui->spinBox,nullptr,ui->label,SLOT(setNum(int)));
}
```

## QSignalMapper

匹配信号发送。

解耦，将不同的页面在不同文件中，但是信号也写在不同文件，向不同的页面传递信号，使用**QSignalMapper**







































## 设置窗口

```c

    // 设置窗口没有标题栏
this->setWindowFlags(Qt::CustomizeWindowHint);

    // 设置窗口无边框
this->setWindowFlags(Qt::FramelessWindowHint);

    //设置窗口置顶
    // 只使用窗口置顶，窗口无边框会无效，所以下面这样写。
this->setWindowFlags(Qt::FramelessWindowHint|Qt::WindowStaysOnTopHint);
```

## 按钮(pushButton)

是输入框有记忆功能。对输入的文本进行提示

```c++
    QString text =ui->lineEdit->text().trimmed();
    qDebug()<<text;
    if (historyList.contains(text)){
        return;
    }
    historyList<<text;
    QCompleter *completer=new QCompleter(historyList);
    ui->lineEdit->setCompleter(completer);
```

控制按钮的显示和隐藏

```c++
ui->pushButton->setVisible(!ui->pushButton->isVisible());
```

## 模态对话框

模态对话框就是点开这个对话框后，必须操作，不能点别的

```c++
// 必须登录了才可以提示出页面。
#include "login2dialog.h"
#include <QWidget>
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    login2Dialog w;
    QWidget m;
    //w必须继承QDialog类
    // w.show();
    int code =w.exec();
    m.setWindowTitle("主窗口");
    if(code==QDialog::Accepted){
        m.show();
        return a.exec();
    }else{
        qDebug()<<"退出程序";
    }
    return a.exec();
}
```

在ui文件中，设置槽，登录按钮的槽cliked()连接accept()，

退出按钮的槽clicked()，连接reject()，

```c++
QObject::connect(pushButton123, &QPushButton::clicked, login2Dialog, qOverload<>(&QDialog::accept));
QObject::connect(pushButton, &QPushButton::clicked, login2Dialog, qOverload<>(&QDialog::reject));
```

## 对话框（下载）

在帮助中搜索Dialog Windows。又多个对话框，下面的代码是上传文件的对话框

```c++
#include <QFileDialog>
//上传
void tool::on_pushButton_clicked()
{
    // 上传单个文件。
   // QString path = QFileDialog::getOpenFileName(this,QString("选择文件"),"./");
   //  if(path != ""){
   //     qDebug()<<path.toStdString().data();
   // }
   //  // 上传多个文件
   //  QStringList path_list = QFileDialog::getOpenFileNames(this,QString("选择文件"),"./");
   // qDebug()<<path_list;
  // 上传多个文件,并指定类型。
    // QStringList path_list = QFileDialog::getOpenFileNames(this,QString("选择文件"),"./", "hpp (*tool*.h *.cpp) ;; MakeFile (*.Release *.Debug)");
    // qDebug()<<path_list;
    // 上传整个文件夹
    // QString path = QFileDialog::getExistingDirectory(this,QString("选择文件"),"./");
    // qDebug()<<path;
}

//下载,
// 下载并不是下载，是返回一个路径，下载的代码还是需要自己写的。
void tool::on_pushButton_2_clicked()
{
    QString path = QFileDialog::getSaveFileName(this,QString("选择文件"),"./");
         if(path != ""){
            qDebug()<<path.toStdString().data();
        }
}
```



## 事件

事件和信号容易混淆

![image-20240623163427830](D:\笔记\QT笔记\assets\image-20240623163427830.png)

#### 处理事件的5个方法

函数的后缀是Event的函数都可以重写。

![image-20240623164151384](D:\笔记\QT笔记\assets\image-20240623164151384.png)

画×就是不推荐

第一种：重写控件。

### 事件循环

![image-20240623163814232](D:\笔记\QT笔记\assets\image-20240623163814232.png)

### 父子之间通信

##### 例子：

在头文件中类中写

```c++
protected:
    void keyPressEvent(QKeyEvent *event);
    bool event(QEvent *e);
```

在函数中写实现但是最后函数要执行父类的方法

```c++
void myshijian::keyPressEvent(QKeyEvent *event)
{

    qDebug()<<"子窗口";
    QLineEdit::keyPressEvent(event);  // 执行父类中的
    event->ignore();	 // 向父窗口传递。
    //event->accept();    // 不向父窗口传递。
}

bool myshijian::event(QEvent *e)
{
    if(e->type()==QEvent::KeyPress){
          qDebug()<<"event";
    }

    return QLineEdit::event(e);  // 执行父类中的
}
```

##### 例子：

鼠标移动控窗口启动

头文件

```c++
// 在class中写
protected:
    void mouseMoveEvent(QMouseEvent *event);
    void mousePressEvent(QMouseEvent *event);

private:
    QPoint m_start;  // 坐标 
```

源文件

```c++
void loginDialog::mouseMoveEvent(QMouseEvent *event)
{
    if(event->buttons()==Qt::LeftButton)  //鼠标左键。
    {
        QPoint targetPos = event->pos()-m_start+pos();   // 鼠标移动后的坐标，
        this->move(targetPos);                       	 // 窗口移动这这个坐标
    }

    QDialog::mouseMoveEvent(event);
}

void loginDialog::mousePressEvent(QMouseEvent *event)
{
    qDebug()<<"点击了";
    if(event->button()==Qt::LeftButton)  //鼠标左键。
    {
       		 qDebug()<<event->pos();  // 输出坐标
            m_start=event->pos();  // 相对于当前控件原点位置
    }
    QDialog::mousePressEvent(event);
   // QWidget::mousePressEvent(event);
}
```

##### 例子：

禁止复制

头文件

```c++
#ifndef TESTCV_H
#define TESTCV_H

#include <QLineEdit>
#include <QWidget>

class testcv : public QLineEdit
{
    Q_OBJECT
public:
    testcv(QWidget *parent=nullptr);
protected:
    void keyPressEvent(QKeyEvent *e);
};

#endif // TESTCV_H

```

源码文件

```c++
#include "testcv.h"

#include <QKeyEvent>

testcv::testcv(QWidget *parent):QLineEdit(parent) {}

void testcv::keyPressEvent(QKeyEvent *e)
{
    // 捕获ctrl c和v;
    if(e->modifiers()==Qt::ControlModifier){
        if(e->key()==Qt::Key_C||e->key()==Qt::Key_V){
            return;
        }
    }
    QLineEdit::keyPressEvent(e);
}

```

## QSS

和css一样

两种设置方法。

第一种是ui中右击设置

第二种是在源文件写。

```c++
Widget::Widget(QWidget *parent)  // 类的构造函数
    : QWidget(parent)
    , ui(new Ui::Widget)
{
    ui->setupUi(this);
    ui->pushButton->setStyleSheet("QPushButton{\
    font-size:20pt;\
    color:red\
}");
}
```

QSS选择器

<img src="D:\笔记\QT笔记\assets\image-20240624161541735.png" alt="image-20240624161541735" style="zoom:50%;" />

通用选择器

```css
*{

}
```

类选择器

```css
QPushButton{
font-size : 20pt;
}

QPushButton,QLabel{
font-size : 20pt;
}
```

id选择器

给组件修改名字后

```css
QLabel#label_1{
font-size : 20pt;
}
```

属性选择器

```css
QPushButton[flag="true"]{

}
```

后代选择器 

右边的图上看

```css
xxx>xxx{
    
   
}
```

子控件选择器

```css
QCheckBox{
font-size:20pt;
color:red
}

QCheckBox::indicator{
border:2px solid bule;
width :20px;
height: 20px;
}
```

状态选择器

鼠标点击或者鼠标触碰就发生变化

```css
QCheckBox:hover{   // 鼠标触碰就发生变化
font-size:30pt;
color:bleak
}
```

![image-20240624164437123](D:\笔记\QT笔记\assets\image-20240624164437123.png)

## 盒子模型

在帮助中搜索qt style

 ![image-20240624165341917](D:\笔记\QT笔记\assets\image-20240624165341917.png)

第一个       
Qt Style Sheets       

Qt Style Sheets 的使用方法  

第二个   

Qt Style Sheets Examples

Qt Style Sheets Examples 样式表设置的使用文档

第三个   

Qt Style Sheets Reference 

Qt Style Sheets Reference   样式状态

   

## 读取文件中的QSS

新建一个c++文件，不需要继承类

`头文件`

```c++
#ifndef FILEHELPER_H
#define FILEHELPER_H

#include <QString>
class filehelper
{
public:
    filehelper();

    static QString readAllText(const QString &filePath);
};

#endif // FILEHELPER_H
```

`源码文件`

```c++
#include "filehelper.h"

#include <QFile>

filehelper::filehelper() {}

QString filehelper::readAllText(const QString &filePath)
{
    QFile file(filePath);
    if(file.exists() && file.open(QIODevice::ReadOnly)){
        QByteArray data= file.readAll();
        file.close();
        return data;
    }
    throw "读取文件失败";
}
```

`main文件`

```c++
#include "logindialog.h"

#include <QApplication>
#include <Qwidget>
#include <filehelper.h>

int main(int argc, char *argv[])
{
    /***************************************************************************/
    QApplication a(argc, argv);
    //1.读取文件中的qss文件
    QString qssStr = filehelper::readAllText("D:/QTfile/login/defult.qss");
    //2.QApplication加载qss文件。
    a.setStyleSheet(qssStr);
    //上面就是读取qss文件
    /************************************************************************/
    loginDialog w;
    w.show();
    return a.exec();
}
```



`qss文件`

```c++
/*设置Qss的默认样式*/
*{
/*白色主题*/
background-color:white;

/*字体*/
font-family: "微软雅黑";
font-size: 10pt;
color: #555555
}

/*通用：设置标题*/
*[style="h1"]{
font: bold 25pt;
color: #111111;
}
*[style="h2"]{
	font: bold 22pt;
	color: #222222;
}
*[style="h3"]{
	font: bold 20pt;
	color: #333333;
}
*[style="h4"]{
	font: bold 16pt;
	color: #444444;
}
*[style="h5"]{
	font: bold 12pt;
}

/*设置通用的QLineEdit*/
QLineEdit{
	border: 1px solid #cccccc;
	border-radius: 2px;/*圆角一般使用偶数进行设置*/
	selection-background-color: darkgray;
	height: 28px;
}
QLineEdit:hover{
	border-color: #1296db;
}

/*通用标签设置*/
QLabel{
	background-color: transparent;
}
QLabel#labelLogo{
	min-width: 32px;
	min-height: 32px;
	border-image: url(":/static/imgs/logo.png");
}

/*通用按钮设置*/
QPushButton{
	background: transparent;
	border: 1px solid #dddddd;
	border-radius: 2px;
	height: 28px;
	width: 56px;
}
QPushButton:hover{
	color:#1296db;
	border-color: #1296db;
}

QPushButton#btnLogin{
	background: #1296db;
	color:white;
    font: bold 12pt;
}

QPushButton#btnClose:hover{
	color:red;
}

```



```c++
//在 qss文件中写。
*[style="h1"]{
		font : bold 25px;
		color :#111111;
}
*[style="h2"]{
		font : bold 22px;
		color :#111111;
}
// 使ui->label_3这个控件使用h1，这个style要上面的qss文件相对应。
ui->label_3->setProperty("style","h1");
```

## 资源文件

将文件放到项目中，就是static

放到资源文件中直接，访问static中的路径







# QString的常用方法

```c++
    QString  s1="ab中文";
    qDebug()<<"s1"<<s1;

    // 使用的utf-8，就不需要QString::fromLocal8Bit()
    QString  s2=QString::fromLocal8Bit("ab中文");
    qDebug()<<"s2"<<s2;
    //这个也是可以的。
    QString  s3=QString::fromUtf8("ab中文");
    qDebug()<<"s3"<<s3;
```



![image-20240702105810866](D:\笔记\QT笔记\assets\image-20240702105810866.png)

## age格式化

```c++
#include <QByteArray>
#include <QTextCodec>
#include <QDebug>
#include <QChar>
#include <QTime>
#include <QDir>

int main(int argc, char *argv[])
{
    /*第一部分编码*/
//    QString s1 = "ab中文";
//    qDebug() << "s1: " << s1;
//    QString s2 = QString::fromLocal8Bit("ab中文");
//    qDebug() << "s2: " << s2;
//    QString s3 = QString::fromUtf8("ab中文");
//    qDebug() << "s3: " << s3;



    /*第二部分 案例*/
    // 1 trimmed 删除两边空白字符
//    qDebug() << QString("   abcd   \n ") << QString("   abcd   \n ").trimmed();

    // 2 simplified 删除两边空白字符，同时删除中间多余的空白符，只保留一个空格
//    qDebug() << QString("   ab     \n   cd   \n ") << QString("   ab     \n   cd   \n ").simplified();

    // 3 arg格式化
    // 3.1 按照时间生成一个日志文件路径 格式为：根目录/logs/时间.log
//    QString rootDir = QDir::currentPath();
//    QString time = QTime::currentTime().toString("hh-mm-ss");
//    QString filePath = QString("%1/logs/%2.log").arg(rootDir, time);
//    qDebug() << filePath;
//    //output: F:/mooc/lessions/code/mooc-lessons/13/build-13-2-Desktop_Qt_5_15_2_MSVC2019_64bit-Debug/logs/17-08-36.log

//    // 3.2 格式化数字字符串，保留2位有效数字
//    qDebug() << QString("%1").arg(123.45678, 0, 'f', 2);

    // 4 合并与拆分
    // 4.1 拼接文件路径 QStringList::join
//    QStringList sList;
//    sList << "resource" << "images" << "png" << "hello.png";
//    qDebug() << sList.join("/");

    // 4.2 获取文件名称 split
    QString filePath = "resource/images/png/hello.png";
//    QStringList nameArray = filePath.split("/");
//    qDebug() << nameArray;
//    qDebug() << nameArray.last();

    // 4.2 获取文件名称 section
    qDebug() << filePath.section("/", -1);
}
```

## QVarviant

qt使用QVarviant，对不同参数类型对外提供统一的接口。

```c++
#include "mainwindow.h"

#include <QApplication>


QList<QStringList> readExcel(){
    QList<QStringList> table;
    QStringList row1;
    QStringList row2;
    QStringList row3;
    row1<<"s1"<<"s2"<<"s3";
    row2<<"11"<<"22"<<"33";
    row3<<"44"<<"44"<<"55";
    table<<row1<<row2<<row3;
    qDebug()<<table;
    return table;
}


QString readCellText(const QVariant& location, const QList<QStringList>& table){
    QString text;
    int row = -1;
    int col = -1;

    if (location.canConvert<QString>()){   // 判断QVariant的类型
        //A1 C1
        QString loc = location.toString();
        QString cols = "ABC";
        col = cols.indexOf(loc.at(0));
        row = loc.at(1).digitValue()-1;
    }
    else if (location.canConvert<QPoint>()) // 判断QVariant的类型
    {
        QPoint point = location.toPoint();
        row = point.x();
        col = point.y();
    }
    else{
        qDebug() << "invalid location: " << location;
        return "";
    }

    return table[row][col];
}

int main(int argc, char *argv[])
{
    // QApplication a(argc, argv);
    // MainWindow w;
    // w.show();
    // return a.exec();
   QList<QStringList> table = readExcel();
    
    qDebug() << "string: " << readCellText("A1", table);
    qDebug() << "point: " << readCellText(QPoint(0, 0), table);
}

```

## QJson

![image-20240702142945372](D:\笔记\QT笔记\assets\image-20240702142945372.png)

一共是4个类。

可以看

```c++
#include "qstringwidget.h"
#include <QApplication>
#include <qdir.h>
#include <QTime>
#include <QJsonDocument>
#include <QJsonObject>



QJsonObject read(const QString &path){
    QFile file(path);
    file.open(QIODevice::ReadOnly);   // 打开这个文件。
    QByteArray data =file.readAll();
    file.close();
    QJsonDocument doc =QJsonDocument::fromJson(data);
    QJsonObject ret=doc.object();
    return ret;
}   
 

void write(const QJsonObject& object, const QString& path){

    QFile file(path);
    file.open(QIODevice::WriteOnly);
    QJsonDocument doc(object);
    file.write(doc.toJson());
    file.close();
}


int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    qstringWidget w;
    w.show();
    QJsonObject object =read("C:/Users/Lenovo/Desktop/QT资料/13/13-4/read.json");
    qDebug()<<object;

    // 修改文件的内容
    object["object"]="123123";
    // 写回到新的文件当中
    write(object, "C:/Users/Lenovo/Desktop/QT资料/13/13-4/write.json");
    return a.exec();
}
```



