import pandas as pd
from googletrans import Translator
from tqdm import tqdm  # 进度条显示库

# 创建翻译器实例
translator = Translator()

# 读取 Excel 文件
file_path = r'C:\Users\xiangli65\Desktop\Google_翻译python包\Kinyarwanda_TYKY_202501_17.xlsx'  # 请替换为您的 Excel 文件路径
df = pd.read_excel(file_path)

# 假设要翻译的列是 '原文' 列
column_to_translate = '原文'  # 需要翻译的列名

# 翻译函数，添加错误处理
def translate_column(text, target_language='zh-CN'):  # 目标语言设置为简体中文
    try:
        if isinstance(text, str):
            translated = translator.translate(text, dest=target_language)
            return translated.text
    except Exception as e:
        print(f"Error translating text: {text}. Error: {e}")
        return text  # 出错时返回原始文本

# 对列进行翻译，添加进度条
tqdm.pandas(desc="翻译中...")
df['谷歌翻译'] = df[column_to_translate].progress_apply(lambda x: translate_column(x))

# 保存修改后的 Excel 文件（直接保存到原路径）
df.to_excel(file_path, index=False)

print(f"翻译完成！翻译结果已保存回原文件：{file_path}")
