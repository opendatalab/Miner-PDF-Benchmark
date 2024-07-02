English | [简体中文](README-zh.md)

# Introduction
   MPB (Miner-PDF-Benchmark) is an end-to-end PDF document comprehension evaluation suite designed for large-scale model data scenarios. It ensures human readability at the file granularity and provides PDF categorization tags. The dataset comprises 350 PDF files and 8410 pages of PDFs, including 11 types of datasets such as books, textbooks, academic literature, PPT to PDF, and examination papers. It serves as a reference for evaluating PDF document comprehension capabilities for developers of large-scale model data and tool developers.
   
# Dataset Source
The MPB dataset is sourced from various origins, including arXiv, Sci-Hub, textbooks, examination papers, historical documents, etc. The source and composition of different subsets are as follows:

| Document Type             | Tag                 | Total Files | Total Pages | Description                                                                                    |
|---------------------------|---------------------|-------------|--------------|------------------------------------------------------------------------------------------------|
| Research Report           | research_report     | 70          | 875          | Research reports are from the Internet, with large tables, complex merged tables, horizontal tables mixed with text, single-column, double-column, and complex layouts       |
| Ordinary Textbook        | ordinary_textbook   | 40          | 388          | The textbooks are from the Internet, with a single-column layout, black and white colors, nested complex formulas, and containing complex matrices.               |
| Academic Literature        | academic_literature | 183         | 3323         | Academic documents are from arXiv and SCIHUB, and have complex layouts including single-column, double-column, charts, formulas, etc. |
| Atlas                     | atlas               | 3           | 269          | Atlas is from the Internet, with the characteristic of a single page containing a large area of ​​pictures |
| Courseware (PPT to PDF)   | courseware         | 7           | 383          | The PDF files are converted from PPT on the Internet, have background color, and contain four subjects: biology, Chinese, English, and physics;|
| Special Exam Paper       | special_exam_paper  | 3           | 80           | Special Exam Papers are from the Internet, have the characteristics of test paper layout, watermark, and text in graphics, and the content includes elementary school pinyin questions and math test questions;         |
| Historical Document       | historical_document | 1           | 3            |  Historical documents are from the Internet, have the characteristics of vertical layout, reading order from right to left, and traditional Chinese font;   |
| Note                     | note               | 3           | 293          | The notes are handwritten from the Internet. They include handwritten notes from 3 junior high school students.  |
| Ordinary Exam Paper      | ordinary_exam_paper | 27          | 372          | Ordinary test papers are from the Internet, with the characteristics of a test paper layout and a mainly black and white background. They include subjects such as computer science, mathematics, and Chinese, covering elementary school, junior high school, high school, and industry question banks. |
| Colorful Textbook        | colorful_textbook   | 3           | 144          | The colorful textbooks are from the Internet and have the characteristics of containing special graphic information. The contents include subjects such as English, mathematics, Chinese (including pinyin), etc. |
| Ordinary Book             | ordinary_book     | 10          | 2280         | Ordinary books come from Internet books, characterized by a single-column layout and a black and white background. |

Note: All our data comes from the internet.

# Statistics of MPB


<img src="https://github.com/opendatalab/Miner-PDF-Benchmark/assets/102640628/cb538c40-d4da-4b21-9367-26e9bb192cee" width="350" height="200" alt="The distribution of pages">  
<img src="https://github.com/opendatalab/Miner-PDF-Benchmark/assets/102640628/a41dc7b7-831d-4642-a8bc-01ddd26dece7" width="350" height="200" alt="The distribution of PDF file"> 

<img src="https://github.com/quyuan01/pdf-extract-bench/assets/102640628/d233a4ca-c54a-41f3-be96-8b80b1b0b740" width="350" height="200" alt="The distribution of md language">  
<img src="https://github.com/quyuan01/pdf-extract-bench/assets/102640628/5ff056a7-6094-420b-8a93-a31585da9451" width="350" height="200" alt="The distribution of PDF  Type">  

# Metrics

We use [metrics](docs/Metric.md) to evaluate the extraction tools.

# Results

We have evaluated extraction tools, including nogout, marker, MinerU, doc2x, ocrmath, and mathpix. The results are as follows.

### Overall Average Score
| Solution               | Extraction Rate (↑) | Similarity Score (↑) | Edit Distance (↓) | BLEU Score (↑) |
|------------------------|----------------------|----------------------|------------------|------------------|
| [MinerU (Open-Source Tool)](https://github.com/magicpdf/Magic-PDF)                 | 98.4%                 | 0.61                 | 0.3             |0.47             |
| [nogout (Open-Source Tool)](https://github.com/facebookresearch/nougat)                 | 100%                 | 0.35                 | 0.57             | 0.33             |
| [marker (Open-Source Tool)](https://github.com/VikParuchuri/marker)                 | 99.4%                | 0.47                 | 0.42             | 0.386            |
| [doc2x (Commercial Tool)](https://doc2x.com/)| 99%                  | 0.67                 | 0.189            | 0.611            |
| [ocrmath (Commercial Tool)](https://open.ocrmath.com/) | 92%                 | 0.56                 | 0.38             | 0.39             |
| [**mathpix (Commercial Tool)**](https://mathpix.com/) | **100%**                | **0.83**                 | **0.08**             | **0.91**         |

### Scores of 11 Types

<img src="https://github.com/opendatalab/Miner-PDF-Benchmark/assets/102640628/da7d62c6-b255-4a83-873c-b36979d82126" width="400" height="350" alt="The distribution of sim_socre">  

<img src="https://github.com/opendatalab/Miner-PDF-Benchmark/assets/102640628/8c113adc-214e-43c0-9448-d5be750695d1" width="400" height="350" alt="The distribution of edit distance">  

<img src="https://github.com/opendatalab/Miner-PDF-Benchmark/assets/102640628/e37753c6-1d07-4834-8220-c78377917886" width="400" height="350" alt="The distribution of bleu">  

notes:
- marker's test version is v0.2.8;
- nogout's test version is v0.1.0 small;
- MinerU's test version is v0.5.11;
- Ocrmath's test time is about Early June;
- Doc2x's test time is about May;
- Mathpix's test time is in Early May;
  
# Get Data
Datasets can be downloaded from [OpenDataLab](https://opendatalab.com/OpenDataLab/Miner-PDF-Benchmark/tree/main);

# Usage
  
1. Clone the project into your environment.

```
git clone https://github.com/opendatalab/Miner-PDF-Benchmark
cd Miner-PDF-Benchmark
```
2. Install(Python 3.9 is recommended)

```
python -m pip install -r requirements.txt
```

3. Download the evaluation set

Download the evaluation set from [OpenDataLab](https://opendatalab.com/OpenDataLab/Miner-PDF-Benchmark/tree/main)(sdk/cli is recommended), and unzip the evaluation set into the `datasets` directory, ensuring the datasets directory contains `pdf` and `annotations`.
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
