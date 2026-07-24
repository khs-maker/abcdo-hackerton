from pathlib import Path
import pymupdf

input_files = [
    Path("raw_assets/notice_008_1.png"),
    Path("raw_assets/notice_008_2.png"),
]
output_file = Path("raw_assets/notice_008.png")

images = [pymupdf.Pixmap(str(path)) for path in input_files]

width = max(image.width for image in images)
gap = 20
height = sum(image.height for image in images) + gap

document = pymupdf.open()
page = document.new_page(width=width, height=height)

y = 0
for path, image in zip(input_files, images):
    x = (width - image.width) / 2
    area = pymupdf.Rect(x, y, x + image.width, y + image.height)
    page.insert_image(area, filename=str(path))
    y += image.height + gap

result = page.get_pixmap(alpha=False)
result.save(str(output_file))
document.close()

print(f"결합 완료: {output_file}")