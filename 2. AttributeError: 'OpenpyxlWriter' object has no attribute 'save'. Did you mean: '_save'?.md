今天试着用pandas在一个excel里保存多个sheet，由于要用到writer = pd.ExcelWriter(......)命令，别的攻略里说最后要用writer.save()保存，但实际运行时遇到了如下报错：

> AttributeError: 'OpenpyxlWriter' object has no attribute 'save'. Did you mean: '_save'?

在stackoverflow上看到这样的说法：

> The save() method has been deprecated and removed in Pandas. You should use close() instead.

也就是说，新版Pandas中save()函数已经被弃用了，只用writer.close()保存即可。
