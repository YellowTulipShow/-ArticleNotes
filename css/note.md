资料来源于: 《CSS设计彻底研究》---人民邮电出版社---编著: 前沿科技 温谦
资料来源于: url:(www.w3school.com.cn) ---W3School教学网站
其他资料来源附录具体内容部分
**************************************************************************************************************************************

// CSS 兼容性
https://caniuse.com/

    // Web前端兼容性在线测试工具
    http://browsershots.org/
        账户: YellowTulipShow
        密码: YellowTulipShowmima

#region 导入式: <style type="text/css">@import "样式表名称.css"</style>#endregion
#region 链接式: <link href="样式表名称.css" rel="stylesheet" type="text/css">#endregion

#region 一般需要设置: 
    
    font-family:```;            /*字体样式*/
    font-size:```;                  /*字体大小*/
    color:```;                  /*字体颜色*/
    
    width:```;                  /*盒子宽度*/
    height:```;                 /*盒子高度*/
    
    margin:```;                 /*盒子外边距*/
    border:```;                 /*盒子边框*/
    padding:```;                    /*盒子内边距*/
    
    float:```;                  /*浮动方式*/
    display:```;                    /*块级、行内、隐藏元素*/
    
    background:```;             /*背景*/
    
    text:```;                       /*内容*/
    
    list···:```;                    /*列表*/
    
    line-height:```;                /*行高*/
#endregion

#region 选择器★
    一、干干净净为“标记选择器”
        如: html,head,body,a,div {}
    二、#号为“ID选择器”
        如: #menu,#kok {}
    三.为“class选择器”
        如: .class {}
    四、逗号为平级，空格为下级
        如: body div {}
            body,div {}
    五、“邻接”选择器
        如: td+td+td {~~~}
        上面用连个加号，连接3个td，就表示每一行的第3个td为选中的元素
        具体的实例在“CSS设计彻底研究”的10-2的书中P242-P243
    六、使用属性选择器的部分匹配功能
		如: 
		[abc^="def"] // 选择 abc 属性值以 "def" 开头的所有元素    
		[abc$="def"] // 选择 abc 属性值以 "def" 结尾的所有元素    
		[abc*="def"] // 选择 abc 属性值中包含子串 "def" 的所有元素
		详解: http://www.w3school.com.cn/cssref/selector_attr_begin.asp
    

===<选择器种类>===
    严格来讲，选择器的种类可以分为三种: 标签名选择器、类选择器和ID选择器。
    而所谓的后代选择器和群组选择器只不过是对前三种选择器的扩展应用。
    而 在标签内写入style=""的方式，应该是CSS的一种引入方式，而不是选择器，因为根本就没有用到选择器。
    而一般人们将上面这几种方式结合在一起，所 以就有了5种或6种选择器了。


===<三种基本的选择器类型>===
    语法如下: 
    ◆标签名选择器，如: p{}，即直接使用HTML标签作为选择器。
    ◆类选择器，如.polaris{}。
    ◆ID选择器，如#polaris{}。
    注意，ID选择器跟类选择器有很大的不同: 一个页面内不能出现相同的ID；
    再就是ID也是后台开发人员会经常用的，所以前端开发人员应该尽量少的使用。
    当然跟后台人员的工作配合十分娴熟之后，这些都不会成为限制。

===<扩展选择器>===
    ◆后代选择器，如.polaris span img{}，后代选贼器实际上是使用多个选择器加上中间的空格来找到具体的要控制标签。
    ◆群组选择器，如div,span,img{}，群组选择器实际上是对CSS的一种简化写法，只不过把有相同定义的不同选择器放在一起，省了很多代码。

===<选择器的优先级别>===
    了解了各种选择器后，还有一个重要的知识点就是CSS选择器的优先级。这也就是为什么polaris会遇到文章开头的问题。举个简单的例子: 
    <div class="polaris"> 
        <span class="beijixing"> 
            beijixing  
        </span> 
        <span> 
            polaris  
        </span> 
    </div> 
    如果已经把.polaris下面span内的字体设置成红色: 
    .polaris span {color:red;} 
    这时，如果要改变.beijixing的颜色为蓝色，用下面的命令是不能实现的: 
    .beijixing {color:blue;} 
    出现这种情况就是因为后一个命令的优先级不够，两条相互冲突的样式设置，浏览器只会执行优先级较高的那个。
    那么选择器的优先级是怎么规定的呢？
        一般而言，选择器越特殊，它的优先级越高。
        也就是选择器指向的越准确，它的优先级就越高。
        通常我们用1表示标签名选择器的优先级，用10表示类选择 器的优先级，用100标示ID选择器的优先级。
        比如上例当中 .polaris span {color:red;}的选择器优先级是 10 + 1 也就是11；而 .polaris 的优先级是10；浏览器自然会显示红色的字。
        理解了这个道理之后下面的优先级计算自是易如反掌: 
    div.test1 .span var 优先级 1+10 +10 +1  
    span#xxx .songs li 优先级1+100 + 10 + 1  
    #xxx li 优先级 100 +1 
    对于什么情况下使用什么选择器，用不同选择器的原则是: 
        第一: 准确的选到要控制的标签；
        第二: 使用最合理优先级的选择器；
        第三: HTML和CSS代码尽量简洁美观。
    通常: 
        1、最常用的选择器是类选择器。
        2、li、td、dd等经常大量连续出现，并且样式相同或者相类似的标签，我们采用类选择器跟标签名选择器结合的后代选择器 .xx li/td/dd {} 的方式选择。
        3、极少的情况下会用ID选择器，当然很多前端开发人员喜欢header，footer，banner，conntent设置成ID选择器的，因为相同的样式在一个页面里不可能有第二次。
    在这里不得不提使用在标签内引入CSS的方式来写CSS，即: 
    <div style="color:red">polaris</div> 
    这时候的优先级是最高的。我们给它的优先级是1000，这种写法不推荐使用，特别是对新手来说。这也完全违背了内容和显示分离的思想。DIV+CSS的优点也不能再有任何体现。


===<后代选择器的定位原则:>===
    在这里介绍一下对于后代选择器，浏览器是如何查找元素的呢？
    浏览器CSS匹配不是从左到右进行查找，而是从右到左进行查找。
    比如DIV#divBox p span.red{color:red;}，浏览器的查找顺序如下: 先查找html中所有class='red'的span元素，
    找到后，再查找其父辈元 素中是否有p元素，再判断p的父元素中是否有id为divBox的div元素，如果都存在则匹配上。
    浏览器从右到左进行查找的好处是为了尽早过滤掉一些无关的样式规则和元素。比如如下html和css:
    <style> 
        DIV#divBox p span.red{color:red;}  
    <style> 
    <body> 
        <div id="divBox"> 
            <p><span>s1</span></p> 
            <p><span>s2</span></p> 
            <p><span>s3</span></p> 
            <p><span class='red'>s4</span></p> 
        </div> 
    </body> 
    如果按从左到右查找，哪会先查找到很多不相关的p和span元素。
    而如果按从左到右的方式进行查找，则首先就查找到<span class='red'>的元素。
    firefox称这种查找方式为key selector(关键字查询)，所谓的关键字就是样式规则中最后(最右边)的规则，上面的key就是span.red。


===<简洁、高效的CSS>===
    所谓高效的CSS就是让浏览器在查找style匹配的元素的时候尽量进行少的查找，下面列出一些我们常见的写CSS犯一些低效错误: 
    ◆不要在ID选择器前使用标签名
    一般写法: DIV#divBox
    更好写法: #divBox
    解释:  因为ID选择器是唯一的，加上div反而增加不必要的匹配。
    ◆不要再class选择器前使用标签名
    一般写法: span.red
    更好写法: .red
    解释: 同第一条，但如果你定义了多个.red，而且在不同的元素下是样式不一样，则不能去掉，比如你css文件中定义如下: 
    p.red{color:red;}  
    span.red{color:#ff00ff} 
    如果是这样定义的就不要去掉，去掉后就会混淆，不过建议最好不要这样写
    ◆尽量少使用层级关系
    一般写法: #divBox p .red{color:red;}
    更好写法: .red{..}
    ◆使用class代替层级关系
    一般写法: #divBox ul li a{display:block;}
    更好写法: .block{display:block;}
#endregion

#region CSS3选择器
    /** :nth-of-type(n) 定义和用法
        :nth-of-type(n) 选择器匹配属于父元素的特定类型的第 N 个子元素的每个元素.
        n 可以是数字、关键词或公式。
        */
        // 规定属于其父元素的第二个 p 元素的每个 p: (指定 "数字" 实例)
        p:nth-of-type(2) {
            background:#ff0000;
        }
        // Odd 和 even 是可用于匹配下标是奇数或偶数的子元素的关键词（第一个子元素的下标是 1）。在这里，我们为奇数和偶数 p 元素指定两种不同的背景色: (指定 "关键词" 实例)
        p:nth-of-type(odd) {
            background:#ff0000;
        }
        p:nth-of-type(even) {
            background:#0000ff;
        }
        // 使用公式 (an + b)。描述: 表示周期的长度，n 是计数器（从 0 开始），b 是偏移值。在这里，我们指定了下标是 3 的倍数的所有 p 元素的背景色:  (指定 "公式" 实例)
        p:nth-of-type(3n+0) {
            background:#ff0000;
        }
#endregion

#region 边框（border）
        color           边框粗细颜色
        width           边框粗细
        style           边框样式
    实例: border:2px black solid;
        一个值: 四个方向都是其值
        二个值: 前者表示上下方向的值，后者表示左右方向的值
        三个值: 前者表示上方向的值，中间表示左右方向的值，后面表示下方向的值
        四个值: 依次为上、右、下、左方向的值，即顺时针排序赋值
    
    // 为"盒子"设置添加圆角
    /*圆形*/
    -moz-border-radius: 50%;
    -webkit-border-radius: 50%;
    border-radius: 50%;
        
    // 为"盒子"设置阴影(不会对位置和宽高度差生影响,但要注意父级的override:hidden;)
    -moz-box-shadow: 10px 10px 5px #888888; /* 老的 Firefox */
    box-shadow: 10px 10px 5px #888888;
    (text-shadow: 水平阴影 垂直阴影 模糊距离 阴影颜色)
    (原则是:  x轴位置顶左边  y轴位置顶上边  阴影模糊程度  阴影颜色)
    
    // 为"盒子"设置使用图片来设置边框
    -moz-border-image:url(/i/border.png) 30 30 round;   /* Old Firefox */
    -webkit-border-image:url(/i/border.png) 30 30 round;    /* Safari and Chrome */
    -o-border-image:url(/i/border.png) 30 30 round;     /* Opera */
    border-image:url(/i/border.png) 30 30 round;
    #region border-image的具体描述
        值                           描述
        border-image-source         用在边框的图片的路径。 
        border-image-slice          图片边框向内偏移。   
        border-image-width          图片边框的宽度。    
        border-image-outset         边框图像区域超出边框的量。   
        border-image-repeat         图像边框是否应平铺(repeated)、铺满(round)或拉伸(stretch)。
        
        border-image:url(/i/border.png) 30 30 round;
        (边框图片: 图片路径  *待查找*  *待查找*  重复的样式(repeat))
    #endregion

    #region 圆角框
        1、固定宽度的圆角框的区域
            内容有标题和<p>标记的段落内容
            方法: 两个背景图片
                一个用在区域<div>的下面，可以从左下角开始铺设
                另一个用在最顶端的<h？>的背景图片中，从左上铺设就可以了
                中间的内容可以在<div>的背景颜色中实现
                    如果在圆角框的内容中，还有边框存在的话也可以使用别的方法，案例有
                最后设置各个元素的margin和padding就完成了
                重点在于制作的背景图片，内容的颜色是圆角框的颜色，而圆角则是页面背景图片的颜色
                案例: 第11章\01\
        2、不同宽度的圆角框
        **************************************************************************************************************************************
            对于宽度“不固定”的说法: 
            1、可变: 
                含义: 这个圆角框本身在网页上的宽度是固定的，
                但是在制作网页的时候，只要简单地设定该圆角框的宽度，
                就能产生正确的效果，而不必重新制作背景图片。
                这样如果一个网页上有3种宽度的圆角框，仅适用一套背景图像就都可以完成了。
                
                实际上对于网页的访问者来说就是固定宽度，使用绝对单位（例如像素）来设置宽度
            2、流动: 
                含义: 圆角框的宽度是跟随浏览器窗口宽度的变化而变化。
                例如标准流方式的div的宽度就是自动横向伸展的，它的宽度就会随时改变。
                
                使用百分比或者auto来设置宽度
            3、弹性: 
                含义: 圆角框的宽度在文字大小不变的情况下，宽度不变，
                而文字大小发生变化的时候，宽度随之改变。
                这里说的文字大小的变化是通过浏览器菜单中的“查看-->文字大小”命令来改变的。
                
                使用相对单位(例如em)来设置宽度。
            
            利用这3种不同的具体方式来设计“不固定”宽度的圆角框的原理都是一样的，只是在具体处理时对宽度设置方法有所不同。
            注意: 文字的行字数: 
                使用流动方式时，要确保不要使文本的一行过长，这样会影响访问者的阅读体验。
                一本16开图书，就像这本《CSS设计彻底研究》，一行的字数时40个字，这是很合适的一个行跨度。
                如果一行很长，读完以后，回到最左端的时候，可能会找不到下一行的位置，这无疑会使访问者的感受很不好。
        **************************************************************************************************************************************
        单色不固定宽度圆角框
            1、“4图像”（也有4图像滑动门P285）
            基本思路: （需要准备4个图像，分别是4个圆角框的圆角像素）
            整体背景色用div的背景设置，然后4个图像分别作为某一个元素的背景，放到适当的位置。
            问题:  在上节的HTML代码中，只用到了3个元素，即div，h3，p。
                    因此，必须要在HTML中增加一个冗余的标记
                        例如:  为标题增加一个a标记，连接到详细页面，
                                或者在div外面套一层div，
                                或者在p标记里面套一层span。
                        实例: 第11章\01\unfixe-dwidth.htm
            2、“5图像”二维滑动门经典圆角框
            基本思路: 
            (1)首先在Photoshop或者Fireworks中绘制一个大约800*600的圆角矩形
                具体的样式和大小可以自己决定，最终完成的圆角框大小不能超过这个大小，如果超过，就会出现裂缝，因此如果需要很大的圆角框，这个图就要做得再大一些。
            (2)在Photoshop或者Fireworks中进行切片，一共产生5个图像文件
                5个图像分别是
                left-top        right-top
                                    right
                left-bottom     right-bottom
                实际中以left-top为主，其他4个都是为其填充边角用
                实例: 第11章\03step-1.htm
    #endregion

    // box-sizing (用于设置边框的表现形式) 属性允许您以特定的方式定义匹配某个区域的特定元素。
    -moz-box-sizing:border-box; /* Firefox */
    -webkit-box-sizing:border-box; /* Safari */
    box-sizing:border-box;
    #region box-sizing (用于设置边框的表现形式) 属性允许您以特定的方式定义匹配某个区域的特定元素。
    定义和用法:
        box-sizing 属性允许您以特定的方式定义匹配某个区域的特定元素。
        例如，假如您需要并排放置两个带边框的框，可通过将 box-sizing 设置为 "border-box"。这可令浏览器呈现出带有指定宽度和高度的框，并把边框和内边距放入框中。
    
    语法:
        box-sizing: content-box|border-box|inherit;

    值                       描述
    content-box             这是由 CSS2.1 规定的宽度高度行为。
                            宽度和高度分别应用到元素的内容框。
                            在宽度和高度之外绘制元素的内边距和边框。

    border-box              为元素设定的宽度和高度决定了元素的边框盒。
                            就是说，为元素指定的任何内边距和边框都将在已设定的宽度和高度内进行绘制。
                            通过从已设定的宽度和高度分别减去边框和内边距才能得到内容的宽度和高度。
                            
    inherit                 规定应从父元素继承 box-sizing 属性的值。
    #endregion
    
#endregion

#region CSS3背景 (background)
    
    // 背景大小(图片)
    background-size: 100%;
    background-size: 64px 100px;
    
    // 属性规定背景图片的定位区域
    background-origin: content-box; // 定位在内容区域
    background-origin: padding-box; // 定位在内边距区域
    background-origin: border-box; // 定位在边框区域(以内,和padding-box的效果差不多)
    
    // CSS3还允许为元素设置两幅或多幅背景图片
    background-image: url("1.jpg"),url("2.jpg");
    
    // 制定规定背景的绘制区域
    background-clip:content-box; // 仅绘制元素内部内容区域
    background-clip:padding-box; // 从内边距的范围内所有区域进行绘制
    background-clip:border-box; // 从边框内部就开始绘制 默认为border-box
	
	// 背景混合模式, 用于将图片和背景颜色进行混合
	background-blend-mode: difference;
    
#endregion

#region 内边距（padding）
        表示“盒子”里的边框和内容之间的距离
        padding-top     上内边距
        padding-left    左内边距
        padding-right   右内边距
        padding-bottom  下内边距
    实例: padding:5px;
        一个值: 四个方向都是其值
        二个值: 前者表示上下方向的值，后者表示左右方向的值
        三个值: 前者表示上方向的值，中间表示左右方向的值，后面表示下方向的值
        四个值: 依次为上、右、下、左方向的值，即顺时针排序赋值
#endregion

#region 外边距（margin）
        表示盒子和盒子之间的距离
        margin-top      上外边距
        margin-left     左外边距
        margin-right    右外边距
        margin-bottom   下外边距
    实例: margin:10px;
        一个值: 四个方向都是其值
        二个值: 前者表示上下方向的值，后者表示左右方向的值
        三个值: 前者表示上方向的值，中间表示左右方向的值，后面表示下方向的值
        四个值: 依次为上、右、下、左方向的值，即顺时针排序赋值
#endregion

#region 盒子属性 (display)
    定义和用法:
        display 属性规定元素应该生成的框的类型。
    说明
        这个属性用于定义建立布局时元素生成的显示框类型。对于 HTML 等文档类型，如果使用 display 不谨慎会很危险，因为可能违反 HTML 中已经定义的显示层次结构。对于 XML，由于 XML 没有内置的这种层次结构，所有 display 是绝对必要的。
    属性内容: 
        none                此元素不会被显示。
        block               此元素将显示为块级元素，此元素前后会带有换行符。
        inline              默认。此元素会被显示为内联元素，元素前后没有换行符。
        inline-block        行内块元素。（CSS2.1 新增的值）
        list-item           此元素会作为列表显示。
        run-in              此元素会根据上下文作为块级元素或内联元素显示。
        compact             CSS 中有值 compact，不过由于缺乏广泛支持，已经从 CSS2.1 中删除。
        marker              CSS 中有值 marker，不过由于缺乏广泛支持，已经从 CSS2.1 中删除。
        table               此元素会作为块级表格来显示（类似 <table>），表格前后带有换行符。
        inline-table        此元素会作为内联表格来显示（类似 <table>），表格前后没有换行符。
        table-row-group     此元素会作为一个或多个行的分组来显示（类似 <tbody>）。
        table-header-group  此元素会作为一个或多个行的分组来显示（类似 <thead>）。
        table-footer-group  此元素会作为一个或多个行的分组来显示（类似 <tfoot>）。
        table-row           此元素会作为一个表格行显示（类似 <tr>）。
        table-column-group  此元素会作为一个或多个列的分组来显示（类似 <colgroup>）。
        table-column        此元素会作为一个单元格列显示（类似 <col>）
        table-cell          此元素会作为一个表格单元格显示（类似 <td> 和 <th>）
        table-caption       此元素会作为一个表格标题显示（类似 <caption>）
        inherit             规定应该从父元素继承 display 属性的值。
        
        box                 弹性布局盒子的属性,下面具体模块讲述 (2009 年发布的老版本,做兼容时用)
        flex                弹性布局盒子的属性,下面具体模块讲述 (2012 年发布的确定版)
        
#endregion

#region 弹性布局 (display: flex;)
    参考技术文章: 
        // Flex 布局教程: 语法篇 (阮一峰老师)
        http://www.ruanyifeng.com/blog/2015/07/flex-grammar.html
        // Flex 布局教程: 实例篇 (阮一峰老师)
        http://www.ruanyifeng.com/blog/2015/07/flex-examples.html
        // 国外flex布局实例
        https://hufan-akari.github.io/solved-by-flexbox/
        
    一、Flex布局是什么？
        Flex是Flexible Box的缩写，意为"弹性布局"，用来为盒状模型提供最大的灵活性。
        
        任何一个容器都可以指定为Flex布局。
        .box{ display: flex; }

        行内元素也可以使用Flex布局。
        .box{ display: inline-flex; }

        Webkit内核的浏览器，必须加上-webkit前缀。
        .box { display: -webkit-flex; /* Safari */ display: flex; }
        注意，设为Flex布局以后，子元素的float、clear和vertical-align属性将失效。
        
        完整属性兼容代码:
        .box { display: -webkit-box; display: -webkit-flex; display: -ms-flexbox; display: flex; }
        
    二、基本概念
        采用Flex布局的元素，称为Flex容器（flex container），简称"容器"。它的所有子元素自动成为容器成员，称为Flex项目（flex item），简称"项目"。
        
        容器默认存在两根轴: 水平的主轴（main axis）和垂直的交叉轴（cross axis）。
        主轴的开始位置（与边框的交叉点）叫做(main start)，结束位置叫做(main end)；交叉轴的开始位置叫做(cross start)，结束位置叫做(cross end)。
        
        项目默认沿主轴排列。单个项目占据的主轴空间叫做(main size)，占据的交叉轴空间叫做(cross size)。
    
    三、容器的属性
        以下6个属性设置在容器上。
            flex-direction      { // 属性决定主轴的方向（即项目的排列方向）。
                .box {
                    flex-direction: row | row-reverse | column | column-reverse;
                }
                展示图片地址: http://www.ruanyifeng.com/blogimg/asset/2015/bg2015071005.png
                    row（默认值）:       主轴为水平方向，起点在左端。
                    row-reverse:         主轴为水平方向，起点在右端。
                    column:              主轴为垂直方向，起点在上沿。
                    column-reverse:      主轴为垂直方向，起点在下沿。
            }
            flex-wrap           { // 默认情况下，项目都排在一条线（又称"轴线"）上。flex-wrap属性定义，如果一条轴线排不下，如何换行。
                .box{
                    flex-wrap: nowrap | wrap | wrap-reverse;
                }
                展示图片地址: http://www.ruanyifeng.com/blogimg/asset/2015/bg2015071006.png
                它可能取三个值。
                    nowrap（默认）:      不换行。
                    wrap:                换行，第一行在上方。
                    wrap-reverse:        换行，第一行在下方。
            }
            flex-flow           { // 属性是flex-direction属性和flex-wrap属性的简写形式，默认值为row nowrap。
                .box {
                    flex-flow: <flex-direction> || <flex-wrap>;
                }
            }
            justify-content     { // 属性定义了项目在主轴上的对齐方式。
                .box {
                  justify-content: flex-start | flex-end | center | space-between | space-around;
                }
                展示图片地址: http://www.ruanyifeng.com/blogimg/asset/2015/bg2015071010.png
                它可能取5个值，具体对齐方式与轴的方向有关。下面假设主轴为从左到右。
                    flex-start（默认值）:    左对齐
                    flex-end:                右对齐
                    center:                  居中
                    space-between:           两端对齐，项目之间的间隔都相等。
                    space-around:            每个项目两侧的间隔相等。所以，项目之间的间隔比项目与边框的间隔大一倍。
            }
            align-items         { // 属性定义了项目在交叉轴上的对齐方式。
                .box {
                    align-items: flex-start | flex-end | center | baseline | stretch;
                }
                展示图片地址: http://www.ruanyifeng.com/blogimg/asset/2015/bg2015071011.png
                它可能取5个值。具体的对齐方式与交叉轴的方向有关，下面假设交叉轴从上到下。
                    flex-start:              交叉轴的起点对齐。
                    flex-end:                交叉轴的终点对齐。
                    center:                  交叉轴的中点对齐。
                    baseline:                项目的第一行文字的基线对齐。
                    stretch（默认值）:       如果项目未设置高度或设为auto，将占满整个容器的高度。
            }
            align-content       { // 属性定义了多根轴线的对齐方式。如果项目只有一根轴线，该属性不起作用。
                .box {
                    align-content: flex-start | flex-end | center | space-between | space-around | stretch;
                }
                展示图片地址: http://www.ruanyifeng.com/blogimg/asset/2015/bg2015071012.png
                该属性可能取6个值。
                    flex-start:          与交叉轴的起点对齐。
                    flex-end:            与交叉轴的终点对齐。
                    center:              与交叉轴的中点对齐。
                    space-between:       与交叉轴两端对齐，轴线之间的间隔平均分布。
                    space-around:        每根轴线两侧的间隔都相等。所以，轴线之间的间隔比轴线与边框的间隔大一倍。
                    stretch（默认值）:   轴线占满整个交叉轴。
            }
    四、项目的属性
        以下6个属性设置在项目上。
            order               { // 属性定义项目的排列顺序。数值越小，排列越靠前，默认为0。
                .item {
                    order: <integer>;
                }
                展示图片地址: 
            }
            flex-grow           { // 属性定义项目的放大比例，默认为0，即如果存在剩余空间，也不放大。
                .item {
                    flex-grow: <number>; /* default 0 */
                }
                展示图片地址: http://www.ruanyifeng.com/blogimg/asset/2015/bg2015071013.png
                如果所有项目的 flex-grow 属性都为1，则它们将等分剩余空间（如果有的话）。
                如果一个项目的 flex-grow 属性为2，其他项目都为1，则前者占据的剩余空间将比其他项多一倍。
            }
            flex-shrink         { // 属性定义了项目的缩小比例，默认为1，即如果空间不足，该项目将缩小。
                .item {
                    flex-shrink: <number>; /* default 1 */
                }
                展示图片地址: http://www.ruanyifeng.com/blogimg/asset/2015/bg2015071015.jpg

                如果所有项目的 flex-shrink 属性都为1，当空间不足时，都将等比例缩小。
                如果一个项目的 flex-shrink 属性为0，其他项目都为1，则空间不足时，前者不缩小。
                负值对该属性无效。
            }
            flex-basis          { // 属性定义了在分配多余空间之前，项目占据的主轴空间（main size）。浏览器根据这个属性，计算主轴是否有多余空间。它的默认值为auto，即项目的本来大小。
                .item {
                    flex-basis: <length> | auto; /* default auto */
                }
                它可以设为跟width或height属性一样的值（比如350px），则项目将占据固定空间。
            }
            flex                { // 属性是flex-grow, flex-shrink 和 flex-basis的简写，默认值为0 1 auto。后两个属性可选。
                .item {
                    flex: none | [ <'flex-grow'> <'flex-shrink'>? || <'flex-basis'> ]
                }
                该属性有两个快捷值: auto (1 1 auto) 和 none (0 0 auto)。
                建议优先使用这个属性，而不是单独写三个分离的属性，因为浏览器会推算相关值。
            }
            align-self          { // 属性允许单个项目有与其他项目不一样的对齐方式，可覆盖 align-items 属性。默认值为auto，表示继承父元素的 align-items 属性，如果没有父元素，则等同于stretch。
                .item {
                    align-self: auto | flex-start | flex-end | center | baseline | stretch;
                }
                展示图片地址: http://www.ruanyifeng.com/blogimg/asset/2015/bg2015071016.png
                该属性可能取6个值，除了auto，其他都与align-items属性完全一致。
            }
#endregion

#region 浮动（float）★
    float:left;     向左浮动
    float:right;    向右浮动
    
    与浮动配套使用的有: 
    清除浮动的影响（clear）
    clear:left;     清除左边浮动所产生的环绕之类的效果
    clear:right;    ----右边----
#endregion

#region 定位（position）★
    position:static;        静态定位，默认的属性值，是盒子按照标准流（包括浮动方式）进行布局
    position:relative;      相对定位，就是在原有标准流的基础上偏移指定的距离，相对定位的盒子依然在标准流中，其他的盒子仍以标准流的方式对待它
    position:absolute;      绝对定位，盒子的位置以它的包含框为基准进行偏移。绝对定位的盒子从标准流中脱离，可以当
    position:fixed;         固定定位，与绝对定位类似，只是一浏览器窗口为基准进行定位，也就是当拖动浏览器的滚动条时，依然保持对象位置不变
    
    当设置了定位position之后，便可设置各个盒子之间的重叠高低关系: 
    z-index:1;
    默认的值为0，当两个块的z-index值一样时，将保持原有的高低覆盖关系
#endregion

#region 小知识★
    1、display
        对于盒子来说，有两种类型: “块级元素”和“行内元素”
        典型的有
            <div>块级元素
            <span>行内元素
        可以通过display属性用于更改和确定元素的类型
            display:inline;         行内元素
            display:block;          块级元素
            display:none;           没有元素类型，便“消失”（隐藏）
    2、长度单位
        em      相对于父元素的字体大小
        ex      相对于小写字母"x"的高度
        gd      一般用在东亚字体排版上，这个与英文并无关系
        rem     相对于根元素字体大小
        vw      相对于视窗的宽度: 视窗宽度是100vw
        vh      相对于视窗的高度: 视窗高度是100vh
        vm      相对于视窗的宽度或高度，取决于哪个更小
        ch      相对于0尺寸
        px      相对于屏幕分辨率而不是视窗大小: 通常为1个点或1/72英寸 像素 1px=0.75pt
        in      inch, 表英寸   in0ch,英寸 1in=2.54cm
        cm      centimeter, 表厘米  centimeter,厘米
        mm      millimeter, 表毫米  millimeter,毫米
        pt      1/72英寸  point,1pt=1in的1/72
        pc      12点活字，或1/12点  pica,1pc=12pt
        %       相对于父元素。正常情况下是通过属性定义自身或其他元素  表示百分比（一般是以“父类”为基准）

        Css3 calc(): 动态计算内容单位方法:
            calc()使用通用的数学运算规则，但是也提供更智能的功能: 
                使用“+”、“-”、“*” 和 “/”四则运算；
                可以使用百分比、px、em、rem等单位；
                可以混合使用各种单位进行计算；
                表达式中有“+”和“-”时，其前后必须要有空格，如"widht: calc(12%+5em)"这种没有空格的写法是错误的；
                表达式中有“*”和“/”时，其前后可以没有空格，但建议留有空格。
            
            如: width: calc(50% - 10px);
            兼容使用:
            .box {
                /*Firefox*/
                width: -moz-calc(50% - 10px);
                /*chrome safari*/
                width: -webkit-calc(50% - 10px);
                /*Standard */
                width: calc(50% - 10px);
            }
    3、时间、频率、角度
        deg     degrees, 角度
        grad    grads, 百分度 100gads相当于90deg。
        rad     radians, 弧度 1.570796326794897rad相当于100gads或是90deg
        turn    turns, 圈数 1turn = 360deg
        ms      milliseconds, 毫秒数
        s       seconds, 秒数
        Hz      Hertz, 赫兹
        kHz     kilohertz, 千赫
    4、圆角框
        /*备选方式，以免在不同的浏览器显示的效果不一样*/
        -moz-border-radius: 15px;   
        border-radius: 15px;
    5、元素的优先级: 越小的显示的优先级越高
    
    /*IE滤镜，透明度50%*/
    filter:alpha(opacity=70);
    -moz-opacity:0.7;
    opacity:0.7;
    
    // text-indent: 1em ! important;
    #region // !important 应用实例:
    !important是CSS1就定义的语法，作用是提高指定样式规则的应用优先权。语法格式{ cssRule !important }，即写在定义的最后面，例如: box{color:red !important;}
    在CSS中，通过对某一样式声明! important ，可以更改默认的CSS样式优先级规则，使该条样式属性声明具有最高优先级，也就是相当于写在最下面。
    
    CSS企图创造一个平衡作者和用户之间的级层样式表。
    默认情况下,CSS规则按级层覆盖，例如在.CSS文件中的定义可以被html文件中<style type="text/css"></style>里的定义覆盖，反之不行；书写在下面的定义可以覆盖写在上面的定义，反之不行。
    然而,对覆盖平衡而言,加上一个“!important”就优先于正常的CSS规则。
    
    例子: // 以下这里例子 如依次顺序书写 最后div 的样式为 display:block;
    div {
        display:block!important;
    }
    div {
        display:inline-block;
    }
    div {
        display:none;
    }
    #endregion
    
    // visibility:hidden;
    #region visibility 属性规定元素是否可见。
        h1.visible {visibility:visible}
        h1.invisible {visibility:hidden}
    #endregion
    
    border: 1px solid transparent; //边框色为透明
    
#endregion

#region 基本字段
    
    color:#000000;
    在color之前没有任何元素时，表示当前盒子的所有的颜色为此值
    
    width:2px;
    表示宽度
    
    height:6px;
    表示高度
    
    text-align:center;
    表示元素中的文本对齐方式
    
    vertical-align:center
    表示垂直对齐
    
    background
    表示背景
    
    line-height:33px;
    表示行高
    
    overflow:hidden;
    防止溢出(将溢出的内容全部隐藏起来)
#endregion

#region CSS3文本效果 ( text word )

    // 用于设置文本字体的阴影效果
    text-shadow: 5px 5px 5px #FF0000;
    (text-shadow: 水平阴影 垂直阴影 模糊距离 阴影颜色)
    (原则是:  x轴位置顶左边  y轴位置顶上边  阴影模糊程度  阴影颜色)
    
    // 允许对长的不可分割的单词进行分割并换行到下一行。
    // 属性允许您允许文本强制文本进行换行-即使这意味着会对单词进行拆分
    word-wrap (值)                   描述
    word-wrap: normal;              只在允许的断字点换行(浏览器保持默认处理)
    word-wrap: break-word;          在长单词或URL地址内容进行换行
    
    // 规定非中日韩文本的换行规则。
    // 在恰当的断字点进行换行  word-break 属性规定自动换行的处理方法
    word-break (值)                  描述
    word-break: normal;             使用浏览器默认的换行规则
    word-break: break-all;          允许在单词内换行
    word-break: keep-all;           只能在半角空格或连字符处换行
    
    // 属性规定当文本溢出包含元素时发生的事情
    text-overflow (值)               描述   一般这个属性要和 overflow:hidden; white-space: nowrap; 搭配使用
    text-overflow: clip;            修剪文本
    text-overflow: ellipsis;        显示省略符号来代表被修剪的文本
    text-overflow: "string";        使用给定的字符串来代表被修剪的文本
    text-overflow: inherit;         继承父级(默认不进行处理)
    
    // 属性设置如何处理元素内的空白 这个属性声明建立布局过程中如何处理元素中的空白符。值 pre-wrap 和 pre-line 是 CSS 2.1 中新增的。
    white-space (值)                 描述
    white-space: normal;            默认。空白会被浏览器忽略。
    white-space: pre;               空白会被浏览器保留。其行为方式类似 HTML 中的 <pre> 标签。
    white-space: nowrap;            文本不会换行，文本会在在同一行上继续，直到遇到 <br> 标签为止。
    white-space: pre-wrap;          保留空白符序列，但是正常地进行换行。
    white-space: pre-line;          合并空白符序列，但是保留换行符。
    white-space: inherit;           规定应该从父元素继承 white-space 属性的值。


#endregion

#region 字体（font）
    font-family:Arial;                      字体样式（太多，不一一列举了）
    font-size:20px;                     字体大小
    
    // 字体加粗
    font-weight:normal; 正常
               :bold;   加粗
    
    // 字体倾斜
    font-style:none;    正常          
              :italic;  意大利体（但不是倾斜，有效果而已）
              :oblique; 倾斜
    
    // 字体大写与小写
    font-transform:capitalize;          首字母大写，其余小写
                  :uppercase;           全部大写
                  :lowercase;           全部小写
    
    // 字体装饰效果
    text-decoration:underline;          下划线
                   :overline;           顶划线
                   :line-through;       删除线
                   :blink;              闪烁
    text-decoration:underline overline line-through /*三种共用*/
    
    // 字体的首行缩进
    text-indent:2em                     首行缩进
	
	// 段落中的字间距是 25 像素：
	word-spacing:25px;
	
	// 文字间距 2 像素
	letter-spacing:2px
    
#endregion

#region @font-face 引用web服务器字体
    /** @font-face 备注注释:
        在CSS3之前,web设计师必须使用已在用户计算机上安装好的字体
        通过CSS3,web设计师可以使用它们喜欢的任意字体
        当您找到活购买到希望使用的字体时,可将该字体文件存放到web服务器上,它会在需要时被自动下载到用户的计算机上
        您"自己的"的字体是在CSS3 @font-face 规则中定义的:
        
        Firefox、Chrome、Safari 以及 Opera 支持 .ttf (True Type Fonts) 和 .otf (OpenType Fonts) 类型的字体。
        Internet Explorer 9+ 支持新的 @font-face 规则，但是仅支持 .eot 类型的字体 (Embedded OpenType)。
        注释: Internet Explorer 8 以及更早的版本不支持新的 @font-face 规则。
        
        使用您需要的字体:
        在新的 @font-face 规则中,您必须首先定义字体的名称(比如myFirstFont),然后指向改字体文件
        如需为HTML元素使用字体,请通过font-family 属性来引用字体的名称(myFirstFont);
    */

    <style> // 定义 @font-face 规则
        @font-face {
            font-family: myFirstFont;
            src:url('Sansation_Light.ttf'),
                url('Sansation_Light.eot'); /* IE9+ */
        }
        
        @font-face {
            // 当使用这种粗体字体的时候,您必须为粗体文本添加另一个包含描述符的@font-face
            // 文件 "Sansation_Bold.ttf" 是另一个字体文件，它包含了 Sansation 字体的粗体字符。
            // 只要 font-family 为 "myFirstFont" 的文本需要显示为粗体，浏览器就会使用该字体。
            // 通过这种方式，我们可以为相同的字体设置许多 @font-face 规则。
            font-family: myFirstFont;
            src: url('Sansation_Bold.ttf'),
                 url('Sansation_Bold.eot'); /* IE9+ */
            font-weight:bold;
        }
    </style>

    div { // 在CSS中使用 @font-face 规则
        font-family:myFirstFont;
        
        // font-weight: bold;
    }

    // 下面列出一些能够在 @font-face 规则中定义的所有字体描述符:
    描述符                     值                       描述
    font-family                 name                    必需,规定字体的名称,用来在css具体的样式中引用
    src                         url                     必需,定义字体文件的URL地址
    font-stretch                normal                  可选,定义如何拉伸字体,默认是"normal"
                                condensed
                                ultra-condensed
                                extra-condensed
                                semi-condensed
                                expanded
                                semi-expanded
                                extra-expanded
                                ultra-expanded
    font-style                  normal                  可选,定义字体的样式,默认是"normal"
                                italic                      表示: 斜体
                                oblique                     表示: 倾斜
    font-weight                 normal                  可选,定义字体的粗细 默认是"normal"
                                bold
                                100
                                200
                                300
                                400
                                500
                                600
                                700
                                800
                                900
    unicode-range               unicode-range           可选,定义字体支持的unicode字符范围,默认是"U+0=10FFFF"
#endregion

#region 表格（table）
1、宽度的确定
    CSS提供了两种确定表格以及内部单元格宽度的方式。
    一种与表格内部的内容相关，称为“自动方式”；一种与内容无关，称为“固定方式”
    使用了自动方式时，实际宽度可能并不是“width”属性的设置值，因为它会根据单元格中的内容多少进行调整。
    而在固定方式下，表格的水平布局不依赖于单元格的内容，而明确地由“width”属性制定。
        如果取值为“auto”就意味着使用“自动方式”进行表格的布局。
    
    如果要使用固定方式，就需要对表格设置它的“table-layout”属性。
        将它设置为“fixed”即为固定方式；设置为“auto”时则为自动方式。浏览器默认使用自动方式
2、设置单元格的边框
    当表格中的单元格边框之间需要合并，不需要分离
    作用是使边框使用重合模式，实现相邻单元格之间的边框是重合在一起的
    使用这条语句: 
    border-collapse:collapse;
    放置的位置是表格所在的“选择器”中
3、相邻边框的合并
    每个单元格都可以设置各自的边框颜色、样式和宽度等属性，那么相邻边框在合并时将以谁为准？
    CSS 2 的规范中定义如下: 
    (1) 如果边框的“border-style”设置为“hidden”
        那么它的优先级高于“任何”其他相冲突的边框。
        任何边框只要有该设置，其他的边框的设置就都将无效。
        
    (2) 如果边框的属性中有“none”
        那么它的优先级时最低的。
        只有在该边重合的所有元素的边框属性都是“none”时，该边框才会被省略。
        
    (3) 如果重合的边框中没有被设置为“hidden”的，并且至少有一个不是“none”
        那么重合的边框中粗的优先于细的。
        如果几个边框的“border-width”相同，
        那么样式的优先次序由高到低能一次为: 
        “double”、
            “solid”、
                “dashed”、
                    “dotted”、
                        “ridge”、
                            “outset”、
                                “groove”、
                                    “inset”
    (4) 如果边框样式的其他设置均相同，只是颜色上有区别，
        那么单元格的样式最优先，
            然后依次是行、行组、列、列组的样式，
                最后是表格的样式
4、边框的分离
    在使用HTML属性格式化表格时可以通过使用cellpadding来设置单元格内容和边框之间的距离（相当于盒子的padding）
    以及使用cellpadding设置相邻单元格边框之间的距离。要用CSS实现cellpadding的作用，可以直接对td使用padding就可以
    但是，要用CSS实现cellspacing的作用时（相当于盒子的margin），对单元格使用margin时无效的
    需要对table使用另一个专门的属性“border-spacing”来代替它。
    位置放在表格的“选择器”属性中
        注意: 在IE6和IE7中都不支持这个属性，所以还是用通过cellpadding和cellspacing来控制
5、单元格的scope属性
    定义和用法
        scope 属性定义将表头单元与数据单元相关联的方法。
        scope 属性标识某个单元是否是列、行、列组或行组的表头。
        scope 属性不会在普通浏览器中产生任何视觉变化。
    屏幕阅读器可以利用该属性。
    详细解释
        使用 scope 属性，可以将数据单元格与表头单元格联系起来。
        通过属性值 row，表头行包括的所有表格都将和表头单元格联系起来。指定 col，会将当前列的所有单元格和表头单元格绑定起来。
        使用 rowgroup 和 colgroup 会将单元格的行组（由 <thead>、<tbody> 或 <tfoot> 标签定义）或列组中的所有单元格和表头单元格绑定起来（由 <col> 或 <colgroup> 标签定义）。
#endregion

#region Tab面板
    网页的Tab面板菜单分为两种: 
    1、本地方式，不需要响应服务器
        切换各个Tab页中的内容时并不刷新浏览器窗口，
        说明各个页中的内容实际装载到页面上，只是被隐藏起来了。
    2、需要响应服务器，相当于一个新的页面。
        切换各个Tab页中的内容时，会刷新浏览器窗口，
        实际上就是更换了一个新的HTML页面
    
    要实现前者的效果，必须通过JavaScript的配合，仅通过CSS来实现是比较困难的，而且实现的功能非常有限。
    
    实际上，也有一些网站使用Ajax技术，可以实现切换到某一页之后，在动态地从服务器上获取数据，
        局部刷新Tab页内的区域，而整个页面的其他部分则不需要重新从服务器获取数据。
    
    思路是: 
        先做一个菜单，用来“选择”
        在做内容框架，设置里面的样式。
            如果是动态地话，选择从服务器动态获取内容就行了。
            静态的就设置隐藏和显示。
#endregion

#region HTML标记
    <div></div>                     容器标记，块级元素（它包含的原色会自动换行）
    <span></span>                   容器标记，行内元素（它的前后不会换行）
    <a></a>                         链接标记，用于超链接
    
    <ul></ul>                       列表框标记，用于放置<li>标记
    <li></li>                       列表标记，用于列出内容
    
    <dl></dl>                       定义列表，用法类似于ul,li，主要相当于<ul>
    <dt></dt>                       定义标题，主要相当于<li>
    <dd></dd>                       定义描述，主要相当于<li>
    例如: <dl>
            <dt>北京市的大学</dt>
                <dd>清华大学</dd>
                <dd>北京大学</dd>
                <dd>人民大学</dd>
            <dt>上海市的大学</dt>
                <dd>复旦大学</dd>
                <dd>同济大学</dd>
                <dd>上海大学</dd>
            <dt>南京市的大学</dt>
                <dd>南京大学</dd>
                <dd>东南大学</dd>
        </dl>
    
    <table></table>                 表格
        <caption></caption>         表格外部标题
        <col></col>                 每一对这个标记对应于表格中的一列，一般全部放置在<thead>标记的上面，主要用于单独设置一列
        <thead></thead>             表格内容的标题部分
        <tbody></tbody>             表格内容的正文
        <tfoot></tfoot>             表格内容的结束部分
            <tr></tr>               表格行标记
            <th></th>               表格的“表头”，在表格中主要用于行或者列的名称，行和列都可以使用各自的名称
            <td></td>               表格单元格
#endregion

#region CSS3 转换 (transform) ★

    /** transform 了解:
        通过CSS3转换,我们能够对元素进行移动、缩放、转动、拉长、拉伸
        
        转换是使元素改变形状、尺寸、位置的一种效果
        
        浏览器支持:
        Internet Explorer 10、Firefox 以及 Opera 支持 transform 属性。
        Chrome 和 Safari 需要前缀 -webkit-。
        注释: Internet Explorer 9 需要前缀 -ms-。
        
        浏览器支持:
        Internet Explorer 10 和 Firefox 支持 3D 转换。
        Chrome 和 Safari 需要前缀 -webkit-。
        Opera 仍然不支持 3D 转换（它只支持 2D 转换）。
    */
    
    #region 所有转换属性:
    属性                          描述
    transform                   { //向元素应用 2D 或 3D 转换。
    }
    transform-origin            { //允许你改变被转换元素的位置。
        transform-origin: 50% 50% 0; (/*默认值*/) { // 属性允许您改变被转换元素的位置
            /** 定义和用法
                transform-origin 属性允许您改变被转换元素的位置。
                2D 转换元素能够改变元素 x 和 y 轴。3D 转换元素还能改变其 Z 轴。
                
                注释: 该属性必须与 transform 属性一同使用。
            */
            // 语法:
            transform-origin: x-axis y-axis z-axis;
            
            值                   描述
            x-axis              定义视图被置于 X 轴的何处。可能的值: 
                                left
                                center
                                right
                                length
                                %
            y-axis              定义视图被置于 Y 轴的何处。可能的值: 
                                top
                                center
                                bottom
                                length
                                %
            z-axis              定义视图被置于 Z 轴的何处。可能的值: 
                                length
        }
    }
    transform-style             { //规定被嵌套元素如何在 3D 空间中显示。
        
        // Firefox 支持 transform-style 属性。
        // Chrome、Safari 和 Opera 支持替代的 -webkit-transform-style 属性。
        
        (实例代码:) { // 使被转换的子元素保留其3D转换
            -webkit-transform: rotateY(60deg);  /* Safari 和 Chrome */
            -webkit-transform-style: preserve-3d;   /* Safari 和 Chrome */
            transform: rotateY(60deg);
            transform-style: preserve-3d;
        }
        
        /// 用法和定义:
        // transform-style 属性规定如何在 3D 空间中呈现被嵌套的元素。
        // 注释: 该属性必须与 transform 属性一同使用。
        值                               描述
        transform-style: flat           子元素将不保留其 3D 位置。
        transform-style: preserve-3d    子元素将保留其 3D 位置。
    }
    perspective                 { //规定 3D 元素的透视效果。
    }
    perspective-origin          { //规定 3D 元素的底部位置。
    }
    backface-visibility         { //定义元素在不面对屏幕时是否可见。
        
        (实例代码:) {// 隐藏被旋转的 div 元素的背面: 
            -webkit-backface-visibility:hidden; /* Chrome 和 Safari */
            -moz-backface-visibility:hidden;    /* Firefox */
            -ms-backface-visibility:hidden;     /* Internet Explorer */
            backface-visibility:hidden;
        }
        
        /// 浏览器支持
        // 只有 Internet Explorer 10+ 和 Firefox 支持 backface-visibility 属性。
        // Opera 15+、Safari 和 Chrome 支持替代的 -webkit-backface-visibility 属性。
        
        backface-visibility: visible;   // 背面是可见的
        backface-visibility: hidden;    // 背面是不可见的
    }
    #endregion
    
    #region 2D transform 方法
    
    函数                          描述
    matrix(n,n,n,n,n,n)             定义 2D 转换，使用六个值的矩阵。
    translate(x,y)                  定义 2D 转换，沿着 X 和 Y 轴移动元素。
    translateX(n)                   定义 2D 转换，沿着 X 轴移动元素。
    translateY(n)                   定义 2D 转换，沿着 Y 轴移动元素。
    scale(x,y)                      定义 2D 缩放转换，改变元素的宽度和高度。
    scaleX(n)                       定义 2D 缩放转换，改变元素的宽度。
    scaleY(n)                       定义 2D 缩放转换，改变元素的高度。
    rotate(angle)                   定义 2D 旋转，在参数中规定角度。
    skew(x-angle,y-angle)           定义 2D 倾斜转换，沿着 X 和 Y 轴。
    skewX(angle)                    定义 2D 倾斜转换，沿着 X 轴。
    skewY(angle)                    定义 2D 倾斜转换，沿着 Y 轴。
    
    #endregion
    
    #region 3D transform 方法
    
    函数                          描述
    matrix3d(n,n,n,n,n,n,
    n,n,n,n,n,n,n,n,n,n)            定义 3D 转换，使用 16 个值的 4x4 矩阵。
    
    translate3d(x,y,z)              定义 3D 转化。
    translateX(x)                   定义 3D 转化，仅使用用于 X 轴的值。
    translateY(y)                   定义 3D 转化，仅使用用于 Y 轴的值。
    translateZ(z)                   定义 3D 转化，仅使用用于 Z 轴的值。
    scale3d(x,y,z)                  定义 3D 缩放转换。
    scaleX(x)                       定义 3D 缩放转换，通过给定一个 X 轴的值。
    scaleY(y)                       定义 3D 缩放转换，通过给定一个 Y 轴的值。
    scaleZ(z)                       定义 3D 缩放转换，通过给定一个 Z 轴的值。
    rotate3d(x,y,z,angle)           定义 3D 旋转。
    rotateX(angle)                  定义沿 X 轴的 3D 旋转。
    rotateY(angle)                  定义沿 Y 轴的 3D 旋转。
    rotateZ(angle)            
    perspective(n)                  定义 3D 转换元素的透视视图。
    
    #endregion
    
    // 一些具体transform方法的实例:
    transform: translate('x','y') { // 元素从其当前位置移动 
        // 通过 translate() 方法，元素从其当前位置移动，
        // 根据给定的 left（x 坐标） 和 top（y 坐标） 位置参数
        // 移动的基点是: 上 左 边方向:  (允许负值)
        
        -ms-transform: translate(50px,100px);       /* IE 9 */
        -webkit-transform: translate(50px,100px);   /* Safari and Chrome */
        -o-transform: translate(50px,100px);        /* Opera */
        -moz-transform: translate(50px,100px);      /* Firefox */
        transform: translate(50px,100px);
        // 值 translate(50px,100px) 把元素从左侧移动 50 像素，从顶端移动 100 像素。
    }
    transform: rotate('angle') { // 元素顺时针旋转给定的角度
        // 通过 rotate() 方法，元素顺时针旋转给定的角度。允许负值，元素将逆时针旋转。
        // 单位 deg 为角度的意思,使用 rotate() 方法时,必须使用此单位
        
        -ms-transform: rotate(30deg);       /* IE 9 */
        -webkit-transform: rotate(30deg);   /* Safari and Chrome */
        -o-transform: rotate(30deg);        /* Opera */
        -moz-transform: rotate(30deg);      /* Firefox */
        transform: rotate(30deg);
        // 值 rotate(30deg) 把元素顺时针旋转 30 度。
    }
    transform: scale('x','y') { // 元素的尺寸会增加或减少
        // 通过 scale() 方法，元素的尺寸会增加或减少，根据给定的宽度（X 轴）和高度（Y 轴）参数: 
        
        -ms-transform: scale(2,4);  /* IE 9 */
        -webkit-transform: scale(2,4);  /* Safari 和 Chrome */
        -o-transform: scale(2,4);   /* Opera */
        -moz-transform: scale(2,4); /* Firefox */
        transform: scale(2,4);
        // 值 scale(2,4) 把宽度转换为原始尺寸的 2 倍，把高度转换为原始高度的 4 倍。
    }
    transform: skew() { // 元素翻转给定的角度(实际上是可以显示拉伸的效果)
        // 通过 skew() 方法，元素翻转给定的角度，根据给定的水平线（X 轴）和垂直线（Y 轴）参数: 
        
        -ms-transform: skew(30deg,20deg);   /* IE 9 */
        -webkit-transform: skew(30deg,20deg);   /* Safari and Chrome */
        -o-transform: skew(30deg,20deg);    /* Opera */
        -moz-transform: skew(30deg,20deg);  /* Firefox */
        transform: skew(30deg,20deg);
        // 值 skew(30deg,20deg) 围绕 X 轴把元素翻转 30 度，围绕 Y 轴翻转 20 度。
    }
    transform: matrix() { // matrix()方法把所有2D转换方法组合在一起
        // matrix() 方法需要六个参数，包含数学函数，允许您: 旋转、缩放、移动以及倾斜元素。
        
        
        //如何使用 matrix 方法将 div 元素旋转 30 度: 
        -ms-transform:matrix(0.866,0.5,-0.5,0.866,0,0);     /* IE 9 */
        -moz-transform:matrix(0.866,0.5,-0.5,0.866,0,0);    /* Firefox */
        -webkit-transform:matrix(0.866,0.5,-0.5,0.866,0,0); /* Safari and Chrome */
        -o-transform:matrix(0.866,0.5,-0.5,0.866,0,0);      /* Opera */
        transform:matrix(0.866,0.5,-0.5,0.866,0,0);
    }
    
#endregion

#region CSS3 过渡 (transition) ★

    /** CSS3 过渡,了解:
        通过CSS3,我们可以在不使用Flash动画或JavaScript的情况下
        当元素从一种样式变换为另一种样式时为元素添加效果
        
        浏览器支持:
        Internet Explorer 10、Firefox、Chrome 以及 Opera 支持 transition 属性。
        Safari 需要前缀 -webkit-。
        注释: Internet Explorer 9 以及更早的版本，不支持 transition 属性。
        注释: Chrome 25 以及更早的版本，需要前缀 -webkit-。
        
        如何工作?
        CSS3 过渡是元素从一种样式逐渐改变为另一种的效果
        要实现这一点,必须规定两项内容:
        规定您希望把效果添加到哪个CSS属性上
        规定效果的时长
    */

    (实际案例代码:) { // 应用于宽度属性的过渡效果,时长为2秒:
        -moz-transition: width 2s;  /* Firefox 4 */
        -webkit-transition: width 2s;   /* Safari 和 Chrome */
        -o-transition: width 2s;    /* Opera */
        transition: width 2s;
    }
    // 注释: 如果时长为规定,则不会有过渡效果,因为默认值是0
    // 效果开始于指定的CSS属性改变值时,CSS属性改变的典型时间是鼠标指针位于元素上时:
    // 注释: 当指针移出元素时,它会逐渐变回原来的样式
    
    /// 多项改变
    // 如需向多个样式添加过渡效果,请添加多个属性,由逗号隔开:
    (实际案例代码:) { // 向宽度,高度和转换添加过渡效果:
        -moz-transition: width 2s, height 2s, -moz-transform 2s;
        -webkit-transition: width 2s, height 2s, -webkit-transform 2s;
        -o-transition: width 2s, height 2s,-o-transform 2s;
        transition: width 2s, height 2s, transform 2s;
    }
    
    #region 所有的过渡属性
    
    属性                              描述
    transition                      { //简写属性，用于在一个属性中设置四个过渡属性。
    }
    transition-property             { //规定应用过渡的 CSS 属性的名称。
    }
    transition-duration             { //定义过渡效果花费的时间。默认是 0。
    }
    transition-timing-function      { //规定过渡效果的时间曲线。默认是 "ease"。
        
        /// 不同的值:
        值                           描述
        linear                      规定以相同速度开始至结束的过渡效果（等于 cubic-bezier(0,0,1,1)）。
        ease                        规定慢速开始，然后变快，然后慢速结束的过渡效果（cubic-bezier(0.25,0.1,0.25,1)）。
        ease-in                     规定以慢速开始的过渡效果（等于 cubic-bezier(0.42,0,1,1)）。
        ease-out                    规定以慢速结束的过渡效果（等于 cubic-bezier(0,0,0.58,1)）。
        ease-in-out                 规定以慢速开始和结束的过渡效果（等于 cubic-bezier(0.42,0,0.58,1)）。
        cubic-bezier(n,n,n,n)       在 cubic-bezier 函数中定义自己的值。可能的值是 0 至 1 之间的数值。
        
        (实例代码范本:) { // 下面是五个不同值的五个不同的div元素
            #div1 {transition-timing-function: linear;}
            #div2 {transition-timing-function: ease;}
            #div3 {transition-timing-function: ease-in;}
            #div4 {transition-timing-function: ease-out;}
            #div5 {transition-timing-function: ease-in-out;}
            /* Firefox 4: */
            #div1 {-moz-transition-timing-function: linear;}
            #div2 {-moz-transition-timing-function: ease;}
            #div3 {-moz-transition-timing-function: ease-in;}
            #div4 {-moz-transition-timing-function: ease-out;}
            #div5 {-moz-transition-timing-function: ease-in-out;}
            /* Safari and Chrome: */
            #div1 {-webkit-transition-timing-function: linear;}
            #div2 {-webkit-transition-timing-function: ease;}
            #div3 {-webkit-transition-timing-function: ease-in;}
            #div4 {-webkit-transition-timing-function: ease-out;}
            #div5 {-webkit-transition-timing-function: ease-in-out;}
            /* Opera: */
            #div1 {-o-transition-timing-function: linear;}
            #div2 {-o-transition-timing-function: ease;}
            #div3 {-o-transition-timing-function: ease-in;}
            #div4 {-o-transition-timing-function: ease-out;}
            #div5 {-o-transition-timing-function: ease-in-out;}
        }
        
        (实例代码范本:) { // 与上面的效果相同 但通过cubic-bezier来规定速度曲线
            #div1 {transition-timing-function: cubic-bezier(0,0,1,1;}
            #div2 {transition-timing-function: cubic-bezier(0.25,0.1,0.25,1);}
            #div3 {transition-timing-function: cubic-bezier(0.42,0,1,1);}
            #div4 {transition-timing-function: cubic-bezier(0,0,0.58,1);}
            #div5 {transition-timing-function: cubic-bezier(0.42,0,0.58,1);}
            /* Firefox 4: */
            #div1 {-moz-transition-timing-function: cubic-bezier(0,0,0.25,1);}
            #div2 {-moz-transition-timing-function: cubic-bezier(0.25,0.1,0.25,1);}
            #div3 {-moz-transition-timing-function: cubic-bezier(0.42,0,1,1);}
            #div4 {-moz-transition-timing-function: cubic-bezier(0,0,0.58,1);}
            #div5 {-moz-transition-timing-function: cubic-bezier(0.42,0,0.58,1);}
            /* Safari and Chrome: */
            #div1 {-webkit-transition-timing-function: cubic-bezier(0,0,1,1;}
            #div2 {-webkit-transition-timing-function: cubic-bezier(0.25,0.1,0.25,1);}
            #div3 {-webkit-transition-timing-function: cubic-bezier(0.42,0,1,1);}
            #div4 {-webkit-transition-timing-function: cubic-bezier(0,0,0.58,1);}
            #div5 {-webkit-transition-timing-function: cubic-bezier(0.42,0,0.58,1);}
            /* Opera: */
            #div1 {-o-transition-timing-function: cubic-bezier(0,0,1,1;}
            #div2 {-o-transition-timing-function: cubic-bezier(0.25,0.1,0.25,1);}
            #div3 {-o-transition-timing-function: cubic-bezier(0.42,0,1,1);}
            #div4 {-o-transition-timing-function: cubic-bezier(0,0,0.58,1);}
            #div5 {-o-transition-timing-function: cubic-bezier(0.42,0,0.58,1);}
        }
        
    }
    transition-delay                { //规定过渡效果何时开始。默认是 0。
    }
        
    #endregion

#endregion

#region CSS3 动画 (@keyframes 规则)
    /**
        通过CSS3,我们能够创建动画,这可以在许多网页中取代动画图片,Flash以及JavaScript
        
        CSS3 @keyframes 规则
        如需在CSS3中创建动画,您需要学习@keyframes规则
        @keyframes规则用户创建动画,在@keyframes中规定某项CSS样式,
        就能创建由当前样式逐渐改为新样式的动画效果
    */
#endregion

#region @media screen 动态网页布局
	准备工作1：设置Meta标签
	首先我们在使用Media的时候需要先设置下面这段代码，来兼容移动设备的展示效果：
		<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
	这段代码的几个参数解释：
		width = device-width：宽度等于当前设备的宽度
		height = device-height：高度等于当前设备的高度
		initial-scale：初始的缩放比例（默认设置为1.0）  
		minimum-scale：允许用户缩放到的最小比例（默认设置为1.0）    
		maximum-scale：允许用户缩放到的最大比例（默认设置为1.0）   
		user-scalable：用户是否可以手动缩放（默认设置为no，因为我们不希望用户放大缩小页面）  
	准备工作2：加载兼容文件JS
	因为IE8既不支持HTML5也不支持CSS3 Media，所以我们需要加载两个JS文件，来保证我们的代码实现兼容效果：
		<!--[if lt IE 9]>
		  <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
		  <script src="https://oss.maxcdn.com/libs/respond.js/1.3.0/respond.min.js"></script>
		<![endif]-->
	 准备工作3：设置IE渲染方式默认为最高(这部分可以选择添加也可以不添加)
	现在有很多人的IE浏览器都升级到IE9以上了，所以这个时候就有又很多诡异的事情发生了，例如现在是IE9的浏览器，但是浏览器的文档模式却是IE8:
	为了防止这种情况，我们需要下面这段代码来让IE的文档模式永远都是最新的：
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
	 （如果想使用固定的IE版本，可写成：<meta http-equiv="X-UA-Compatible" content="IE=EmulateIE9">）

	不过我最近又发现了一个更给力的写法：
		<meta http-equiv="X-UA-Compatible" content="IE=Edge，chrome=1">
	怎么这段代码后面加了一个chrome=1，这个Google Chrome Frame（谷歌内嵌浏览器框架GCF），如果有的用户电脑里面装了这个chrome的插件，就可以让电脑里面的IE不管是哪个版本的都可以使用Webkit引擎及V8引擎进行排版及运算，无比给力，不过如果用户没装这个插件，那这段代码就会让IE以最高的文档模式展现效果。这段代码我还是建议你们用上，不过不用也是可以的。
	 
	进入CSS3 Media写法
	我们先来看下下面这段代码，估计很多人在响应式的网站CSS很经常看到类似下面的这段代码：
		@media screen and (max-width: 960px){
			body{
				background: #000;
			}
		}
	这个应该算是一个media的一个标准写法，上面这段CSS代码意思是：当页面小于960px的时候执行它下面的CSS.这个应该没有太大疑问。
	 
	应该有人会发现上面这段代码里面有个screen，他的意思是在告知设备在打印页面时使用衬线字体，在屏幕上显示时用无衬线字体。但是目前我发现很多网站都会直接省略screen,因为你的网站可能不需要考虑用户去打印时，你可以直接这样写：
		@media (max-width: 960px){
			body{
				background: #000;
			}
		}
	 
	CSS2 Media用法
	其实并不是只有CSS3才支持Media的用法，早在CSS2开始就已经支持Media，具体用法，就是在HTML页面的head标签中插入如下的一段代码：
		<link rel="stylesheet" type="text/css" media="screen" href="style.css">
	 
	上面其实是CSS2实现的衬线用法，那CSS2的media难道就只能支持上面这一个功能吗？答案当然不是，他还有很多用法。
	 
	例如我们想知道现在的移动设备是不是纵向放置的显示屏，可以这样写：
		<link rel="stylesheet" type="text/css" media="screen and (orientation:portrait)" href="style.css">
	 
	我们把第一段的代码也用CSS2来实现，让它一样可以让页面宽度小于960的执行指定的样式文件：
		<link rel="stylesheet" type="text/css" media="screen and (max-width:960px)" href="style.css">
	 
	既然CSS2可以实现CSS的这个效果为什么不用这个方法呢，很多人应该会问，但是上面这个方法，最大的弊端是他会增加页面http的请求次数，增加了页面负担，我们用CSS3把样式都写在一个文件里面才是最佳的方法。
	 
	回归CSS3 Media
	上面我们大概讲了下CSS2的媒体查询用法，现在我们重新回到CSS3的媒体查询，在第一段代码上面我用的是小于960px的尺寸的写法，那现在我们来实现等于960px尺寸的代码：
		@media screen and (max-device-width:960px){
			body{
				background:red;
			}
		}
	 
	然后就是当浏览器尺寸大于960px时候的代码了：
		@media screen and (min-width:960px){
			body{
				background:orange;
			}
		}
	 
	我们还可以混合使用上面的用法：
		@media screen and (min-width:960px) and (max-width:1200px){
			body{
				background:yellow;
			}
		}
	上面的这段代码的意思是当页面宽度大于960px小于1200px的时候执行下面的CSS。
	 
	Media所有参数汇总
	以上就是我们最常需要用到的媒体查询器的三个特性，大于，等于，小于的写法。媒体查询器的全部功能肯定不止这三个功能，下面是我总结的它的一些参数用法解释：
		width:浏览器可视宽度。
		height:浏览器可视高度。
		device-width:设备屏幕的宽度。
		device-height:设备屏幕的高度。
		orientation:检测设备目前处于横向还是纵向状态。
		aspect-ratio:检测浏览器可视宽度和高度的比例。(例如：aspect-ratio:16/9)
		device-aspect-ratio:检测设备的宽度和高度的比例。
		color:检测颜色的位数。（例如：min-color:32就会检测设备是否拥有32位颜色）
		color-index:检查设备颜色索引表中的颜色，他的值不能是负数。
		monochrome:检测单色楨缓冲区域中的每个像素的位数。（这个太高级，估计咱很少会用的到）
		resolution:检测屏幕或打印机的分辨率。(例如：min-resolution:300dpi或min-resolution:118dpcm)。
		grid：检测输出的设备是网格的还是位图设备。

	注意下顺序，如果你把@media (min-width: 768px)写在了下面那么很悲剧，
	@media (min-width: 1200){} //>=1200的设备 }
	@media (min-width: 992px){} //>=992的设备 }
	@media (min-width: 768px){} //>=768的设备 }
	因为如果是1440,由于1440>768那么你的1200就会失效。
	所以我们用min-width时，小的放上面大的在下面，同理如果是用max-width那么就是大的在上面，小的在下面
	@media (max-width: 1199){} //<=1199的设备 }
	@media (max-width: 991px){} //<=991的设备 }
	@media (max-width: 767px){} //<=768的设备 }
	1280分辨率以上（大于1200px）
	@media screen and (min-width:1200px){
		#page{ width: 1100px; }#content,.div1{width: 730px;}#secondary{width:310px}
	}
	 
	1100分辨率（大于960px，小于1199px）
	@media screen and (min-width: 960px) and (max-width: 1199px) {
		#page{ width: 960px; }#content,.div1{width: 650px;}#secondary{width:250px}select{max-width:200px}
	}
	 
	880分辨率（大于768px，小于959px）
	@media screen and (min-width: 768px) and (max-width: 959px) {
		#page{ width: 900px; }#content,.div1{width: 620px;}#secondary{width:220px}select{max-width:180px}
	}
	 
	720分辨率（大于480px，小于767px）
	@media only screen and (min-width: 480px) and (max-width: 767px){
		#page{ width: 450px; }#content,.div1{width: 420px;position: relative; }#secondary{display:none}#access{width: 450px; }#access a {padding-right:5px}#access a img{display:none}#rss{display:none}#branding #s{display:none}
	}
	 
	440分辨率以下（小于479px）
	@media only screen and (max-width: 479px) {
		#page{ width: 300px; }#content,.div1{width: 300px;}#secondary{display:none}#access{width: 330px;} #access a {padding-right:10px;padding-left:10px}#access a img{display:none}#rss{display:none}#branding #s{display:none}#access ul ul a{width:100px}
	}
	 
	[css] view plain copy
	在CODE上查看代码片派生到我的代码片
		/* 竖屏 */  
		@media screen and (orientation: portrait) and (max-width: 720px) { 对应样式 }  
		  
		/* 横屏 */  
		@media screen and (orientation: landscape) { 对应样式 }  

	上面的代码中用到了screen ，他的意思是在告知设备在打印页面时使用衬线字体，在屏幕上显示时用无衬线字体。但是目前我发现很多网站都会直接省略screen,因为你的网站可能不需要考虑用户去打印时。

	PC端按屏幕宽度大小排序（主流的用橙色标明）
	分辨率   比例 | 设备尺寸
	1024*500 （8.9寸）
	1024*768 （比例4：3  | 10.4寸、12.1寸、14.1寸、15寸; ）
	1280*800（16：10  |15.4寸）
	1280*1024(比例：5：4  | 14.1寸、15.0寸)
	1280*854(比例：15：10 | 15.2）
	1366*768 (比例：16：9 | 不常见）
	1440*900 （16：10  17寸 仅苹果用）
	1440*1050（比例：5：4  | 14.1寸、15.0寸）
	1600*1024（14：9  不常见）
	1600*1200 （4：3 | 15、16.1）
	1680*1050（16：10 | 15.4寸、20.0寸）
	1920*1200 (23寸）
	通过上面的电脑屏蔽及尺寸的例表上我们得到了几个宽度
	1024  1280  1366  1440  1680  1920  
	CSS代码
	@media (min-width: 1024px){
		body{font-size: 18px}
	} /*>=1024的设备*/
	@media (min-width: 1100px) {
		body{font-size: 20px}
	} /*>=1024的设备*/
	@media (min-width: 1280px) {
		body{font-size: 22px;}
	} 
	@media (min-width: 1366px) {
		body{font-size: 24px;}
	}
	@media (min-width: 1440px) {
		body{font-size: 25px !important;}
	} 
	@media (min-width: 1680px) {
		body{font-size: 28px;}
	} 
	@media (min-width: 1920px) {
		body{font-size: 33px;}
	}
#endregion

#region 压缩 CSS 代码
    正则:
        ([^}])\s+
            ||
        $1`空格`
#endregion


// 清除浮动 清除 float
http://www.cnblogs.com/wangfupeng1988/p/4314804.html




