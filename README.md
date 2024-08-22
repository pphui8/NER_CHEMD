# NER_CHEMD
spaCy based NER on dataset CHEMD

## customized training

1. Download the .cfg file.

2. Cover the .cfg file in the `models` folder.
```bash
python -m spacy init fill-config base_config.cfg config.cfg
```

3. load data, write mode, make a .spaCy file
| modify the path in Transfer.py to trasfer training data and validation data
```bash
cd dataset
python Transfer.py
```
4. train  
| here paths.dev we simply use train
```bash
python -m spacy train config.cfg --output ./output --paths.train ./dataset/training.spacy --paths.dev ./dataset/validation.spacy
```

#### Expected output
```bash
=========================== Initializing pipeline ===========================
[2024-08-21 14:41:07,969] [INFO] Set up nlp object from config
[2024-08-21 14:41:07,969] [INFO] Set up nlp object from config
[2024-08-21 14:41:07,974] [INFO] Pipeline: ['transformer', 'ner']
[2024-08-21 14:41:07,974] [INFO] Pipeline: ['transformer', 'ner']
[2024-08-21 14:41:07,976] [INFO] Created vocabulary
[2024-08-21 14:41:07,977] [INFO] Finished initializing nlp object
[2024-08-21 14:41:07,977] [INFO] Finished initializing nlp object
Some weights of the model checkpoint at roberta-base were not used when initializing RobertaModel: ['lm_head.dense.weighSome weights of the model checkpoint at roberta-base were not used when initializing RobertaModel: ['lm_head.dense.weight', 'lm_head.layer_norm.bias', 'lm_head.layer_norm.weight', 'lm_head.decoder.weight', 'lm_head.dense.bias', 'lm_head.bias']
- This IS expected if you are initializing RobertaModel from the checkpoint of a model trained on another task or with another architecture (e.g. initializing a BertForSequenceClassification model from a BertForPreTraining model).
- This IS NOT expected if you are initializing RobertaModel from the checkpoint of a model that you expect to be exactly identical (initializing a BertForSequenceClassification m identical (initializing a BertForSequenceClassification model from a BertForSequenceClassification model).
[2024-08-21 14:41:13,394] [INFO] Initialized pipeline components: ['transformer', 'ner']
✔ Initialized pipeline

============================= Training pipeline =============================
ℹ Pipeline: ['transformer', 'ner']
ℹ Initial learn rate: 0.0
E    #       LOSS TRANS...  LOSS NER  ENTS_F  ENTS_P  ENTS_R  SCORE
---  ------  -------------  --------  ------  ------  ------  ------
  0       0         258.09    560.32    0.02    0.04    0.01    0.00
  0     200       16605.67  40713.77   58.92   66.71   52.75    0.59
  0     400        2708.43   7235.33   67.08   65.49   68.76    0.67
  1     600        4012.99   5779.37   73.76   77.93   70.01    0.74
  1     800        7018.30   5382.55   75.21   73.57   76.92    0.75
  2    1000        3322.78   4188.22   75.83   77.25   74.47    0.76
  2    1200        2638.04   3854.50   77.25   77.32   77.17    0.77
  3    1400        1695.14   3455.24   79.14   81.27   77.11    0.79
  3    1600        1625.26   3165.13   79.12   76.94   81.42    0.79
  4    1800        1367.68   2755.34   78.90   76.06   81.95    0.79
  4    2000        1132.44   2479.03   80.53   81.55   79.54    0.81
  5    2200         929.05   2289.94   78.84   78.80   78.87    0.79
  5    2400        1730.70   1966.87   81.39   82.37   80.42    0.81
  5    2600         781.58   1974.35   81.03   81.19   80.86    0.81
  6    2800        1036.96   1858.08   80.35   79.13   81.62    0.80
  6    3000        1354.55   1777.93   81.49   82.13   80.86    0.81
  7    3200        1484.37   1500.41   80.17   80.14   80.19    0.80
  7    3400         714.71   1558.69   81.54   83.03   80.10    0.82
  8    3600         952.58   1415.85   80.77   80.27   81.27    0.81
  8    3800        3942.35   1366.03   81.51   80.91   82.12    0.82
  9    4000        1222.79   1389.95   81.89   83.11   80.70    0.82
  9    4200        1940.54   1258.02   81.60   82.24   80.97    0.82
 10    4400        2960.61   1306.16   82.28   83.29   81.30    0.82
 10    4600         571.22   1077.28   82.46   81.60   83.35    0.82
 10    4800        5003.98   1300.98   81.37   80.64   82.12    0.81
 11    5000         508.92    991.21   81.71   81.55   81.86    0.82
 11    5200        1094.34   1035.57   82.13   83.73   80.59    0.82
 12    5400         900.20    943.65   81.72   83.61   79.92    0.82
 12    5600        1354.94    960.60   81.97   82.33   81.62    0.82
 13    5800         391.42    834.11   82.35   85.89   79.09    0.82
 13    6000         550.52    820.36   82.28   81.75   82.82    0.82
 14    6200         378.49    809.97   82.10   82.88   81.34    0.82
```