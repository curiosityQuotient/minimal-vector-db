"""
A minimal implementation of a vector database using pandas

CuriosityQuotient, 2024
"""

import pandas as pd
from pypdf import PdfReader


class documentLoader:
    """
    A class for loading documents to text and chunking them.
    """

    def load_pdf(self, filepath: str):

        # load pdf
        text = ""
        self.text = text
