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