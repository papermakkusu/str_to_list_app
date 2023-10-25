import re
import codecs
from copy import copy


class StrToListApp:

    filter_param = re.compile(r'\d{2,}')

    @staticmethod
    def __filter_digits(input_text: str):
        inp_txt = codecs.escape_decode(bytes(copy(input_text), "utf-8"))[0].decode("utf-8")
        substring = re.sub(StrToListApp.filter_param, str(), inp_txt)
        return substring

    @staticmethod
    def convert(data: str):
        if type(data) == str:
            return list(StrToListApp.__filter_digits(data))
        raise TypeError

