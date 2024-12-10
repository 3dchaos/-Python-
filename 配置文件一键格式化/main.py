import os


def backup_file(file_path):
    """备份原文件，在原文件名后添加.bak后缀"""
    dir_name, file_name = os.path.split(file_path)
    base_name, ext_name = os.path.splitext(file_name)
    backup_name = os.path.join(dir_name, base_name + '.bak' + ext_name)
    os.rename(file_path, backup_name)
    return backup_name


def process_text_to_table(input_path):
    """读取文本内容，处理成表格形式的文本内容"""
    table_content = []
    with open(input_path, 'r', encoding='ANSI') as f:
        for line in f:
            line = line.rstrip()
            if line.startswith(';'):
                table_content.append(line)
                continue
            cells = line.split()  # 通过空白字符（空格、制表符等）划分单元格
            table_content.append('\t'.join(cells))
    return '\n'.join(table_content)


def save_table_to_file(content, output_path):
    """将处理后的表格内容保存到文件中"""
    with open(output_path, 'w', encoding='ANSI') as f:
        f.write(content)


if __name__ == "__main__":
    input_path = input("请输入要处理的txt文件路径: ")
    backup_path = backup_file(input_path)
    table_content = process_text_to_table(backup_path)
    save_table_to_file(table_content, input_path)