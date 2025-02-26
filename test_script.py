import requests
import ollama
import os, base64

def load_image_file(file_path="test_image.png"):
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
    return get_text.message.content.replace('-', '')


def solve_answer():
    img_resp = load_image_file()
    text_resp = output_text_from_image(img_resp)
    print(text_resp)

if __name__ == "__main__":
    print(solve_answer())