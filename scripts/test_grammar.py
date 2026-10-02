# -*- coding: utf-8 -*-
import os

content = """# PHẦN 2 — KIẾN THỨC NGỮ PHÁP BẮT BUỘC (PHẦN 1: CHỦ ĐIỂM 01 - 10)
Tài liệu biên soạn chuyên sâu theo chuẩn CEFR B2 & VSTEP Bậc 4.
"""
with open(r"02_grammar\topics_01_10.md", "w", encoding="utf-8") as f:
    f.write(content)
print("File topics_01_10.md created successfully.")
