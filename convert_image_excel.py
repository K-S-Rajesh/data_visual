from image_to_excel import BaseClass
from pathlib import Path


app = BaseClass("config.yml")

app.image_to_excel(
    Path("ESTIMATE AVANI.png"), 100, Path("output.xlsx")
)