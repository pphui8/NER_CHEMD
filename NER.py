import spacy

print("Loading from", ".\SrpCNNER\SrpCNNER")
nlp = spacy.load(".\SrpCNNER\SrpCNNER")
print("Loaded")
text = "Van Gogh's early works consist of mostly still lifes and depictions of peasant laborers. In 1886, he moved to Paris, where he met members of the artistic avant-garde, including Émile Bernard and Paul Gauguin, who were seeking new paths beyond Impressionism. Frustrated in Paris and inspired by a growing spirit of artistic change and collaboration, in February 1888, Van Gogh moved to Arles in southern France to establish an artistic retreat and commune. Once there, Van Gogh's art changed. His paintings grew brighter and he turned his attention to the natural world, depicting local olive groves, wheat fields and sunflowers. Van Gogh invited Gauguin to join him in Arles and eagerly anticipated Gauguin's arrival in the fall of 1888."
doc = nlp(text)
for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)