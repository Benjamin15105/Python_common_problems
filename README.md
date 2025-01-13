# Python_common_problems
记录一些常见问题的报错以及解决方法  
1.在路径中使用普通字符串时出现了 Unicode 转义错误
> SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape

2.[Pandas] to_excel保存时writer.save() 报错问题：  
> AttributeError: 'OpenpyxlWriter' object has no attribute 'save'. Did you mean: '_save'?
