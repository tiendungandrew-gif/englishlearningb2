import os
import glob
import re

ROOT_DIR = r"d:\projectbuild\hoctienganh"

def clean_latex(text):
    # 1. Replace arrows
    text = re.sub(r"\$\\rightarrow\$|\$\\to\$|\\rightarrow", "➔", text)
    # 2. Replace ge / le
    text = re.sub(r"\$\\ge\$|\\ge\b", "≥", text)
    text = re.sub(r"\$\\le\$|\\le\b", "≤", text)
    text = re.sub(r"\$\\pm\$|\\pm\b", "±", text)
    
    # 3. Specific verb forms with \text
    text = re.sub(r"\$V\\text\{-ing\}\$", "**V-ing**", text)
    text = re.sub(r"V\\text\{-ing\}", "V-ing", text)
    text = re.sub(r"\$V\\text\{-s/es\}\$", "**V(s/es)**", text)
    text = re.sub(r"V\\text\{-s/es\}", "V(s/es)", text)
    text = re.sub(r"\$V\\text\{-bare\}\$", "**V(bare)**", text)
    text = re.sub(r"V\\text\{-bare\}", "V(bare)", text)
    text = re.sub(r"\$V\\text\{-ed\}\$", "**V(ed)**", text)
    text = re.sub(r"V\\text\{-ed\}", "V(ed)", text)
    text = re.sub(r"Adj/Adv\\text\{-er\}", "Adj/Adv-er", text)
    text = re.sub(r"Adj/Adv\\text\{-est\}", "Adj/Adv-est", text)

    # 4. Strip \text{...}
    text = re.sub(r"\\text\{([^}]+)\}", r"\1", text)

    # 5. Fix math formulas wrapped in $...$
    def clean_formula(match):
        inner = match.group(1)
        # clean backslash spaces
        inner = inner.replace(r"\ ", " ")
        inner = inner.replace(r"\text", "")
        inner = re.sub(r"[{}]", "", inner)
        inner = inner.replace("_1", "1").replace("_2", "2")
        return f"**{inner.strip()}**"

    # Block formulas $$ ... $$
    text = re.sub(r"\$\$(.+?)\$\$", clean_formula, text, flags=re.DOTALL)
    # Inline formulas $ ... $
    text = re.sub(r"\$([^$\n]+?)\$", clean_formula, text)

    # Clean double bold like ****
    text = text.replace("****", "**")
    return text

# Process all markdown files outside scripts
md_files = glob.glob(os.path.join(ROOT_DIR, "*", "*.md"))
md_files.append(os.path.join(ROOT_DIR, "README.md"))

cleaned_count = 0
for fpath in md_files:
    if "scripts" in fpath:
        continue
    with open(fpath, "r", encoding="utf-8") as fp:
        original = fp.read()
    
    cleaned = clean_latex(original)
    if cleaned != original:
        with open(fpath, "w", encoding="utf-8") as fp:
            fp.write(cleaned)
        cleaned_count += 1
        print(f"Cleaned LaTeX/Font formatting in: {os.path.basename(fpath)}")

print(f"\nDone! Cleaned {cleaned_count} files.")
