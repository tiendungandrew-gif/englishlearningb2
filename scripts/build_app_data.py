import os
import re
import json

ROOT_DIR = r"d:\projectbuild\hoctienganh"
JS_DIR = os.path.join(ROOT_DIR, "js")
os.makedirs(JS_DIR, exist_ok=True)

modules_config = [
    {
        "id": "00_master_maps",
        "title": "Bản Đồ Năng Lực & Điều Phối",
        "badge": "00",
        "icon": "fa-map",
        "desc": "Bản đồ năng lực chuẩn CEFR B2 & VSTEP Bậc 4, ma trận ngữ pháp, từ vựng và 4 kỹ năng"
    },
    {
        "id": "01_b2_overview",
        "title": "Tổng Quan B2 & Định Dạng VSTEP",
        "badge": "01",
        "icon": "fa-award",
        "desc": "Định nghĩa B2, quy chế tính điểm làm tròn VSTEP, chiến lược an toàn 6.0 - 6.5"
    },
    {
        "id": "02_grammar",
        "title": "30 Chủ Điểm Ngữ Pháp Học Thuật",
        "badge": "02",
        "icon": "fa-book-open",
        "desc": "Toàn bộ 30 chủ điểm ngữ pháp cốt lõi với 10 tiêu chí sư phạm chi tiết"
    },
    {
        "id": "03_vocabulary",
        "title": "Từ Vựng 30 Chủ Đề VSTEP",
        "badge": "03",
        "icon": "fa-spell-check",
        "desc": "1.050+ từ vựng học thuật bao quát 100% các lĩnh vực thường gặp trong đề thi"
    },
    {
        "id": "04_collocations_phrasal",
        "title": "Collocations & Phrasal Verbs",
        "badge": "04",
        "icon": "fa-layer-group",
        "desc": "8 nhóm collocations học thuật, cụm động từ chọn lọc cho Speaking & Writing"
    },
    {
        "id": "05_listening",
        "title": "Kỹ Năng Nghe Hiểu (Listening)",
        "badge": "05",
        "icon": "fa-headphones",
        "desc": "Chiến lược 3 Parts, hóa giải bẫy Distractors, kỹ thuật tốc ký Cornell"
    },
    {
        "id": "06_reading",
        "title": "Kỹ Năng Đọc Hiểu (Reading)",
        "badge": "06",
        "icon": "fa-book-reader",
        "desc": "Quy tắc 13-2, 10 dạng câu hỏi chuẩn hóa, 5 bẫy đọc hiểu, Full Mini-Test"
    },
    {
        "id": "07_speaking",
        "title": "Kỹ Năng Nói (Speaking)",
        "badge": "07",
        "icon": "fa-microphone",
        "desc": "Chiến thuật thi máy tính: A.R.E.A Part 1, Thảo luận Part 2, Mind Map Part 3"
    },
    {
        "id": "08_writing",
        "title": "Kỹ Năng Viết (Writing)",
        "badge": "08",
        "icon": "fa-pen-nib",
        "desc": "Task 1 Thư trang trọng/thân mật, Task 2 Luận PEEL 4 đoạn, bài mẫu Band 8.0"
    },
    {
        "id": "09_pronunciation",
        "title": "Phát Âm Chuẩn & Sửa Lỗi L1",
        "badge": "09",
        "icon": "fa-volume-high",
        "desc": "44 âm IPA, trọng âm từ học thuật, Connected speech, trị 10 lỗi phát âm người Việt"
    },
    {
        "id": "10_word_formation",
        "title": "Cấu Tạo Từ & Ma Trận Họ Từ",
        "badge": "10",
        "icon": "fa-cubes",
        "desc": "Tiền tố/hậu tố học thuật, ma trận 80+ họ từ Verb - Noun - Adj - Adv"
    },
    {
        "id": "11_paraphrasing",
        "title": "Nghệ Thuật Paraphrasing B1 ➔ B2",
        "badge": "11",
        "icon": "fa-arrows-rotate",
        "desc": "5 kỹ thuật cốt lõi, kho 105 cặp câu chuyển đổi tương đương theo chủ đề"
    },
    {
        "id": "12_common_mistakes",
        "title": "50+ Lỗi Sai Kinh Điển & Phác Đồ",
        "badge": "12",
        "icon": "fa-triangle-exclamation",
        "desc": "Khắc phục triệt để lỗi can thiệp tiếng mẹ đẻ L1: cú pháp, mạo từ, liên từ kép"
    },
    {
        "id": "13_checklists",
        "title": "Bảng Kiểm Năng Lực B2",
        "badge": "13",
        "icon": "fa-list-check",
        "desc": "Hệ thống tự đánh giá 🔴 🟡 🟢 trước kỳ thi, kiểm soát toàn diện ngữ pháp & từ vựng"
    },
    {
        "id": "14_roadmaps",
        "title": "Lộ Trình Học Tập Khoa Học",
        "badge": "14",
        "icon": "fa-route",
        "desc": "Lộ trình 16 tuần (B1->B2) và 24 tuần (A2->B2), thời khóa biểu 90 phút/ngày"
    },
    {
        "id": "15_review_system",
        "title": "Hệ Thống Ôn Tập Spaced Repetition",
        "badge": "15",
        "icon": "fa-brain",
        "desc": "Đường cong Ebbinghaus, Active Recall, Hộp Leitner 5 ngăn, tối ưu hóa Flashcards"
    },
    {
        "id": "16_resources",
        "title": "Kho Tài Nguyên Học Thuật",
        "badge": "16",
        "icon": "fa-folder-open",
        "desc": "Giáo trình VSTEP/Cambridge, báo chí phân tích, podcast học thuật, 4 đại từ điển"
    },
    {
        "id": "17_master_curriculum",
        "title": "Giáo Trình 5 Cấp Độ 200 Bài Học",
        "badge": "17",
        "icon": "fa-graduation-cap",
        "desc": "Khung chương trình xoắn ốc đào tạo toàn diện từ A2/B1 đến VSTEP B2"
    }
]

app_data = {
    "modules": [],
    "grammarTopics": [],
    "vocabTopics": [],
    "collocations": [],
    "flashcards": [],
    "paraphraseList": [],
    "mistakesList": [],
    "wordFamilies": [],
    "checklistItems": [],
    "quizItems": []
}

# 1. Modules
for m in modules_config:
    mod_dir = os.path.join(ROOT_DIR, m["id"])
    files_data = []
    if os.path.exists(mod_dir):
        for fname in sorted(os.listdir(mod_dir)):
            if fname.endswith(".md"):
                fpath = os.path.join(mod_dir, fname)
                with open(fpath, "r", encoding="utf-8") as f:
                    content = f.read()
                h1_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
                title = h1_match.group(1).strip() if h1_match else fname
                files_data.append({
                    "filename": fname,
                    "title": title,
                    "content": content
                })
    app_data["modules"].append({
        **m,
        "files": files_data
    })

with open(os.path.join(ROOT_DIR, "README.md"), "r", encoding="utf-8") as f:
    readme_content = f.read()
app_data["readme"] = {
    "title": "VSTEP B2 & CEFR B2 Master Knowledge Base",
    "content": readme_content
}

# 2. Grammar Topics
grammar_files = ["topics_01_10.md", "topics_11_20.md", "topics_21_30.md"]
for gfile in grammar_files:
    gpath = os.path.join(ROOT_DIR, "02_grammar", gfile)
    if os.path.exists(gpath):
        with open(gpath, "r", encoding="utf-8") as f:
            content = f.read()
        sections = content.split("\n## CHỦ ĐIỂM ")
        for s in sections[1:]:
            lines = s.strip().split("\n")
            header = lines[0].strip()
            match = re.match(r"(\d+):\s*(.+)", header)
            num = match.group(1) if match else "00"
            gtitle = match.group(2) if match else header
            app_data["grammarTopics"].append({
                "num": num,
                "title": gtitle,
                "fullTitle": f"Chủ điểm {num}: {gtitle}",
                "content": "## CHỦ ĐIỂM " + s.strip()
            })

# 3. Vocabulary Topics
vocab_files = [
    "topics_01_05.md", "topics_06_10.md", "topics_11_15.md",
    "topics_16_20.md", "topics_21_25.md", "topics_26_30.md"
]
for vfile in vocab_files:
    vpath = os.path.join(ROOT_DIR, "03_vocabulary", vfile)
    if os.path.exists(vpath):
        with open(vpath, "r", encoding="utf-8") as f:
            content = f.read()
        sections = content.split("\n## CHỦ ĐỀ ")
        for s in sections[1:]:
            lines = s.strip().split("\n")
            header = lines[0].strip()
            body = "\n".join(lines[1:])
            match = re.match(r"(\d+):\s*(.+)", header)
            num = match.group(1) if match else "00"
            vtitle = match.group(2) if match else header
            
            words_match = re.search(r"-\s*35 từ/cụm từ(?: học thuật)? cốt lõi:\s*(.+)", body)
            words = []
            if words_match:
                raw_words = words_match.group(1).strip()
                words = [w.strip() for w in raw_words.split(",") if w.strip()]
            
            example_match = re.search(r"-\s*Ví dụ B2:\s*(.+)", body)
            example = example_match.group(1).strip() if example_match else ""
            
            speaking_match = re.search(r"-\s*Vận dụng Speaking:\s*(.+)", body)
            speaking = speaking_match.group(1).strip() if speaking_match else ""
            
            writing_match = re.search(r"-\s*Vận dụng Writing(?: Task \d)?:\s*(.+)", body)
            writing = writing_match.group(1).strip() if writing_match else ""
            
            vocab_obj = {
                "num": num,
                "title": vtitle,
                "wordsCount": len(words),
                "words": words,
                "example": example,
                "speaking": speaking,
                "writing": writing
            }
            app_data["vocabTopics"].append(vocab_obj)
            
            # Add top words to flashcards
            for i, w in enumerate(words[:10]):
                app_data["flashcards"].append({
                    "id": f"vocab_{num}_{i+1}",
                    "category": "Vocabulary B2",
                    "topic": vtitle,
                    "front": w,
                    "type": "word",
                    "back": f"Chủ đề: {vtitle}\n\nVí dụ câu B2:\n\"{example}\"",
                    "example": example
                })

# 4. Paraphrasing Pairs (line-by-line parsing)
para_path = os.path.join(ROOT_DIR, "11_paraphrasing", "master_paraphrasing_b2.md")
if os.path.exists(para_path):
    with open(para_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    current_b1 = None
    current_idx = 1
    for line in lines:
        line_str = line.strip()
        # Look for 1. **B1:** ...
        b1_match = re.match(r"^\d+\.\s*\*\*B1:\*\*\s*(.+)", line_str)
        if b1_match:
            current_b1 = b1_match.group(1).strip()
            continue
        # Look for -> **B2:** ...
        if current_b1 and ("**B2:**" in line_str):
            b2_clean = re.sub(r"^[$\-\\>*\s]*\*\*B2:\*\*\s*", "", line_str).strip()
            app_data["paraphraseList"].append({
                "idx": current_idx,
                "b1": current_b1,
                "b2": b2_clean
            })
            app_data["flashcards"].append({
                "id": f"para_{current_idx}",
                "category": "Paraphrase B1 ➔ B2",
                "topic": "Sentence Transformation",
                "front": current_b1,
                "type": "sentence",
                "back": f"✔️ B2 Upgrade:\n{b2_clean}",
                "example": b2_clean
            })
            current_idx += 1
            current_b1 = None

# 5. Common Mistakes
mistakes_path = os.path.join(ROOT_DIR, "12_common_mistakes", "master_common_mistakes_b2.md")
if os.path.exists(mistakes_path):
    with open(mistakes_path, "r", encoding="utf-8") as f:
        content = f.read()
    sections = content.split("\n### LỖI ")
    for s in sections[1:]:
        lines = s.strip().split("\n")
        header = lines[0].strip()
        m_id = header.split(":")[0].strip()
        m_title = header.split(":", 1)[1].strip() if ":" in header else header
        
        wrong_examples = []
        correct_examples = []
        l1_reason = ""
        
        for l in lines[1:]:
            l_str = l.strip()
            if "❌" in l_str and "**SAI:**" in l_str:
                wrong_examples.append(re.sub(r"^-\s*❌\s*\*\*SAI:\*\*\s*", "", l_str).strip("*_ "))
            elif "✔️" in l_str and "**ĐÚNG" in l_str:
                correct_examples.append(re.sub(r"^-\s*✔️\s*\*\*ĐÚNG[^*]*:\*\*\s*", "", l_str).strip("*_ "))
            elif "🔍" in l_str and "**Nguyên nhân L1:**" in l_str:
                l1_reason = re.sub(r"^-\s*🔍\s*\*\*Nguyên nhân L1:\*\*\s*", "", l_str).strip("*_ ")
        
        if wrong_examples and correct_examples:
            app_data["mistakesList"].append({
                "id": m_id,
                "title": m_title,
                "wrong": wrong_examples[0],
                "correct": correct_examples[0],
                "reason": l1_reason
            })
            app_data["flashcards"].append({
                "id": f"mistake_{m_id}",
                "category": "Trị Lỗi Sai L1",
                "topic": m_title,
                "front": f"❌ Lỗi sai thường gặp:\n{wrong_examples[0]}",
                "type": "error",
                "back": f"✔️ Viết chuẩn B2:\n{correct_examples[0]}\n\n🔍 Nguyên nhân L1:\n{l1_reason}",
                "example": correct_examples[0]
            })

# 6. Word Families from 10_word_formation
wf_path = os.path.join(ROOT_DIR, "10_word_formation", "master_word_formation_b2.md")
if os.path.exists(wf_path):
    with open(wf_path, "r", encoding="utf-8") as f:
        content = f.read()
    # Table rows: | 1 | acquire | acquisition | acquisitive | — | Đạt được... |
    table_lines = re.findall(r"\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|", content)
    for row in table_lines:
        wf_obj = {
            "stt": row[0].strip(),
            "verb": row[1].strip().strip("*"),
            "noun": row[2].strip().strip("*"),
            "adj": row[3].strip().strip("*"),
            "adv": row[4].strip().strip("*"),
            "meaning": row[5].strip()
        }
        app_data["wordFamilies"].append(wf_obj)
        # Add to flashcards
        app_data["flashcards"].append({
            "id": f"wf_{wf_obj['stt']}",
            "category": "Word Family Matrix",
            "topic": f"Gốc từ: {wf_obj['verb'] or wf_obj['noun']}",
            "front": f"Họ từ của: {wf_obj['verb'] or wf_obj['noun']} ({wf_obj['meaning']})",
            "type": "wordfamily",
            "back": f"• Verb: {wf_obj['verb']}\n• Noun: {wf_obj['noun']}\n• Adj: {wf_obj['adj']}\n• Adv: {wf_obj['adv']}\n• Nghĩa: {wf_obj['meaning']}",
            "example": f"Verb: {wf_obj['verb']} | Noun: {wf_obj['noun']} | Adj: {wf_obj['adj']}"
        })

# 7. Checklists from 13_checklists
chk_path = os.path.join(ROOT_DIR, "13_checklists", "master_b2_core_checklist.md")
if os.path.exists(chk_path):
    with open(chk_path, "r", encoding="utf-8") as f:
        content = f.read()
    rows = re.findall(r"\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|\s*\[\s*\]\s*\|\s*\[\s*\]\s*\|\s*\[\s*\]\s*\|\s*([^|]+?)\s*\|", content)
    for r in rows:
        app_data["checklistItems"].append({
            "id": f"chk_{r[0]}",
            "num": r[0].strip(),
            "title": r[1].strip(),
            "indicator": r[2].strip()
        })

# 8. Quiz items (12 diverse questions covering Grammar, Collocations, Reading, Listening, Writing)
app_data["quizItems"] = [
    {
        "id": "q1",
        "category": "Grammar Tenses",
        "question": "By the time the committee submits the report tomorrow, they ______ all customer complaints.",
        "options": [
            "will review",
            "will have reviewed",
            "have reviewed",
            "are reviewing"
        ],
        "answer": 1,
        "explanation": "Mốc 'by the time + hiện tại' diễn tả một hành động sẽ hoàn tất trước một thời điểm hoặc sự kiện trong tương lai -> bắt buộc dùng thì Tương lai Hoàn thành (Future Perfect)."
    },
    {
        "id": "q2",
        "category": "Inversion (Đảo ngữ)",
        "question": "Choose the grammatically correct inverted sentence:",
        "options": [
            "Seldom the government has intervened in market pricing.",
            "Seldom has the government intervened in market pricing.",
            "Seldom did the government has intervened in market pricing.",
            "Seldom the government intervened in market pricing."
        ],
        "answer": 1,
        "explanation": "Khi trạng từ phủ định/bán phủ định 'Seldom' đứng đầu câu, trợ động từ bắt buộc phải đảo lên trước chủ ngữ: Seldom + Trợ động từ + S + V."
    },
    {
        "id": "q3",
        "category": "Conditionals (Câu điều kiện)",
        "question": "Had the environmental authorities implemented stringent regulations earlier, the catastrophic river pollution ______.",
        "options": [
            "would be prevented",
            "would have been prevented",
            "will have prevented",
            "was prevented"
        ],
        "answer": 1,
        "explanation": "Đây là cấu trúc đảo ngữ của câu điều kiện loại 3 (Had + S + V3/ed..., S + would have + V3/ed) diễn tả giả định trái ngược với quá khứ ở thể bị động."
    },
    {
        "id": "q4",
        "category": "Common Mistakes (Sửa lỗi sai)",
        "question": "Which sentence avoids negative L1 language transfer errors?",
        "options": [
            "Although artificial intelligence offers immense benefits, but it poses significant ethical risks.",
            "Although artificial intelligence offers immense benefits, it poses significant ethical risks.",
            "Because he studied diligently, so he secured the B2 certificate.",
            "The committee discussed about the ecological crisis yesterday."
        ],
        "answer": 1,
        "explanation": "Trong tiếng Anh, mỗi câu phức chỉ dùng DUY NHẤT một liên từ phụ thuộc ('Although', không đi kèm 'but'). Động từ 'discuss' là ngoại động từ không đi với giới từ 'about'."
    },
    {
        "id": "q5",
        "category": "Word Formation (Cấu tạo từ)",
        "question": "Rapid urbanization has precipitated an ______ increase in housing costs across the metropolitan area.",
        "options": [
            "precedent",
            "precedented",
            "unprecedented",
            "precedence"
        ],
        "answer": 2,
        "explanation": "Cần một tính từ mang nghĩa 'chưa từng có tiền lệ' để bổ nghĩa cho danh từ 'increase' -> 'unprecedented'."
    },
    {
        "id": "q6",
        "category": "Reading Skills",
        "question": "Trong bài thi VSTEP Reading, khi gặp câu hỏi 'The word X in paragraph 2 is closest in meaning to...', chiến thuật tối ưu nhất là gì?",
        "options": [
            "Dịch nghĩa đơn lẻ của từ X trong từ điển rồi chọn ngay",
            "Đọc câu chứa từ X và câu liền kề để xác định nghĩa theo ngữ cảnh cụ thể (Context Clues)",
            "Luôn chọn từ dài nhất và phức tạp nhất trong 4 phương án",
            "Bỏ qua câu này để làm các câu Main Idea trước"
        ],
        "answer": 1,
        "explanation": "Từ vựng trong bài đọc học thuật thường mang nghĩa chuyên biệt theo ngữ cảnh (polysemous words). Việc đọc câu chứa từ và đối chiếu mối quan hệ logic (tương phản, nguyên nhân, đồng nghĩa) là chìa khóa then chốt."
    },
    {
        "id": "q7",
        "category": "Listening Skills",
        "question": "Trong bài thi Nghe VSTEP Part 1, khi người nói phát biểu: 'The departure gate was initially scheduled as Gate 12. However, due to tarmac maintenance, please proceed immediately to Gate 19', đây là bẫy gì?",
        "options": [
            "Bẫy đồng âm khác nghĩa (Homophone Trap)",
            "Bẫy đổi ý / Thay đổi phương án phút chót (Self-correction / Reversal Trap)",
            "Bẫy tốc độ nói quá nhanh",
            "Bẫy phủ định ngầm"
        ],
        "answer": 1,
        "explanation": "Đây là Bẫy Đổi Ý kinh điển (Reversal Trap). Tín hiệu 'initially' báo hiệu kế hoạch cũ và 'However' chuyển hướng sang thông tin thực tế cuối cùng (Gate 19)."
    },
    {
        "id": "q8",
        "category": "Academic Writing",
        "question": "Cấu trúc một đoạn thân bài bài luận học thuật Task 2 (Body Paragraph) theo công thức P-E-E-L gồm những thành phần nào?",
        "options": [
            "Purpose - Example - Evaluation - Link",
            "Point (Câu chủ đề) - Explanation (Giải thích chuyên sâu) - Example (Dẫn chứng cụ thể) - Link (Câu chốt liên kết)",
            "Problem - Effect - Evidence - Lesson",
            "Past - Present - Future - Conclusion"
        ],
        "answer": 1,
        "explanation": "P-E-E-L là công thức vàng chuẩn mực quốc tế: Point (Nêu luận điểm), Explanation (Mở rộng lý do tại sao), Example (Ví dụ thực tế/số liệu), Link (Chốt hạ kết nối về câu luận đề)."
    },
    {
        "id": "q9",
        "category": "Paraphrasing",
        "question": "Nâng cấp câu B1 'Many people believe that money cannot buy real happiness' lên câu chuẩn B2 học thuật:",
        "options": [
            "A lot of people think money never buys true joy.",
            "It is widely asserted that pecuniary wealth does not necessarily equate to genuine life satisfaction.",
            "Because money is not happiness, so people believe it.",
            "People say having much cash is not real happiness."
        ],
        "answer": 1,
        "explanation": "Phương án B sử dụng kỹ thuật Bị động khách quan ('It is widely asserted that...') và từ vựng học thuật ('pecuniary wealth', 'equate to', 'genuine life satisfaction')."
    },
    {
        "id": "q10",
        "category": "Collocations",
        "question": "Select the correct academic collocation: 'The international summit urged countries to ______ fossil fuels and transition to renewables.'",
        "options": [
            "throw away",
            "phase out",
            "drop off",
            "give up"
        ],
        "answer": 1,
        "explanation": "'phase out' (từng bước loại bỏ) là collocation học thuật chuẩn trong chủ đề Môi trường & Năng lượng."
    }
]

output_js = f"window.KB_DATA = {json.dumps(app_data, ensure_ascii=False, indent=2)};"
with open(os.path.join(JS_DIR, "data.js"), "w", encoding="utf-8") as f:
    f.write(output_js)

print("SUCCESS: Generated js/data.js")
print(f"- Modules: {len(app_data['modules'])}")
print(f"- Grammar Topics: {len(app_data['grammarTopics'])}")
print(f"- Vocab Topics: {len(app_data['vocabTopics'])}")
print(f"- Flashcards: {len(app_data['flashcards'])}")
print(f"- Paraphrase items: {len(app_data['paraphraseList'])}")
print(f"- Mistakes items: {len(app_data['mistakesList'])}")
print(f"- Word Families: {len(app_data['wordFamilies'])}")
print(f"- Checklist items: {len(app_data['checklistItems'])}")
print(f"- Quiz items: {len(app_data['quizItems'])}")
print(f"- File size: {round(os.path.getsize(os.path.join(JS_DIR, 'data.js')) / 1024, 2)} KB")
