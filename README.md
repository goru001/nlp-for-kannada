# NLP for Kannada

This repository contains State of the Art Language models
 and Classifier for Kannada, which is spoken predominantly by
  Kannada people in India, mainly in the state of Karnataka.

The models trained here have been used in [Natural Language Toolkit for Indic Languages
 (iNLTK)](https://github.com/goru001/inltk)

## Dataset

#### Created as part of this project
1. [Kannada Wikipedia Articles](https://www.kaggle.com/disisbig/kannada-wikipedia-articles)

2. [Kannada News Dataset](https://www.kaggle.com/disisbig/kannada-news-dataset)

#### Open Source Datasets
1. [IndicNLP News Article Classification Dataset - Kannada](https://github.com/ai4bharat-indicnlp/indicnlp_corpus#indicnlp-news-article-classification-dataset)

## Results

### Language Model Perplexity (on validation set)

| Architecture/Dataset | Kannada Wikipedia Articles |
|:--------:|:----:|
|   ULMFiT  |  70.10  |
|  TransformerXL |  61.97  |

### Classification Metrics

##### ULMFiT

| Dataset | Accuracy | MCC | Notebook to Reproduce results |
|:--------:|:----:|:----:|:----:|
| IndicNLP News Article Classification Dataset - Kannada |  98.87  |  98.30  | [Link](https://github.com/goru001/nlp-for-kannada/blob/master/classification/Kannada_Classification_Model.ipynb) |

### Visualizations
 
##### Word Embeddings

| Architecture | Visualization |
|:--------:|:----:|
| ULMFiT | [Embeddings projection](https://projector.tensorflow.org/?config=https://raw.githubusercontent.com/goru001/nlp-for-kannada/master/language-model/embedding_projector_config.json) |
| TransformerXL | [Embeddings projection](https://projector.tensorflow.org/?config=https://raw.githubusercontent.com/goru001/nlp-for-kannada/master/language-model/embedding_projector_transformer_config.json)  |

## Pretrained Models

#### Language Models 
Download pretrained Language Model from [here](https://drive.google.com/open?id=1s8d83UKyw_C6h-wbGUqYSXtHxuFUcVlS)

#### Tokenizer

Trained tokenizer using Google's [sentencepiece](https://github.com/google/sentencepiece)

Download the trained model and vocabulary from [here](https://drive.google.com/open?id=1BN0KgTcX6CWAJ-YF2DiwZhDUSEwVjvIH)