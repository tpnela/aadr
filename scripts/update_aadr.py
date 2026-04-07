import os
import glob
import re

def process_aadr():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    records_dir = os.path.join(repo_root, "records")
    aggr_dir = os.path.join(repo_root, "aggregations")
    readme_path = os.path.join(repo_root, "README.md")
    
    if not os.path.exists(aggr_dir):
        os.makedirs(aggr_dir)

    aadr_files = sorted(glob.glob(os.path.join(records_dir, "AADR-*.md")))
    
    records_metadata = []
    domain_contents = {}

    for file_path in aadr_files:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        file_name = os.path.basename(file_path)
        
        # Parse title
        # Looks like:
        # # Title
        # AADR-nnn - Something
        title_match = re.search(r"# Title\s+(AADR-\d+\s+-\s+.*)", content)
        title = title_match.group(1).strip() if title_match else file_name
        
        records_metadata.append({"file": file_name, "title": title})
        
        # Parse domains
        # Looks like:
        # # Applies
        # - JAVA
        # - SECURITY
        domains = []
        applies_match = re.search(r"# Applies\s+(.*?)(?=\n# |\Z)", content, re.DOTALL)
        if applies_match:
            applies_text = applies_match.group(1)
            for line in applies_text.splitlines():
                line = line.strip()
                if line.startswith("- "):
                    # Extract the domain, remove possible markdown formatting if any, usually just raw caps
                    domain = line[2:].strip()
                    domains.append(domain)
                    
        for domain in domains:
            if domain not in domain_contents:
                domain_contents[domain] = []
            domain_contents[domain].append(content.strip())

    # Write domain aggregations
    domain_files = []
    for domain, contents in domain_contents.items():
        domain_file_name = f"{domain}.md"
        domain_files.append(domain_file_name)
        
        aggr_file_path = os.path.join(aggr_dir, domain_file_name)
        with open(aggr_file_path, "w", encoding="utf-8") as f:
            f.write("\n\n---\n\n".join(contents))
            f.write("\n")
            
    domain_files.sort()

    # Update README
    with open(readme_path, "r", encoding="utf-8") as f:
        readme_content = f.read()
    
    # Generate Records section
    records_text = "## Records\n"
    for rm in records_metadata:
        records_text += f"- [{rm['title']}](records/{rm['file']})\n"
        
    domains_text = "## Specialisation domains\n"
    for d in domain_files:
        # Strip .md for display name
        display_domain = d[:-3]
        domains_text += f"- [{display_domain}](aggregations/{d})\n"

    # Replace in README
    # Find `# Content\n...` until `# How this works`
    content_pattern = re.compile(r"(# Content\n.*?)# How this works", re.DOTALL)
    
    new_content_section = f"# Content\n{records_text}\n{domains_text}\n"
    new_readme = content_pattern.sub(f"{new_content_section}# How this works", readme_content)

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(new_readme)

if __name__ == "__main__":
    process_aadr()
