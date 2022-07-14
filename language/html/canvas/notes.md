# 基础: 创建 canvas 环境上下文

```js
var canvas = document.getElementById('tutorial');
if (!canvas.getContext) {
    alert('不支持 canvas.getContext 意味: 不支持 canvas 属性');
    return;
}
var ctx = canvas.getContext('2d');

// console.log('canvas: ', canvas);
// console.log('ctx: ', ctx);
```

#### 第一个简单示例:
```js
ctx.fillStyle = "rgb(200,0,0)";
ctx.fillRect (10, 10, 55, 50);

ctx.fillStyle = "rgba(0, 0, 200, 0.5)";
ctx.fillRect (30, 30, 55, 50);
```

![](https://mdn.mozillademos.org/files/228/canvas_ex1.png)

# 栅格:

* canvas元素默认被网格所覆盖
* 网格中的一个单元相当于canvas元素中的一像素
* 栅格的起点(原点)是: `左上角` (坐标为: 0,0)
* 所有元素的位置相对于原点定位
* 可以平移原点到不同的坐标上

![](https://mdn.mozillademos.org/files/224/Canvas_default_grid.png)

# 矩形绘制

```js
// 绘制一个填充的矩形
ctx.fillRect(x, y, width, height)

// 绘制一个矩形的边框
ctx.strokeRect(x, y, width, height)

// 清除指定矩形区域，让清除部分完全透明。
ctx.clearRect(x, y, width, height)
```

#### 矩形示例:

```js
ctx.fillRect(25,25,100,100);
ctx.clearRect(45,45,60,60);
ctx.strokeRect(50,50,50,50);
```

![](https://mdn.mozillademos.org/files/245/Canvas_rect.png)

# 绘制路径

图形的基本元素是路径, 路径是通过不同颜色和宽度的线段和曲线相连形成的不同形状的点的集合, 一个路径, 甚至一个子路径, 都是`闭合`的. 使用路径绘制图形需要一些额外的步骤.

1. 首先, 你需要创建路径起始点
2. 然后你使用画图命令去画出路径
3. 之后你把路径封闭
4. 一旦路径生成, 你就能通过描边或填充路径区域来渲染图形

以下是所要用到的函数:

```js
// 新建一条路径，生成之后，图形绘制命令被指向到路径上生成路径。
ctx.beginPath()

// 闭合路径之后图形绘制命令又重新指向到上下文中。
ctx.closePath()

// 通过线条来绘制图形轮廓。
ctx.stroke()

// 通过填充路径的内容区域生成实心的图形。
ctx.fill()
```

生成的路径的第一步叫做 `beginPath()` 本质上, 路径是由很多子路径构成的, 这些子路径都是在一个列表中, 所有的子路径(线, 弧形, 等等)构成图形. 而每次这个方法调用之后, 列表清空重置, 然后我们就可以重新绘制新的图形

第二步就是调用函数指定绘制路径

第三, 就是闭合路径 `closePath()` 不是必需的, 这个方法会通过绘制一条从当前点到开始点的直线来闭合图形(类似于PS的路径). 如果图形是已经闭合了的, 即当前点为开始点, 该函数什么也不做

绘制一个三角形:
```js
ctx.beginPath();
ctx.moveTo(75,50);
ctx.lineTo(100,75);
ctx.lineTo(100,25);
ctx.fill();
```

![](https://mdn.mozillademos.org/files/9847/triangle.png)

## 移动笔触:

一个非常有用的函数, 而这个函数实际上并不能画出任何东西, 也是上面所述的路径列表的一部分, 这个函数就是 `moveTo()`

或者可以想象一下在纸上作业, 一直钢笔或铅笔的笔尖从一个点到另一个点的移动过程

```js
// 将笔触移动到指定的坐标 x 以及 y 上.
ctx.moveTo(x, y)
```

笑脸实例:

```js
ctx.beginPath();
ctx.arc(75,75,50,0,Math.PI*2,true); // 绘制
ctx.moveTo(110,75);
ctx.arc(75,75,35,0,Math.PI,false); // 口(顺时针)
ctx.moveTo(65,65);
ctx.arc(60,65,5,0,Math.PI*2,true); // 左眼
ctx.moveTo(95,65);
ctx.arc(90,65,5,0,Math.PI*2,true); // 右眼
ctx.stroke();
```

![](https://mdn.mozillademos.org/files/252/Canvas_smiley.png)

如果想看到连续的线, 你可以移除调用的moveTo()

## 线, 直线

绘制直线, 需要用到的方法 `lineTo()`

```js
// 绘制一条从当前位置当指定 x 以及 y 位置的直线
ctx.lineTo(x, y)
```

实例: 绘制两个三角形:

```js
// 填充三角形
ctx.beginPath();
ctx.moveTo(25, 25);
ctx.lineTo(105, 25);
ctx.lineTo(25, 105);
ctx.fill();

// 描边三角形
ctx.beginPath();
ctx.moveTo(125, 125);
ctx.lineTo(125, 45);
ctx.lineTo(45, 125);
ctx.closePath();
ctx.stroke();
```

![](https://mdn.mozillademos.org/files/238/Canvas_lineTo.png)

注意:
* 使用 `fill()` 时路径会自动闭合
* 使用 `stroke()` 则不会闭合路径, 如果没有添加闭合路径 `closePath()` 到描述三角形函数中, 则只绘制了两条线段

## 圆弧

绘制圆弧或圆, 需要使用 `arc()` 方法. 也可以使用 `arcTo()`, 但这个方法的实现并不可靠, 所以不做考虑(具体原因待查...)

```js
// 画一个以 (x, y) 为圆心
// 以 radius 为半径的圆弧(圆)
// 从 startAngle 开始到 endAngle 结束
// 按照 anticlockwise  给定的方向(默认为false:顺时针)来生成 true:逆时针, false:顺时针
ctx.arc(x, y, radius, startAngle, endAngle, anticlockwise)

// radius 半径
// Angle 角度
// anticlockwise 逆时针

// 根据给定的控制点和半径画一段圆弧, 再以直线连接两个控制点
arcTo(x1, y1, x2, y2, radius)
```
详解 `arc()` 方法:
* `x, y` 为绘制圆弧所在圆上的圆心坐标
* `radius` 为半径
* `startAngle` 以及 `endAngle` 参数用弧度定义了开始以及结束的弧度, 这些都是以 `x` 轴 为基准.
* `anticlockwise` 为一个布尔值, 为 true 时, 是逆时针方向, 否则顺时针方向

注意:  `acr()` 函数中的角度单位是弧度, 不是角度, 角度与弧度的 `js` 表达式: `radians=(Math.PI/180)*degrees`

degrees: 度


#### 弧度测试实例:
下面的例子比上面的要复杂一下，下面绘制了12个不同的角度以及填充的圆弧。

下面两个`for`循环，生成圆弧的行列（`x,y`）坐标。每一段圆弧的开始都调用`beginPath()`。代码中，每个圆弧的参数都是可变的，实际生活中，我们并不需要这样做。

`x,y` 坐标是可变的。半径（`radius`）和开始角度（`startAngle`）都是固定的。结束角度（`endAngle`）在第一列开始时是180度（半圆）然后每列增加90度。最后一列形成一个完整的圆。

`clockwise`语句作用于第一、三行是顺时针的圆弧，`anticlockwise`作用于二、四行为逆时针圆弧。`if`语句让一、二行描边圆弧，下面两行填充路径。

```js
for(var i=0;i<4;i++){
    for(var j=0;j<4;j++){
        ctx.beginPath();
        var x = 15+j*30; // x 坐标值
        var y = 15+i*30; // y 坐标值
        var radius = 10; // 圆弧半径
        var startAngle = 0; // 开始点
        var endAngle = Math.PI/180 * 90*(j+1); // 结束点
        var anticlockwise = i%2==0 ? false : true; // 顺时针或逆时针

        ctx.arc(x, y, radius, startAngle, endAngle, anticlockwise);
        console.log('i', i, 'j', j, 'x', x, 'y', y, 'radius', radius, 'startAngle', startAngle, 'endAngle', endAngle, 'anticlockwise', anticlockwise);

        if (i>1){
            ctx.fill();
        } else {
            ctx.stroke();
        }
    }
}
```

![](https://mdn.mozillademos.org/files/204/Canvas_arc.png)

## 二次贝赛尔曲线及三次贝赛尔曲线

二次贝赛尔曲线及三次贝赛尔曲线都非常有用, 一般用来绘制复杂有规律的图形
```js
// 绘制二次贝塞尔曲线，`cp1x,cp1y`为一个控制点，`x,y为`结束点。
quadraticCurveTo(cp1x, cp1y, x, y)

// 绘制三次贝塞尔曲线，`cp1x,cp1y`为控制点一，`cp2x,cp2y`为控制点二，`x,y`为结束点。
bezierCurveTo(cp1x, cp1y, cp2x, cp2y, x, y)
```
二次贝塞尔曲线:
* 一个开始点
* 一个结束点
* 一个控制点

三次贝塞尔曲线:
* 一个开始点
* 一个结束点
* 二个控制点

![](https://mdn.mozillademos.org/files/223/Canvas_curves.png)

#### 使用二次贝尔塞曲线渲染对话气泡
```js
ctx.beginPath();
ctx.moveTo(75,25);
ctx.quadraticCurveTo(25, 25, 25, 62.5);
ctx.quadraticCurveTo(25, 100, 50, 100);
ctx.quadraticCurveTo(50, 120, 30, 125);
ctx.quadraticCurveTo(60, 120, 65, 100);
ctx.quadraticCurveTo(125, 100, 125, 62.5);
ctx.quadraticCurveTo(125, 25, 75, 25);
ctx.stroke();
```

![](https://mdn.mozillademos.org/files/243/Canvas_quadratic.png)

#### 使用三次贝塞尔曲线绘制心形
```js
ctx.beginPath();
ctx.moveTo(75, 40);
ctx.bezierCurveTo(75, 37, 70, 25, 50, 25);
ctx.bezierCurveTo(20, 25, 20, 62.5, 20, 62.5);
ctx.bezierCurveTo(20, 80, 40, 102, 75, 120);
ctx.bezierCurveTo(110, 102, 130, 80, 130, 62.5);
ctx.bezierCurveTo(130, 62.5, 130, 25, 100, 25);
ctx.bezierCurveTo(85, 25, 75, 37, 75, 40);
ctx.fill();
```

![](https://mdn.mozillademos.org/files/207/Canvas_bezier.png)

## 矩形路径

将矩形路径绘制到路径上

```js
// 绘制一个左上角坐标为 (x, y) 宽高为 width 以及 height 的矩形
ctx.rect(x, y, width, height)
```
> 当该方法执行的时候,  `moveTo()` 自动设置坐标参数 `(0, 0)`
> 也就是说, 当前笔触自动重置回默认坐标

## 组合使用

绘制一个图形并没有限制使用数量以及类型

#### 组合使用所有的路径函数来重现一组著名的游戏人物
```js
roundedRect(ctx,12,12,150,150,15);
roundedRect(ctx,19,19,150,150,9);
roundedRect(ctx,53,53,49,33,10);
roundedRect(ctx,53,119,49,16,6);
roundedRect(ctx,135,53,49,33,10);
roundedRect(ctx,135,119,25,49,10);

ctx.beginPath();
ctx.arc(37,37,13,Math.PI/7,-Math.PI/7,false);
ctx.lineTo(31,37);
ctx.fill();

for(var i=0;i<8;i++){
    ctx.fillRect(51+i*16,35,4,4);
}

for(i=0;i<6;i++){
    ctx.fillRect(115,51+i*16,4,4);
}

for(i=0;i<8;i++){
    ctx.fillRect(51+i*16,99,4,4);
}

ctx.beginPath();
ctx.moveTo(83,116);
ctx.lineTo(83,102);
ctx.bezierCurveTo(83,94,89,88,97,88);
ctx.bezierCurveTo(105,88,111,94,111,102);
ctx.lineTo(111,116);
ctx.lineTo(106.333,111.333);
ctx.lineTo(101.666,116);
ctx.lineTo(97,111.333);
ctx.lineTo(92.333,116);
ctx.lineTo(87.666,111.333);
ctx.lineTo(83,116);
ctx.fill();

ctx.fillStyle = "white";
ctx.beginPath();
ctx.moveTo(91,96);
ctx.bezierCurveTo(88,96,87,99,87,101);
ctx.bezierCurveTo(87,103,88,106,91,106);
ctx.bezierCurveTo(94,106,95,103,95,101);
ctx.bezierCurveTo(95,99,94,96,91,96);
ctx.moveTo(103,96);
ctx.bezierCurveTo(100,96,99,99,99,101);
ctx.bezierCurveTo(99,103,100,106,103,106);
ctx.bezierCurveTo(106,106,107,103,107,101);
ctx.bezierCurveTo(107,99,106,96,103,96);
ctx.fill();

ctx.fillStyle = "black";
ctx.beginPath();
ctx.arc(101,102,2,0,Math.PI*2,true);
ctx.fill();

ctx.beginPath();
ctx.arc(89,102,2,0,Math.PI*2,true);
ctx.fill();

// 封装的一个用于绘制圆角矩形的函数.
function roundedRect(ctx,x,y,width,height,radius){
    ctx.beginPath();
    ctx.moveTo(x,y+radius);
    ctx.lineTo(x,y+height-radius);
    ctx.quadraticCurveTo(x,y+height,x+radius,y+height);
    ctx.lineTo(x+width-radius,y+height);
    ctx.quadraticCurveTo(x+width,y+height,x+width,y+height-radius);
    ctx.lineTo(x+width,y+radius);
    ctx.quadraticCurveTo(x+width,y,x+width-radius,y);
    ctx.lineTo(x+radius,y);
    ctx.quadraticCurveTo(x,y,x,y+radius);
    ctx.stroke();
}
```

![](https://mdn.mozillademos.org/files/9849/combinations.png)

# Path2D 对象

正如在前面例子中看到的, 你可以使用一系列的路径和绘图命令来把对象"画"在画布上, 为了简化代码和提高性能, `Path2D` 对象已可以在较新版本的浏览器中使用, 用来缓存或记录绘画命令, 这样你将能快速回顾路径

```js
// 会返回一个新初始化的Path2D对象
// (可能将某一个路径作为变量--创建一个它的副本,
// 或者将一个包含 SVG path 数据的字符串作为变量)
Path2D()
```

使用:
```js
new Path2D(); // 空的Path对象
new Path2D(path); // 克隆Path对象
new Path2D(d); // 从SVG建立Path对象
```

所有的路径方法比如 `moveTo()` , `rect()` , `arc()` 或 `quadraticCurveTo()` 等, 如我们前面见过的, 都可以在 `Path2D` 中使用

`Path2D API`  添加了 `addPath` 作为将 `path` 结合起来的方法, 当你想要从几个元素中来创建对象时, 这将很实用, 比如:

```js
// 添加了一条路径到当前路径(可能添加了一个变换矩阵)
Path2D.addPath(path, [, transform])
```

#### Path2D示例:
```js
var rectangle = new Path2D();
rectangle.rect(10, 10, 50, 50);

var circle = new Path2D();
circle.moveTo(125, 35);
circle.arc(100, 35, 25, 0, Math.PI*2)

ctx.stroke(rectangle);
ctx.fill(circle)
```

![](https://mdn.mozillademos.org/files/9851/path2d.png)

#### 使用 SVG paths

新的 `Path2D API` 有另一个强大的特点, 就是使用 `SVG Path data` 来初始化 `canvas` 上的路径, 这将使你获取路径时可以以 `SVG` 或 `canvas` 的方式来重用它们

使用 `SVG path` 构建路径代码如下:
```js
// 这条路径将先移动到点(M10 10)
// 然后在水平移动 80个单位(h 80)
// 然后下移 80个单位(v 80)
// 接着左移 80个单位(h -80)
// 最终应该出来一个矩形
var p = new Path2D("M10 10 h 80 v 80 h -80 Z");
```

# 色彩 Colors

想要给图形上色, 有两个重要的属性可以做到: `fillStyle` 和 `strokeStyle`

```js
// 设置图形的填充颜色
ctx.fillStyle = color

// 设置图形的轮廓的颜色
ctx.strokeStyle = color
```

> `color` 可以是表示 `CSS 颜色值`的字符串, `渐变对象` 或者 `图案对象`
> 默认情况下: 线条和填充颜色都是 `黑色` (`CSS` 颜色值: `#000000`)

> 注意:
> 一旦您设置了 `strokeStyle` 或者 `fillStyle` 的值, 那么这个新值就会成为新绘制的图形的默认值, 如果你要给每个图形上不同的颜色, 你需要重新设置 `strokeStyle` 或者 `fillStyle` 的值
> 您输入的应该是符合 [CSS3颜色值标准](https://www.w3.org/TR/css-color-3/) 的有效字符串, 下面的例子都表示同一种颜色
```js
// 这些 fillStyle 的值均为 '橙色'
ctx.fillStyle = "orange";
ctx.fillStyle = "#FFA500";
ctx.fillStyle = "rgb(255,165,0)";
ctx.fillStyle = "rgba(255,165,0,1)";
```

#### fillStyle 示例
```js
for (var i = 0; i < 6; i++) {
    for (var j = 0; j < 6; j++) {
        var r = Math.floor(255 - 42.5*i);
        var g = Math.floor(255 - 42.5*j);
        var b = 0;
        ctx.fillStyle = 'rgb('+r+','+g+','+b+')';
        ctx.fillRect(j*25, i*25, 25, 25);
    }
}
```
> 示例中, 再度使用了两层 `for` 循环来绘制方格阵列, 每个方格不同的颜色
> 使用了两个变量来为每一个方块产生唯一的 `RGB` 色彩值, 其中仅修改红色和绿色通道的值, 而保持三蓝色通道的值不变,

![](https://mdn.mozillademos.org/files/5417/Canvas_fillstyle.png)

#### strokeStyle 示例
```js
for (var i = 0; i < 6; i++) {
    for (var j = 0; j < 6; j++) {
        var r = Math.floor(255 - 42.5*i);
        var g = Math.floor(255 - 42.5*j);
        var b = 0;
        ctx.strokeStyle = 'rgb('+r+','+g+','+b+')';
        ctx.beginPath();
        ctx.arc(12.5+j*25, 12.5+i*25, 10, 0, Math.PI*2, true);
        ctx.stroke();
    }
}
```
> 与 `fillStyle` 示例类似代码, 但画的不是方格, 而是用 `arc()` 方法来画图

![](https://mdn.mozillademos.org/files/253/Canvas_strokestyle.png)

## 透明度 Transparency

除了可以绘制实色图形, 我们还可以用 **canvas** 来绘制半透明的图形, 通过设置 **globalAlgha** 属性或者使用一个 **半透明颜色** 作为轮廓或填充的样式

```js
// 这个属性影响到 canvas 里所有图形的透明度，有效的值范围是 0.0 （完全透明）到 1.0（完全不透明），默认是 1.0
// CanvasRenderingContext2D.globalAlpha 是 Canvas 2D API 用来描述在canvas上绘图之前，设置图形和图片透明度的属性。 数值的范围从 0.0 （完全透明）到1.0 （完全不透明）。
ctx.globalAlpha = transparencyValue
```

> `globalAlpha` 属性在需要绘制大量拥有相同透明度的图形时候相当有效
> 不过 `MDN` 作者认为下面的方法可操作性更强一点
> 因为 `strokeStyle` 和 `fillStyle` 属性接收符合 `CSS 3` 规范的颜色值
> 那我们可以用下面的写法来设置具有透明度的颜色, 如下:

```js
// 指定透明的颜色, 用于描边和填充样式
ctx.strokeStyle = "rgba(255, 255, 255, 0.5)";
ctx.fillStyle = "rgba(255, 255, 255, 0.5)";
```

> `rgba()` 方法与 `rgb()` 方法类似, 就多了一个用于设置色彩透明度的参数
> 它的有效范围是从 **0.0 (完全透明)** 到 **1.0 (完全不透明)**
> 而且 既然浏览器支持 `canvas` 那基本是就支持了 `rgba()` 所以不存在 兼容性问题

#### globalAlpha 示例

```js
// 绘制 四色 背景
ctx.fillStyle = '#FD0';
ctx.fillRect(0, 0, 75, 75);

ctx.fillStyle = '#6C0';
ctx.fillRect(75, 0, 75, 75);

ctx.fillStyle = '#09F';
ctx.fillRect(0, 75, 75, 75);

ctx.fillStyle = '#F30';
ctx.fillRect(75, 75, 75, 75);

ctx.fillStyle = '#FFF';
// 设置透明度值
ctx.globalAlpha = 0.2;

// 画半透明圆
for (var i = 0; i < 7; i++) {
    ctx.beginPath();
    ctx.arc(75, 75, 10+10*i, 0, Math.PI*2, true);
    ctx.fill();
}
```

> 例子中:
> 将用四色格作为背景
> 设置 `globalAlpha` 为 `0.2` 后, 在上面画一系列半径递增的半透明圆
> 最终结果是一个径向渐变效果, 圆叠加得越多, 原先所画的圆的透明度会越低
> 通过增加循环次数, 画更多的圆, 背景图的中心部分会完全消失

![](https://mdn.mozillademos.org/files/232/Canvas_globalalpha.png)

#### rgba() 示例

```js
// 绘制 四色 背景
ctx.fillStyle = 'rgb(255, 221, 0)';
ctx.fillRect(0, 0, 150, 37.5);

ctx.fillStyle = 'rgb(102, 204, 0)';
ctx.fillRect(0, 37.5, 150, 37.5);

ctx.fillStyle = 'rgb(0, 153, 255)';
ctx.fillRect(0, 75, 150, 37.5);

ctx.fillStyle = 'rgb(255, 51, 0)';
ctx.fillRect(0, 112.5, 150, 37.5);

// 画半透明矩形
for (var i = 0; i < 10; i++) {
    ctx.fillStyle = 'rgba(255, 255, 255, ' + (i+1) / 10 + ')';
    for (var j = 0; j < 4; j++) {
        ctx.fillRect(5 + i*14, 5 + j*37.5, 14, 27.5)
    }
}
```

> 这个示例和 上一个 `globalAlpha` 示例类似
> 不过不是画圆, 而是画矩形
> 还可以看出, `rgba()` 可以分别设置轮廓和填充样式, 因而具有更好的可操作性和使用灵活性

![](https://mdn.mozillademos.org/files/246/Canvas_rgba.png)

## 线型 Line styles

可以通过一系列属性来设置线的样式

```js
// 设置线条宽度
ctx.lineWidth = value

// 设置线条末端样式
ctx.lineCap = type['butt', 'round', 'square']

// 设定线条与线条间接合处的样式
ctx.lineJoin = type['round', 'bevel', 'miter']

// 限制当两条线相交处交接处最大长度
// 所谓交接处长度(斜接长度)是指线条交接处内角顶点到外交顶点的长度
ctx.miterLimit = value

// 返回一个包含当期那虚线样式, 长度为非负偶数的数组
ctx.getLineDash()

// 设置当期那虚线样式 segments:段
ctx.setLineDash(segments)

// 设置虚线样式的起始偏移量
ctx.lineDashOffset = value
```

通过下面的例子会更加容易理解:

#### lineWidth 属性 示例:
```js
for (var i = 0; i < 10; i++) {
    ctx.lineWidth = 1+i;
    ctx.beginPath();
    ctx.moveTo(5 + i*14, 5);
    ctx.lineTo(5 + i*14, 140);
    ctx.stroke();
}
```
> 设置了当前绘制 线 的粗细, 属性必须为正整数, 默认值是: **1.0**
> 线宽是指给路径的中心到两边的粗细, 换句话说的就是在路径的两边各绘制线宽的一半
> 因为画布的坐标并不和像素直接对应, 当需要获得精准的水平或垂直线的时候要特别注意
> 这个示例, 用递增的宽度绘制了10条直线, 最左边的线宽1.0单位, 并且, 最左边的以及所有宽度为奇数的线并不能精确呈现, 这就是因为路径的定位问题

![示例结果](https://mdn.mozillademos.org/files/239/Canvas_linewidth.png)

想要获得精确的线条, 必须对线条是如果描绘出来的有所理解, 见下图, 用网格来代表 `canvas` 的坐标格, 每一格对应屏幕上一个像素点, 在第一个图中, 填充了(2, 1) 至(5, 5)的矩形, 整个区域的边界刚好落在像素边缘上, 这样就可以使得得到的矩形有着清晰的边缘

![绘制图](https://mdn.mozillademos.org/files/201/canvas-grid.png)

想要绘制一条从 (3, 1) 到 (3, 5), 宽度是1.0 的线条, 就会得到想第二幅图一样的结果, 实际填充区域(深蓝色部分) 仅仅延伸至路径两旁各一个像素, 而这半个像素又会以近似的方式进行渲染, 这意味着那些像素只是部分着色, 结果就是以实际笔触颜色一般色调的颜色来填充整个区域, (浅蓝和深蓝的部分) 这就是上例中为何宽度为 1.0 的线并不准确的原因

要解决整个问题, 你必须对路径施以更加精准的控制. 已知粗1.0的线条会在路径两边各延伸半像素, 那么像第三幅图那样绘制从 (3.5, 1) 到 (3.5, 5) 的线条, 其边缘正好落在像素边界上, 填充出来就是准确的宽为 1.0 的线条

>  **注意:** 在这个竖线的例子中，其Y坐标刚好落在网格线上，否则端点上同样会出现半渲染的像素点（但还要注意，这种行为的表现取决于当前的lineCap风格，它默认为butt；您可能希望通过将lineCap样式设置为square正方形，来得到与奇数宽度线的半像素坐标相一致的笔画，这样，端点轮廓的外边框将被自动扩展以完全覆盖整个像素格）。
> 还请注意，只有路径的起点和终点受此影响：如果一个路径是通过closePath()来封闭的，它是没有起点和终点的；相反的情况下，路径上的所有端点都与上一个点相连，下一段路径使用当前的lineJoin设置（默认为miter），如果相连路径是水平和/或垂直的话，会导致相连路径的外轮廓根据相交点自动延伸，因此渲染出的路径轮廓会覆盖整个像素格。接下来的两个小节将展示这些额外的行样式。

#### lineCap 属性的示例:

属性 `lineCap` 的值决定了 线段端点显示的样式, 可以为: `butt` , `round` , `square` 其中一种, 默认是 `butt`

```js
// 创建路径
ctx.strokeStyle = '#09f';
ctx.beginPath();
ctx.moveTo(10, 10);
ctx.lineTo(140, 10);
ctx.moveTo(10, 140);
ctx.lineTo(140, 140);
ctx.stroke();

// 画线条
ctx.strokeStyle = 'black';

var lineCap = ['butt', 'round', 'square'];
for (var i = 0; i < lineCap.length; i++) {
    ctx.lineWidth = 15;
    ctx.lineCap = lineCap[i];
    ctx.beginPath();
    ctx.moveTo(25 + i*50, 10);
    ctx.lineTo(25 + i*50, 140);
    ctx.stroke();
}
```

![](https://mdn.mozillademos.org/files/236/Canvas_linecap.png)

> 在这个例子里面，我绘制了三条直线，分别赋予不同的 `lineCap` 值。还有两条辅助线，为了可以看得更清楚它们之间的区别，三条线的起点终点都落在辅助线上。
> 最左边的线用了默认的 `butt` 。可以注意到它是与辅助线齐平的。中间的是 `round` 的效果，端点处加上了半径为一半线宽的半圆。右边的是 `square` 的效果，端点处加上了等宽且高度为一半线宽的方块。

#### lineJoin 属性的示例

`lineJoin` 的属性值决定了图形中两线段连接处所显示的样子。它可以是这三种之一：`round`, `bevel` 和 `miter。`默认是 `miter``。`

```js
var lineJoin = ['round', 'bevel', 'miter'];
ctx.lineWidth = 10;
for (var i = 0; i < lineJoin.length; i++) {
    ctx.lineJoin = lineJoin[i];
    ctx.beginPath();
    ctx.moveTo(-5, 5 + i*40);
    ctx.lineTo(35, 45 + i*40);
    ctx.lineTo(75, 5 + i*40);
    ctx.lineTo(115, 45 + i*40);
    ctx.lineTo(155, 5 + i*40);
    ctx.stroke();
}
```

![](https://mdn.mozillademos.org/files/237/Canvas_linejoin.png)

> 这里我同样用三条折线来做例子，分别设置不同的 `lineJoin` 值。最上面一条是 `round` 的效果，边角处被磨圆了，圆的半径等于线宽。中间和最下面一条分别是 `bevel` 和 `miter` 的效果。当值是 `miter` 的时候，线段会在连接处外侧延伸直至交于一点，延伸效果受到下面将要介绍的 `miterLimit` 属性的制约。

#### miterLimit 属性的例子
如上一个例子所见的应用 `miter` 的效果,线段的外侧边缘会延伸交汇于一点上, 线段直接夹角比较大, 交点不会太远, 但当夹角减少时, 交点距离会呈指数级增大

`miterLimit` 属性就是用来设定外延交点与连接点的最大距离, 如果交点距离大于此值, 连接效果会变成了 `bevel`

### 使用虚线

使用 `setLineDash` 方法和 `lineDashOffset` 属性来制定虚线样式, `setLineDash` 方法接收一个数组, 来指定线段与间隙的交替, `lineDashOffset` 属性设置起始偏移值

```js
var offset = 0;
function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.setLineDash([4, 12]);
    ctx.lineDashOffset = -offset;
    ctx.strokeRect(10, 10, 100, 100);
}
function march() {
    offset++;
    if (offset > 16) {
        offset = 0;
    }
    draw();
    setTimeout(march, 20);
}
march();
```

> 此实例首先创建一个蚂蚁线的效果
> 它往往应用在计算机图形程序选取工具动态效果中
> 它可以帮助用户通过动画的边界来区分图像背景选区边框

![](https://mdn.mozillademos.org/files/9853/marching-ants.png)

## 渐变 Gradients

就好像一般的绘图软件一样, 我们可以用线性或者径向的渐变来填充或描边, 我们用下面的方法新建一个 `canvasGradient` 对象, 并且赋给图形的 `fillStyle` 或 `strokeStyle` 属性

```js
// 方法接收4个参数, 表示渐变的起点(x1, y1)与终点(x2, y2)
ctx.createLinearGradient(x1, y1, x2, y2)
var lineargradient = ctx.createLinearGradient(0, 0, 150, 150);

// 方法接收6个参数, 前三个定义一个以(x1, y1)为原点, 半径为 r1 的圆
// 后三个参数则定义另一个以(x2, y2)为原点, 半径为 r2 的圆
ctx.createRadialGradient(x1, y1, r1, x2, y2, r2)
var radialgradient = ctx.createRadialGradient(75, 75, 0, 75, 75, 100);
```

创建出 `canvasGradient` 对象后, 我们就可以用 `addColorStop` 方法给它上色了

```js
// 方法接受2个参数, position参数必须是一个0.0与1.0之间的数值
// 表示渐变中颜色所在的相对位置, 例如, 0.5表示颜色会出现在正中间
// color 参数必须是一个有效的 CSS颜色值(如: #FFF, rgba(0, 0, 0, 1)等等)
gradient.addColorStop(position, color)
```

```js
// 可以根据需要添加任意多个色标(color, stops)
// 下面是最简单的线性黑白渐变的例子:
var lineargradient = ctx.createLinearGradient(0, 0, 150, 150);
lineargradient.addColorStop(0, 'white');
lineargradient.addColorStop(1, 'black');
```

#### createLinearGradient 的例子

```js
// Create gradients
var lineargradient = ctx.createLinearGradient(0, 0, 0, 150);
lineargradient.addColorStop(0, '#00ABEB');
lineargradient.addColorStop(0.5, '#fff');
lineargradient.addColorStop(0.5, '#26C000');
lineargradient.addColorStop(1, '#fff');

var lineargradient2 = ctx.createLinearGradient(0, 50, 0, 95);
lineargradient2.addColorStop(0.5, '#000');
lineargradient2.addColorStop(1, 'rgba(0, 0, 0, 0)');

// assign gradients to fill and stroke style
ctx.fillStyle = lineargradient;
ctx.strokeStyle = lineargradient2;

// draw shapes
ctx.fillRect(10, 10, 130, 150);
ctx.strokeRect(50, 50, 50, 50);
```

> 本例中: 做了两种不同的渐变:
> 第一种: 是背景渐变, 给同一位置设置了两种颜色, 你也可以用这来实现突变的效果, 就像这里从白色到绿色的突变. 一般情况下, 色标的定义是无所谓顺序的, 但是色标位置重复时, 顺序就变得非常重要了, 所以, 保持色标定义顺序和它理想的顺序一致, 结果应该没什么大问题
> 第二种渐变: 并不是从 0.0 位置开始定义色标, 因为那并不是那么严格, 在 0.5 处设一黑色色标, 渐变灰默认认为从起点到色标之间都是黑色
> 而且, `strokeStyle` 和 `fillStyle` 属性都可以接受 `canvasGradient` 对象

#### createRadialGradient 的例子

```js
var radialgradient4 = ctx.createRadialGradient(0, 150, 50, 0, 140, 90);
radialgradient4.addColorStop(0, '#F4F201');
radialgradient4.addColorStop(0.8, '#E4C700');
radialgradient4.addColorStop(1, 'rgba(228, 199, 0, 0)');
ctx.fillStyle = radialgradient4;
ctx.fillRect(0, 0, 150, 150);

var radialgradient3 = ctx.createRadialGradient(95, 15, 15, 102, 20, 40);
radialgradient3.addColorStop(0, '#00C9FF');
radialgradient3.addColorStop(0.8, '#00B5E2');
radialgradient3.addColorStop(1, 'rgba(0, 201, 255, 0)');
ctx.fillStyle = radialgradient3;
ctx.fillRect(0, 0, 150, 150);

var radialgradient2 = ctx.createRadialGradient(105, 105, 20, 112, 120, 50);
radialgradient2.addColorStop(0, '#FF5F98');
radialgradient2.addColorStop(0.75, '#FF0188');
radialgradient2.addColorStop(1, 'rgba(255, 1, 136, 0)');
ctx.fillStyle = radialgradient2;
ctx.fillRect(0, 0, 150, 150);

// 创建渐变
var radialgradient = ctx.createRadialGradient(45, 45, 10, 52, 50, 30);
radialgradient.addColorStop(0, '#A7D30C');
radialgradient.addColorStop(0.9, '#019F62');
radialgradient.addColorStop(1, 'rgba(1, 159, 98, 0)');
// 画图形
ctx.fillStyle = radialgradient;
ctx.fillRect(0, 0, 150, 150);
```

> 让起点稍微偏离终点, 这样就可以达到一种球状3D效果, 但最好不要让里圆与外圆部分交叠, 那样会产生什么效果就真的不得而知了
> 4个径向渐变效果的最后一个色标都是透明色, 如果想要两色标直接的过度柔和一些, 只要两个颜色值一致就可以了

## 图案样式 Pattern

使用循环来实现图案的效果, 这里有一个更加简单的方法:

```js
// 方法接收两个参数,
// image 可以是一个 image 对象的引用, 或者另一个 canvas 对象
// type 必须是下面的字符串值之一: repeat, repeat-x, repeat-y 和 no-repeat
ctx.createPattern(image, type)
```
> 注意: 使用 canvas 对象作为 image 参数在 Firefox 1.5(Gecko 1.8) 中是无效的

```js
var img = new Image();
img.src = 'testimage.png';
var pattern = ctx.createPattern(img, 'repeat');
```
> 注意: 与 drawImage 有点不同, 你需要确认 image 对象已经装载完毕, 否则图案效果可能不对

```js
var img = new Image();
img.src = '../images/bilogo.png';
img.onload = function() {
    // 创建图案
    var pattern = ctx.createPattern(img, 'repeat');
    ctx.fillStyle = pattern;
    ctx.fillRect(0, 0, 150, 150);
}
```
> 实例中:
> 创建了一个图案然后赋给了 `fillStyle` 属性
> 唯一要注意的是, 使用 Image 对象的 `onload` handler 来确保设置图案之前图像已经装载完毕

## 阴影 Shadow

```js
// shadowOffsetX 和 shadowOffsetY 用来设定阴影在 X 和 Y 轴的延伸距离
// 它们是不受变换矩形所影响的, 负值表示阴影或往上或往左延伸, 正值则表示会往下或右延伸
// 它们默认都为 0
ctx.shadowOffsetX = float;

ctx.shadowOffsetY = float;

// 用于设置阴影的模糊程序, 其数值并不跟像素数量挂钩, 也不受变化矩阵影响, 默认为 0
ctx.shadowBlur = float;

// 使用标准CSS颜色值, 用户设定阴影颜色效果, 默认是全透明的黑色
ctx.shadowColor = color;
```

#### 文字阴影的例子:

```js
ctx.shadowOffsetX = 2;
ctx.shadowOffsetY = 2;
ctx.shadowBlur = 2;
ctx.shadowColor = 'rgba(0, 0, 0, 0.5)';

ctx.font = '20px Times New Roman';
ctx.fillStyle = 'Black';
ctx.fillText('Sample String', 5, 30);
```
![](https://mdn.mozillademos.org/files/2505/shadowed-string.png)


## Canvas 填充规则

当我们使用 `fill` (或者 `clip` 和 `isPointinPath`) 你可以选择一个填充规则, 该填充规则根据某处在路径的外面或者里面来决定该处是否被填充, 这对于自己与自己路径相交或者路径被嵌套的时候是有用的

两个可能的值:
* `nonzero` : [non-zero winding rule](https://en.wikipedia.org/wiki/Nonzero-rule) 默认值
* `evenodd` : [even-odd winding rule](https://en.wikipedia.org/wiki/Even%E2%80%93odd_rule)

使用规则 `evenodd`
```js
ctx.beginPath();
ctx.arc(50, 50, 30, 0, Math.PI * 2, true);
ctx.arc(50, 50, 15, 0, Math.PI * 2, true);
ctx.fill('evenodd');

ctx.beginPath();
ctx.arc(150, 50, 30, 0, Math.PI * 2, true);
ctx.arc(150, 50, 15, 0, Math.PI * 2, true);
ctx.fill('nonzero');
```
![](https://mdn.mozillademos.org/files/9855/fill-rule.png)


# 绘制文本

`canvas` 提供了两种方法来渲染文本:

```js
// 在指定的 (x, y) 位置填充指定的文本, 绘制的最大宽度是可选的
ctx.fillText(text, x, y [, maxWidth])'

// 在指定的 (x, y) 位置绘制文本边框, 绘制的最大宽度是可选的
ctx.strokeText(text, x, y [, maxWidth]);
```

填充文本的示例:
```js
ctx.font = '48px serif';
ctx.fillText('Hello World!', 10, 50);

ctx.font = '48px serif';
ctx.strokeText('Hello World!', 10, 50);
```

#### 有样式的文本:

```js
// 当前我们用来绘制文本的样式, 这个字符串使用和 CSS font 属性相同的语法
// 默认的字体是 10px sans-serif
ctx.font = value;

// 文本对齐选项, 可选值: start end left right center 默认值是: start
ctx.textAlign = vlaue;

// 基线对齐选项, 可选值: top hanging middle alphabetic ideographic bottom 默认值是: alphabetic
ctx.textBaseline = value;

// 文本方向, 可选值: ltr rtl inherit 默认值: inherit
ctx.direction = value;
```

实例:
```js

```

下图是 `textBaseline` 属性支持的不同的基线情况:
![](https://html.spec.whatwg.org/images/baselines.png)

### 预测量文本宽度

当你需要获得更多的文本细节时, 下面的方法可以给你测量文本的方法

```js
// 将返回一个 TextMetrics 对象的宽度, 所在像素, 这些体现文本特性的属性
ctx.measureText()
```

实例:
```js
var text = ctx.measureText('foo'); // TextMetrics object
console.log('text: ', text);
console.log('text.width: ', text.width);
```

## Geoko特性说明

在Geoko（Firefox，Firefox OS及基于Mozilla的应用的渲染引擎）中，曾有一些版本较早的 [API](https://developer.mozilla.org/zh-CN/docs/Web/API/CanvasRenderingContext2D#Prefixed_APIs) 实现了在canvas上对文本作画的功能，但它们现在已不再使用。


# 状态的保存和恢复 Saving and restoring state

绘制复杂图形时必不可少的方法:
```js
// 用于保存和恢复 canvas 状态, 都没有参数
// canvas 状态就是当前画面应用的所有样式和变形的一个快照
ctx.save();
ctx.restore();
```

`canvas` 状态存储在栈中, 每当 `save()` 方法被调用后, 当前的状态就被推送到栈中保存
一个绘画状态包括
* 当前应用的变形 (即移动, 旋转, 缩放)
* `strokeStyle` `fillStyle` `globalAlpha` `lineWidth` `lineCap` `lineJoin` `miterLimit` `shadowOffsetX` `shadowOffsetY` `shadowBlur` `shadowColor` `globalCompositeOperation` 的值
* 当前的裁剪路径 (clipping path)

你可以调用任意多次 `save` 方法

每一个调用 `restore` 方法, 上一次保存的状态就从栈中弹出, 所有设定都恢复

#### `sava()` 与 `restore()` 的例子:
```js
ctx.fillStyle = '#000';
ctx.fillRect(0, 0, 150, 150);   // 使用默认设置绘制一个矩形
ctx.save();                     // 保存默认状态设置

ctx.fillStyle = '#09F';         // 在原有配置基础上对颜色进行改变
ctx.fillRect(15, 15, 120, 120); // 使用新的设置绘制一个矩形
ctx.save();                     // 保存当前状态

ctx.fillStyle = '#FFF';         // 再次改变颜色配置
ctx.globalAlpha = 0.5;          // 另外改变透明度
ctx.fillRect(30, 30, 90, 90);   // 使用新的配置绘制一个矩形

ctx.restore();                  // 重新加载之前的颜色状态, 放弃当前状态
ctx.fillRect(45, 45, 60, 60);   // 使用上一次的配置绘制一个矩形

ctx.restore();                  // 加载第一次的颜色配置
ctx.fillRect(60, 60, 30, 30);   // 使用第一次的配置再绘制一个矩形
```

> 使用这个连续矩形的例子来描述 `canvas` 的状态栈是如何工作的
> 第一步是用默认设置画一个大四方形, 然后保存一下状态
> 改变填充颜色画第二个小一点的蓝色四方形, 然后在保存一下状态
> 再次改变填充颜色绘制更小一点的半透明的白色四方形
>
> 到目前为止所做的动作和前面的内容都很类似
> 不过一旦我们调用 `restore` 状态栈中最后的状态会弹出, 并恢复所有设置
> 如果不是之前用 `save` 保存了状态, 那么我们就需要手动改变设置来回到前一个状态
> 这个对于三两个属性的还是适用的, 一旦多了, 我们的代码将会猛涨
>
> 当第二次调用 `restore` 时, 已经恢复到最初的状态, 因此最后是再一次绘制出一个黑色的四方形

![](https://mdn.mozillademos.org/files/249/Canvas_savestate.png)
