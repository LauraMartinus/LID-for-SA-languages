# Language Identification for South African Languages
The following system can detect the 11 Official South African languages. Currently, the model is just simply trained using FastText. The system performs best with longer sentences.

Data obtained from https://github.com/praekelt/feersum-lid-shared-task.git

### Requirements
>git clone https://github.com/facebookresearch/fastText.git

>cd fastText

>make

>cd ..

### Training
In order to retrain the LID models, use the bash script train_langid.sh. This file currently has hardcoded paths.
> bash train_langid.sh

### Testing
First extract the langdetect model.

> tar xf langdetect.tar.xz

Call language_id.py with your input test file.

> python language_id.py data/label_test_full.txt

**Results**

| Metric | Value |
| --- | --- |
| P@1    | 0.991 |
| R@1    | 0.991 |

> python language_id.py data/label_test_15.txt

**Results**

| Metric | Value |
| --- | --- |
| P@1    | 0.164 |
| R@1    | 0.164 |

If you dont have the labels and want to predict the languages of sentences you need to specify an output file:

> python language_id.py test_sent.txt --output output.txt

### TODO:
Make the labels return just the label code, and not "__label__code"

Remove hardcoded paths

Improve results for shorter sentences