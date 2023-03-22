<p align="center">
  <a href="https://www.fri.uni-lj.si/" target="blank"><img src="logo.png" 
  width="420" alt="University of Ljubljana, Faculty of Computer and Information Science" /></a>
</p>
  
<p align="center">
  This is the documentation about the bachelor thesis project with the title: Grammar error handling in school written works using natural language processing. This documentation covers the deployment of the GEH pipeline application and all of its needed components. <br />
</p>

### Table of Contents

- [About](#about-the-thesis)
- [Used Technologies](#used-technologies)
  - [Python](#1-python)
  - [Hugging Face](#2-hugging-face)
  - [PyTorch](#3-pytorch)
  - [Pandas](#4-pandas)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Prepare Slovene Specification](#prepare-slovene-specification)
  - [Prepare Datasets](#prepare-datasets)
  - [Analyze Datasets](#analyze-datasets)
  - [Train Models](#train-models)
  - [How to use Application?](#how-to-use-application)
- [Contributing](#contributing)
- [License](#license)
- [Citation](#citation)
- [Author](#author)

# About the thesis

The thesis presents the development of a grammar error handling system, which was divided into three sub-problems: error detection, recognition, and correction. We addressed these problems using large language models based on the transformer architecture. Specifically, we used the SloBERTa model, the Slovenian version of the BERT model, to detect and recognize grammatical errors. Additionally, we used the SloT5 model, the Slovenian version of the T5 model, to correct grammatical errors. The models were trained and evaluated on the Slovene corpora of grammar corrections Šolar and Lektor. We also used the Slovene morphological lexicon Sloleks and the Classla-Stanza tagging tool. To evaluate the performance of the models, we used several metrics. The detection and recognition models achieved the F-score of 88% and 14%, respectively. The correction model achieved the GLEU score of 50%.

**Keywords**: grammar error handling, deep neural networks, transformer
architecture, SloBERTa model, SloT5 model, Šolar corpus, Lektor corpus,
Sloleks lexicon, Classla-Stanza tool.

# Used technologies

In general, the development of the GEH pipeline application is consisted of one main technology i.e. [Python](https://www.python.org/) programming language. We have also used [Hugging Face](https://huggingface.co/) and [PyTorch](https://pytorch.org/) for fine-tuning, and [Pandas](https://pandas.pydata.org/) for data analysis.

### 1. Python

Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built-in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. Python's simple, easy-to-learn syntax emphasizes readability and therefore reduces the cost of program maintenance. Python supports modules and packages, which encourages program modularity and code reuse. The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms and can be freely distributed.

Most of the GEH pipeline application is written in the Python programming language.

### 2. Hugging Face

HuggingFace is an AI community that promotes open source contributions. It is a hub of open source models for Natural Language Processing, computer vision, and other fields where AI plays its role. Even the tech giants like Google, Facebook, AWS, Microsoft, and others use the models, datasets, and libraries.

### 3. PyTorch

PyTorch is a machine learning framework based on the Torch library, used for applications such as computer vision and natural language processing, originally developed by Meta AI and now part of the Linux Foundation umbrella. It is free and open-source software released under the modified BSD license. Although the Python interface is more polished and the primary focus of development, PyTorch also has a C++ interface.

### 4. Pandas

Pandas is an open source Python package that is most widely used for data science/data analysis and machine learning tasks. It is built on top of another package named Numpy, which provides support for multi-dimensional arrays. As one of the most popular data wrangling packages, Pandas works well with many other data science modules inside the Python ecosystem, and is typically included in every Python distribution.

# Getting started

## Prerequisites

To run the GEH pipeline application on your machine you will need to install the **Python** programming langugage. You can find the documentation on how to install Python here: [https://www.python.org/downloads/](https://www.python.org/downloads/).

> **_NOTE:_** If you want to run the application, you have to export all `*.ipynb` files into `*.py` files.

## Installation

The folder structure in this project is like the following:

```
.
├── data
│   ├── dataset
│   │   ├── gec
│   │   ├── ged
│   │   └── ger
│   ├── lektor
│   │   └── lektor.xml
│   ├── sloleks
│   │   └── sloleks.csv
│   └── solar
│       └── solar.xml
├── slovene_specification
|   ├── slovene_specification.py
|   └── slovene_specification.xml
├── src
│   ├── analyze_data
│       └── analyze_data.py
│   ├── models
│   │   ├── gec_model_finetuned
│   │   ├── ged_model_finetuned
│   │   └── ger_model_finetuned
│   ├── prepare_data
│   │   └── prepare_data.py
│   ├── train_model
│   │   ├── prepare_gec_dataset.py
│   │   ├── prepare_ged_dataset.py
│   │   ├── prepare_ger_dataset.py
│   │   ├── train_gec_model.py
│   │   ├── train_ged_model.py
│   │   └── train_ger_model.py
│   └── grammar_error_handling.py
├── .gitignore
├── LICENSE
└── requirements.txt
```

First, we clone the repo to download and extract the compressed archive.

```bash
git clone git@github.com:mokot/diplomsko-delo.git
cd diplomsko-delo
```

Next, download the required files and move them into the appropriate directory.

- Corpus Lektor: `lektor.xml` is available at [https://www.dropbox.com/s/96i8rcwakf0knok/lektor.xml](https://www.dropbox.com/s/96i8rcwakf0knok/lektor.xml)
- Corpus Šolar: `solar.xml` is available at [https://www.dropbox.com/s/qf0di2svbwr4erb/solar.xml](https://www.dropbox.com/s/qf0di2svbwr4erb/solar.xml)
- Lexicon Sloleks: source Sloleks files are available at [https://www.clarin.si/repository/xmlui/handle/11356/1745](https://www.clarin.si/repository/xmlui/handle/11356/1745)
- Slovene Specification: `slovene_specification.xml` is available at [http://nl.ijs.si/ME/Vault/V4/msd/xml/msd-sl.xml](http://nl.ijs.si/ME/Vault/V4/msd/xml/msd-sl.xml)

If you are installing an application locally, you should install it in a [virtual environment](https://docs.python.org/3/library/venv.html). If you're unfamiliar with Python virtual environments check out the [user guide](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/).

Secondly, create a virtual environment with the version of Python you're going to use and activate it.

> **_NOTE:_** This application is tested on Python 3.10.

Then you will need to install all required libraries, using pip as follows:

```bash
pip3 install -r requirements.txt
```

If you are using [conda](https://docs.conda.io), install requirements as follows:

```bash
conda install --file requirements.txt
```

## Prepare Slovene Specification

After you have completed the installation, prepare the slovene specification files with the following commands:

```bash
cd slovene_specification
python slovene_specification.py
cd ..
```

## Prepare Datasets

Before training the model we also have to generate datasets. First, move to the required directory with:

```bash
cd src/prepare_data
```

Next, run the `prepare_data` Python script using:

```bash
python prepare_data.py
```

> **_NOTE:_** The process of data preparation might take some time, so be patient :)

After all files are successfully generated move back to the root of the project directory.

```bash
cd ../..
```

## Analyze Datasets

This step is completely optional and will do a simple analysis about the generated datasets. For the analysis run the following commands:

```bash
cd src/analyze_data
python analyze_data.py
cd ../..
```

## Train Models

The last thing we have to do before using the GEH pipeline application is to train our large language models.

First, move to the appropriate directory and generate specific labeled datasets using:

```bash
cd src/train_model
python prepare_ged_dataset.py
python prepare_ger_dataset.py
python prepare_gec_dataset.py
```

These commands should generate three datasets, which are stored in the `./data/datasets` folder.

Next, we can fine-tune our models with the following commands:

```bash
python train_ged_model.py
python train_ger_model.py
python train_gec_model.py
```

> **_NOTE:_**  This process will take a lot of time. The Hugging Face library supports parallelism on GPU with CUDA. If you value your time, make sure to use that :)

After the process is done, you should have three best fine-tuned models in the `./src/models` folder.

At the end, move back to the source directory.

```bash
cd ../..
```

## How to use Application?

Now we are ready to use the grammar error handling pipeline application. First move into the `src` directory:

```bash
cd src
```

Then you can use the pipeline with the following command:

```bash
python grammar_error_handling.py --text "Hello, World!"
```

# Contributing

Contributions are what makes the open source community such an amazing place to
learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/amazing-feature`)
3. Commit your Changes (`git commit -m 'Add some amazing features`)
4. Push to the Brach (`git push origin feature/amazing-feature`)
5. Open a Pull Request

# License

Distributed under the **GPL-3.0 license** License. See `LICENSE` for more information.

```
                      GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
Everyone is permitted to copy and distribute verbatim copies
of this license document, but changing it is not allowed.
```

# Citation

You can cite the bachelor [thesis](https://repozitorij.uni-lj.si/Dokument.php?id=167503&lang=slv) with the title: **Grammar error handling in school written works using natural language processing**.

```
@thesis{diplomsko_delo_rok_mokotar,
  title={Obvladovanje slovničnih napak v šolskih pisnih izdelkih z metodami za obdelavo naravnega jezika},
  url={https://repozitorij.uni-lj.si/IzpisGradiva.php?id=144932&lang=slv},
  school={Univerza v Ljubljani, Fakulteta za računalništvo in informatiko},
  author={Mokotar, Rok},
  year={2023}
}
```

# Author

- [Rok Mokotar](https://www.linkedin.com/in/mokot/) - rm6551@student.uni-lj.si
