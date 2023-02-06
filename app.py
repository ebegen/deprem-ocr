import gradio as gr
from easyocr import Reader
from PIL import Image
import io
import json
import csv

reader = Reader(["tr"])


def get_text(input_img):

    result = reader.readtext(input_img, detail=0)
    return " ".join(result)


def save_json(mahalle, il, sokak, apartman):

    adres_full = [mahalle, il, sokak, apartman]

    with open("adress_book.csv", "a", encoding="utf-8") as f:
        write = csv.writer(f)

        write.writerow(adres_full)


with gr.Blocks() as demo:
    gr.Markdown(""" # Image to Text - Adres""")
    with gr.Row():

        img_area = gr.Image()
        ocr_result = gr.Textbox(value="Deneme")

    submit_button = gr.Button()
    submit_button.click(get_text, img_area, ocr_result)

    with gr.Row():
        with gr.Column():
            mahalle = gr.Textbox(label="mahalle")
            sokak = gr.Textbox(label="sokak")
            apartman = gr.Textbox(label="apartman")
            il = gr.Textbox(label="il")
            tarif = gr.Textbox(label="Tarif")

    adres_submit = gr.Button()
    adres_submit.click(save_json, [mahalle, il, sokak, apartman], None)

if __name__ == "__main__":
    demo.launch(share=True)
