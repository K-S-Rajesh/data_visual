from image_to_excel import BaseClass
from pathlib import Path

app = BaseClass("config.yml")

app.image_to_excel(
    Path("bill_ramesh.jpeg"), 100, Path("output.xlsx")
)