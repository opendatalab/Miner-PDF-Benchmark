"""
Calculating performance indicators
"""
import argparse
import json
import os
import re

import nltk
from Levenshtein import distance
from nltk.tokenize import word_tokenize
from nltk.translate.bleu_score import SmoothingFunction, sentence_bleu

nltk.download('punkt')
import scoring

parser = argparse.ArgumentParser(description='get directory')
parser.add_argument(
    '--document_types',
    nargs='+',
    choices=[
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
    ],
    help='Choose one or more document_types',
    default=[
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
    ],
)

parser.add_argument(
    '--tool_name',
    type=str,
    required=True,
    help='tool name',
)
parser.add_argument(
    '--download_dir',
    type=str,
    required=True,
    help='input download dir',
)
parser.add_argument(
    '--results',
    type=str,
    required=True,
    help='results path(end with .json)',
)
args = parser.parse_args()
fw = open(args.results, 'w+', encoding='utf-8')


def simple_bleu_score(candidate, reference):
    """
    Calculating BLEU score
    """
    candidate_tokens = word_tokenize(candidate)
    reference_tokens = word_tokenize(reference)
    return sentence_bleu([reference_tokens], candidate_tokens, smoothing_function=SmoothingFunction().method1)


class Scoring:
    """
    Calculating performance indicators
    """

    def __init__(self):
        self.edit_distances = []
        self.bleu_scores = []
        self.sim_scores = []
        self.filenames = []
        self.score_dict = {}
        self.annotation_cnt = 0

    def preprocess_string(self, input_str):
        """
        Args:
            input_str: String to be processed
        """
        sub_enter = re.sub(r'\n+', '\n', input_str)
        return re.sub(r' {2}', ' ', sub_enter)

    def calculate_similarity(self, annotation, actual, tool_name):
        """
        Calculate simscore
        """
        class_dict = {}
        edit_distances = []
        bleu_scores = []
        sim_scores = list()
        total_file = 0
        for filename in os.listdir(annotation):
            if filename.endswith('.md') and not filename.startswith('.'):
                total_file = total_file + 1
                with open(os.path.join(annotation, filename), 'r', encoding='utf-8') as file_a:
                    content_a = file_a.read()
                self.annotation_cnt = self.annotation_cnt + 1
                filepath_b = os.path.join(actual, filename)
                if os.path.exists(filepath_b):
                    with open(filepath_b, 'r', encoding='utf-8') as file_b:
                        content_b = file_b.read()
                        self.filenames.append(filename)
                        edit_dist = distance(
                            self.preprocess_string(content_b), self.preprocess_string(content_a)
                        ) / max(len(content_a), len(content_b))
                        self.edit_distances.append(edit_dist)
                        edit_distances.append(edit_dist)
                        bleu_score = simple_bleu_score(content_b, content_a)
                        bleu_scores.append(bleu_score)
                        self.bleu_scores.append(bleu_score)
                        # Calculate simscore score, refer to (https://github.com/VikParuchuri/marker?tab=readme-ov-file)
                        simscore = scoring.score_text(content_b, content_a)
                        sim_scores.append(simscore)
                        self.sim_scores.append(simscore)
                        class_dict[filename] = {'edit_dist': edit_dist, 'bleu_score': bleu_score, 'sim_score': simscore}
                        self.score_dict[filename] = {
                            'edit_dist': edit_dist,
                            'bleu_score': bleu_score,
                            'sim_score': simscore,
                        }
                else:
                    print(f'File {filename} not found in actual directory.')
        class_average_edit_distance = sum(edit_distances) / len(edit_distances) if edit_distances else 0
        class_average_bleu_score = sum(bleu_scores) / len(bleu_scores) if bleu_scores else 0
        class_average_sim_score = sum(sim_scores) / len(sim_scores) if sim_scores else 0
        fw.write(json.dumps(class_dict, ensure_ascii=False) + '\n')
        ratio = len(class_dict) / total_file
        fw.write(f'{tool_name} extract ratio:  {ratio}' + '\n')
        fw.write(f'{tool_name} Average Levenshtein Distance: {class_average_edit_distance}' + '\n')
        fw.write(f'{tool_name} Average BLEU Score: {class_average_bleu_score}' + '\n')
        fw.write(f'{tool_name} Average Sim Score: {class_average_sim_score}' + '\n')

        print(f'{tool_name} extract ratio: {ratio}')
        print(f'{tool_name} Average Levenshtein Distance: {class_average_edit_distance}')
        print(f'{tool_name} Average BLEU Score: {class_average_bleu_score}')
        print(f'{tool_name} Average Sim Score: {class_average_sim_score}')
        return self.score_dict

    def summary_scores(self):
        """
        Calculate the overall average
        """
        average_edit_distance = sum(self.edit_distances) / len(self.edit_distances) if self.edit_distances else 0
        average_bleu_score = sum(self.bleu_scores) / len(self.bleu_scores) if self.bleu_scores else 0
        average_sim_score = sum(self.sim_scores) / len(self.sim_scores) if self.sim_scores else 0
        fw.write(f'Overall extract cnt: {len(self.score_dict) / self.annotation_cnt}' + '\n')
        fw.write(f'Overall Average Levenshtein Distance: {average_edit_distance}' + '\n')
        fw.write(f'Overall Average BLEU Score: {average_bleu_score}' + '\n')
        fw.write(f'Overall Average Marker Score: {average_sim_score}' + '\n')
        print(f'Overall extract ratio: {len(self.score_dict) / self.annotation_cnt}')
        print(f'Overall Average Levenshtein Distance: {average_edit_distance}')
        print(f'Overall Average BLEU Score: {average_bleu_score}')
        print(f'Overall Average Marker Score: {average_sim_score}')
        fw.close()

    def calculate_similarity_total(self, tool_name, document_types, data_dir):
        """
        write result
        """
        for file_type in document_types:
            annotation = os.path.join(data_dir, file_type, 'annotations', 'cleaned')
            actual = os.path.join(data_dir, file_type, tool_name, 'cleaned')
            self.calculate_similarity(annotation, actual, file_type)


if __name__ == '__main__':
    file_types = list()
    tool_type = args.tool_name
    download_dir = args.download_dir
    if args.document_types:
        print('Selected types:', args.document_types)
        for type_ in args.document_types:
            file_types.append(type_)
    else:
        print('No types selected')
    print(f'Type {file_types} is selected. Executing related operations...')
    score = Scoring()
    score.calculate_similarity_total(tool_type, file_types, download_dir)
    score.summary_scores()
