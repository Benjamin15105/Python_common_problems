# Python_common_problems
记录一些常见问题的报错以及解决方法  
1.在路径中使用普通字符串时出现了 Unicode 转义错误
> SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape

2.[Pandas] to_excel保存时writer.save() 报错问题：  
> AttributeError: 'OpenpyxlWriter' object has no attribute 'save'. Did you mean: '_save'?

3.如何查看自己电脑的Python位置呢？

4.关于Python中模块和库的区别

5.Search engine ID是什么?

6.关于如何配置自己电脑的服务器网络凭据?

7.解压出来的文件名字前带点和下划线

8.Github的2FA验证如何识别网页二维码，手机端app未找到扫一扫

9.Google的python翻译包，效果不太好(跟网页端相比)

10.避免使用+操作符在python中连接字符串,for循环和os.join()函数的性能对比（https://blog.csdn.net/qq_34769162/article/details/108902354）  

11.打印中文字符串长度,在学习小组时，想到打印单个字母的字符串，长度为11，如果是单个中文字时，长度是多少，以及印象中中文字符是两个字节还是两个字符来着？

12.Pycharm如何预览markdown文件？之前老是找不到

13.Python的随机种子问题，在待处理数据中抽取抽样数据，讨论随机种子的应用场景

14.Google Chrome浏览器进入ChatGPT界面，右上角用户头像消失，无法更换用户账号？

15.7z分卷压缩包如何解压？

16.Python中with……as是什么

17.关于read(),readline(),readlines()三个函数的用法

18.在凭据管理器里添加Windows凭据后，要重启才能生效.

19.笔记本电脑iNode连接获取当前网卡的ip地址失败.
(先连接wifi在连iNode)

20.使用记事本编辑.txt文件时，阿拉伯语和中文交替出现编辑时出现跳码问题（编码格式:带有BOM的UTF-8）:
                    如：“ غداً” 和 “ غدا”，以及 “مرحباً ”和 “مرحبا”、
  删除"以及"后，变成了如：“ غداً” 和 “ غدا”， “مرحباً ”和 “مرحبا”、
