import json

# 读取JSON文件的第一行
with open('ccccc.json', 'r', encoding='utf-8') as file:
    first_line = file.readline()
    json_data = json.loads(first_line.strip())

# 读取JSONL文件并创建一个集合来存储pdf名称
pdf_names = set()
with open('filtered_pdfs.jsonl', 'r', encoding='utf-8') as file:
    for line in file:
        jsonl_data = json.loads(line)
        pdf_names.add(jsonl_data['pdf_name'])

# 筛选JSON数据
filtered_data = {md_file: data for md_file, data in json_data.items() if md_file in pdf_names}

# 初始化统计变量
edit_distances = []
bleu_scores = []
sim_scores = []

# 计算筛选数据的统计值
for data in filtered_data.values():
    edit_distances.append(data['edit_dist'])
    bleu_scores.append(data['bleu_score'])
    sim_scores.append(data['sim_score'])

# 计算每类平均值
class_average_edit_distance = sum(edit_distances) / len(edit_distances) if edit_distances else 0
class_average_bleu_score = sum(bleu_scores) / len(bleu_scores) if bleu_scores else 0
class_average_sim_score = sum(sim_scores) / len(sim_scores) if sim_scores else 0

# 计算提取比例
ratio = len(filtered_data) / len(json_data)

# 准备要写入新文件的数据
output_data = {
    "filtered_data": filtered_data,
    "statistics": {
        "extract_ratio": ratio,
        "average_edit_distance": class_average_edit_distance,
        "average_bleu_score": class_average_bleu_score,
        "average_sim_score": class_average_sim_score
    }
}

# 将筛选后的数据和统计值写入新的JSON文件
with open('filtered_output.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(output_data, indent=4, ensure_ascii=False))
