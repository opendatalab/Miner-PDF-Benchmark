import json
import argparse

# 定义命令行参数解析
def parse_args():
    parser = argparse.ArgumentParser(description='Filter PDFs based on conditions.')
    parser.add_argument('-f', '--file', type=str, required=True, help='Path to the JSONL file')
    parser.add_argument('--tag', type=str, help='Tag to filter by')
    parser.add_argument('--language', type=str, help='Language to filter by')
    parser.add_argument('--bool_scan', action='store_true', help='Filter by scan availability')
    parser.add_argument('--bool_watermark', action='store_true', help='Filter by watermark presence')
    parser.add_argument('--bool_txt', action='store_true', help='Filter by txt availability')
    return parser.parse_args()

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

# 主程序
if __name__ == '__main__':
    args = parse_args()
    data = load_data(args.file)
    filters = {
        'tag': args.tag,
        'language': args.language,
        'bool_scan': args.bool_scan,
        'bool_watermark': args.bool_watermark,
        'bool_txt': args.bool_txt
    }
    filtered_names = filter_pdfs(data, **filters)
    with open('filtered_pdfs.jsonl', 'w') as outfile:
        for name in filtered_names:
            json.dump({"pdf_name": name}, outfile)
            outfile.write('\n')
    print(f'筛选完成，共找到 {len(filtered_names)} 个符合条件的PDF文件。')

# python sift.py -f config.jsonl --tag academic_literature --language en --bool_scan --bool_watermark --bool_txt
