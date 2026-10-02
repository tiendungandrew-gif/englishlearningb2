# -*- coding: utf-8 -*-
import os

maps_content = """# B2 MASTER COMPETENCY MAP & KNOWLEDGE BLUEPRINT

## 1. Sơ đồ năng lực tổng quát (Competency Map)
Trình độ CEFR B2 (Vantage Level) - Bậc 4 Khung 6 bậc Việt Nam (VSTEP.3-5) là ngưỡng chuyển tiếp từ người học phụ thuộc (Basic/Independent sơ cấp) sang người dùng độc lập có khả năng tư duy biện luận và vận dụng linh hoạt ngôn ngữ trong học thuật và công việc.

```
       [ NỀN TẢNG CỐT LÕI (Foundational System) ]
       ├── Pronunciation (IPA, Connected Speech, Intonation)
       ├── Grammar (Core Tenses, Clauses, Transformations)
       └── Lexical Resource (Collocations, Academic Word List, Word Families)
                          │
                          ▼
       [ KỸ NĂNG TIẾP NHẬN (Receptive Skills) ]
       ├── Listening: Xử lý diễn ngôn tốc độ tự nhiên, lọc nhiễu, suy luận
       └── Reading: Đọc hiểu 2000 từ học thuật, nắm bắt ẩn ý và luận điểm
                          │
                          ▼
       [ BỘ NÃO XỬ LÝ TRUNG GIAN (Cognitive Processing) ]
       ├── Paraphrasing & Summarizing (Chuyển đổi linh hoạt cấu trúc/từ vựng)
       └── Critical Thinking & Idea Generation (Lập luận đa chiều, phản biện)
                          │
                          ▼
       [ KỸ NĂNG SẢN SINH (Productive Skills) ]
       ├── Speaking: Phản xạ trôi chảy, phân tích giải pháp, thuyết trình
       └── Writing: Viết email/thư chuẩn văn phong, viết luận học thuật chặt chẽ
```

## 2. Tiêu chuẩn 4 Trụ cột Năng lực B2:
1. **Grammatical Accuracy & Range (Độ chuẩn xác và đa dạng ngữ pháp):** Kiểm soát tốt các thì và câu phức; hạn chế lỗi hệ thống; vận dụng linh hoạt câu điều kiện, mệnh đề quan hệ rút gọn, bị động, câu chẻ, đảo ngữ.
2. **Lexical Resource (Vốn từ vựng):** Sở hữu từ 3.500 - 4.500 từ vựng chủ động; làm chủ Collocations và Phrasal verbs; tránh dùng từ lặp bằng cách paraphrase.
3. **Fluency & Coherence (Độ trôi chảy và mạch lạc):** Duy trì lời nói không bị ngắt quãng kéo dài; bài viết có cấu trúc đoạn chuẩn (Topic sentence - Supporting idea - Example - Concluding remark) kết hợp liên từ chuyển tiếp tự nhiên.
4. **Pragmatic Appropriacy (Tính phù hợp văn cảnh):** Phân biệt rành mạch văn phong trang trọng (formal) và thân mật (informal) trong bài thi VSTEP Task 1 & Task 2.
"""

with open(r"00_master_maps\01_b2_competency_map.md", "w", encoding="utf-8") as f:
    f.write(maps_content)

print("01_b2_competency_map.md written.")
