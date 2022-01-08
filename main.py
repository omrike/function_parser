import os
import pandas as pd
import tree_sitter

from function_parser.language_data import LANGUAGE_METADATA
from function_parser.process import DataProcessor
from tree_sitter import Language


def main():
    language = 'haskell'
    # Language.build_library(
    #     # Store the library in the directory
    #     'tree-sitter-languages.so',
    #     # Include one or more languages
    #     [
    #         'C:/Users/omrik/Documents/semester_7/Data Augmentation Project/function_parser/tree-sitter-haskell',
    #         'C:/Users/omrik/Documents/semester_7/Data Augmentation Project/function_parser/tree-sitter-python'
    #     ]
    # )

    DataProcessor.PARSER.set_language(Language('C:/Users/omrik/Documents/semester_7/Data Augmentation Project/function_parser/tree-sitter-languages.so',language))
    processor = DataProcessor(language=language,language_parser=LANGUAGE_METADATA[language]['language_parser'])
    dependee = 'haskell/parsec'
    # dependee = 'keras-team/keras'
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