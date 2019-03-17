# NLP for Kannada

This repository contains State of the Art Tokenizer, Language model
 and Classifier for Kannada, which is spoken predominantly by
  Kannada people in India, mainly in the state of Karnataka.

## Dataset

* Download [Kannada Wikipedia Articles Dataset](https://drive.google.com/open?id=1KBAch8djPwVLwN4O-CCCQoaV_FcS4AwU) (32,997 articles) which I scraped, cleaned and
used to train the language model

* Download [Kannada News classification Dataset](https://drive.google.com/open?id=1Qgnn03Wrju6Nv8cs1-PQlzk26X4rpfsg) which I scraped and used to train 
the classifier

## Results

#### Language Model

`on 20% validation set`

* Perplexity of language model: ~70

#### Classifier

* Accuracy of classification model: ~94%
* Kappa score of classification model: ~90

## Pretrained Language Model

Download pretrained Language Model from [here](https://drive.google.com/open?id=1s8d83UKyw_C6h-wbGUqYSXtHxuFUcVlS)


## Classifier

Download classifier from [here](https://drive.google.com/open?id=1mPFvR-QP1eenfYSWYJnck7LtB4IS_PM5)


## Tokenizer

Trained tokenizer using Google's [sentencepiece](https://github.com/google/sentencepiece)

Download the trained model and vocabulary from [here](https://drive.google.com/open?id=1BN0KgTcX6CWAJ-YF2DiwZhDUSEwVjvIH)