# -*- coding: utf-8 -*-
"""Untitled14.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vZdLM3D6RjEtX8gFus8K1Igpy3Pu2fYL
"""

from langchain.llms import LlamaCpp
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Load LLAMA2 model locally (ensure you have the .gguf file)
llm = LlamaCpp(
    model_path="models/llama-2-7b-chat.gguf",  # Update with your model path
    temperature=0.7,
    max_tokens=800,
    top_p=0.9,
    n_ctx=2048,
    verbose=True
)

# Define prompt template
prompt = PromptTemplate(
    input_variables=["topic"],
    template="""
    You are an expert blog writer.
    Write a clear, engaging, SEO-friendly blog post about the topic: "{topic}".

    Structure:
    - Title
    - Introduction
    - 3 to 4 Sections
    - Conclusion
    - Include headings and bullet points if needed

    Keep it informative and reader-friendly.
    """
)

# Create the blog generation chain
blog_chain = LLMChain(llm=llm, prompt=prompt)

# Example: Generate a blog
topic = "How AI is Revolutionizing the Healthcare Industry"
result = blog_chain.run(topic)

# Save or print the blog
with open("generated_blog.txt", "w", encoding="utf-8") as f:
    f.write(result)

print("✅ Blog generated successfully!\n")
print(result)

