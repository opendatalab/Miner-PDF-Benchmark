import pypandoc
import re
import htmltabletomd
import os

# 定义文件夹路径
download_dir = './academic_literature/annotations'

def clean_markdown_images(content):
    pattern = re.compile(r'!\[[^\]]*\]\([^)]*\)', re.IGNORECASE)
    cleaned_content = pattern.sub('', content)
    return cleaned_content

def clean_ocrmath_photo(content):
    pattern = re.compile(r'\\includegraphics\[.*?\]\{.*?\}', re.IGNORECASE)
    cleaned_content = pattern.sub('', content)
    return cleaned_content

def convert_html_table_to_md(html_table):
    lines = html_table.strip().split('\n')
    md_table = ''
    if lines and '<tr>' in lines[0]:
        in_thead = True
        for line in lines:
            if '<th>' in line:
                cells = re.findall(r'<th>(.*?)</th>', line)
                md_table += '| ' + ' | '.join(cells) + ' |\n'
                in_thead = False
            elif '<td>' in line and not in_thead:
                cells = re.findall(r'<td>(.*?)</td>', line)
                md_table += '| ' + ' | '.join(cells) + ' |\n'
        md_table = md_table.rstrip() + '\n'
    return md_table

def convert_latext_to_md(content):
    tables = re.findall(r'\\begin\{tabular\}(.*?)\\end\{tabular\}', content, re.DOTALL)
    placeholders = []
    for table in tables:
        placeholder = f"<!-- TABLE_PLACEHOLDER_{len(placeholders)} -->"
        replace_str = f"\\begin{{tabular}}{table}\\end{{tabular}}"
        content = content.replace(replace_str, placeholder)
        try:
            pypandoc.convert_text(replace_str, format="latex", to="md", outputfile="output.md", encoding="utf-8")
        except:
            markdown_string = replace_str
        else:
            markdown_string = open('output.md', 'r', encoding='utf-8').read()
        placeholders.append((placeholder, markdown_string))
    new_content = content
    for placeholder, md_table in placeholders:
        new_content = new_content.replace(placeholder, md_table)
    return new_content

def convert_htmltale_to_md(content):
    tables = re.findall(r'<table>(.*?)</table>', content, re.DOTALL)
    placeholders = []
    for table in tables:
        placeholder = f"<!-- TABLE_PLACEHOLDER_{len(placeholders)} -->"
        content = content.replace(f"<table>{table}</table>", placeholder)
        try:
            convert_table = htmltabletomd.convert_table(table)
        except:
            convert_table = table
        placeholders.append((placeholder, convert_table))
    new_content = content
    for placeholder, md_table in placeholders:
        new_content = new_content.replace(placeholder, md_table)
    return new_content

def clean_data(download_dir):
    # 创建一个名为'cleaned'的子文件夹来存放清洗好的文件
    cleaned_dir = os.path.join(download_dir, 'cleaned')
    if not os.path.exists(cleaned_dir):
        os.makedirs(cleaned_dir)

    # 遍历下载目录中的所有文件
    filenames = os.listdir(download_dir)
    for filename in filenames:
        if filename.endswith('.md'):
            input_file = os.path.join(download_dir, filename)
            output_file = os.path.join(cleaned_dir, filename)
            with open(input_file, 'r', encoding='utf-8') as fr:
                content = fr.read()
                new_content = convert_htmltale_to_md(content)
                new_content = clean_markdown_images(new_content)
                new_content = clean_ocrmath_photo(new_content)
                new_content = convert_latext_to_md(new_content)
                with open(output_file, 'w', encoding='utf-8') as fw:
                    fw.write(new_content)

# 主程序
if __name__ == '__main__':
    clean_data(download_dir)
