# Slashing API
S/ing Project에서 사용하는 API입니다. (using Flask.)

---
### 2021-04-10 Update
 * Youtube link를 GET으로 받아들이면, youtube-dl 모듈을 이용하여 해당 동영상의 음원을 mp3로 저장합니다.
   + youtube-dl (https://anaconda.org/conda-forge/youtube-dl)
 * spleeter를 이용하여, 저장한 mp3로부터 보컬 목소리만 추출합니다.
   + spleeter (https://github.com/deezer/spleeter)
---
### 2021-04-12 Update
 * spleeter를 이용하여 추출한 보컬 목소리를 mozilla deepspeech server로 POST 요청합니다.
 * mozilla deepspeech 결과(JSON)를 반환합니다.
---