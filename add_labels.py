with open('data/label_valid.txt', 'w') as f:
    for line in open('data/valid.txt'):
        f.write("__label__%s" % line)

with open('data/label_train.txt', 'w') as f:
    for line in open('data/train.txt'):
        f.write("__label__%s" % line)

with open('data/label_test_full.txt', 'w') as f:
    for line in open('data/test_full.txt'):
        f.write("__label__%s" % line)

with open('data/label_test_15.txt', 'w') as f:
    for line in open('data/test_15.txt'):
        f.write("__label__%s" % line)