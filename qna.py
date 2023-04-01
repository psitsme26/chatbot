from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("declare-lab/flan-alpaca-base")
model = AutoModelForSeq2SeqLM.from_pretrained("declare-lab/flan-alpaca-base")

# question = "what are next actions?"
# context = """
# IBCC for claim
# CM has been assigned
# Customer is not happy since the roof is not repaired properly.
#
# access amount 1500$
# CM yasmin will contact customer
#
# Next Actions:
# - CM to call customer
# - Plan repairs
# - Check coverage
# """
# t5query = f"question: {question} context: {context}"
#
#
# #t5query = f"""Question: Select the item from this list which is "{query}". Context: * {" * ".join(options)}"""
# inputs = tokenizer(t5query, return_tensors="pt")
# outputs = model.generate(**inputs, max_new_tokens=45)
#
#
# print(tokenizer.batch_decode(outputs, skip_special_tokens=True)[0])

def get_answer(question, context):
    t5query = f"question: {question} context: {context}"

    # t5query = f"""Question: Select the item from this list which is "{query}". Context: * {" * ".join(options)}"""
    inputs = tokenizer(t5query, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=45)

    return tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]

