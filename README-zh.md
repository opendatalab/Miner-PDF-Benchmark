# 简介
MPB（Miner-PDF-Benchmark）是一套为大规模模型数据场景设计的端到端PDF文档理解评估套件。它确保了文件粒度上的人类可读性，并提供了PDF分类标签。该数据集总共包含350个PDF文件和8410页PDF，包括书籍、教材、学术文献、PPT转PDF、试卷等11种类型的数据集。它为大规模模型数据的开发者和工具开发者提供了PDF文档理解能力的评估参考。


# 数据集来源
MPB 数据集来源于多种渠道，包括 arXiv、Sci-Hub、教科书、试卷、历史文献等。不同子集的来源和组成如下：

| 类别           | 对应标签             | 文件数 | 总页数 | 简介                                                                 |
|----------------|----------------------|--------|--------|--------------------------------------------------------------------|
| 研报           | research_report      | 70     | 875    | 来自于互联网的财报, 具有大型表格、复杂合并表格，横向表格混合正文、有单栏、双栏和复杂布局等特点      |
| 普通教材       | ordinary_textbook    | 40     | 388    | 来自于互联网的教材, 具有单栏布局，颜色为黑白，嵌套复杂公式和包含复杂大型矩阵的特点 |
| 学术文献       | academic_literature  | 183    | 3323   | 来自于arXiv和SCIHUB，具有含单栏、双栏、图表、公式等复杂版式的特点 |
| 图册           | atlas               | 3      | 269    | 来自于互联网的图册集, 具有单页包含大面积图片的特点  |
| PPT2PDF        | courseware          | 7      | 383    | 来自于互联网PPT转的PDF文件，有背景色，包含生物、语文、英语、物理4个学科 |
| 特殊图文试卷   | special_exam_paper   | 3      | 80     | 来自于互联网，具有版面为试卷、含水印、文字在图形中的特征的特点，内容包括小学拼音题目和数学试题等|
| 历史文献       | historical_document| 1      | 3      | 来自于互联网，具有排版为竖排，阅读顺序从右到左的特征，字体为繁体的特点 |
| 笔记           | note               | 3      | 293    | 来自于互联网，具有含手写体的特点，内容包括3个初中的学生手写笔记  |
| 普通试卷       | ordinary_exam_paper  | 27     | 372    | 来自于互联网，具有版面为试卷类型、背景黑白为主的特点，包括计算机科学、数学、语文等学科，涵盖小学、初中、高中、行业题库 |
| 特殊图文教材   | colorful_textbook    | 3      | 144    | 来自于互联网，具有包含特殊图文信息的特点，内容包括英语、数学、中文（含拼音）等学科 |
| 普通书         | ordinary_book       | 10     | 2280   | 来自于互联网书籍，特征为单栏布局、背景为黑白色的书 |

说明：我们的数据均来自于互联网。

# 统计信息
<img src="https://github.com/opendatalab/Miner-PDF-Benchmark/assets/102640628/cb538c40-d4da-4b21-9367-26e9bb192cee" width="350" height="200" alt="The distribution of pages">  
<img src="https://github.com/opendatalab/Miner-PDF-Benchmark/assets/102640628/a41dc7b7-831d-4642-a8bc-01ddd26dece7" width="350" height="200" alt="The distribution of PDF file"> 

<img src="https://github.com/quyuan01/pdf-extract-bench/assets/102640628/d233a4ca-c54a-41f3-be96-8b80b1b0b740" width="350" height="200" alt="The distribution of md language">  
<img src="https://github.com/quyuan01/pdf-extract-bench/assets/102640628/5ff056a7-6094-420b-8a93-a31585da9451" width="350" height="200" alt="The distribution of PDF  Type">  

# 指标

我们采用了[评估指标](docs/Metric.md)对抽取工具进行评价。

# 结果

我们对nogout、marker、MinerU、doc2x、ocrmath、mathpix几个抽取工具进行了评估，评估结果如下。

### 总体平均得分
| 方案         | 抽取率（↑） | sim_score(↑) | 编辑距离(↓) | bleu(↑) |
|--------------|--------------|--------------|--------------|----------|
| [MinerU (开源工具)](https://github.com/magicpdf/Magic-PDF)                 | 98.4%                 | 0.61                 | 0.3             |0.47             |
| [nogout (开源工具)](https://github.com/facebookresearch/nougat)       | 100%         | 0.35         | 0.57         | 0.33     |
| [marker(开源工具)](https://github.com/VikParuchuri/marker)       | 99.4%        | 0.47         | 0.42         | 0.386    |
| [doc2x（商业工具）](https://doc2x.com/) | 99%          | 0.67         | 0.189        | 0.611    |
| [ocrmath（商业工具）](https://open.ocrmath.com/) | 92%          | 0.56         | 0.38         | 0.39     |
| [mathpix（商业工具）](https://mathpix.com/) | 100%         | 0.83         | 0.08         | 0.91     |

### 11种类型的得分
<img src="https://github.com/opendatalab/Miner-PDF-Benchmark/assets/102640628/da7d62c6-b255-4a83-873c-b36979d82126" width="400" height="350" alt="The distribution of sim_socre">  

<img src="https://github.com/opendatalab/Miner-PDF-Benchmark/assets/102640628/8c113adc-214e-43c0-9448-d5be750695d1" width="400" height="350" alt="The distribution of edit distance">  

<img src="https://github.com/opendatalab/Miner-PDF-Benchmark/assets/102640628/e37753c6-1d07-4834-8220-c78377917886" width="400" height="350" alt="The distribution of bleu">  

notes:
- marker's test version is v0.2.8;
- nogout's test version is v0.1.0 small;
- MinerU's test version is v0.5.11;
- ocrmath的测试时间为2024年6月初;
- Doc2x的测试时间为2024年5月份;
- Mathpix的测试时间为2024年5月初;

# 获取数据
数据集可以从[OpenDataLab](https://opendatalab.com/OpenDataLab/Miner-PDF-Benchmark/tree/main)下载；

# 使用方法

1. 克隆项目

```
git clone https://github.com/opendatalab/Miner-PDF-Benchmark
cd Miner-PDF-Benchmark
```

2. 安装依赖(推荐使用Python 3.9)

```
python -m pip install -r requirements.txt
```

3. 下载评测集

请从[OpenDataLab](https://opendatalab.com/OpenDataLab/Miner-PDF-Benchmark/tree/main)（推荐使用cli/sdk下载）下载评测集，并将评测集解压到`datasets`目录下，确保`datasets`目录下为`pdf`和`annotations`。
准备的评测集，经过组织后目录如下：

```
- Miner-PDF-Benchmark/
  - datasets/
    - academic_literature/
      - annotations/
        - academic_literature_xx.md
      - pdf/ 
    - atlas/
      - annotations/
        - atlas_xx.md
      - pdf/
    - ...
  - evaluate_tool/
```

4. 评测集预处理

由于当前未对评测集中的图片评测，您需要执行以下命令对图片预处理：
```
cd evaluate_tool
python clean_photo.py --tool_name annotations --download_dir ../datasets
```

5. 待评估工具的评测结果准备

请将您需要评估工具生成的`Markdown`文件按照类型复制到`datasets/document_types/tool_name`目录中,`document_types`为11种类别对应的标签,`tool_name`为您的工具名称。
复制后的目录结构如下：
```
- Miner-PDF-Benchmark/
  - datasets/
    - academic_literature/
      - annotations/
        - academic_literature_xx.md
      - tool_name/
        - academic_literature_xx.md
      - pdf/ 
    - atlas/
      - tool_name/
        - atlas_xx.md
    - ...
```
执行以下命令对您待评估工具生成的进行预处理：

```
cd evaluate_tool
python clean_photo.py --tool_name tool_name --download_dir ../datasets/
```

6. 计算分数

请执行以下命令计算分数, 其中 `--tool_name`为您待评估的工具名称, `--document_types`为可选的11种类型对应标签，默认包含所有类型，您也可以指定需要评估的某个或多个类型，多个类型请用空格分开; `--download_dir`指定json文件保存的路径。
```
cd evaluate_tool
python markdown_calculate.py --tool_name tool_name --download_dir ../datasets/ --document_types <document_types> --results xx.json
```

# 使用示例

使用评估工具对marker工具的学术文献类型进行评估，并生成结果文件。示例如下：
```
cd evaluate_tool
python clean_photo.py --tool_name annotations --download_dir ../datasets/
python clean_photo.py --tool_name marker --download_dir ../datasets/
python markdown_calculate.py --tool_name marker --download_dir ../datasets/ --results result.json --document_types academic_literature 
```
结果文件见[result.json](evaluate_tool/result.json), 结果包含了每个PDF文件对应的分数，以及所选`document_types`的分数，以及整体平均分数。


# 致谢
- [marker](https://github.com/VikParuchuri/marker?tab=readme-ov-file)
  
# 联系方式

关于数据集的任何问题，请通过微信联系作者：opendatalab_yunying。

