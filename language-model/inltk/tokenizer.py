from fastai.text import *
import sentencepiece as spm

class KannadaTokenizer(BaseTokenizer):
    def __init__(self, lang:str):
        self.lang = lang
        self.sp = spm.SentencePieceProcessor()
        self.sp.Load("/home/gaurav/PycharmProjects/nlp-for-kannada/tokenizer/kannada_lm.model")
        
    def tokenizer(self, t:str) -> List[str]:
        return self.sp.EncodeAsPieces(t)
