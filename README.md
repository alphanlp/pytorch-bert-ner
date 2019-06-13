# pytorch-bert-ner
基于bert的命名实体识别，pytorch实现，支持中英文

# Requirements

-  `python3`
- `pip3 install -r requirements.txt`

# Run Exmaple
--bert_model is the pre_trained pytorch bert model path(pytorch)
if tensorflow bert model, should convert to pytoch bert model as follow command:
`python3 convert_tf_checkpoint_to_pytorch.py --tf_checkpoint_path ../bert_model.ckpt --bert_config_file ../bert_config.json --pytorch_dump_path ../pytorch_model.bin`

### English
`python3 run_ner.py --data_dir=data/ --bert_model=bert-base-cased --task_name=ner --output_dir=models --max_seq_length=64 --do_train --num_train_epochs 5 --do_eval --warmup_proportion=0.4`

### Chinese
`python3 run_ner.py --data_dir=data/ --bert_model=chinese-base-uncased --task_name=chinese_ner --output_dir=models --max_seq_length=64 --do_train --num_train_epochs 5 --do_eval --warmup_proportion=0.4
`


# Result

### Validation Data
```
             precision    recall  f1-score   support

       MISC     0.9407    0.9304    0.9355       273
        LOC     0.9650    0.9881    0.9764       419
        PER     0.9844    0.9783    0.9813       322
        ORG     0.9794    0.9852    0.9822       337

avg / total     0.9683    0.9734    0.9708      1351
```
### Test Data
```
             precision    recall  f1-score   support

        ORG     0.9152    0.9073    0.9113       464
        PER     0.9767    0.9692    0.9730       260
        LOC     0.9397    0.9263    0.9330       353
       MISC     0.8276    0.9014    0.8629       213

avg / total     0.9198    0.9240    0.9217      1290
```

## Pretrained model download from [here](https://drive.google.com/file/d/1UKE2UVFStXZFtXFgZObGg5mo_MzW-ZoC/view?usp=sharing) 

# Inference

`python3 predict.py`
```
{'2': {'tag': 'B_T', 'confidence': 0.9999847412109375}, '0': {'tag': 'I_T', 'confidence': 0.9989903569221497}, '1': {'tag': 'I_T', 'confidence': 0.9995298385620117}, '4': {'tag': 'I_T', 'confidence': 0.9996459484100342}, '年': {'tag': 'I_T', 'confidence': 0.9996104836463928}, '新': {'tag': 'O', 'confidence': 0.9995424747467041}, '的': {'tag': 'O', 'confidence': 0.9997028708457947}, '开': {'tag': 'O', 'confidence': 0.9999663829803467}, '始': {'tag': 'O', 'confidence': 0.9999591112136841}, '，胡': {'tag': 'O', 'confidence': 0.9999748468399048}, '阿': {'tag': 'I_PER', 'confidence': 0.9997753500938416}, '沛': {'tag': 'I_PER', 'confidence': 0.9993517994880676}, '很': {'tag': 'O', 'confidence': 0.9993890523910522}, '高': {'tag': 'O', 'confidence': 0.9992743134498596}, '兴': {'tag': 'O', 'confidence': 0.9999097585678101}}
```

or refer:
```
from bert import Ner

model = Ner("models/")
output = model.predict("Steve went to Paris")

print(output)
# {
#     "Steve": {
#         "tag": "B-PER",
#         "confidence": 0.999879002571106
#     },
#     "went": {
#         "tag": "O",
#         "confidence": 0.9968552589416504
#     },
#     "to": {
#         "tag": "O",
#         "confidence": 0.9996656179428101
#     },
#     "Paris": {
#         "tag": "B-LOC",
#         "confidence": 0.999504804611206
#     }
# }
```
