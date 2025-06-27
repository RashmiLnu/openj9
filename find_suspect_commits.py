import subprocess

# Hardcoded for now — replace with dynamic inputs later
GOOD_SHA = "ab9584ee40"
BAD_SHA = "4d92969242"
failure_files = [".java"]

def get_commits_between(good, bad):
    cmd = ["git", "log", "--pretty=format:%H", f"{good}..{bad}"]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, text=True)
    return result.stdout.strip().splitlines()

def get_files_changed(commit):
    cmd = ["git", "show", "--name-only", "--pretty=format:", commit]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, text=True)
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]

def find_suspect_commits(commits, failure_files):
    suspects = []
    for sha in commits:
        files = get_files_changed(sha)
        for fail_file in failure_files:
            if any(fail_file in f for f in files):
                suspects.append((sha, files))
                break
    return suspects

# === MAIN ===
commits = get_commits_between(GOOD_SHA, BAD_SHA)
suspects = find_suspect_commits(commits, failure_files)

for sha, files in suspects:
    print(f"🔍 Suspect Commit: {sha}")
    print(f"🔗 https://github.com/eclipse-openj9/openj9/commit/{sha}")
    print(f"📂 Changed files: {files}")
    print("-" * 60)
