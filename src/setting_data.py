# -*- coding: utf-8 -*-

from os import path
from pathlib import Path
import os
import shutil

if __name__ == '__main__':

    corpus = "aristoBERTo/text/roberta.txt"

    lm_data_dir = "aristoBERTo/text/train/"
    eval_data_dir = "aristoBERTo/text/validation/"

    with open(corpus, 'r', encoding="utf8") as f:
        lines = f.readlines()

    train_split = 0.97
    train_data_size = int(len(lines) * train_split)

    with open(os.path.join(lm_data_dir, 'train.txt'), 'w') as f:
        for item in lines[:train_data_size]:
            f.write(item)

    with open(os.path.join(eval_data_dir, 'eval.txt'), 'w') as f:
        for item in lines[train_data_size:]:
            f.write(item)

    model_path = "aristoBERTo/model/"
    weights_dir = model_path + "aristoBERTo"

    if path.exists(model_path):
        shutil.rmtree('aristoBERTo/model')

    Path(weights_dir).mkdir(parents=True)
