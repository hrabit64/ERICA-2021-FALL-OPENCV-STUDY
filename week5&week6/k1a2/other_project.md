# Color Tracking
[repo](https://github.com/gaborvecsei/Color-Tracker/)  
특정 색깔의 물체의 움직임을 탐지합니다.

## 사용된 기법
### 모폴로지 연산과 외곽선 추출
[사용된 부분](https://github.com/gaborvecsei/Color-Tracker/blob/e9167f4a1ac83d1e976ea7f9c665cce2de677f0a/color_tracker/utils/helpers.py#L93)
1. inRange() 함수로 특정 영역의 색상만 추출
2. 모폴로지 연산을 통해 추출된 색 영역의 모양과 구조 분석
3. 구한 이미지에서 외곽선 검출
