# Extracting Entities from Text

[spaCy](https://spacy.io/) is a popular NLP (natural language processing) Python library.

We can use spaCy to do named entity recognition on some text and see what you might get out of it.

spaCy provides pretrained models for several language already. In this example, we're going to leverage the [large English model](https://spacy.io/models/en#en_core_web_lg).

Essentially all this example is doing is using a pretrained model and extracting named entities from some text passage, in this case, a few paragraphs from the [science Wikipedia page](https://en.wikipedia.org/wiki/Science).

After outputting the discovered entities, you might have questions about what these types might be. Here's [documentation](https://spacy.io/usage/linguistic-features#entity-types) on spaCy about the types.
