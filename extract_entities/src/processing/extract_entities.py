from pathlib import Path
import spacy

data_dir = Path.cwd().joinpath("extract_entities", "data", "raw")

file_to_open = data_dir / "science-raw.txt"

# Load the large English NLP model
nlp = spacy.load('en_core_web_lg')

# # Load the text we want to examine
with open(file_to_open, 'r') as textFile:
  # The text we want to examine
  text = textFile.read()

# # Parse the text with spaCy. This runs the entire pipeline.
doc = nlp(text)

# 'doc' now contains a parsed version of text. We can use it to do anything we want!
# For example, this will print out all the named entities that were detected:
for entity in doc.ents:
    print(f"{entity.text} ({entity.label_})")
