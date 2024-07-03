import json

# 从文件中读取数据
def load_data(file_path):
    with open(file_path, 'r') as file:
        return [json.loads(line) for line in file]

# 筛选函数，可以接受任意数量的条件
def filter_pdfs(data, **filters):
    filtered_data = []
    for entry in data:
        if all(entry.get(key) == value for key, value in filters.items() if value is not None):
            # 将文件名中的.pdf后缀替换为.md
            filtered_data.append(entry['pdf_name'].replace('.pdf', '.md'))
    return filtered_data

# 您的JSONL文件路径
file_path = 'config.jsonl'  # 请替换为您的文件路径

# 加载数据
data = load_data(file_path)

# 设置筛选条件，未设置的条件将被忽略
filters = {
    'tag': "academic_literature",  # 例如: "academic_literature" 或 None
    'language': "en",              # 例如: "en" 或 None
    'bool_scan': False,            # 例如: False 或 None
    'bool_watermark': False,       # 例如: False 或 None
    'bool_txt': True               # 例如: True 或 None
}

# 筛选数据
filtered_names = filter_pdfs(data, **filters)

# 将筛选结果输出到新的JSONL文件
with open('filtered_pdfs.jsonl', 'w') as outfile:
    for name in filtered_names:
        json.dump({"pdf_name": name}, outfile)
        outfile.write('\n')

print(f'筛选完成，共找到 {len(filtered_names)} 个符合条件的PDF文件。')
