> SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape  

解决方式:
这个错误表明您在使用普通字符串时出现了 **Unicode 转义错误**，具体是因为路径中的 `\` 被当作转义字符处理，例如 `\U` 被解释为 Unicode 转义序列。

在 Python 中，路径中的反斜杠 `\` 是转义字符，例如 `\t` 表示制表符，`\n` 表示换行符。如果路径中的某个字符组合（如 `\U`）与合法的 Unicode 转义序列类似，但并不完整，就会导致 **`unicodeescape` 错误**。

---

### 解决方法

#### 1. 使用原始字符串（推荐）
将路径字符串前面加上字母 `r`，告诉 Python 不要处理字符串中的转义字符：

```python
input_file = r'C:\Users\tyqiu.IFLYTEK\Desktop\瑞典已验收文本_0109.txt'  # 输入文件路径
```

#### 2. 替换反斜杠为正斜杠
在 Windows 路径中，可以将反斜杠 `\` 替换为正斜杠 `/`，Python 能正确识别：

```python
input_file = 'C:/Users/tyqiu.IFLYTEK/Desktop/瑞典已验收文本_0109.txt'  # 输入文件路径
```

#### 3. 双反斜杠转义
如果坚持使用反斜杠，则需要用双反斜杠 `\\`，这样 Python 不会将其当作转义字符：

```python
input_file = 'C:\\Users\\tyqiu.IFLYTEK\\Desktop\\瑞典已验收文本_0109.txt'  # 输入文件路径
```

---

### 推荐的解决方案
优先使用 **原始字符串**（方法 1），它是最简洁和清晰的方式。

---

### 为什么会出现这个问题？

在您的路径中，`C:\Users` 中的 `\U` 被误认为是 Unicode 转义字符的开头（`'\UXXXXXXXX'` 是表示 Unicode 码点的合法形式），但由于后续内容不符合完整的 Unicode 规范，导致了 **SyntaxError**。

### 总结
通过使用 **`r''`** 或 **`/`**（正斜杠），可以避免路径中的转义字符问题，解决此错误。
