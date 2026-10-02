# -*- coding: utf-8 -*-
import os

grammar_map = """# B2 GRAMMAR MAP: MA TRẬN 30 CHỦ ĐIỂM NGỮ PHÁP PHÂN TẦNG

Phân loại 30 chủ điểm theo 3 cấp độ:
- **[CORE]**: Kiến thức nền tảng bắt buộc phải làm đúng 100%, sai là mất điểm B1/B2.
- **[B2]**: Kiến thức phân loại, chìa khóa để đạt chuẩn B2 (6.0 - 8.0 VSTEP).
- **[ADVANCED]**: Kiến thức nâng cao tạo điểm nhấn ấn tượng trong Writing & Speaking (hướng tới 7.5 - 8.5+).

| STT | Chủ điểm ngữ pháp | Phân tầng | Mục tiêu ứng dụng trong VSTEP B2 |
|---|---|---|---|
| 1 | Tenses Overview (Tổng quan 12 thì) | [CORE] | Nắm trục thời gian, nhận diện dấu hiệu trong Reading/Listening |
| 2 | Present / Past / Future | [CORE] | Mô tả sự việc, thói quen, kế hoạch chuẩn xác trong Speaking Part 1 & Writing |
| 3 | Perfect Tenses (Hiện tại/Quá khứ/Tương lai hoàn thành) | [B2] | Diễn đạt tính liên tục, kinh nghiệm, mốc thời gian hoàn tất trong Writing Task 2 |
| 4 | Continuous Tenses (Tiếp diễn & Hoàn thành tiếp diễn) | [CORE] | Nhấn mạnh tính quá trình, hành động nền trong Speaking & Listening |
| 5 | Passive Voice (Bị động đơn & Bị động nâng cao) | [B2] | Giọng văn học thuật khách quan trong Writing Task 2; xử lý câu hỏi Reading |
| 6 | Modal Verbs (Động từ khuyết thiếu & Modal Perfect) | [B2] | Thể hiện mức độ chắc chắn, đưa ra khuyến nghị, suy đoán trong Speaking Part 2/3 |
| 7 | Conditionals (Type 0, 1, 2, 3 & Mixed) | [B2] | Lập luận logic, phản biện "nếu... thì...", phân tích giải pháp Speaking Part 2 |
| 8 | Wish / If only (Ước muốn ở hiện tại, tương lai, quá khứ) | [B2] | Bộc lộ quan điểm, nuối tiếc, giả định tình huống trong Speaking Part 1 & 2 |
| 9 | Reported Speech (Câu gián tiếp & Reporting Verbs) | [B2] | Trích dẫn ý kiến chuyên gia, báo cáo lại lời nói trong Writing Task 1 & 2 |
| 10 | Relative Clauses (Xác định, Không xác định, Rút gọn) | [B2] | Ghép câu phức, bổ nghĩa rõ ràng, biến đổi câu đơn thành câu ghép tự nhiên |
| 11 | Noun Clauses (Mệnh đề danh từ với that/if/whether/wh-) | [B2] | Mở rộng chủ ngữ/tân ngữ học thuật: *The fact that...*, *Whether it is beneficial...* |
| 12 | Adverbial Clauses (Chỉ nguyên nhân, nhượng bộ, kết quả, thời gian) | [B2] | Tạo liên kết logic chặt chẽ trong bài luận Writing Task 2 |
| 13 | Gerund & Infinitive (V-ing vs. To-V & Verbs đổi nghĩa) | [CORE] | Viết đúng kết cấu vị ngữ; tránh lỗi sai phổ biến của người Việt |
| 14 | Participle Clauses (Hiện tại & Quá khứ phân từ rút gọn) | [ADVANCED] | Rút gọn mệnh đề nâng cao, tăng tính cô đọng cho Writing Task 2 |
| 15 | Comparisons (So sánh kép, so sánh bội, so sánh hơn/nhất) | [B2] | So sánh các phương án trong Speaking Part 2, mô tả sự phát triển trong Writing |
| 16 | Articles (A / An / The & Zero Article) | [CORE] | Tránh lỗi sai mạo từ kinh niên của người Việt; nâng tính tự nhiên của câu |
| 17 | Determiners (This, that, each, every, other, another...) | [CORE] | Đảm bảo tính liên kết tham chiếu (Reference) trong Reading và Writing |
| 18 | Quantifiers (Few, little, much, many, a lot of, plenty of...) | [CORE] | Sử dụng đúng danh từ đếm được/không đếm được trong lập luận số liệu |
| 19 | Prepositions (Giới từ chỉ thời gian, nơi chốn, đi kèm cố định) | [CORE] | Tránh lỗi dịch word-by-word từ tiếng Việt |
| 20 | Conjunctions (Coordinating, Subordinating, Correlative) | [CORE] | Kết nối câu đơn thành câu ghép và câu phức |
| 21 | Subject-Verb Agreement (Sự hòa hợp chủ - vị nâng cao) | [CORE] | Xử lý chủ ngữ phức, danh từ tập hợp, cấu trúc song song không bị chia sai |
| 22 | Question Forms (Wh- questions, Indirect questions) | [CORE] | Phản xạ hiểu câu hỏi Listening & đặt câu hỏi lịch sự trong Writing Task 1 |
| 23 | Tag Questions (Câu hỏi đuôi đặc biệt) | [B2] | Sử dụng trong giao tiếp tự nhiên Speaking Part 1; xử lý bẫy Listening |
| 24 | Causative Structures (Have/Get sth done, Make/Let/Have sb do) | [B2] | Diễn đạt hành động nhờ/khiến ai đó làm gì trong Speaking và Writing |
| 25 | Inversion (Đảo ngữ với Never, Rarely, Not only, Only after, Under no circumstances) | [ADVANCED] | Điểm nhấn ngữ pháp đắt giá (score-boosting) trong Writing Task 2 |
| 26 | Emphasis (Cleft Sentences: It is... that / What... is...) | [B2] | Nhấn mạnh luận điểm chính trong bài viết học thuật và Speaking Part 3 |
| 27 | Linking Structures (Discourse Markers & Transitions) | [B2] | Đạt điểm tối đa tiêu chí Coherence & Cohesion (Furthermore, Consequently...) |
| 28 | Complex Sentences (Cấu trúc đa mệnh đề cân bằng) | [B2] | Kiểm soát câu dài từ 25-35 từ mà không bị rối cấu trúc hoặc vỡ ngữ pháp |
| 29 | Sentence Transformation (Biến đổi câu tương đương) | [B2] | Kỹ năng Paraphrasing để mở bài Writing Task 2 và tóm tắt ý Listening/Reading |
| 30 | Cấu trúc B2 đặc trưng (Subjunctive, Had better/Would rather, It is high time...) | [B2] | Xử lý các câu hỏi ngữ pháp phân loại và tăng tính học thuật |
"""

with open(r"00_master_maps\02_grammar_map.md", "w", encoding="utf-8") as f:
    f.write(grammar_map)

print("02_grammar_map.md written.")
