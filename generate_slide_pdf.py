import os
from PIL import Image

slide_img = Image.open("part2_prompt_experiment_slide.png").convert("RGB")
slide_pdf_path = "/Users/Kartikkk/.gemini/antigravity/brain/e402d1ae-01a4-471c-a718-981f2e006f12/Part2_Prompt_Experiment_Slide.pdf"
slide_img.save(slide_pdf_path)
print("Slide PDF created at:", slide_pdf_path)
