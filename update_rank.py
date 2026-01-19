# update_rank.py (깃허브가 대신 실행해줄 코드)
import requests
import os
import json

# 깃허브 비밀 금고에서 키를 가져옵니다 (보안 완벽!)
API_KEY = os.environ.get('MY_API_KEY')
# 분석하고 싶은 블로그 리스트 (여기에 주소를 추가하세요!)
BLOGS = ["https://tistory.com", "https://google.com"]

def get_data():
    results = []
    for blog in BLOGS:
        url = f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={blog}&category=seo&key={API_KEY}"
        res = requests.get(url)
        if res.status_code == 200:
            score = res.json()['lighthouseResult']['categories']['seo']['score'] * 100
            results.append({"url": blog, "seo_score": score})
    
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    get_data()
