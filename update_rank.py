import requests
import os
import json

API_KEY = os.environ.get('MY_API_KEY')
# 샘플로 딱 하나만 깊게 파보겠습니다.
BLOG_URL = "https://moneystory1981.tistory.com/entry/%ED%95%9C%EC%A0%84%EA%B8%B0%EC%88%A0-%EC%A3%BC%EA%B0%80-%EC%A0%84%EB%A7%9D-%EB%AA%A9%ED%91%9C%EC%A3%BC%EA%B0%80-15%EB%A7%8C%EC%9B%90-%EC%83%81%ED%96%A5-2026%EB%85%84-%EC%8B%A4%EC%A0%81-%ED%8F%AD%EB%B0%9C-%EC%A0%84-%EA%BC%AD-%EB%B4%90%EC%95%BC-%ED%95%A0-%EB%B6%84%EC%84%9D"

def save_full_report():
    # 모든 카테고리를 요청합니다.
    url = f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={BLOG_URL}&category=seo&category=performance&category=accessibility&category=best-practices&key={API_KEY}"
    
    res = requests.get(url)
    if res.status_code == 200:
        full_data = res.json()
        
        # 'lighthouseResult' 안에 모든 세부 지표가 들어있습니다.
        with open('full_report.json', 'w', encoding='utf-8') as f:
            json.dump(full_data['lighthouseResult']['audits'], f, ensure_ascii=False, indent=2)
        
        print(f"✅ 리포트 저장 완료! 'data.json' 파일을 열어보세요.")
        print(f"분석 항목 개수: {len(full_data['lighthouseResult']['audits'])}개")
    else:
        print(f"❌ 에러: {res.status_code}")

if __name__ == "__main__":
    save_full_report()
