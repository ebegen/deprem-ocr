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


def save_csv(mahalle, il, sokak, apartman):

    adres_full = [mahalle, il, sokak, apartman]

    with open("adress_book.csv", "a", encoding="utf-8") as f:
        write = csv.writer(f)
        write.writerow(adres_full)
    return adres_full

def get_json(mahalle, il, sokak, apartman):
    adres = {'mahalle':mahalle, 'il':il, 'sokak':sokak, 'apartman':apartman}
    dump = json.dumps(adres, indent=4, ensure_ascii=False)
    return dump

with gr.Blocks() as demo:
    gr.Markdown(""" # Image to Text - Adres""")
    with gr.Row():

        img_area = gr.Image()
        ocr_result = gr.Textbox(value="Deneme")

    submit_button = gr.Button()
    submit_button.click(get_text, img_area, ocr_result)

    
    with gr.Column():
        with gr.Row():
            mahalle = gr.Textbox(label="mahalle")
            sokak = gr.Textbox(label="sokak")
        with gr.Row():
            apartman = gr.Textbox(label="apartman")
            il = gr.Textbox(label="il")
        tarif = gr.Textbox(label="Tarif")
    
    json_out = gr.Textbox()
    csv_out = gr.Textbox()

    adres_submit = gr.Button()
    adres_submit.click(save_csv, [mahalle, il, sokak, apartman], None)
    adres_submit.click(get_json, [mahalle, il, sokak, apartman], json_out)
    adres_submit.click(save_csv, [mahalle, il, sokak, apartman], csv_out)


    


if __name__ == "__main__":
    demo.launch()
