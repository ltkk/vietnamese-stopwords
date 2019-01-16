import regex as re
import utils
from pyvi import ViTokenizer
EMAIL = re.compile(r"([\w0-9_\.-]+)(@)([\d\w\.-]+)(\.)([\w\.]{2,6})")
URL = re.compile(r"https?:\/\/(?!.*:\/\/)\S+")
PHONE = re.compile(r"(09|01[2|6|8|9])+([0-9]{8})\b")
MENTION = re.compile(r"@.+?:")
NUMBER = re.compile(r"\d+.?\d*")
DATETIME = '\d{1,2}\s?[/-]\s?\d{1,2}\s?[/-]\s?\d{4}'

RE_HTML_TAG = re.compile(r'<[^>]+>')
RE_CLEAR_1 = re.compile("[^_<>\s\p{Latin}]")
RE_CLEAR_2 = re.compile("__+")
RE_CLEAR_3 = re.compile("\s+")


#
def word_tokenize(txt):
    try:
        data = {'txt': txt}
        respond = utils.call_api(data, "http://localhost:4567/tokenize", "POST")
        if respond.status_code == 200:
            return respond.text
        return txt
    except:
        return txt


class TextPreprocess:
    @staticmethod
    def replace_common_token(txt):
        txt = re.sub(EMAIL, ' ', txt)
        txt = re.sub(URL, ' ', txt)
        txt = re.sub(MENTION, ' ', txt)
        txt = re.sub(DATETIME, ' ', txt)
        txt = re.sub(NUMBER, ' ', txt)
        return txt

    @staticmethod
    def remove_emoji(txt):
        txt = re.sub(':v', '', txt)
        txt = re.sub(':D', '', txt)
        txt = re.sub(':3', '', txt)
        txt = re.sub(':\(', '', txt)
        txt = re.sub(':\)', '', txt)
        return txt

    @staticmethod
    def remove_html_tag(txt):
        return re.sub(RE_HTML_TAG, ' ', txt)

    def preprocess(self, txt, tokenize=True):
        txt = self.remove_html_tag(txt)
        txt = re.sub('&.{3,4};', ' ', txt)
        txt = utils.convertwindown1525toutf8(txt)
        if tokenize:
            txt = ViTokenizer.tokenize(txt)
        txt = txt.lower()
        txt = self.replace_common_token(txt)
        txt = self.remove_emoji(txt)
        txt = re.sub(RE_CLEAR_1, ' ', txt)
        txt = re.sub(RE_CLEAR_2, ' ', txt)
        txt = re.sub(RE_CLEAR_3, ' ', txt)
        txt = utils.chuan_hoa_dau_cau_tieng_viet(txt)
        return txt.strip()
