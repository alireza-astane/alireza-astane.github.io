import os
import requests
import base64
import datetime
import re

# GitHub API
GITHUB_USERNAME = "alireza-astane"
GITHUB_API = "https://api.github.com"

# Directory for Jekyll posts
POSTS_DIR = "_posts"
os.makedirs(POSTS_DIR, exist_ok=True)


def get_repos():
    """Fetches the list of public repositories for the user."""
    url = f"{GITHUB_API}/users/{GITHUB_USERNAME}/repos"
    response = requests.get(url)
    return response.json()


def get_readme(repo_name):
    """Fetches the README file of a repository in Markdown format."""
    url = f"{GITHUB_API}/repos/{GITHUB_USERNAME}/{repo_name}/readme"
    response = requests.get(url)

    if response.status_code == 200:
        content = response.json()["content"]
        return base64.b64decode(content).decode("utf-8")
    return None


def remove_links(content):
    """
    Removes all hyperlinks (both internal and external).
    - Removes: `![image](...)`
    - Removes: `[label](...)` but keeps `label`
    """
    # Remove images completely
    content = re.sub(r"!\[.*?\]\(.*?\)", "", content)

    # Remove all links but keep labels
    content = re.sub(r"\[(.*?)\]\(.*?\)", r"\1", content)

    return content


def save_post(repo, content):
    """Saves the README content as a Markdown file with front matter."""
    repo_name = repo["name"]
    repo_desc = (
        repo["description"] if repo["description"] else "No description available."
    )
    today = datetime.datetime.utcnow()
    date_str = today.strftime("%Y-%m-%d")
    time_str = today.strftime("%Y-%m-%d %H:%M:%S +0000")
    filename = f"{POSTS_DIR}/{date_str}-{repo_name}.md"

    content = remove_links(content)

    front_matter = f"""---
title: {repo_name}
date: {time_str}
categories: [GitHub, Repositories]
tags: [github, {repo_name.lower()}]
---

---
description: {repo_desc}
---
---
toc: false
---

{content}
"""

    with open(filename, "w", encoding="utf-8") as file:
        file.write(front_matter)


def generate_posts():
    """Fetches README files, removes links, and saves them as Markdown posts."""
    repos = get_repos()
    for repo in repos:
        readme_content = get_readme(repo["name"])
        if readme_content:
            save_post(repo, readme_content)


if __name__ == "__main__":
    generate_posts()
