# bert_chinese_pytorch
参考代码：https://github.com/huggingface/pytorch-pretrained-BERT
参考代码：https://github.com/duanzhihua/bert_chinese_pytorch


## using in mac os

```
# 转换样本格式
python pyscript/text2json_wb.py -i data/classify/wb_2k.txt -o /tmp/wb_2k.json

# 生成train/test/val集
# In mac : gshuf
# In linux : shuf
gshuf /tmp/wb_2k.json > data/classify/wb_2k.json
head -1500 data/classify/wb_2k.json > data/classify/train.json
tail -500 data/classify/wb_2k.json | head -250 > data/classify/test.json
tail -500 data/classify/wb_2k.json | tail -250 > data/classify/val.json

# 执行训练
python bert.py --do_train --max_seq_length=100  --num_train_epochs=100 --train_batch_size=128
```

