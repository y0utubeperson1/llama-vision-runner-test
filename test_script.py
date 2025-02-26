import requests
import ollama
import os, base64, time

def load_image_file(file_path):
    with open(file_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_string

def output_text_from_image(img_b64):
    get_text = ollama.chat(
            model='llama3.2-vision',
            messages=[{
                'role': 'user',
                'content': 'I am trying to read this text from this image. Please write the letters in the image. Only output the letters, no other text.',
                'images': [img_b64]
            }]
        )
    return get_text.message.content


import time

def solve_answer():
    files = ["test_image.png", "test_image_2.png", "test_image_3.png"]
    for file in files:
        start_time = time.time()
        print("--------------------------")
        print(f"Reading file: {file}")
        img_resp = load_image_file(file)
        text_resp = output_text_from_image(img_resp)
        print(f" > {text_resp}")
        end_time = time.time()
        elapsed = end_time - start_time
        minutes = int(elapsed // 60)
        seconds = elapsed % 60
        print(f"Iteration time: {minutes} minutes, {seconds:.2f} seconds\n")


if __name__ == "__main__":
    solve_answer()