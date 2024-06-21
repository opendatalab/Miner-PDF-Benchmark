# 简介
MPB（Miner-PDF-Benchmark）是一套为大规模模型数据场景设计的端到端PDF文档理解评估套件。它确保了文件粒度上的人类可读性，并提供了PDF分类标签。该数据集总共包含350个PDF文件和8410页PDF，包括书籍、教材、学术文献、PPT转PDF、试卷等11种类型的数据集。它为大规模模型数据的开发者和工具开发者提供了PDF文档理解能力的评估参考。


# 数据集来源
MPB 数据集来源于多种渠道，包括 arXiv、Sci-Hub、教科书、试卷、历史文献等，参考了 Llama 的语料库比例。不同子集的来源和组成如下：

| 类别           | 对应标签             | 文件数 | 总页数 | 简介                                                                 |
|----------------|----------------------|--------|--------|--------------------------------------------------------------------|
| 研报           | research_report      | 70     | 875    | 包含丰富的表格信息，有单栏、双栏和复杂布局；                         |
| 普通教材       | ordinary_textbook    | 40     | 388    | 单栏布局，颜色为黑白，包含丰富的公式；                                |
| 学术文献       | academic_literature  | 183    | 3323   | 数据来源于arXiv和SCIHUB，包括单栏、双栏、图表、公式等复杂版式       |
| 图册           | atlas               | 3      | 269    | 特征为单页包含大面积图片                                             |
| PPT2PDF        | courseware          | 7      | 383    | 包含生物、语文、英语、物理4个学科；                                   |
| 特殊图文试卷   | special_exam_paper   | 3      | 80     | 包含水印、文字在图形中、小学拼音和数学试题；                         |
| 历史文献       | historical_documents| 1      | 3      | 排版为竖排，阅读顺序从右到左；                                     |
| 笔记           | notes               | 3      | 293    | 包括3个初中的学生手写笔记                                           |
| 普通试卷       | ordinary_exam_paper  | 27     | 372    | 包括计算机科学、数学、语文等学科，涵盖小学、初中、高中、行业题库，背景以黑白为主； |
| 特殊图文教材   | colorful_textbook    | 3      | 144    | 包括英语、数学、中文（含拼音）等学科，包含彩色图形信息；             |
| 普通书         | ordinary_books       | 10     | 2280   | 单栏布局、背景为黑白色的书，包含计算机、文学、建筑领域的书籍；       |

# 统计信息
<img src="https://github.com/quyuan01/pdf-extract-bench/assets/102640628/43176747-4f03-42ad-b48b-a4448fc0dc0e" width="350" height="200" alt="The distribution of pages">  

<img src="https://github.com/quyuan01/pdf-extract-bench/assets/102640628/fb06f784-f22f-4897-9b7e-00cf7f622e38" width="350" height="200" alt="The distribution of PDF file"> 

<img src="https://github.com/quyuan01/pdf-extract-bench/assets/102640628/d233a4ca-c54a-41f3-be96-8b80b1b0b740" width="350" height="200" alt="The distribution of md language">  
<img src="https://github.com/quyuan01/pdf-extract-bench/assets/102640628/5ff056a7-6094-420b-8a93-a31585da9451" width="350" height="200" alt="The distribution of PDF  Type">  

# 指标

## 提取率
提取率（ER）是从PDF文件成功生成Markdown（.md）文件的数量与PDF文件总数的比率。

$$ \text{ER} = \frac{\text{hypothesiscnt}}{\text{referencecnt}} $$

## 相似度得分

### 相似得分
对于一组假设文本块 `H` 和一组参考文本块 `R`，使用函数 $F(H_{\text{chunk}}, R_{\text{chunk}})$ 计算每个假设文本块与参考文本块之间的最大相似度得分，该函数返回0到1之间的值。

$${maxscore}(H_{\text{chunk}}, R) = \max_{R_{\text{chunk}} \in R} \left[ F(H_{\text{chunk}}, R_{\text{chunk}}) \right]$$

### 平均得分
对于所有假设文本块的最大得分集合 `maxscore`，计算平均得分 $ \text{Mean\_score} $：

$$\text{Mean\\_score} = \text{mean}(maxscore)$$

### 最终得分
最终得分是假设文本块集合与参考文本块集合之间的平均对齐得分，表示为 $ \text{Score}(T_H, T_R) $：

$$ \text{Score}(T_H, T_R) = \text{Mean}\left(\max_{R_{\text{chunk}} \in R} \left[F(H_{\text{chunk}}, R_{\text{chunk}}) \right]\right) $$

## 编辑距离

### 描述
它是一种测量两个字符串之间差异的方法。它定义为将一个字符串转换为另一个字符串所需的最少单字符编辑操作次数。这些编辑操作包括插入、删除和替换字符。

### 用途
为了减少换行和空格对得分的影响，我们在预处理后计算两个字符串之间的编辑距离。

### 引用
[Levenshtein, V.I., et al.: Binary codes capable of correcting deletions, insertions,
and reversals. In: Soviet physics doklady. vol. 10, pp. 707–710. Soviet Union (1966)]
https://nymity.ch/sybilhunting/pdf/Levenshtein1966a.pdf


## BLEU

### 描述
BLEU分数是一个介于0到1之间的值，较高的BLEU分数通常表示更好的翻译质量。

### 用途
我们在nltk分词后计算两个字符串的sentence_bleu，使用method1作为平滑函数。

### 引用
[Papineni, K., Roukos, S., Ward, T., Zhu, W.J.: Bleu: a method for automatic
evaluation of machine translation. In: Proceedings of the 40th annual meeting of
the Association for Computational Linguistics. pp. 311–318 (2002)]
https://aclanthology.org/P02-1040.pdf 

# 结果
### 总体平均得分
| 方案         | 抽取率（↑） | sim_score(↑) | 编辑距离(↓) | bleu(↑) |
|--------------|--------------|--------------|--------------|----------|
| nogout       | 100%         | 0.35         | 0.57         | 0.33     |
| marker       | 99.4%        | 0.47         | 0.42         | 0.386    |
| doc2x（商业工具） | 99%          | 0.67         | 0.189        | 0.611    |
| ocrmath（商业工具） | 92%          | 0.56         | 0.38         | 0.39     |
| mathpix（商业工具） | 100%         | 0.83         | 0.08         | 0.91     |

### 11种类型的得分
<img src="https://github.com/quyuan01/pdf-extract-bench/assets/102640628/473223d0-fee9-4158-8b79-52c09066d8e1" width="350" height="200" alt="The distribution of sim_socre">  

<img src="https://github.com/quyuan01/pdf-extract-bench/assets/102640628/eb537cf8-f8d0-4815-b1c4-0494d72aa9ae" width="350" height="200" alt="The distribution of edit distance">  

<img src="https://github.com/quyuan01/pdf-extract-bench/assets/102640628/f358d113-72fd-4cea-9f68-d46f01249219" width="350" height="200" alt="The distribution of bleu">  

# 获取数据
数据集可以从[OpenDataLab](https://opendatalab.com/OpenDataLab/Miner-PDF-Benchmark/tree/main)下载；

# 使用方法
1. **步骤1**  
   
将项目克隆到您的环境。

```
git clone https://github.com/opendatalab/Miner-PDF-Benchmark
cd Miner-PDF-Benchmark
```

2. **步骤2**  
   
安装依赖。

```
python -m pip install -r requirements.txt
```

3. **步骤3**  

评测集准备。

请从[OpenDataLab](https://opendatalab.com/OpenDataLab/Miner-PDF-Benchmark/tree/main)下载评测集，并将评测集解压到`datasets`目录下，确保`datasets`目录下为`pdf`和`annotations`。


4. **步骤4**  
   
评测集预处理。

由于当前未对评测集中的图片评测，您需要执行以下命令对图片预处理：
```
cd evaluate_tool
python clean_photo.py --tool_type annotations --download_dir ../datasets
```

5. **步骤5**

待评估工具的数据集准备。

请将您需要评估工具生成的`Markdown`文件按照类型复制到`datasets/tool_type/tool_name`目录中,`too_type`为11种类别对应的标签,`tool_name`为您的工具名称。
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
python clean_photo.py --tool_type tool_name --download_dir ../datasets/
```

6. **步骤6**
  
计算分数。

请执行以下命令计算分数, 其中 `--tool_type`为您待评估的工具名称, `--file_types`为可选的11种类型对应标签，默认包含所有类型，您也可以指定需要评估的某个或多个类型，多个类型请用空格分开; `--download_dir`指定json文件保存的路径。
```
cd evaluate_tool
python markdown_calculate.py --tool_type tool_name --download_dir ../datasets/ --results xx.json
```

# 联系方式

关于数据集的任何问题，请通过微信联系作者：opendatalab_yunying。

