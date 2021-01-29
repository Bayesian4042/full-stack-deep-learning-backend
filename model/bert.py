from transformers import pipeline
import wikipedia

BERT_PIPELINE = pipeline("question-answering")
BART_SUMMARY = pipeline("summarization")


def find_answer(q, term):
    wikipedia.set_lang('en')
    context = wikipedia.page(term).summary
    return BERT_PIPELINE({
        'question': q,
        'context': context})
