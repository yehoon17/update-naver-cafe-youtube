# 네이버 카페 대문 유튜브 영상 URL 자동 업데이트

이 프로그램은 가장 최근 유튜브 영상의 URL을 네이버 카페의 대문(HTML)에 자동으로 반영하는 자동화 스크립트입니다.



## 🔧 기능

1. Chrome 브라우저 실행
2. 유튜브 채널 접속 및 최신 영상 클릭
3. 공유 → 복사 버튼을 통해 영상 URL 복사
4. 네이버 카페 대문 편집 페이지 접속
5. HTML 모드에서 기존 영상 URL을 새 URL로 교체
6. "바로 적용" 버튼 클릭
7. 완료 팝업 닫기



## 🛠️ 사용법

**깃허브에서 레포지토리를 클론**

   ```bash
   git clone https://github.com/yehoon17/update-naver-cafe-youtube.git
   ```

#### 로컬 
**가상 환경 설정(optional)**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```


1. 필요한 종속성을 설치

   ```bash
   pip install -r requirements.txt
   ```

2. 설정 파일 수정
   - `config.json` 파일 열기
   - 각 항목의 내용 수정
     - "youtube_channel_name": 유튜브 채널 이름
     - "naver_cafe_id": 네이버 카페 id([카페 관리 페이지](https://github.com/yehoon17/update-naver-cafe-youtube/blob/master/assets/naver_cafe_id.png)에서 확인)
     - "chrome_path": 크롬 실행 파일 경로(윈도우 OS 기본값으로 설정되어 있음)


3. 스크립트 실행

   ```bash
   python update_script.py
   ```

4. 자동으로 Chrome이 실행되고 유튜브, 네이버 카페를 순서대로 조작합니다.




## 이미지 파일

* `kebab_menu.png` – 유튜브 영상의 우측 상단 점 3개 메뉴
* `share_button.png` – 공유 버튼
* `copy_button.png` – URL 복사 버튼
* `html_checkbox.png` – HTML 모드 체크박스
* `apply_button.png` – "바로 적용" 버튼



## 🖱️ 마우스 및 키보드 조작

* `pyautogui`를 이용해 실제 사람처럼 마우스와 키보드를 조작합니다.
* 네이버에 Chrome 로그인이 되어 있어야 합니다.
* 크롬 창이 열리고 화면이 보이는 상태여야 정상 작동합니다.



## 📌 주의사항

* 모니터 해상도 및 크롬 UI 위치가 변경되면 이미지 인식이 실패할 수 있습니다.
* 모든 이미지 파일은 너무 크거나 작지 않게, **정확하게 해당 UI 요소만 잘라서** 저장하세요.
* DPI 스케일이 100%여야 가장 안정적으로 작동합니다.


## 🤝 기여 방법 (Contributing)

이 프로젝트에 기여하고 싶으시다면 언제든지 환영합니다!

1. 이 레포지토리를 포크합니다.
2. 새로운 브랜치를 생성합니다 (`git checkout -b feature/새기능`).
3. 코드를 수정하고 커밋합니다 (`git commit -m '새 기능 추가'`).
4. 브랜치에 푸시합니다 (`git push origin feature/새기능`).
5. Pull Request를 생성해주세요.

버그 리포트, 개선 아이디어, 문서 보완 등 모든 기여는 소중히 반영됩니다 🙏
