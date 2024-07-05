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


# 致谢
- [marker](https://github.com/VikParuchuri/marker?tab=readme-ov-file)
  
# 联系方式

关于数据集的任何问题，请通过微信联系作者：opendatalab_yunying。

