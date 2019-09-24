head -n 100 feersum-lid-shared-task/lid_task_2017a/train_full_3k.csv > data/valid.txt
tail -n +101 feersum-lid-shared-task/lid_task_2017a/train_full_3k.csv > data/train.txt
cat feersum-lid-shared-task/lid_task_2017a/test_full_1k.csv > data/test_full.txt
cat feersum-lid-shared-task/lid_task_2017a/test_15_1k.csv > data/test_15.txt

python add_labels.py

fastText/fasttext supervised -input data/label_train.txt -output langdetect -dim 16 
fastText/fasttext test langdetect.bin data/label_valid.txt