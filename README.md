English | [简体中文](README-zh.md)

# Introduction
   MPB (Miner-PDF-Benchmark) is an end-to-end PDF document comprehension evaluation suite designed for large-scale model data scenarios. It ensures human readability at the file granularity and provides PDF categorization tags. The total dataset comprises 350 PDF files and 8410 pages of PDFs, including 11 types of datasets such as books, textbooks, academic literature, PPT to PDF conversions, and examination papers. It serves as a reference for evaluating PDF document comprehension capabilities for developers of large-scale model data and tool developers.
   
# Dataset Source
The MPB dataset is sourced from a variety of origins, including arXiv, Sci-Hub, textbooks, examination papers, historical documents, etc. The sources and composition of different subsets are as follows:

| Document Type             | Tag                 | File Count | Total Pages | Description                                                                                    |
|---------------------------|---------------------|-------------|--------------|------------------------------------------------------------------------------------------------|
| Research Reports           | research_report     | 70          | 875          | Contains rich tabular information with single-column, double-column, and complex layouts.       |
| Ordinary Textbooks        | ordinary_textbook   | 40          | 388          | Single-column layout, black and white, includes a wealth of formulas.                         |
| Academic Literature        | academic_literature | 183         | 3323         | Data sourced from arXiv and Sci-Hub, includes single-column, double-column, charts, formulas, and other complex formats. |
| Atlas                     | atlas               | 3           | 269          | Characterized by a single page containing large area images.                                 |
| Courseware (PPT to PDF)   | courseware         | 7           | 383          | Includes subjects such as Biology, Chinese, English, and Physics.                              |
| Special Exam Papers       | special_exam_paper  | 3           | 80           | Includes watermarks, text within graphics, primary school Pinyin, and math problems.         |
| Historical Documents       | historical_documents | 1           | 3            | The Layout is vertical, and the reading order is from right to left.                                     |
| Notes                      | notes               | 3           | 293          | Includes handwritten notes from three junior high school students.                            |
| Ordinary Exam Papers       | ordinary_exam_paper | 27          | 372          | Includes subjects such as Computer Science, Mathematics, and Chinese, covering primary school, junior high school, high school, and industry question banks, mainly in black and white. |
| Colorful Textbooks        | colorful_textbook   | 3           | 144          | Includes subjects such as English, Mathematics, and Chinese (including Pinyin), containing colorful graphic information. |
| Ordinary Books             | ordinary_books      | 10          | 2280         | Single-column layout, black and white background books.                                       |

Note: All our data comes from the internet.

# Statistics of MPB

<img src="https://github.com/quyuan01/pdf-extract-bench/assets/102640628/43176747-4f03-42ad-b48b-a4448fc0dc0e" width="350" height="200" alt="The distribution of pages">  

<img src="https://github.com/quyuan01/pdf-extract-bench/assets/102640628/fb06f784-f22f-4897-9b7e-00cf7f622e38" width="350" height="200" alt="The distribution of PDF file"> 

<img src="https://github.com/quyuan01/pdf-extract-bench/assets/102640628/d233a4ca-c54a-41f3-be96-8b80b1b0b740" width="350" height="200" alt="The distribution of md language">  
<img src="https://github.com/quyuan01/pdf-extract-bench/assets/102640628/5ff056a7-6094-420b-8a93-a31585da9451" width="350" height="200" alt="The distribution of PDF  Type">  

# Metrics

We use [metrics](docs/Metric.md) to evaluate the extraction tools.

# Results

We have evaluated extraction tools, including nogout, marker, doc2x, ocrmath, and mathpix. The results are as follows.

### Overall Average Score
| Solution               | Extraction Rate (↑) | Similarity Score (↑) | Edit Distance (↓) | BLEU Score (↑) |
|------------------------|----------------------|----------------------|------------------|------------------|
| nogout (Open-Source Tool)                 | 100%                 | 0.35                 | 0.57             | 0.33             |
| marker (Open-Source Tool)                 | 99.4%                | 0.47                 | 0.42             | 0.386            |
| doc2x (Commercial Tool)| 99%                  | 0.67                 | 0.189            | 0.611            |
| ocrmath (Commercial Tool) | 92%                 | 0.56                 | 0.38             | 0.39             |
| **mathpix (Commercial Tool)** | **100%**                | **0.83**                 | **0.08**             | **0.91**         |

### Scores of 11 Types
<img src="https://github.com/quyuan01/pdf-extract-bench/assets/102640628/473223d0-fee9-4158-8b79-52c09066d8e1" width="350" height="200" alt="The distribution of sim_socre">  

<img src="https://github.com/quyuan01/pdf-extract-bench/assets/102640628/eb537cf8-f8d0-4815-b1c4-0494d72aa9ae" width="350" height="200" alt="The distribution of edit distance">  

<img src="https://github.com/quyuan01/pdf-extract-bench/assets/102640628/f358d113-72fd-4cea-9f68-d46f01249219" width="350" height="200" alt="The distribution of bleu">  

notes:
- marker's test version is v0.2.8;
- nogout's test version is v0.1.0 small;
  
# Get Data
Datasets can be downloaded from [OpenDataLab](https://opendatalab.com/OpenDataLab/Miner-PDF-Benchmark/tree/main);

# Usage
  
1. Clone the project into your environment.

```
git clone https://github.com/opendatalab/Miner-PDF-Benchmark
cd Miner-PDF-Benchmark
```
2. Install

```
python -m pip install -r requirements.txt
```

3. Download the evaluation set

Download the evaluation set from [OpenDataLab](https://opendatalab.com/OpenDataLab/Miner-PDF-Benchmark/tree/main), and unzip the evaluation set into the `datasets` directory, ensuring the datasets directory contains `pdf` and `annotations`.
After downloading all of them, organize the data as follows:

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

4. Preprocess the evaluation set

Since the images in the evaluation set have not been evaluated yet, you need to execute the following command to preprocess the images:

```
cd evaluate_tool
python clean_photo.py --tool_name annotations --download_dir ../datasets/
```

5. Prepare the datasets for tools to be evaluated

Please copy the `Markdown` file generated by the evaluation tool you need to evaluate to the `datasets/document_types/tool_name` directory. `document_types` is the label corresponding to the 11 categories, and `tool_name` is the name of tools to be evaluated.
The directory structure after copying is as follows:
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

Execute the following command to preprocess the dataset generated by the tool you want to evaluate:
```
cd evaluate_tool
python clean_photo.py --tool_name tool_name --download_dir ../datasets/
```

6. Calculate the score

Please execute the following command to calculate the score, `--tool_name` is the name of the tool you want to evaluate, `--document_types` is the optional 11 types of corresponding labels, which includes all types by default. You can also specify one or more types to be evaluated, please separate multiple types with spaces; `--download_dir` specifies the path where the json file is saved.

```
cd evaluate_tool
python markdown_calculate.py --tool_name tool_name --download_dir ../datasets/ --document_types <document_types> --results xx.json
```

# Demo

The following is a demo of the evaluation of the `marker` tool in the document type of academic_literature.
```
cd evaluate_tool
python clean_photo.py --tool_name annotations --download_dir ../datasets/
python clean_photo.py --tool_name marker --download_dir ../datasets/
python markdown_calculate.py --tool_name marker --download_dir ../datasets/ --results result.json --document_types academic_literature 
```
Here [result.json](evaluate_tool/result.json) are the results: The result.json file contains scores for each PDF file, scores for the selected document_types, and the overall average score.

# Contact
For any questions about the dataset, please contact the authors by WeChat opendatalab_yunying.
