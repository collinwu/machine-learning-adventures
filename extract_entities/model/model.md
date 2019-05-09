# Leveraging a spaCy language model

In this case, let's leverage the `en_core_web_lg` model.

> English multi-task CNN trained on OntoNotes, with GloVe vectors trained on Common Crawl. Assigns word vectors, context-specific token vectors, POS tags, dependency parse and named entities.

To install, run:
`$python -m spacy download en_core_web_lg`

Then you can load the model via `spacy.load('en_core_web_lg)`
