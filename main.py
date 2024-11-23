#!pip install --upgrade transformers
#!pip install --upgrade huggingface_hub
#!pip install tensorflow
#!pip install tf-keras

# you can also use pytorch instead of tensorflow but you might need other libraries as well

import tensorflow as tf
tf.get_logger().setLevel('ERROR')

from transformers import pipeline

def beantwoord(vraag):
    qa_pipeline = pipeline("text2text-generation", model="google/flan-t5-large")
    antwoord = qa_pipeline(f"question: {vraag}")
    return antwoord[0]["generated_text"]

def maak_prompt(context,vraag):
    return "Context: " + context + "\n Question: " + vraag + "\n Answer: "

context = ""
while True:
    put = input("enter question: ")
    if put == "!exit":
        break;
    vraag = maak_prompt(context, put)
    context = put
    antw = beantwoord(vraag)
    context += antw
    print(vraag)
    print(antw)
