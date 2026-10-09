import requests
from bs4 import BeautifulSoup

def evaluate_seo(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        return {'score': 0, 'issues': [f"Error fetching the URL: {e}"]}

    soup = BeautifulSoup(response.text, 'lxml')
    
    score = 100
    issues = []

    # Check title tag
    title_tag = soup.title
    if title_tag is None or len(title_tag.text) < 10:
        issues.append("Missing or too short title tag.")
        score -= 20

    # Check meta description tag
    meta_description = soup.find("meta", attrs={"name": "description"})
    if meta_description is None or len(meta_description.get("content", "")) < 50:
        issues.append("Missing or too short meta description.")
        score -= 20

    # Check for h1 tag
    h1_tags = soup.find_all("h1")
    if not h1_tags:
        issues.append("Missing h1 tag.")
        score -= 20
    elif len(h1_tags) > 1:
        issues.append("Multiple h1 tags found.")
        score -= 10

    # Check for alt attributes in images
    images = soup.find_all('img')
    for img in images:
        if not img.get('alt'):
            issues.append("Image missing alt attribute.")
            score -= 5

    # Check internal links
    links = soup.find_all('a', href=True)
    internal_links = [link for link in links if url in link['href']]
    if len(internal_links) < 3:
        issues.append("Fewer than 3 internal links found.")
        score -= 10

    # Check for heading structure
    if len(soup.find_all('h2')) < 1:
        issues.append("No h2 tags found.")
        score -= 5

    return {
        'score': score,
        'issues': issues,
    }

if __name__ == "__main__":
    url = input("Enter the URL of your website: ")
    result = evaluate_seo(url)
    
    print(f"SEO Score: {result['score']}")
    if result['issues']:
        print("Issues found:")
        for issue in result['issues']:
            print(f"- {issue}")
    else:
        print("No issues found! Your SEO is in good shape.")