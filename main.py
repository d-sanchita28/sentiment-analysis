import spacy
#from spacy.pipeline import Sentencizer
import pandas as pd

from preprocess import preprocess, construct_spacy_obj
import ft
import training
from feature_extraction import feature_extraction
from classification import classify

nlp = spacy.load('en_core_web_sm')
# sentencizer = Sentencizer(punct_chars=[".", "!", "?", "\n", "\r", ";"])
# nlp.add_pipe(sentencizer)
if "sentencizer" not in nlp.pipe_names:
    nlp.add_pipe("sentencizer", config={"punct_chars": [".", "!", "?", "\n", "\r", ";"]})
ft_model = ft.get_model()
model = training.get_model(nlp, ft_model)

def get_features_and_classification(filename):
	df = pd.read_csv("csv_files/" + filename, header=None, names=['reviewText', 'rating'])
	df = preprocess(df, nlp)
	df = construct_spacy_obj(df, nlp)

	features = feature_extraction(df, ft_model, nlp)
	result, _, __ = classify(df, features, model)

	return features, result