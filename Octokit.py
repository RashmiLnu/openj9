import requests

GITHUB_TOKEN = "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"  # Replace with your actual token
OWNER = "eclipse-openj9"
REPO = "openj9"
COMMIT_SHA = "10fbdc14673072822e1e6c3ba75768243561e673"  # Example SHA

def get_changed_files(owner, repo, sha, token):
    url = f"https://api.github.com/repos/{owner}/{repo}/commits/{sha}"
    headers = {"Authorization": f"Bearer {token}"}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        files = [f["filename"] for f in data.get("files", [])]
        return files
    else:
        print(f"Error: {response.status_code} — {response.text}")
        return []

# Test it
files_changed = get_changed_files(OWNER, REPO, COMMIT_SHA, GITHUB_TOKEN)
print("Changed files:")
for f in files_changed:
    print(f)
