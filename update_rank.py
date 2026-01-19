import requests
import os
import json

API_KEY = os.environ.get('MY_API_KEY')
# 분석할 블로그 리스트
BLOGS = ["https://huedor2.tistory.com/1725", "https://mkkrw.tistory.com/"]

def get_data():
    results = []
    for blog in BLOGS:
        # 모든 카테고리(성능, SEO, 접근성, 권장사항)를 요청합니다.
        url = f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={blog}&category=seo&category=performance&category=accessibility&category=best-practices&key={API_KEY}"
        res = requests.get(url)
        if res.status_code == 200:
            data = res.json()['lighthouseResult']['categories']
            results.append({
                "url": blog,
                "seo": data['seo']['score'] * 100,             # 검색 최적화
                "performance": data['performance']['score'] * 100, # 로딩 속도
                "accessibility": data['accessibility']['score'] * 100, # 접근성
                "best_practices": data['best-practices']['score'] * 100 # 권장사항
            })
    
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    get_data()
