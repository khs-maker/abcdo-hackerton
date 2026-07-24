# AURA Layer 데이터 수집 — 1단계

지금은 30개를 모두 모으지 않습니다. 먼저 안전한 공공 문서 1개만 찾아서 `N001` 행을 완성합니다.

## 폴더 사용법

- `source_assets/`: 개인정보가 없는 공식 원본 PDF·이미지
- `raw_assets/`: AI에 입력할 최종 PNG (`notice_001.png` 등)
- `license_evidence/`: 원문 제목과 공공누리 표시가 보이는 증거 화면
- `data_catalog.csv`: 출처·라이선스·개인정보 상태를 기록하는 장부

## 첫 번째 자료를 찾았을 때

1. 공식 기관 페이지의 제목과 URL을 복사합니다.
2. 해당 게시물 또는 첨부자료에 공공누리 유형이 표시됐는지 확인합니다.
3. 게시물 제목과 공공누리 표시가 함께 보이도록 화면을 캡처합니다.
4. 증거 화면을 `license_evidence/notice_001_license.png`로 저장합니다.
5. 개인정보가 없는 공식 원본을 `source_assets/`에 저장합니다.
6. AI에 넣을 PNG를 `raw_assets/notice_001.png`로 저장합니다.
7. `data_catalog.csv`의 `N001` 행만 채웁니다.

## CSV에서 어려운 칸

- `source_title`: 공식 페이지에 표시된 게시물·자료 제목
- `source_url`: 자료를 내려받은 공식 페이지 주소
- `institution`: 자료를 공개한 기관
- `doc_type`: 예: 복지 신청 안내, 지방세 납부 안내
- `license_type`: 예: 공공누리 제1유형
- `accessed_at`: 확인한 날짜, 예: 2026-07-22
- `asset_origin`: 공식 자료는 `official`, 자체 제작은 `synthetic`
- `mapped_service_name`: 사용자가 최종적으로 이용할 공식 서비스 이름
- `mapped_service_url`: 위 서비스의 공식 주소
- `pii_status`: 개인정보가 없으면 `no_pii`; 확인 전이면 `not_checked`
- `usable`: 검토 전 `pending`, 사용 가능 `yes`, 제외 `no`

## 반드시 지킬 것

- 블로그·카페·커뮤니티의 개인 고지서는 내려받지 않습니다.
- 이름·주소·납부번호·QR코드·바코드가 있는 실제 개인 고지서는 사용하지 않습니다.
- 사이트가 공공기관이라는 이유만으로 공공누리 제1유형이라고 기록하지 않습니다.
- 라이선스가 정확히 확인되지 않으면 `usable=no`로 두고 다음 후보를 찾습니다.
