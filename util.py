# encoding=utf8

from pytorch_pretrained_bert.tokenization import BertTokenizer


class BertTokenizerCn(BertTokenizer):

    def __init__(self, vocab_file, do_lower_case=True, max_len=None):
        super(BertTokenizerCn, self).__init__(vocab_file, do_lower_case, max_len)
        self.do_lower_case = do_lower_case

    def tokenize_char_cn(self, text):
        """Tokenizes a piece of text."""
        text = text.strip()
        if not text:
            return []

        if self.do_lower_case:
            tokens = [c for c in text.lower()]
        else:
            tokens = [c for c in text]
        return tokens

