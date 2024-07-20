import re
import sys


def clean_text(text):
    """
    删除文本中的英文，保留中文汉字。
    """
    # 使用正则表达式匹配非中文字符（包括英文、数字、符号等）
    cleaned_text = re.sub(r'[^\u4e00-\u9fa5]', '', text)
    return cleaned_text


def read_and_clean_file(file_path):
    """
    读取文件，清洗内容（删除英文），并打印清洗后的内容。
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = list(file.readlines())
            for line in lines:
                line = line.strip()
                cleaned_line = clean_text(line)
                if line != cleaned_line:
                    print(cleaned_line)
    except FileNotFoundError:
        print(f"文件 {file_path} 未找到。")
    except Exception as e:
        print(f"读取或处理文件时发生错误：{e}")

    # 假设我们有一个名为 "example.txt" 的文件


if __name__ == '__main__':
    print('参数个数为:', len(sys.argv), '个参数。')
    print('参数列表:', str(sys.argv))
    file_path = sys.argv[1]
    read_and_clean_file(file_path)