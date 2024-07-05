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


# Acknowledgments
- [marker](https://github.com/VikParuchuri/marker?tab=readme-ov-file)


# Contact
For any questions about the dataset, please contact the authors by WeChat opendatalab_yunying.
