#                                                           vue

# 导入方式

使用Vue的四种方式：
• 在HTML中以CDN包的形式导入
• 下载JS文件保存到本地再导入
• 使用npm安装
• 使用官方VueCli脚手架构建项目（不建议新手直接用）

# 常用指令

**指令**：带有 v- 前缀的特殊属性。 

**指令的作用**：当表达式的值改变时，将其产生的连带影响，响应式地作用于 DOM。

![屏幕截图 2023-08-27 114150](D:\笔记\vue\assets\屏幕截图 2023-08-27 114150.png)

## v-txet

v-text作用与双大花括号作用一样，将数据填充到标签中。但没有闪烁问题！

```html
<div id="app">
    {{message}}                  //这两个效果一样
    <p v-text="message"></p>    //这两个效果一样
    <p> 统计{{counter}}</p>
</div>
<script>
    const Helloapp = {
        data() {
            return {
                message: 'hello沈泽昊',
                counter: '0'
            }
        },
        // 打开页面就执行。
        mounted() {
            setInterval(() => {
                this.counter++     //counter递增加一。
            },1000)
        }
    }

    Vue.createApp(Helloapp).mount('#app')
</script>
```

## v-html

某些情况下，从服务端请求的数据本身就是一个HTML代码，如果用双大括号会将数据解释为普通文本，而非HTML代码，为了输出真正的HTML，需要使用v-html指令：

```html
<div id="app">
    <p v-html="msg_html">nihao</p>
</div>
<script>
    const Helloapp = {
        data() {
            return {
                msg_html: "<span>nihao</span>",
            }  //用v-html就可以会直接给页面渲染你好，而不是html代码
        },
        mounted() {
            setInterval(() => {
                this.counter++     //递增加一。
            }, 1000)
        }
    }

    Vue.createApp(Helloapp).mount('#app')
</script>
```

## v-on

常监听用户发生的事件，例如点击、拖拽、键盘事件等

v-on: 冒号后面是event参数，例如click、change

```html
<div id="app">
<p>点击按钮的次数{{number}}</p>
    <button v-on:click="number++">按钮</button>
</div>
<script>
    const Helloapp = {
        data() {
            return {
                number: 0
            }
        },
        mounted() {
        }

    }
    Vue.createApp(Helloapp).mount('#app')
</script>
```

指令缩写

```html
v-on:click 可以写成@click
<input type="button" value="添加样式" @click="btn">
@change
```

## v-bind

动态渲染

• v-bind 指令后接收一个参数，以冒号分割。

• v-bind 指令将该元素的 href 属性与表达式 url 的值绑定。

eg:

给div标签添加class:active,isActive=ture时添加成功，为false时不会添加。

添加类

```html
    <style>
        .text{
                background-color: blue;
                width: 100px;
                height: 100px;
        }
        .active{
            background-color: red;
        }
    </style>
</head>
<body>

<div id="app">
    {{message}}
    <div  class="text" v-bind:class="{active: isActive}" >你好</div>
    <input type="button" value="添加样式" v-on:click="btn">
</div>
<script>
    const Helleapp = {
        data() {
            return {
                isActive:false
            }
        },

        methods:{
            btn(){
                if(this.isActive){
                    this.isActive=false
                }else {
                    this.isActive=true
                }
            }
        }
    }
    Vue.createApp(Helleapp).mount('#app')
```

eg:

添加style

```html
<div id="app">
    <div class="text" v-bind:style="{background:background}">你好</div>
</div>
<script>
    const Helleapp = {
        data() {
            return {
                background:"red"
            }
        },
    }
    Vue.createApp(Helleapp).mount('#app')
</script>
```

还可以

eg：

```html
<div id="app">
    <div class="text" v-bind:style="xxxx">你好</div>
</div>
<script>
    const Helleapp = {
        data() {
            return {
                  xxxx:{
                    background:"black"
                }
            }
        },
    }
    Vue.createApp(Helleapp).mount('#app')
</script>
```

指令缩写

```html
v-bind  可以写成 :
eg：
<a :href="xxxx"></a>  //就写个:就可以。
```

## v-if

判断

```html
<div id="app">
    //p标签是根据seen的值而定，seen为false时第二个p标签显示。第一个不显示，ture相反。
<p v-if="seen">今天的天气好？</p>
<p v-else>不好</p>
</div>
<script>
    const Helloapp = {
        data() {
            return {
            seen:false
            }
        },
    }
    const vm =Vue.createApp(Helloapp).mount('#app')
</script>
```

eg:

```html
<body>
<div id="app">
    <p>沈泽昊</p>
    <p v-if="type=='B'">我是B</p>        //判断type的值，如果是B就输入我是B，否则就是输出我是A。
    <p v-else-if="type=='A'">我是A</p>
</div>
<script>
    const Helloapp = {
        data() {
            return {
                type: "B"

            }
        },
    }
    const vm = Vue.createApp(Helloapp).mount('#app')
</script>
```

## v-show

v-show：另一个用于条件性展示元素的指令，与v-if不同的是，v-show的元素始终会被渲 染并保留再DOM中，所以v-show只是简单地切换元素的display CSS属性。

这个指令不删除，可以在源码中找到，只是在标签中加了一个style="display: none;"

```html
<div id="app">
    <p>沈泽昊</p>
    <p v-show="seen">你好，我的名字是沈泽昊</p>     //seen为ture就显示p标签，否则不显示
</div>
<script>
    const Helloapp = {
        data() {
            return {
                seen: false,

            }
        },
    }
    const vm = Vue.createApp(Helloapp).mount('#app')
</script>
```

注意，`v-show` 不支持 `<template>` 元素，也不支持 `v-else`。

## v-for

```html
<div id="app">
    <p>沈泽昊</p>
    <p v-show="seen">你好，我的名字是沈泽昊</p>
    <ul>
        <li v-for="(stu,index) in students">名字：{{stu.name}}年龄：{{stu.age}}</li>  //index是索引，stu是对象，
    </ul>
</div>
<script>
    const Helloapp = {
        data() {
            return {
                seen: false,
                students: [{"name": "shen", "age": 22}, {"name": "dong", "age": 24}, {"name": "zhang", "age": 21}],

            }
        },
    }
    const vm = Vue.createApp(Helloapp).mount('#app')
</script>
```

在v-for中加入v-if

```html
# 其他的和上面的一样。    
<ul>
        <template v-for="(stu,index) in students">
        <li v-if="stu.age>21">符号{{index}}名字：{{stu.name}}年龄：{{stu.age}}</li>
        </template>
    </ul>
```

## v-model

双向绑定，就是data中的值也改变，所有使用data中的值的标签都改变。

v-model指令提供表单输入绑定，可以在input及select 元素上创建双向 数据绑定。

eg:

```html
<!-- input标签输入什么，p标签中的msg也会改变，   -->
<div id="app">
    <input type="text" v-model="msg">
    <p v-text="msg"></p>
    <!--  单选，选择第一个vue时，v-model中的sing也会变成value中的值，sing也改变 -->
    <input type="radio" name="name" v-model="sing" value="vue">vue
    <input type="radio" name="name" v-model="sing" value="python">python
    <p>{{sing}}</p>
</div>
<script>
    const Helloapp = {
        data() {
            return {
                msg:"你好，沈泽昊",
                sing:""
            }
        },


    }
    const vm = Vue.createApp(Helloapp).mount('#app')
```

eg：登录案例

```html
<div id="app">
    <form action="" onclick="return false" >    <!-- onclick="return false" 页面就不会刷新 -->
        用户名<input type="text" name="username" v-model="form.username"><br>
        密码<input type="password" name="password" v-model="form.password"><br>
        <p>
            <button @click="loginBtn">登录</button>
        </p>
        <p>{{username}}--{{password}}</p>
    </form>
    <p v-if="error">输入的错误</p>
</div>
<script>
    const Helloapp = {
        data() {
            return {
                form: {
                    username: "",  
                    password: "",  
                },
                error:false

            }
        },
        methods: {
            loginBtn() {
                if(this.form.username=="" || this.form.password==""){
                    this.error=true
                }
                else {
                    // 提交服务端
                    this.error=false
                }
                console.log(this.form)
            }
        }
    }
    const vm = Vue.createApp(Helloapp).mount('#app')
```

# 常用属性

## 获取data中的值

```html
<body>

<div id="app"></div>
<script>
    const Helleapp = {
        data() {
            return {
                msg:"hello vue!"
            }
        },
    }
    const vm =Vue.createApp(Helleapp).mount('#app')
    console.log(vm.msg)
    vm.msg="沈泽昊"     //可以修改数据
    console.log(vm.msg)
    vm.msg="沈泽"
    console.log(vm.msg)
</script>
</body>
```

## 方法(methods)

处理数据的函数。在methods选项中定义的函数称为方法。 

示例：添加方法及调用

在methods中写自己的方法。

```html
<input type="button" value="添加样式" @click="btn">
<script>    
methods: {      //methods用来写自己定义的函数(方法)。
        btn()
        {
            if (this.isActive) {
                this.isActive = false
            } else {
                this.isActive = true
            }
        }
    }
</script>
```

## 计算属性(computed)

在computed中定义函数sum，函数返回结果。

```html
<div id="app">
    <span>{{sum}}</span>     
</div>
<script>
    const Helleapp = {
        data() {
            return {
                a:2,
                b:3,
                c:9
            }
        },
        //计算属性，一般用作运算，具备缓存能力，
        computed:{
            sum:function (){
                return this.a+this.b+this.c
            }
        }

    }
    const vm =Vue.createApp(Helleapp).mount('#app')
</script>
```

计算属性一般就是用来通过其他的数据算出一个新数据，而且它有一个好处就是， 它把新的数据缓存下来了，当其他的依赖数据没有发生改变，它调用的是缓存的数据，这 就极大的提高了我们程序的性能。而如果写在methods里，数据根本没有缓存的概念，所 以每次都会重新计算。这也是为什么不用methods的原因！

## 监听属性(watch)

数据变化是就需要用到监听，主要监听data中的值，

监听属性（watch）：是一个观察动作，监听data数 据变化后触发对应函数，函数有newValue（变化之后 结果）和oldValue（变化之前结果）两个参数。 当需要在数据变化时执行异步或开销较大的操作时， 这个方式是最有用的。

```html
<div id="app">
    <input value="修改hello" type="button" @click="btn" >
    <p>消息：{{msg}}</p>
    <p>{{newwatch}}</p>
</div>
<script>
    const Helloapp = {
        data() {
            return {
                msg:"hello word",
                newmsg: ""    //写一个空值，msg发生变化后，将新的msg数值， 赋值到newmsg中。
            }
        },
        // 监听数据，数据在发生变化时执行。
        // 如果msg发生变化，会将新值和旧值返回结果
        watch:{
            msg(newValue,oldValue){
                console.log(newValue,oldValue)
                this.newmsg=newValue  //给newmsg赋值newValue
            }

        },
        methods:{
            btn(){
                //点击后将msg赋值"hello 沈泽昊"
                this.msg="hello 沈泽昊"
            }
        }

    }
    const vm =Vue.createApp(Helloapp).mount('#app')
</script>
```

#  生命周期

<img src="D:\笔记\vue\assets\lifecycle.16e4c08e.png" alt="lifecycle.16e4c08e" style="zoom:50%;" />

生命周期是指Vue实例从创建到销毁的过程。就是vue实例从开始创建、 初始化数据、编译模板、挂载Dom、渲染->更新->渲染、卸载等⼀系 列过程，在vue⽣命周期中提供了⼀系列的⽣命周期函数，如图所⽰。

![屏幕截图 2023-08-27 121533](D:\笔记\vue\assets\屏幕截图 2023-08-27 121533.png)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/vue/3.0.5/vue.global.js"></script>

</head>
<body>

<div id="app">
    <p ref="p1">{{num}}</p>
    <input type="text" v-model="num">
</div>

<script>
    const helloapp = {
        data() {
            return {
                num: 0,
            }
        },
        beforeCreate() {
            console.log("--------data数据被赋值到vm对象之前---------");
            console.log("this", this);
            console.log("num:", this.num);
            console.log("$el", this.$el);
        },
        created() { // 重点掌握，最常用，开发中一般会在这里编写ajax代码，发送http请求获取来自服务端的数据
            console.log("--------data数据被赋值到vm对象之后---------");
            console.log("this", this);
            console.log("num:", this.num);
            console.log("$el", this.$el);
            this.num = 10
        },
        beforeMount() {
            console.log("--------把data数据渲染到HTML模板之前---------");
            console.log("this", this);
            console.log("num:", this.num);
            console.log("$el", this.$el);
        },
        mounted() { // 重点掌握，最常用，开发中一般会在这里编写页面初始化的操作，一般就是根据条件/状态，进行页面跳转，改变页面的特效。
            console.log("--------把data数据渲染到HTML模板之后---------");
            console.log("this", this);
            console.log("num:", this.num);
            console.log("$el", this.$el.parentElement);
        },
        beforeUpdate() {
            console.log("--------data数据发生改变以后，同步到HTML模板之前，此时data和模板的数据是不一致的---------");
            console.log("this", this);
            console.log("num:", this.num);
            console.log("$el", this.$el.parentElement.innerHTML);
        },
        updated() {
            console.log("--------data数据发生改变以后，同步到HTML模板之后，此时data和模板中的数据保持一致---------");
            alert(123)
            console.log("this", this);
            console.log("num:", this.num);
            console.log("$el", this.$el.parentElement.innerHTML);
        }
    }
    const vm = Vue.createApp(helloapp).mount('#app')
</script>

</body>
</html>
```

# Vue Cli 脚手架

## Vue Cli 的介绍

如果用Vue开发整个前端项目，组建Vue项目结构及配置还是比较复杂的，例如引入各种js文 件、打包上线等。因此，为了提高开发效率，官方开发了VueCli脚手架快捷搭建开发环境。

Vue CLI 是一个基于 Vue.js 进行快速开发的完整系统，

提供： 

-  通过` @vue/cli` 实现的交互式的项目脚手架。 

- 通过 `@vue/cli` +` @vue/cli-service-global` 实现的零配置原型开发。 

-  一个运行时依赖 `@vue/cli-service`，该依赖：

​		• 可升级； 

​			• 基于 webpack 构建，并带有合理的默认配置； •

​			• 可以通过项目内的配置文件进行配置； •

​			• 可以通过插件进行扩展。 

- 一个丰富的官方插件集合，集成了前端生态中最好的工具。 

- 一套完全图形化的创建和管理 Vue.js 项目的用户界面。 



Vue CLI 致力于将 Vue 生态中的工具基础标准化。它确保了各种构建工具能够基于智能的默认配 置即可平稳衔接，这样你可以专注在撰写应用上，而不必花好几天去纠结配置的问题



Vue CLI 有几个独立的部分——如果你看到了我们的[源代码](https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue)，你会发现这个仓库里同时管理了多个单独发布的包。

- CLI

CLI (`@vue/cli`) 是一个全局安装的 npm 包，提供了终端里的 `vue` 命令。它可以通过 `vue create` 快速搭建一个新项目，或者直接通过 `vue serve` 构建新想法的原型。你也可以通过 `vue ui` 通过一套图形化界面管理你的所有项目。我们会在接下来的指南中逐章节深入介绍。

- CLI 服务

CLI 服务 (`@vue/cli-service`) 是一个开发环境依赖。它是一个 npm 包，局部安装在每个 `@vue/cli` 创建的项目中

## 安装

使用Vue Cli前需要下载node.js

Vue CLI 4.x 需要 [Node.js](https://nodejs.org/) v8.9 或更高版本 (推荐 v10 以上)。你可以使用 [n](https://github.com/tj/n)，[nvm](https://github.com/creationix/nvm) 或 [nvm-windows](https://github.com/coreybutler/nvm-windows) 在同一台电脑中管理多个 Node 版本。

可以使用命令安装这个新的包：

```
npm install -g @vue/cli
# 或者
yarn global add @vue/cli
# 下载时间长
```

## 使用

在某个文件夹下打开cmd输入`vue create 项目名字，练习直接选择vue3就可以。生产环境选择手动模式。`  Manually select features  # 手动配置`

等安装好，会有提示

```
cd 项目里
npm run serve
可以访问。
```

在pycharm中，打开这个vue项目

在Scripts 中输入serve

![屏幕截图 2023-08-27 155731](D:\笔记\vue\assets\屏幕截图 2023-08-27 155731.png)

配置成功后运行。

## 文件目录

![屏幕截图 2023-08-27 155441](D:\笔记\vue\assets\屏幕截图 2023-08-27 155441.png)

各文件夹中的意思

![屏幕截图 2023-08-27 155825](D:\笔记\vue\assets\屏幕截图 2023-08-27 155825.png)

我们主要就是在src中写。

将代码给别人时一般不给别人node_modules。(因为这个文件夹太大)

进入项目中执行`npm install`，就可以下载项目的所需包

# vue组件

组件：一段独立的，能代表页面某一个部分的代码片段，拥有自己独立的数据、JavaScript脚本、 以及CSS样式。 组件是可复用的Vue实例，在开发过程中可以把经常重复的功能，封装为组件，达到快捷开发的 目的。 

组件（Component）是自定义封装的功能。在前端开发过程中，经常出现多个网页的功能是重复的，而且很多不同的页面之间，也存在同样的功能。而在网页中实现一个功能，需要使用html定义功能的内容结构，使用css声明功能的外观样式，还要使用js来定义功能的特效，因此就产生了把一个功能相关的[HTML、css和javascript]代码封装在一起组成一个整体的代码块封装模式，我们称之为“组件”。所以，组件就是一个html网页中的功能，一般就是一个标签，标签中有自己的html内容结构，css样式和js特效。这样，前端人员就可以在组件化开发时，只需要书写一次代码，随处引入即可使用。

`可以将组件看成一个一个的函数，可以被引入。`

组件的好处： 

-  提高开发效率 
-  方便重复使用 
- 易于管理和维护

## 文件格式

Vue单文件组件（又名*.vue文件，缩写为SFC）是一种特殊 的文件格式，它允许讲Vue组件的模板、逻辑与样式封装在 单个文件中。 正如所见，Vue SFC 是经典的 HTML、CSS 与 JavaScript 三 个经典组合的自然延伸。每个 *.vue 文件由三种类型的顶层 代码块组成：

1. <template> 部分定义了组件的模板。
   
2. <script> 部分是一个标准的 JavaScript 模块。
    它应该导出一个 Vue 组件定义作为其默认导出。

3. <style> 部分定义了与此组件关联的 CSS

## 使用

使用具体流程：

1、在src/components目录里开发一个组件文件（首字母大写） （名字要成，用驼峰式）

2、在父组件里引用子组件 import xxx from‘xxx’ 

3、在默认导出里注册组件 

4、在template模板里使用组件

```
开发组件>>>>>>>>>>>>注册组件>>>>>>>>>>>>>>>>>>>>使用组件
```

用Vue Cli构建项目在`components`中写自己的代码

```html
<template> 
    <!--  写自己的HTML文件  -->
  <div class="test">{{ msg }}</div>
</template>

<script>
    ///////写js的
export default {
  name: "ShenZehao",
  data() {
    return {
      msg: "hello vue"
    }

  }
}
</script>

<style scoped>
    //// 写css
.test {
  color: red;

}
</style>
```

用Vue Cli构建项目在App.vue中去使用组件

```html
将上面的代码导入到vue中。
<template>
<!--         调用组件 ，调用组件是由顺序的从上倒下引入         -->
  <img alt="Vue logo" src="./assets/logo.png">
  <ShenZehao msg="Welcome to Your Vue.js App"/>
  <HelloWorld msg="Welcome to Your Vue.js App"/>
</template>

<script>
////////////////////导入组件
import HelloWorld from './components/HelloWorld.vue';
import ShenZehao from './components/ShenZehao.vue';


export default {
  /////////////////注册组件
  name: 'App',
  components: {
    HelloWorld,
    ShenZehao
  }
}
</script>
```

## 全局注册和局部注册

上面的代码就是局部注册

全局注册是在main.js中注册，

`main.js`

```js
import {createApp} from 'vue'
import App from './App.vue'



import ShenZehao from "@/components/ShenZehao";


const app = createApp(App)
app.component("ShenZehao", ShenZehao)
app.mount("#app")
```

在app.vue中直接引用。全局注册直接调用就可以，不要在导入和注册

```html
<template>
<!--  调用组件 ，调用组件是由顺序的从上倒下引入-->
  <img alt="Vue logo" src="./assets/logo.png">
  <ShenZehao/>
</template>
```

## 子父组件传递数据

子传父>>>>>>>>>事件

父传子>>>>>>>>>props

### 父传子

`app.vue`

```html
<template>
<!--  调用组件 ，调用组件是由顺序的从上倒下引入-->
  <img alt="Vue logo" src="./assets/logo.png">
  <HelloWorld msg="欢迎使用vue"/>
  <ShenZehao testmsg="你好，我是父组件的数据"/>
</template>
```

子组件通过props接受testmsg的数据

`ShenZehao`

```html
<template>
  <div class="xxx">{{ msg }}</div>
  <div class="xxx">{{ testmsg }}</div>
</template>

<script>
export default {
  name: "ShenZehao",  
  props:{
    testmsg:String      //接受父组件传递数据，testmsg是父组件中的名字。String是固定的。
  },
  data() {
    return {
      msg: "hello vue"
    }
  }
}
</script>
```

### 子传父

# Axios

前后端数据交互

```
# 下载json-server用作练习。
npm install json-server
```

创建一个json文件用作练习

在webstorm中创建文件`db.json`

```json
{
  "students": [
    {
      "name": "张三",
      "age": 18,
      "gender": "男",
      "id": 1
    },
    {
      "id": 2,
      "name": "李四",
      "age": 20,
      "gender": "女"
    },
    {
      "id": 3,
      "name": "王五",
      "age": 22,
      "gender": "男"
    },
    {
      "id": 4,
      "name": "赵六",
      "age": 24,
      "gender": "女"
    },
  ]
}
```

运行`json-server`

```bash
json-server -w db.json
-w 监控这个文件的变动
db.json是个文件
```

打开postman，创建接口

```Bash
# 增
POST  http://localhost:3000/students
# id 会自增长
 {
      "name": "赵六",
      "age": 24,
      "gender": "女"
    }
#删 
# 以id为搜索，删除id为1的值
DELETE  http://localhost:3000/students/1
# 改   
# 全字段更新，不传就删除,以id为搜索，修改id为3的值
PUT      http://localhost:3000/students/3
# 改
# 单字段修改，
PATCH    http://localhost:3000/students/2
# 这两个都可以用来单个修改，不过为了练习，一个全改，一个单改。
# 查
# 查全部
GET     http://localhost:3000/students
# 详细查
GET     http://localhost:3000/students/2
```

下载

```
npm install axios
```



使用的cli创建vue。在`mian.js`中注册axios

```js
import axios from "axios";

const app = createApp(App)
app.config.globalProperties.$axios = axios
```

在组件中使用

```html
<template>
  <div class="xxx">{{ msg }}</div>
  <table border="1">
    <thead>
    <tr>
      <td>id</td>
      <td>name</td>
      <td>age</td>
      <td>gender</td>
    </tr>
    </thead>
    <tbody>
    <tr v-for="row in tableDate" :key="row.id">
      <td>{{row.id}}</td>
      <td>{{row.name}}</td>
      <td>{{row.age}}</td>
      <td>{{row.gender}}</td>
    </tr>
    </tbody>
  </table>
</template>

<script>
export default {
  name: "ShenZehao",  //接受父组件传递数据，key是父组件使用子组
  data() {
    return {
      msg: "hello vue",
      xxxxmsg: "你好啊，我的名字是vue。",
      tableDate:[],
    }
  },

  methods: {
    getData() {
      this.$axios.get("http://localhost:3000/students/2")
          .then(res => {
          //处理成功情况
            this.tableData = res.data
            console.log(res.data)
          })
          .catch(res =>{
          //处理失败情况
                console.log(res.data)
              }
             )
    },
  },
  mounted() {
    this.getData()
  }
}
```

## 全局默认值

有时候服务端接口有多个地址，就会涉及请求的域名不同、配置不同等，这时自定义实例可以很好解决。

在lic创建 vue在main.js中写

```js
import axios from "axios";
axios.defaults.baseURL = 'http://localhost:3000/';    //全局默认
axios.defaults.timeout = 5000;       //此实例的请求都将等待2.5秒，然后才会超时
app.config.globalProperties.$axios = axios
```

这样在写组件时，用到axios。url不需要写全，只需要写`http://localhost:3000/`后面的部分url。

```js
methods: {
    getData() {
      this.$axios.get("/students")
          .then(res => {
            this.tableData = res.data
            console.log(res.data)
          })
```

也可以写成一个文件。

在根目录下创建文件夹`api`,在api中创建js文件`http.js`，这两个文件随便起名字。

```js
import axios from "axios"           //导入axios
//创建实列
const instance = axios.create({             
    baseURL: 'http://localhost:3000/',           //url地址
    timeout:5000,  //5秒                         //此实例的请求都将等待2.5秒，然后才会超时
});


export default instance                       //导出，否则其他文件收不到
```

在main.js中引入

```js
import axios from "/api/http";
app.config.globalProperties.$http = axios     //$http  如果这里改成http，所以组件中也需要改
```

组件

```js
      this.$http.get("/students")      //这里也改成$http
          .then(res => {
            this.tableData = res.data
            console.log(res.data)
          })
```

## 拦截器

在请求或响应被 then 或 catch 处理前拦截它们。

拦截代码写在创建的`api.http.js`中,也可以写在main.js中。

```js
const instance = axios.create({
    baseURL: 'http://localhost:3000/',
    timeout:5000,  //5秒
});
//因为声明了instance=axios了所以下面使用了instance。写在main.js就是axios.interceptors......
// 添加请求拦截器
instance.interceptors.request.use(function (config) {  //config放着一些数据，可以修改。
    // 在发送请求之前做些什么
    console.log(config)
    return config;
}, function (error) {
    // 对请求错误做些什么
    console.log(error)
    return Promise.reject(error);
});

// 添加响应拦截器
instance.interceptors.response.use(function (response) {
    // 2xx 范围内的状态码都会触发该函数。
    // 对响应数据做点什么
    return response;
}, function (error) {
    // 超出 2xx 范围的状态码都会触发该函数。
    // 对响应错误做点什么
    return Promise.reject(error);
});


export default instance
```

但是为了解耦，可以将axios独自写一个文件出来。

使用vite创建vue项目

在`vite.config.js`中写

解决跨域请求问题

```js
export default defineConfig({
  resolve:{
    alias:{
      "~":path.resolve(__dirname,"src")
    }
  },
  plugins: [vue(),WindiCSS()],
  server:{
      proxy: {
          '/api': {
              target: '',       //这里写url，eg：http://ceshi13.dishait.cn
              changeOrigin: true,
              rewrite: (path) => path.replace(/^\/api/, ''),
          }}
  }
})
```

在`src`中创建一个axios.js文件

`axios.js`

```js
import axios from "axios"

const service = axios.create({
    baseURL:"/api"    // 这个api就是上面写了http://ceshi13.dishait.cn
})

export default service
```

在`src`中创建文件夹`api`，在`api`文件夹中创建文件`manager.js`这两个文件夹的名字随变叫

```js
import axios from "~/axios"   // ~代表src

export function login(username, password) {
    return axios.post("/admin/login", {
        username, password
    })
}
```

在组件中使用

```html
<script setup>
import { login } from "~/api/manager.js";        //导入axios
login(form.username, form.password)              // 执行函数，向函数中传入值。
      .then((res) => {                           // 执行成功运行的函数
});
     .catch((err) => {                          // 执行失败运行的函数
        ....

  });
</script>
```

#  Router

下载Router

```
npm install vue-router 
npm install vue-router@3    vue2使用3版本多
npm install vue-router@4    vue3使用3版本多
```

使用的vue_cli，在webstorm的终端中输入

```
vue add router
有两个yes
会多出两个文件夹。views和router .  router是路由配置文件，views是视图，
输入这个文件会修改app.vue这个文件的内容,所以才会问你需不需要yes。
```

引入路由

 ![屏幕截图 2023-10-12 231143](D:\笔记\vue\assets\屏幕截图 2023-10-12 231143.png)

`main.js`

```js
import router from "./router/router.js";

const app = createApp(App)

app.use(router)

app.mount('#app')

```

使用流程： 

1. 开发页面（组件） 
2. 定义路由 
3.  组件使用路由

`index.js`

```js
import { createRouter, createWebHistory } from 'vue-router' // 1。

const routes = [
  {
    meta:{
        title: "shen的网站-站点首页",   //路由说明
        keepAlive: true    //页面加载时有一个缓存效果。
    },  
    path: '/',          // url。
    name: 'home',       // url的组件。
    component: HomeView    //引用组件。上面的import HomeView from '../views/HomeView.vue'
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.

    //引入组件，第二种方式。
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')    //引入组件
  }
]
//创建路由实列传递上面定义的路由对象。
const router = createRouter({
  history: createWebHistory(),   //路由模式  vite使用
 //  history: createWebHistory(process.env.BASE_URL),    vue-cli使用
  routes
})
//导出
export default router
// 路由模式，模式还有
createMemoryHistory    缓存路由
createRouterMatcher    用这个浏览器输出url时会有一个#号
createWebHistory
```

`app.vue`

```html
<template>
  <router-view></router-view>
</template>
```

## 导航守卫

正如其名，vue-router 提供的导航守卫主要用来通过跳转或取消的方式守卫导航。这里有很多方式植入路由导航中：全局的，单个路由独享的，或者组件级的。

正如其名，vue-router 提供的导航守卫主要用来通过跳转或取消的方式守卫导航。 简单来说，就是在路由跳转时候的一些钩子，当从一个页面跳转到另一个页面时， 可以在跳转前、中、后做一些事情。

类似和拦截器差不多，可以定向的跳转后，在打开新的页面，作一些事情

运行时先运行全局，在运行单独

```js
//全局的导航守卫
router.beforeEach((to, from，next) => { 
    //  ...
    //  to: 即将要进入的目标 用一种标准化的方式
	//  from: 当前导航正要离开的路由
    //  next: next：可选，是一个方法
    //  返回 false 以取消导航
    return false
    //可以返回的值如下：
	//• false：取消当前的导航。如果浏览器的 URL 改变了(可能
	//是用户手动或者浏览器后退按钮)，那么 URL 地址会重置
	//到 from 路由对应的地址。
	//• 一个路由地址：通过一个路由地址跳转到一个不同的地址。
})


```

还可以在单独的守卫，在设置路由时写

```js
    {
        path: '/',          // url。
        name: 'home',       // url的组件。
        component: HomeView,   //引用组件。上面的import HomeView from '../views/HomeView.vue'
        beforeEach:((to, from,next) => {
            // ...
            // 返回 false 以取消导航
            return false
        })
    },
```

页面跳转

在main.js中挂在，注册了router在组件中，

```js
import {useRouter} from "vue-router";
const router = useRouter();

router.push("/");   // 跳转到哪个页面就写哪个路由。
```



# element-plus

全部下载

```
npm install element-plus --save
```

引入

在main.js中引入

```js
import { createApp } from 'vue'
import App from './App.vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

const app = createApp(App)

app.use(ElementPlus)
app.mount('#app')
```

局部下载(推荐)

```
npm install unplugin-vue-components
```

`vite.config.js`

```js
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import Components from 'unplugin-vue-components/vite'
import { ElementPlusResolver } from 'unplugin-vue-components/resolvers'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    Components({
      resolvers: [ElementPlusResolver()],
    }),
  ]
});
```

使用element-puls的图标

下载

```
npm install @element-plus/icons-vue
```

导入

`main.js`

```js
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component)
}
```



# vite	

打开文件夹

```
查看npm版本 npm -v是哪个版本就是用哪个命令
# npm 6.x
npm create vite@latest 

# npm 7+, extra double-dash is needed:
npm create vite@latest 

# 等命令结束，按照说明输入命令
# cd ...
# npm install
# npm run dev 
```

使用vite创建的文件是需要自己写router的，不能使用`vue add router`命令,需要自己在`src`文件夹中创建`router文件夹和index.js文件`内容也需要自己写。复制上面的router即可，引入路由和上面的一样。

运行代码和cli的一样，

就是将`serve`换成了dev

![屏幕截图 2023-08-30 172607](D:\笔记\vue\assets\屏幕截图 2023-08-30 172607.png)

# windiCSS

在vite创建的vue3项目中引入windiCSS

可查看官网

`https://cn.windicss.org/`

下载

```
npm i -D vite-plugin-windicss windicss
```

然后，在你的 Vite 配置中添加插件：

`vite.config.js`

```js
import WindiCSS from 'vite-plugin-windicss'

export default {
  plugins: [
    WindiCSS(),
  ],
}
```

最后，在你的 Vite 入口文件中导入 `virtual:windi.css`：

`main.js`

```js
import 'virtual:windi.css'
```

# 知识点

## src变成~

每次写src很多，我们将src变成~

`vite.config.js`

```js
import path from "path"

export default defineConfig({
  resolve:{
    alias:{
      "~":path.resolve(__dirname,"src")      // 
    }
  },
  plugins: [vue(),WindiCSS()]
})

// 在defineConfig 里添加下面的代码
import path from "path"
resolve:{
    alias:{
      "~":path.resolve(__dirname,"src")      
    }
  },
```

## 404页面捕获

配置路由

```js
import NotFound from '~/pages/404.vue'   //~指的是src ，看上面的代码。引入404文件。

const routes = [
{ 
    path: '/:pathMatch(.*)*', 
    name: 'NotFound', 
    component: NotFound 
}
]
```

## 跳转页面

在vue中导入router后

在组件中

```js
import { useRouter } from "vue-router";     // 导入
const router = useRouter();

router.push("/");  // 登录成功后，跳转到首首页。
```

# 组合式api

没有this，this指向的是undefined

serup选项，有语法糖，在<script setup></script>中直接写数据就可以了。

```html
<script setup>
const xxx=()=>{
    console.log("大家好，我的名字是沈泽昊")
    console.log(this)
}
const a="你好"
</script>
```

## reactive

作用：接受对象类型数据的参数传入并返回一个响应式对象

```js
import {reactive} from "vue"   //导入
//执行函数  传入参数  变量接受
const state =reactive(对象类型数据)   //state可以随便起名字。
```

eg：

```html

<script setup>
import {reactive} from "vue"

// const写在reactive中后const就变成了响应式对象。在页面中就会改变。不写在里面。就不会变。
const state =reactive中({         
    const:0
})
const setCount=()=>{
    state.const++
}
</script>

<template>

    <div>
        <button @click="setCount">{{ state.const }}</button>
    </div>
</template>
```

## ref

因为reactive只接受对象类型数据，而对于简单类型就有了ref。

作用：接受简单类型或者对象类型数据传入并返回一个响应式对象。

```js
import {ref} from "vue"   //导入ref

const state =ref(简单类型或者对象类型)
```

eg:传入简单类型

```html
<script setup>
import {ref} from "vue"


const state =ref(0)
const setCount=()=>{
    //脚本区域修改ref产生的响应式对象数据，必须通过.value属性
    state.value++
}
</script>

<template>
    <div>
        <button @click="setCount">{{state}}</button>
    </div>
</template>
```

eg：传入对象类型

```html
<script setup>
const state =ref({
    a:0
})

const setCount=()=>{
    //脚本区域修改ref产生的响应式对象数据，必须通过.value属性
    state.value.a++
}
</script>

<template>
    <div>
        <button @click="setCount">{{state.a}}</button>
    </div>
</template>
```

## computde

计算属性函数 

```js
import {computed} from "vue"  //导入函数
const cpmp=computed(()=>{
  ....
})
```

eg:

```html
<script setup>
import {computed,ref} from "vue"
const list=ref([1,2,3,4,5,6,7,8,9])

const cpmp=computed(()=>{    
    return list.value.filter(item =>item >2) //过滤掉list中大于2的数据。
})
setTimeout(()=>{
    list.value.push(9,10)   //3秒后向list添加9和10
},3000)
</script>

<template>
<div>原始响应式数组-{{ list }}</div>
<div>原始响应式数组-{{ cpmp }}</div>
</template>
```

## watch

作用：监听一个或多个数据的变化，数据变化时执行回调函数

两个额外参数：1.immediate（立即执行）  2.deep（深度监听）

监听：

```html
// 监听一个数据
<script setup>
import {watch,ref} from "vue"

watch(count,(newValue,oldValve)=>{
    console.log(`count发生了变化，老值为${oldValve},新值为${newValue}`)
})
</script>
<!--count就是要监听的值， newValue oldValve ，新值和旧值-->

// 监听多个数据
<script setup>
import {watch,ref} from "vue"

const count=ref(0)
const name =ref(10)
watch([count,name],
(([newConut,newName],[oldConut,oldName])=>{
    console.log(`新值${newConut},旧值${oldConut}`)
    console.log(`新值${newName},旧值${oldName}`)
})
)
</script>
<!-- 将监听的数据放到数组中， -->
```

### immediate

在监听器创建时立即触发回调，响应式数据变化之后继续执行回调。

```html
// 注意看immediate写在哪里了
<script setup>
import {watch,ref} from "vue"

watch(count,(newValue,oldValve)=>{
    console.log(`count发生了变化，老值为${oldValve},新值为${newValue}`)
},{
    immediate:true
}
)
</script>
```

### deep

通过watch监听的ref对象默认是浅层监听，直接修改嵌套的对象属性是不会出发回调函数执行，需要开启deep选项。

eg:

将监听的数据放到对象中，deep:true才会监听到

```html
<script setup>
import {watch,ref} from "vue"

const state=ref({
    count:0
})
const setCount=() =>{
    state.value.count++
}


watch(state,(newValue,oldValve)=>{
    console.log(`count发生了变化，老值为${oldValve.count},新值为${newValue.count}`)
},{
    deep:true
}
)
</script>

<template>
<button @click="setCount">按钮</button>
<div v-text="state.count"></div>
</template>
```

### 只监听特定的属性

一般不建议开启deep，有资源的浪费，所以监听一个值。

```js
const state=ref({
    count:0,
    age:20
})
// 只监听一个数据
```

```html
<script setup>
import {watch,ref} from "vue"

const state=ref({
    count:0,
    age:20
})
const setCount=() =>{
    state.value.count++
}

const setAge=()=>{
    state.value.age--
}
// 只监听age ，不监听count，
watch(
    () =>state.value.age,
    () => {
        console.log("age改变了")
    }
)


</script>

<template>
<button @click="setCount">按钮</button>
<div v-text="state.count"></div>
<button @click="setAge">按钮</button>
<div v-text="state.age"></div>
</template>
```

## 生命周期函数

![屏幕截图 2023-09-01 143000](D:\笔记\vue\assets\屏幕截图 2023-09-01 143000.png)

onMounted的使用

```js
onMounted(
    () => {
      axios({
        method: "get",
        url: "https://api.luffycity.com/api/v1/course/actual/",
        headers: {
          "Content-Type": "application/json"
        }
      }).then((res) => {
        data.value.couresList = res.data.data.result
      })
    }
)
```





## 父子通讯

### 父传子

![屏幕截图 2023-09-01 143758](D:\笔记\vue\assets\屏幕截图 2023-09-01 143758.png)

### 子传父

![屏幕截图 2023-09-01 143848](D:\笔记\vue\assets\屏幕截图 2023-09-01 143848.png)

## 模板引用

```html
<script setup>
import {ref,onMounted} from "vue"
// 1.调用ref
const h1Ref =ref(null) 
//组件挂载完毕之后才可以获取
onMounted(()=>{
    console.log(h1Ref.value)     //输出结果是<h1>我是dom标签h1</h1>
})
</script>


<template>
<h1 ref="h1Ref">我是dom标签h1</h1>
<h1>子组件</h1>
</template>
```

## provide和inject

这两个组件要在setup中。

作用：顶层组件向任意底层组件传递数据和方法，实现跨层组件通信。

顶层组件通过provide函数提供数据

底层组件通过inject函数获取数据

![屏幕截图 2023-09-01 144847](D:\笔记\vue\assets\屏幕截图 2023-09-01 144847.png)

传递静态数据

![屏幕截图 2023-09-01 151137](D:\笔记\vue\assets\屏幕截图 2023-09-01 151137.png)

传递响应式数据

![屏幕截图 2023-09-01 151325](D:\笔记\vue\assets\屏幕截图 2023-09-01 151325.png)

跨层传递方法

![屏幕截图 2023-09-01 151444](D:\笔记\vue\assets\屏幕截图 2023-09-01 151444.png)

## defineProps和defineEmits

### defineProps

组件之间传值





### defineEmit

`下的可以直接用`

子组件向父组件事件传递

父组件

```vue
<template>
  <h1>我是父</h1>
  <span @click="ff">点击</span>z
  <el-dialog :width="600" v-model="fu_data.res" >
      <!-- 当子组件运行emit("successhandle")时运行successhandle事件。运行mm函数 -->
      <!-- @successhandle这个事件必须写在导入的子组件中<ZI @successhandle="xxx"></ZI> -->
    <ZI @successhandle="mm"></ZI>
  </el-dialog>
</template>

<script setup>
import ZI from "../components/ZI.vue"
import {reactive} from "vue";


const fu_data = reactive({
  res: false
})
const ff = () => {
  fu_data.res=true
}
const mm=()=>{
  fu_data.res=false
}
</script>


<style scoped>

</style>
```

子组件

```vue
<template>
<h1>我是子</h1>
  <span @click="gg">点击</span>
</template>

<script setup>
//子组件用defineEmits定义了一个时间
const emit = defineEmits(["successhandle",])
//运行gg函数，
const gg=()=>{
   //运行到emit("successhandle")时，会执行父组件中的successhandle事件。
  emit("successhandle")
}


</script>

<style scoped>

</style>
```



# vueuse

保存cookies

这两个都下载

```
 npm i @vueuse/integrations
 npm i universal-cookie
```

```html
<template>
    <el-button @click="set">设置</el-button>
    <el-button  @click="get">读取</el-button>
    <el-button>删除</el-button>
</template>

<script setup>
import { useCookies } from "@vueuse/integrations/useCookies";
const cookies = useCookies();

function set() {
    cookies.set("admin-token", "123456");
}
function get(){
    cookies.get("admin-token")
    console.log(cookies.get("admin-token"))
}
function remove(){
    cookies.remove("admin-token")
}
</script>
```

# vuex

如何将用户信息共享给其他页面。vuex可以说是个容器，保存信息，官方vuex是一个vue.js应用程序开发的状态管理模式

![vuex](D:\笔记\vue\assets\vuex.png)

下载

```
npm install vuex@next --save
使用vue`_cli快捷方式
vue add vuex
```

  actions类似于mutations，不同的在于

- actions提交的是mutation，而不是直接变更状态
- actions可以支持异步操作（主要）

在`src`中创建一个文件夹，`store`在文件 夹下创建文件`index.js`。 文件夹和文件随便起名字。

```js
import { createStore } from 'vuex'

const store = createStore({
    state() {
        return {
            // 用户信息
            user: {}
        }
    },
    mutations: {
        // 记录用户信息
        SET_USERINFO(state,user){
            state.user = user
        }
    }
})

export default store
```

在main中注册

```js
import store from './store'

app.use(store)
```

在组件中使用，将信息添加到vuex中

```js
import { useStore } from 'vuex'         //导入
const store = useStore()                //创建实例

        
getinfo().then(res2=>{                  //使用用axios，自己定义的getinfo()，成功访问后将res2添加到SET_USERINFO中。
                store.commit("SET_USERINFO",res2)
              
            })
```

在其他组件，取出vuex中的数据

```html
<template>
    <div>
        后台首页 
        {{ $store.state.user }}
    </div>
</template>
```

eg：登录后显示用户名

注册，保存用户信息。

```js
import { createStore } from 'vuex'

const store = createStore({
    state() {
        return {
            // 定义数据，
            Islogin:false,
            user: {}
        }
    },
    mutations: {
        // 记录完成用户信息
        SET_USERINFO(state,info){    // state 就是上面的state
            state.Islogin=true;       
            state.user = info;      
            //info用户传来的数据，存到state.user中，
        }
    },
    actions:{}
})

export default store
```

在组件中可以使用，可以通过下面的方式拿到vuex中定义的常量。

```js
{{ $store.state.user.username }}

v-if="$store.state.Islogin"
```

eg：

```html
<div v-if="$store.state.Islogin">{{ $store.state.user.username }}</div>
<router-link v-else to="/newPage">登录</router-link>
```

在组件中给vuex传值

```html
<template>
  <div>
    <input type="text" v-model="info.username" placeholder="用户名">
    <input type="password" v-model="info.password" placeholder="密码">
    <input type="button" value="登录" @click="login">
  </div>
</template>

<script setup>
import {ref} from "vue";
import {useStore} from "vuex";
import {useRouter} from "vue-router";


const router = useRouter();
const store = useStore();
const info = ref({
  username: "",
  password: ""
})

const login = function () {

  // 1.用户登录
  store.commit("SET_USERINFO", info)             
    // 给vuex中定义的SET_USERINFO函数传值info。
	// info就是用户的数据
    // 2.登录成功修改状态
  router.push("/");
}

</script>
```

# flex布局

在css中fles可以非常便捷的帮助我们实现对页面的布局

```html
<template>
  <div class="menu">
    <div class="item">布局1</div>
    <div class="item">布局2</div>
    <div class="item">布局1</div>
    <div class="item">布局2</div>
    <div class="item">布局1</div>
    <div class="item">布局2</div>
    <div class="item">布局1</div>
    <div class="item">布局2</div>
  </div>
</template>

<div class="menu"  加到这里的样式是容器样式>
   <div class="item" 加到这里的样式是元素样式></div>
   <div class="item" 加到这里的样式是元素样式></div>
</div>
</template>


<style scoped>
.menu{
  display: flex;      //将menu设置成flex布局。
}
</style>
```

## 容器

```html
<template>
  <div class="menu">
    <div class="item">布局1</div>
    <div class="item">布局2</div>
    <div class="item">布局1</div>
    <div class="item">布局2</div>
    <div class="item">布局1</div>
    <div class="item">布局2</div>
    <div class="item">布局1</div>
    <div class="item">布局2</div>
  </div>
</template>


<style scoped>
.menu{
  display: flex;            // 将menu设置成flex布局。
  flex-direction: row;      // 主轴是横轴，副轴是纵轴。 flex-direction: column; 相反
  justify-content: space-evenly;   /* 三种主轴不同的分布*/
  justify-content: space-between;  
  justify-content: space-around;  
  align-content   /* 通过 align-content进行副轴的设置*/
  flex-wrap: nowrap;           /*当元素过多时操作元素不换行*/
  flex-wrap: wrap;            /*当元素过多时操作元素换行*/
  align-content: flex-start;   /* */ 
}
    
.item{
  border: 1px solid green;
  padding: 5px;
  width: 50px;
}

</style>
```

## 元素布局

```html
//可以通过 order: 2进行排序，order默认为0， 先排0，在排没有装饰order的，最后排有order，数值越小排列越靠前。


<template>
  <div class="menu">
    <div class="item" style="order: 2">布局1</div>
    <div class="item" style="order: 1">布局2</div>
    <div class="item" style="order: 0">布局3</div>
    <div class="item">布局4</div>
    <div class="item">布局5</div>
    <div class="item">布局6</div>
    <div class="item">布局7</div>
    <div class="item">布局8</div>
  </div>
</template>


<style scoped>
.menu {
  border: 1px solid red;
  width: 1000px;
  display: flex;
}

.item {
  border: 1px solid green;
  padding: 5px;
  width: 50px;
}
</style>
```

分配剩余空间

flex-grow，默认0，用于决定标签在剩余空间请何况下是否放大，默认不放大。

```css
flex-grow: 数字
```

```html
    <div class="item" style="order: 3;flex-grow: 1" >布局4</div>
```

布局4将剩下的空间占完。

![屏幕截图 2023-09-05 191209](D:\笔记\vue\assets\屏幕截图 2023-09-05 191209.png)

# Axios的补充

一般我们会将axios单独放到一个文件夹下。

![屏幕截图 2023-10-11 195108](D:\笔记\vue\assets\屏幕截图 2023-10-11 195108.png)



`axios.js`

```js
import axios from "axios"

const http = axios.create({
    // timeout: 2500,                             // 请求超时，有大文件上传需要关闭这个配置
    baseURL: "http://127.0.0.1:8000/",             // 设置api服务端的默认地址[如果基于服务端实现的跨域，这里可以填写api服务端的地址，如果基于nodejs客户端测试服务器实现的跨域，则这里不能填写api服务端地址]
    withCredentials: false,                       // 是否允许客户端ajax请求时携带cookie
})

// 请求拦截器
http.interceptors.request.use((config)=>{
    console.log("http请求之前");
    return config;
}, (error)=>{
    console.log("http请求错误");
    return Promise.reject(error);
});

// 响应拦截器
http.interceptors.response.use((response)=>{
    console.log("服务端响应数据成功以后，返回结果给客户端的第一时间，执行then之前");
    return response;
}, (error)=>{
    console.log("服务端响应错误内容的时候。...");
    return Promise.reject(error);
});

export default http;
```

视图中的代码

```js
<template>
  <div class="home">
    <Header></Header>

    <Footer></Footer>
  </div>
</template>

<script setup>
// vite中导入非ts.js文件时，必须填写文件后缀
import Header from "../components/Header.vue"
import Footer from "../components/Footer.vue"

// 测试CORS的跨域配置是否有问题
import http from "../utils/http";

// 测试服务端的跨域是否配置成功
// http.get("/api/home/demo/").then(response=>{
//   console.log(response.data);
// })

// 测试服务端的跨域是否配置成功
http.get("/home/test").then(response=>{
  console.log(response.data);
})
</script>

<style scoped>

</style>
```

