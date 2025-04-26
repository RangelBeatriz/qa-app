from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, TrainingArguments, Trainer
from datasets import load_dataset
from peft import get_peft_model, LoraConfig, TaskType
import torch

#Loading base model.
model_name = "google/flan-t5-base"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

#Configuring LoRA
lora_config = LoraConfig(r=8, lora_alpha=16, target_modules=["q", "v"], lora_dropout=0.1, bias="none", task_type=TaskType.SEQ_2_SEQ_LM)

model = get_peft_model(model, lora_config)

#tokenizing the data
dataset = load_dataset("json", data_files="data/editais_data.jsonl")["train"]

def tokenize(sample):
    inputs = tokenizer(sample["instruction"], padding="max_length", truncation=True, max_length=512)
    targets = tokenizer(sample["output"], padding="max_length", truncation=True, max_length=128)
    inputs["labels"] = targets["input_ids"]
    return inputs

tokenized_dataset = dataset.map(tokenize)
