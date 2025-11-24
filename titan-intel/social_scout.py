import requests
import os
import time
import json
from concurrent.futures import ThreadPoolExecutor

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
DASHBOARD_DIR = os.path.join(CURRENT_DIR, '..', 'Dashboard', 'static', 'reports')
SITES_FILE = os.path.join(CURRENT_DIR, 'wordlists', 'social_sites.json')

def load_sites_json(filepath):
    """Loads the site list from a .json file."""
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        return {"GitHub": "https://github.com/{}"} # Fallback

SOCIAL_SITES = load_sites_json(SITES_FILE)

# Comprehensive "not found" indicators - more aggressive detection
NOT_FOUND_PATTERNS = [
    # Generic
    "404", "not found", "page not found", "user not found",
    "doesn't exist", "does not exist", "page doesn't exist",
    "account doesn't exist", "profile not found",
    
    # Platform-specific
    "nobody on reddit goes by that name",  # Reddit
    "hmm...this page doesn't exist",  # Twitter/X
    "couldn't find this account",  # TikTok
    "sorry, this page isn't available",  # Instagram (for non-existent)
    "nothing to see here",  # TryHackMe
    "we can't find that page",  # Kaggle
    "the page you requested was not found",
    "this account is unavailable",
    "user cannot be found",
    "profile cannot be found",
    
    # Keep private as existing
    # "this account is private" - handled separately
]

def check_site(site_name, url_format, username):
    url = url_format.format(username)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }
    try:
        response = requests.get(url, headers=headers, timeout=10, allow_redirects=True)
        
        # First check: HTTP status code
        if response.status_code == 404:
            return None
        
        if response.status_code != 200:
            return None
        
        # Get response content (lowercase for case-insensitive matching)
        page_content = response.text.lower()
        final_url = response.url.lower()
        
        # Check if redirected to error/notfound page
        if any(pattern in final_url for pattern in ['notfound', '404', 'error', 'pagenotfound']):
            return None
        
        # Check for "not found" patterns in content
        for pattern in NOT_FOUND_PATTERNS:
            if pattern in page_content:
                return None
        
        # Special case: Private accounts exist, just not publicly visible
        if 'this account is private' in page_content or 'private account' in page_content:
            return {'site': site_name, 'url': url, 'status': 'Found (Private)'}
        
        # If we got here with status 200 and no "not found" indicators, likely valid
        return {'site': site_name, 'url': url, 'status': 'Found'}
        
    except requests.RequestException:
        # Connection errors mean we can't determine existence
        pass
    return None

def run_scout(username):
    if not username: 
        return {'error': 'No username provided.'}
    
    found = []
    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = [executor.submit(check_site, k, v, username) for k, v in SOCIAL_SITES.items()]
        for future in futures:
            res = future.result()
            if res: 
                found.append(res)
                
    results = {'username': username, 'results': found}
    
    TIMESTAMP = time.strftime("%Y%m%d_%H%M%S")
    report_filename = f"social_scout_{username}_{TIMESTAMP}.txt"
    REPORT_FILE_TXT = os.path.join(DASHBOARD_DIR, report_filename)
    
    try:
        os.makedirs(DASHBOARD_DIR, exist_ok=True)
        with open(REPORT_FILE_TXT, 'w') as f:
            f.write("--- Social Media Scout Report ---\n")
            f.write(f"Time: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Target Username: {username}\n")
            f.write("--------------------------------------\n\n")

            if results['results']:
                f.write(f"Found {len(results['results'])} matching accounts:\n\n")
                for account in results['results']:
                    status = account.get('status', 'Found')
                    f.write(f"[+] {account['site']}: {account['url']} [{status}]\n")
            else:
                f.write("No matching accounts found on common sites.\n")
        
        results['report_filename'] = report_filename
                
    except Exception as e:
        print(f"Error saving social scout report: {e}")
        
    return results