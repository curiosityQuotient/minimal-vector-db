"""
A minimal implementation of a vector database using pandas

CuriosityQuotient, 2024
"""

import pandas as pd
from pypdf import PdfReader


class DocumentLoader:
    """
    A class for loading documents to text and chunking them.
    """

    def load_pdf(self, filepath: str):
        """method for loading text from pdf into object"""
        # load pdf
        reader = PdfReader(filepath)
        text = ""
        for page in reader.pages:
            text = text + page.extract_text()
        self.text = text


class TextChunker:
    """
    A class for chunking text that has been loaded
    """

    def chunk_text(self, text: str, chunkLen: int, overlap: int):
        # add chunking function
        chunks = []
        chunkEnd = text.find(" ")
        while chunkEnd >= 0:
            chunkEnd = text.find(" ")
            nn = 0
            while nn < chunkLen and chunkEnd >= 0:
                chunkEnd = text.find(" ", chunkEnd + 1)
                nn += 1
            chunks.append(text[:chunkEnd])
            mm = 0
            nextChunk = chunkEnd
            while mm < overlap:
                nextChunk = text.rfind(" ", 0, nextChunk)
                mm += 1
            text = text[nextChunk:]
        self.chunks = chunks


docLoader = DocumentLoader()
docLoader.load_pdf("Everyone-loves-trees.pdf")
chunker = TextChunker()
chunker.chunk_text(docLoader.text, 25, 3)
print("lol")
