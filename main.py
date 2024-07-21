import os.path
import re
import sys
import difflib


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
            for i, line in enumerate(lines):
                line = line.strip()
                cleaned_line = clean_text(line)
                if line != cleaned_line:
                    print("Line: {} | should be: {}".format(i, cleaned_line))
    except FileNotFoundError:
        print(f"文件 {file_path} 未找到。")
    except Exception as e:
        print(f"读取或处理文件时发生错误：{e}")

    # 假设我们有一个名为 "example.txt" 的文件

def read_and_clean_file_with_report(file_path):
    template_block1 = """## 代码修改建议  
  
在审查过程中，我发现以下文件中有几处需要修改或调整。以下是详细的修改建议：  
  
| 文件名 | 行号 | 当前内容 | 建议修改内容 |  
|--------|------|----------|--------------|  
| `example.js` | 10   | `let a = 1;` | `const a = 1;` |"""

    template_block2 = """**注意**：  
- 请确保在提交修改前，已经对代码进行了充分的测试，以避免引入新的问题。  
- 如果对以上修改有任何疑问或需要进一步的讨论，请随时在评论中回复。  

希望这些修改建议对你有所帮助！"""
    try:
        block = []
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = list(file.readlines())
            for i, line in enumerate(lines):
                line = line.strip()
                cleaned_line = clean_text(line)
                if line != cleaned_line:
                    block.append("| {} | {} | {} | {} |".format(os.path.basename(file_path), i, line, cleaned_line))
        print(template_block1)
        print("\n".join(block))
        print(template_block2)
    except FileNotFoundError:
        print(f"文件 {file_path} 未找到。")
    except Exception as e:
        print(f"读取或处理文件时发生错误：{e}")

    # 假设我们有一个名为 "example.txt" 的文件


if __name__ == '__main__':
    # print('参数个数为:', len(sys.argv), '个参数。')
    # print('参数列表:', str(sys.argv))
    file_path = sys.argv[1]
    read_and_clean_file_with_report(file_path)
