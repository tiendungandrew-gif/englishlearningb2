# -*- coding: utf-8 -*-
import os

skills_map = """# B2 SKILLS MAP: MA TRẬN 4 KỸ NĂNG VSTEP B2

Bài thi VSTEP (Vietnamese Standardized Test of English Proficiency) bậc 3-5 đánh giá toàn diện 4 kỹ năng trên máy tính với tổng thang điểm 10. Điểm B2 tương ứng với mức điểm từ 6.0 đến 8.0 (làm tròn đến 0.5).

```
========================================================================================
                                 MA TRẬN 4 KỸ NĂNG VSTEP
========================================================================================
[1. LISTENING] (~40 phút, 35 câu hỏi, chỉ nghe 1 lần duy nhất)
  ├── Part 1 (8 câu): Thông báo, hướng dẫn ngắn (chọn 1 trong 4 đáp án A, B, C, D)
  ├── Part 2 (12 câu): 3 đoạn hội thoại dài (mỗi đoạn 4 câu hỏi)
  └── Part 3 (15 câu): 3 bài giảng/thuyết trình học thuật (mỗi bài 5 câu hỏi)
  🎯 Mục tiêu B2: 20 - 26/35 câu đúng (tương đương 6.0 - 7.5/10)

[2. READING] (60 phút, 40 câu hỏi trắc nghiệm, 4 bài đọc ~2.000 từ)
  ├── Passage 1 & 2 (~450 từ/bài): Chủ đề đời sống, xã hội, khoa học phổ thông
  └── Passage 3 & 4 (~550 từ/bài): Chủ đề học thuật chuyên sâu (lịch sử, kinh tế, tâm lý học)
  🎯 Mục tiêu B2: 24 - 30/40 câu đúng (tương đương 6.0 - 7.5/10)

[3. WRITING] (60 phút, 2 phần, gõ trên bàn phím máy tính)
  ├── Task 1 (20 phút, tối thiểu 120 từ, chiếm 1/3 tổng điểm Writing):
  │     Viết thư/email (trang trọng, bán trang trọng, hoặc thân mật) trả lời tình huống
  └── Task 2 (40 phút, tối thiểu 250 từ, chiếm 2/3 tổng điểm Writing):
        Viết bài luận học thuật (Nghị luận xã hội: Opinion, Discussion, Problem-Solution)
  🎯 Mục tiêu B2: 6.0 - 7.5/10 (Đáp ứng đầy đủ yêu cầu đề, chia đoạn chuẩn, từ vựng C1/B2, ngữ pháp đa dạng)

[4. SPEAKING] (12 phút, 3 phần, thu âm trực tiếp qua tai nghe & micro máy tính)
  ├── Part 1 (3 phút): Social Interaction (2 chủ đề quen thuộc, 3-6 câu hỏi)
  ├── Part 2 (4 phút): Solution Discussion (1 tình huống + 3 lựa chọn; chọn 1 và phản biện 2 lựa chọn còn lại)
  └── Part 3 (5 phút): Topic Development (Phát triển chủ đề với mind-map + câu hỏi mở rộng)
  🎯 Mục tiêu B2: 6.0 - 7.5/10 (Trôi chảy, phát âm rõ ràng có trọng âm & ngữ điệu, dùng tốt liên từ và từ vựng B2)
========================================================================================
```
"""

checklist = """# B2 MASTER CHECKLIST (BẢNG THEO DÕI TIẾN ĐỘ TOÀN DIỆN)

Hệ thống đánh giá theo 3 cấp độ trạng thái:
- 🔴 **Chưa biết**: Chưa học hoặc chưa hiểu rõ bản chất.
- 🟡 **Biết nhưng chưa dùng được**: Hiểu lý thuyết nhưng khi Nói/Viết vẫn hay sai hoặc bị ngắc ngứ.
- 🟢 **Thành thạo**: Phản xạ tự nhiên, dùng chính xác và linh hoạt trong mọi ngữ cảnh.

---

## 1. Grammar Master Checklist (30 Chủ điểm)
- [ ] 🔴 🟡 🟢 01. Tenses Overview & Timeline Matrix
- [ ] 🔴 🟡 🟢 02. Present / Past / Future Foundations
- [ ] 🔴 🟡 🟢 03. Perfect Tenses (Present Perfect vs. Past Simple, Past Perfect, Future Perfect)
- [ ] 🔴 🟡 🟢 04. Continuous Tenses & Stative vs. Dynamic Verbs
- [ ] 🔴 🟡 🟢 05. Passive Voice (Basic, Impersonal Passive, Causative Passive)
- [ ] 🔴 🟡 🟢 06. Modal Verbs & Modal Perfects (should have, must have, could have)
- [ ] 🔴 🟡 🟢 07. Conditionals (Type 0, 1, 2, 3, Mixed Conditionals & Inverted Conditionals)
- [ ] 🔴 🟡 🟢 08. Wish & If Only Structures
- [ ] 🔴 🟡 🟢 09. Reported Speech & Advanced Reporting Verbs (urge, suggest, insist, deny)
- [ ] 🔴 🟡 🟢 10. Relative Clauses & Reduced Relative Clauses (V-ing / V3-ed / To-V)
- [ ] 🔴 🟡 🟢 11. Noun Clauses (That-clauses, Wh-clauses, Whether/If-clauses)
- [ ] 🔴 🟡 🟢 12. Adverbial Clauses (Concession, Reason, Purpose, Result, Condition)
- [ ] 🔴 🟡 🟢 13. Gerunds & Infinitives (Verb patterns, Verbs with meaning shifts)
- [ ] 🔴 🟡 🟢 14. Participle Clauses (Rút gọn đồng chủ ngữ, nguyên nhân - hệ quả)
- [ ] 🔴 🟡 🟢 15. Advanced Comparisons (Double comparative, Proportional comparisons)
- [ ] 🔴 🟡 🟢 16. Articles (A/An/The & Zero Article với danh từ chung/riêng/trừu tượng)
- [ ] 🔴 🟡 🟢 17. Determiners & Reference Words
- [ ] 🔴 🟡 🟢 18. Quantifiers (Countable vs. Uncountable, nuance differences)
- [ ] 🔴 🟡 🟢 19. Dependent Prepositions (Verbs, Adjectives & Nouns + Prepositions)
- [ ] 🔴 🟡 🟢 20. Conjunctions & Discourse Markers
- [ ] 🔴 🟡 🟢 21. Subject-Verb Agreement (Complex subjects, Quantifiers, Inversions)
- [ ] 🔴 🟡 🟢 22. Question Forms & Indirect Questions
- [ ] 🔴 🟡 🟢 23. Special Tag Questions
- [ ] 🔴 🟡 🟢 24. Causative Structures (Have/Get sth done, Make/Let/Have sb do)
- [ ] 🔴 🟡 🟢 25. Inversion (Negative adverbials: Never, Seldom, Not only, Rarely...)
- [ ] 🔴 🟡 🟢 26. Cleft Sentences (It is... that, What... is...)
- [ ] 🔴 🟡 🟢 27. Linking Words for Academic Cohesion & Coherence
- [ ] 🔴 🟡 🟢 28. Complex Sentences (Đa mệnh đề không bị ngắt ngọn hoặc thừa từ)
- [ ] 🔴 🟡 🟢 29. Sentence Transformation (Biến đổi câu tương đương B1 ➔ B2)
- [ ] 🔴 🟡 🟢 30. B2 Specific Structures (Subjunctive mood, Would rather, It is high time)

---

## 2. Vocabulary Master Checklist (30 Chủ đề)
- [ ] 🔴 🟡 🟢 01. Education & Academic Development
- [ ] 🔴 🟡 🟢 02. Work, Employment & Career Prospects
- [ ] 🔴 🟡 🟢 03. Technology, Innovation & Gadgets
- [ ] 🔴 🟡 🟢 04. Artificial Intelligence & Automation
- [ ] 🔴 🟡 🟢 05. Environment, Conservation & Biodiversity
- [ ] 🔴 🟡 🟢 06. Climate Change, Global Warming & Natural Disasters
- [ ] 🔴 🟡 🟢 07. Health, Healthcare System & Mental Well-being
- [ ] 🔴 🟡 🟢 08. Society, Demographics & Social Inequalities
- [ ] 🔴 🟡 🟢 09. Family Structures & Parenting Styles
- [ ] 🔴 🟡 🟢 10. Personal & Professional Relationships
- [ ] 🔴 🟡 🟢 11. Communication & Language Acquisition
- [ ] 🔴 🟡 🟢 12. Mass Media, Journalism & Advertising
- [ ] 🔴 🟡 🟢 13. Internet, Cyberspace & Digital Privacy
- [ ] 🔴 🟡 🟢 14. Science, Scientific Research & Space Exploration
- [ ] 🔴 🟡 🟢 15. Economy, Inflation & Personal Finance
- [ ] 🔴 🟡 🟢 16. Business, Entrepreneurship & Marketing
- [ ] 🔴 🟡 🟢 17. Transportation & Traffic Congestion
- [ ] 🔴 🟡 🟢 18. Travel, Cultural Exploration & Heritage
- [ ] 🔴 🟡 🟢 19. Tourism, Mass Tourism & Ecotourism
- [ ] 🔴 🟡 🟢 20. Culture, Traditions & Preservation
- [ ] 🔴 🟡 🟢 21. Entertainment, Arts & Cinema
- [ ] 🔴 🟡 🟢 22. Government, Public Policy & Civic Duties
- [ ] 🔴 🟡 🟢 23. Law, Regulations & Justice System
- [ ] 🔴 🟡 🟢 24. Crime, Cybercrime & Rehabilitation
- [ ] 🔴 🟡 🟢 25. Globalization & International Integration
- [ ] 🔴 🟡 🟢 26. Urbanization, Smart Cities & Rural-Urban Migration
- [ ] 🔴 🟡 🟢 27. Food Security, Agriculture & Diet
- [ ] 🔴 🟡 🟢 28. Lifestyle, Minimalism & Work-Life Balance
- [ ] 🔴 🟡 🟢 29. Sports, Physical Fitness & Commercialization
- [ ] 🔴 🟡 🟢 30. Renewable Energy & Fossil Fuels

---

## 3. Four Skills & Test Readiness Checklist
### Listening
- [ ] 🔴 🟡 🟢 Xử lý hội thoại tốc độ chuẩn không bị trôi tai
- [ ] 🔴 🟡 🟢 Nhận diện bẫy Distractors (phủ định ngầm, sửa lời, chuyển ý)
- [ ] 🔴 🟡 🟢 Bắt trọn Keywords và Paraphrasing giữa audio và đáp án
- [ ] 🔴 🟡 🟢 Nghe hiểu bài giảng học thuật (Part 3) và ghi chú nhanh (Note-taking)

### Reading
- [ ] 🔴 🟡 🟢 Skimming nắm ý chính bài đọc 500 từ trong 60 giây
- [ ] 🔴 🟡 🟢 Scanning tìm chính xác số liệu, tên riêng, thuật ngữ trong 30 giây
- [ ] 🔴 🟡 🟢 Đoán nghĩa từ vựng mới qua ngữ cảnh mà không cần từ điển
- [ ] 🔴 🟡 🟢 Phân tích câu hỏi suy luận (Inference) và mục đích tác giả (Author's purpose)

### Speaking
- [ ] 🔴 🟡 🟢 Trả lời Part 1 tự nhiên, mở rộng 3-4 câu với liên từ
- [ ] 🔴 🟡 🟢 Trả lời Part 2 mạch lạc: chọn 1 giải pháp, đưa ra 2 lý do, phản biện 2 giải pháp còn lại
- [ ] 🔴 🟡 🟢 Trả lời Part 3 tự tin: phát triển ý theo sơ đồ tư duy, bổ sung ý riêng, trả lời câu hỏi mở rộng
- [ ] 🔴 🟡 🟢 Phát âm chuẩn âm đuôi (/s/, /z/, /t/, /d/, /ed/), có trọng âm từ và ngữ điệu tự nhiên

### Writing
- [ ] 🔴 🟡 🟢 Task 1: Viết đúng bố cục thư/email chuẩn (120-150 từ trong 20 phút)
- [ ] 🔴 🟡 🟢 Task 2: Viết bài luận học thuật 4 đoạn chuẩn (250-300 từ trong 40 phút)
- [ ] 🔴 🟡 🟢 Kiểm soát ngữ pháp và liên kết câu (không mắc lỗi run-on hoặc fragment)
- [ ] 🔴 🟡 🟢 Vận dụng ít nhất 3-5 cấu trúc câu phức/đặc biệt và từ vựng học thuật B2
"""

with open(r"00_master_maps\04_skills_map.md", "w", encoding="utf-8") as f:
    f.write(skills_map)

with open(r"00_master_maps\05_master_checklist.md", "w", encoding="utf-8") as f:
    f.write(checklist)

print("04_skills_map.md and 05_master_checklist.md written.")
