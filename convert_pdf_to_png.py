from pathlib import Path
import pymupdf

pdf_path = Path("source_assets/source_029.pdf")
png_path = Path("raw_assets/notice_029.png")

if not pdf_path.exists():
    raise FileNotFoundError(f"PDF를 찾을 수 없습니다: {pdf_path}")

with pymupdf.open(pdf_path) as source_document:
    page_count = len(source_document)

    if page_count == 0:
        raise ValueError("PDF에 변환할 페이지가 없습니다.")

    print(f"PDF 페이지 수: {page_count}")

    # 모든 페이지의 폭을 가장 넓은 페이지에 맞춤
    output_width = max(page.rect.width for page in source_document)

    page_heights = []

    for page in source_document:
        scale = output_width / page.rect.width
        page_heights.append(page.rect.height * scale)

    output_height = sum(page_heights)

    # 모든 원본 페이지를 세로로 배치할 단일 페이지 PDF 생성
    combined_document = pymupdf.open()
    combined_page = combined_document.new_page(
        width=output_width,
        height=output_height
    )

    current_y = 0

    for page_number, page_height in enumerate(page_heights):
        target_rect = pymupdf.Rect(
            0,
            current_y,
            output_width,
            current_y + page_height
        )

        combined_page.show_pdf_page(
            target_rect,
            source_document,
            page_number,
            keep_proportion=True
        )

        current_y += page_height
        print(f"{page_number + 1}페이지 배치 완료")

    # 결합된 한 페이지를 PNG로 변환
    pixmap = combined_page.get_pixmap(
        dpi=200,
        alpha=False
    )
    pixmap.save(png_path)

    combined_document.close()

print(f"변환 완료: {png_path}")