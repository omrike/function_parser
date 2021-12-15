import os
import pandas as pd

from function_parser.language_data import LANGUAGE_METADATA
from function_parser.process import DataProcessor
from tree_sitter import Language


def main():
    language = 'python'
    DataProcessor.PARSER.set_language(Language('C:/Users/omrik/Documents/semester_7/Data Augmentation Project/function_parser' + '/tree-sitter-languages.so',language))
    processor = DataProcessor(language=language,language_parser=LANGUAGE_METADATA[language]['language_parser'])
    dependee = 'keras-team/keras'
    definitions = processor.process_dee(dependee, ext=LANGUAGE_METADATA[language]['ext'])
    definitions_pd = pd.DataFrame(definitions)
    print(pd.DataFrame(definitions).head())

    library_candidates = {}
    library_candidates[dependee.split('/')[-1]] = definitions
    dependent = dependee  # 'eriklindernoren/Keras-GAN'
    # Generate approximate call graph
    calls, edges = processor.process_dent(dependent, ext=LANGUAGE_METADATA[language]['ext'],
                                          library_candidates=library_candidates)
    pd.DataFrame(calls).head()

if __name__ == '__main__':
    main()