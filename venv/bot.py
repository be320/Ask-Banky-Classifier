import re
import pandas as pd


def text_normalize(text):
    text = str(text)
    # denoise
    noise = re.compile(""" ّ    | # Tashdid
                             َ    | # Fatha
                             ً    | # Tanwin Fath
                             ُ    | # Damma
                             ٌ    | # Tanwin Damm
                             ِ    | # Kasra
                             ٍ    | # Tanwin Kasr
                             ْ    | # Sukun
                             ـ     # Tatwil/Kashida
                         """, re.VERBOSE)
    text = re.sub(noise, '', text)
    # text normalizer
    text = re.sub(r"أ|إ|آ", "ا", text)
    text = re.sub(r"ء|ئ|ؤ", "ء", text)
    text = re.sub(r"ى|ي", "ي", text)
    text = re.sub(r"ه|ة", "ه", text)

    # number noramlize
    text = re.sub(r"\d+", "NUM", text)

    # remove non letters
    text = re.sub(r"\W", " ", text)

    # if the word is very small neglect it
    text = " ".join([word for word in text.split() if len(word) >= 3])

    return text



def chat(inp):
    dataset = pd.DataFrame()