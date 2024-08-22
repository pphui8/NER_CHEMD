## customized training

1. Download the .cfg file.

2. Cover the .cfg file in the `models` folder.
```bash
python -m spacy init fill-config base_config.cfg config.cfg
```

3. load data, write mode, make a .spaCy file
```bash
cd dataset
python Transfer.py
```
4. train  
| here paths.dev we simply use train
```bash
python -m spacy train config.cfg --output ./output --paths.train ./dataset/train.spacy --paths.dev ./dataset/train.spacy
```