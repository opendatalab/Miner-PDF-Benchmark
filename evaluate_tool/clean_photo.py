"""
Preprocessing Data
"""
import argparse
import os
import re

import htmltabletomd
import pypandoc

parser = argparse.ArgumentParser(description='get tool name, download_dir')
parser.add_argument(
    '--tool_name',
    type=str,
    required=True,
    help='input tool name',
)
parser.add_argument(
    '--download_dir',
    type=str,
    required=True,
    help='input download dir',
)
args = parser.parse_args()


def clean_markdown_images(content: str):
    """
    Clean up markdown pictures
    """
    pattern = re.compile(r'!\[[^]]*]\([^)]*\)', re.IGNORECASE)
    cleaned_content = pattern.sub('', content)
    return cleaned_content


def clean_ocrmath_photo(content: str):
    """
    Clean up latex pictures
    """
    pattern = re.compile(r'\\includegraphics\[.*?]\{.*?}', re.IGNORECASE)
    cleaned_content = pattern.sub('', content)
    return cleaned_content


def convert_html_table_to_md(html_table: str):
    """
    Convert HTML table to Markdown table
    """
    lines = html_table.strip().split('\n')
    md_table = ''
    if lines and '<tr>' in lines[0]:
        in_head = True
        for line in lines:
            if '<th>' in line:
                cells = re.findall(r'<th>(.*?)</th>', line)
                md_table += '| ' + ' | '.join(cells) + ' |\n'
                in_head = False
            elif '<td>' in line and not in_head:
                cells = re.findall(r'<td>(.*?)</td>', line)
                md_table += '| ' + ' | '.join(cells) + ' |\n'
        md_table = md_table.rstrip() + '\n'
    return md_table


def convert_latext_to_md(content: str):
    """
    Convert latex table to markdown table
    """
    tables = re.findall(r'\\begin\{tabular}(.*?)\\end\{tabular}', content, re.DOTALL)
    placeholders = []
    for table in tables:
        placeholder = f'<!-- TABLE_PLACEHOLDER_{len(placeholders)} -->'
        replace_str = f'\\begin{{tabular}}{table}cl\\end{{tabular}}'
        content = content.replace(replace_str, placeholder)
        try:
            pypandoc.convert_text(replace_str, format='latex', to='md', outputfile='output.md', encoding='utf-8')
        except ValueError:
            markdown_string = replace_str
        else:
            markdown_string = open('output.md', 'r', encoding='utf-8').read()
        placeholders.append((placeholder, markdown_string))
    new_content = content
    for placeholder, md_table in placeholders:
        new_content = new_content.replace(placeholder, md_table)
    return new_content


def convert_htmltale_to_md(content: str):
    """
    Convert htmltable to markdown table
    """
    tables = re.findall(r'<table>(.*?)</table>', content, re.DOTALL)
    placeholders = []
    for table in tables:
        placeholder = f'<!-- TABLE_PLACEHOLDER_{len(placeholders)} -->'
        content = content.replace(f'<table>{table}</table>', placeholder)
        try:
            convert_table = htmltabletomd.convert_table(table)
        except ValueError:
            convert_table = table
        placeholders.append((placeholder, convert_table))
    new_content = content
    for placeholder, md_table in placeholders:
        new_content = new_content.replace(placeholder, md_table)
    return new_content


def clean_data(prod_type: str, data_dir: str):
    """
    Cleaning the data
    """
    file_type = [
        'academic_literature',
        'atlas',
        'courseware',
        'colorful_textbook',
        'historical_document',
        'note',
        'ordinary_book',
        'ordinary_exam_paper',
        'ordinary_textbook',
        'research_report',
        'special_exam_paper',
    ]
    for filetype in file_type:
        tgt_dir = os.path.join(data_dir, filetype, prod_type, 'cleaned')
        if not os.path.exists(tgt_dir):
            os.makedirs(tgt_dir)
        source_dir = os.path.join(data_dir, filetype, prod_type)
        filenames = os.listdir(source_dir)
        for filename in filenames:
            if filename.endswith('.md'):
                input_file = os.path.join(source_dir, filename)
                output_file = os.path.join(tgt_dir, 'cleaned_' + filename)
                with open(input_file, 'r', encoding='utf-8') as fr:
                    content = fr.read()
                    new_content = convert_htmltale_to_md(content)
                    new_content = clean_markdown_images(new_content)
                    new_content = clean_ocrmath_photo(new_content)
                    new_content = convert_latext_to_md(new_content)
                    with open(output_file, 'w', encoding='utf-8') as fw:
                        fw.write(new_content)


if __name__ == '__main__':
    tool_type = args.tool_name
    download_dir = args.download_dir
    clean_data(tool_type, download_dir)
