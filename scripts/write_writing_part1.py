# -*- coding: utf-8 -*-
"""
Script to create Part 1 of master_writing_b2.md:
- Section 1: Overview & Rubrics of VSTEP Writing (Task 1 & Task 2)
- Section 2: Task 1 Mastery - Letter / Email Writing (120+ words, 20 mins)
  - Formal vs. Informal Register Matrix
  - 5 Core Letter Types (Complaint, Inquiry, Request, Advice, Apology)
  - Full Templates & 2 Complete B2 Model Letters with Examiner Commentary
"""
import os

target_path = os.path.join(r"d:\projectbuild\hoctienganh", "08_writing", "master_writing_b2.md")

content = r"""# PHẦN 8: KỸ NĂNG VIẾT HỌC THUẬT B2 (B2 WRITING MASTERY)
## CHIẾN LƯỢC TOÀN DIỆN CHINH PHỤC VSTEP WRITING (TARGET 6.5 - 8.5)

---

## MỤC LỤC CHI TIẾT
1. [TỔNG QUAN ĐỊNH DẠNG & MA TRẬN ĐỀ THI VSTEP WRITING](#1-tổng-quan-định-dạng--ma-trận-đề-thi-vstep-writing)
   - 1.1. Cấu trúc 2 phần thi và tỷ trọng điểm số (Task 1 vs. Task 2)
   - 1.2. Bốn tiêu chí chấm điểm chính thức (Task Fulfillment, Coherence, Lexical Resource, Grammar)
   - 1.3. Chiến lược phân bổ 60 phút vàng (Quy tắc 20 - 40)
2. [TASK 1: BẬC THẦY VIẾT THƯ & EMAIL (LETTER / EMAIL MASTERY - 120+ TỪ)](#2-task-1-bậc-thầy-viết-thư--email-letter--email-mastery---120-từ)
   - 2.1. Ma trận phân biệt văn phong Trang trọng (Formal) vs. Thân mật (Informal)
   - 2.2. Khung xương cấu trúc 4 phần chuẩn mực của một lá thư B2
   - 2.3. Cẩm nang từ vựng & cấu trúc theo 5 dạng thư VSTEP kinh điển
   - 2.4. Bài mẫu 1: Thư khiếu nại dịch vụ (Formal Complaint Letter) - Band 8.0
   - 2.5. Bài mẫu 2: Thư tư vấn bạn bè (Informal Advice Letter) - Band 8.0
3. [TASK 2: BẬC THẦY BÀI LUẬN HỌC THUẬT (ACADEMIC ESSAY - 250+ TỪ)](#3-task-2-bậc-thầy-bài-luận-học-thuật-academic-essay---250-từ)
   - 3.1. Phân loại 4 dạng đề luận VSTEP trọng điểm
   - 3.2. Cấu trúc 4 đoạn chuẩn học thuật (The 4-Paragraph Academic Essay Blueprint)
   - 3.3. Phương pháp P-E-E-L bẻ khóa đoạn thân bài thuyết phục
   - 3.4. Hệ thống liên từ & thiết bị liên kết học thuật (Cohesive Devices Matrix)
   - 3.5. Bài mẫu 1: Dạng Opinion / Agree or Disagree (Trí tuệ nhân tạo & Lao động) - Band 8.0
   - 3.6. Bài mẫu 2: Dạng Discussion / Both Views (Học trực tuyến vs. Truyền thống) - Band 8.0
4. [KHO MẪU CÂU B2 ĐỘT PHÁ CHO BÀI LUẬN VSTEP](#4-kho-mẫu-câu-b2-đột-phá-cho-bài-luận-vstep)
   - 4.1. Mẫu câu viết Thesis Statement sắc bén
   - 4.2. Mẫu câu viết Topic Sentence dẫn dắt đoạn
   - 4.3. Mẫu câu đưa dẫn chứng thực nghiệm & số liệu nghiên cứu
   - 4.4. Mẫu câu Nhượng bộ - Phản biện (Counter-argument & Rebuttal)
5. [QUY TRÌNH TỰ KIỂM LỖI & CHECKLIST NỘP BÀI (SELF-EDITING CHECKLIST)](#5-quy-trình-tự-kiểm-lỗi--checklist-nộp-bài-self-editing-checklist)
   - 5.1. 5 Lỗi ngữ pháp chí mạng làm rớt band B2
   - 5.2. Biểu mẫu tự soát lỗi 5 phút cuối giờ

---

## 1. TỔNG QUAN ĐỊNH DẠNG & MA TRẬN ĐỀ THI VSTEP WRITING

Bài thi Viết VSTEP được đánh giá là một trong những phần thi có khả năng kiểm soát điểm số tốt nhất nếu người học nắm vững cấu trúc khung bài (templates) và phương pháp phát triển luận điểm logic.

### 1.1. Cấu trúc 2 phần thi và tỷ trọng điểm số
- **Tổng thời gian thi:** 60 phút (làm trực tiếp trên bàn phím máy tính).
- **Tổng số nhiệm vụ:** 2 Tasks.

```
+--------+--------------------------+--------------------+----------------+--------------------+
| Task   | Thể loại văn bản         | Độ dài tối thiểu   | Tỷ trọng điểm  | Thời gian khuyến nghị|
+--------+--------------------------+--------------------+----------------+--------------------+
| Task 1 | Letter / Email           | 120 từ             | 1/3 (33.3%)    | 20 phút            |
|        | (Thân mật hoặc Trang trọng)|                  |                |                    |
+--------+--------------------------+--------------------+----------------+--------------------+
| Task 2 | Academic Essay           | 250 từ             | 2/3 (66.7%)    | 40 phút            |
|        | (Bài luận học thuật)     |                    |                |                    |
+--------+--------------------------+--------------------+----------------+--------------------+
```

> **Lưu ý số lượng từ:**
> - Viết dưới 120 từ ở Task 1 hoặc dưới 250 từ ở Task 2 sẽ bị **trừ điểm nặng ở tiêu chí Task Fulfillment**.
> - **Độ dài lý tưởng để đạt điểm cao:**
>   - Task 1: **140 – 160 từ**.
>   - Task 2: **270 – 320 từ**.

### 1.2. Bốn tiêu chí chấm điểm chính thức (Rubrics B2 - Bậc 4)
Bài thi Viết được chấm dựa trên 4 tiêu chí đồng đều (mỗi tiêu chí chiếm 25% tổng điểm):

1. **Task Fulfillment / Response (Hoàn thành nhiệm vụ):**
   - Trả lời đầy đủ, chi tiết tất cả các yêu cầu/gợi ý trong đề bài.
   - Thể hiện rõ quan điểm lập trường xuyên suốt toàn bộ bài viết.
   - Luận điểm được khai triển sâu, có ví dụ minh họa và giải thích thuyết phục.
2. **Coherence & Cohesion (Độ mạch lạc và liên kết):**
   - Bố cục đoạn văn rõ ràng: Mở bài, các đoạn Thân bài, Kết luận.
   - Mỗi đoạn thân bài chỉ tập trung vào một ý chính rõ ràng (*Central topic*).
   - Sử dụng đa dạng các phương tiện liên kết (*Cohesive devices*), tránh lặp từ nối và tránh lạm dụng cơ học các từ nối đơn điệu (*Firstly, Secondly, Furthermore*).
3. **Lexical Resource (Vốn từ vựng):**
   - Sử dụng từ vựng học thuật B2 chính xác, tự nhiên theo ngữ cảnh.
   - Sử dụng thành thạo các cụm từ kết hợp cố định (*Collocations*) và cấu trúc diễn đạt thành ngữ phù hợp.
   - Không mắc lỗi chính tả lặp lại; tránh dùng từ ngữ khẩu ngữ hoặc tiếng lóng trong văn bản trang trọng.
4. **Grammatical Range & Accuracy (Độ đa dạng và chính xác ngữ pháp):**
   - Sử dụng linh hoạt nhiều kiểu câu: Câu đơn, câu ghép, câu phức nhiều tầng (*Complex sentences*).
   - Áp dụng các cấu trúc B2 nâng cao: Câu điều kiện, câu bị động khách quan (*It is argued that...*), mệnh đề quan hệ rút gọn, cấu trúc đảo ngữ (*Inversion*).
   - Dấu câu chuẩn xác (dấu phẩy, dấu chấm phẩy, dấu hai chấm); không mắc lỗi câu què (*sentence fragment*) hay câu chạy dài không ngắt nghỉ (*run-on sentence*).

### 1.3. Chiến lược phân bổ 60 phút vàng (Quy tắc 20 - 40)
```
   [00:00 - 03:00] : TASK 1 - Đọc đề, phân tích văn phong (Formal/Informal), vạch 3 ý chính ra nháp
   [03:00 - 18:00] : TASK 1 - Gõ bài trên máy tính (Mục tiêu: 140 - 160 từ)
   [18:00 - 20:00] : TASK 1 - Soát lỗi chính tả, chia động từ, mạo từ
   -----------------------------------------------------------------------------------------
   [20:00 - 25:00] : TASK 2 - Đọc kỹ đề luận, xác định lập trường, lập dàn ý P-E-E-L ra nháp
   [25:00 - 55:00] : TASK 2 - Gõ bài luận 4 đoạn hoàn chỉnh (Mục tiêu: 280 - 310 từ)
   [55:00 - 60:00] : TASK 2 - 5 phút vàng soát lỗi ngữ pháp, liên từ, câu phức và dấu câu!
```

---

## 2. TASK 1: BẬC THẦY VIẾT THƯ & EMAIL (LETTER / EMAIL MASTERY - 120+ TỪ)

### 2.1. Ma trận phân biệt văn phong Trang trọng (Formal) vs. Thân mật (Informal)
Sai lầm chí mạng của nhiều thí sinh là lẫn lộn giữa hai văn phong, ví dụ viết thư khiếu nại cho hiệu trưởng hay quản lý khách sạn mà lại dùng *"Hi John"*, *"gonna/wanna"* hoặc viết tắt *"don't/can't"*.

| Yếu tố văn bản | Thư Trang trọng (Formal / Semi-formal) | Thư Thân mật (Informal) |
| :--- | :--- | :--- |
| **Đối tượng nhận** | Quản lý, nhà tuyển dụng, ban giám hiệu, đối tác kinh doanh, người lạ | Bạn thân, thành viên gia đình, bạn cùng lớp |
| **Lời chào đầu** | *Dear Mr. Smith, / Dear Sir or Madam,* | *Dear Alex, / Hi Sarah,* |
| **Mở đầu thư** | Nêu ngay lý do viết thư một cách lịch sự, trang nhã | Hỏi thăm sức khỏe, cảm xúc, nhắc kỷ niệm gần nhất |
| **Viết tắt (Contractions)** | **TUYỆT ĐỐI KHÔNG** (*do not, cannot, would like*) | **ĐƯỢC PHÉP** (*don't, can't, I'd like*) |
| **Tiếng lóng & Khẩu ngữ** | **CẤM** (*utilize, apologize, comprehensive*) | **ĐƯỢC DÙNG** (*awesome, pretty good, chill out*) |
| **Cấu trúc câu** | Câu phức, câu bị động, câu gián tiếp lịch sự | Câu đơn, câu ghép, câu cảm thán, câu hỏi thăm ngắn |
| **Lời kết thúc thư** | *Yours faithfully,* (khi chào Dear Sir/Madam) <br> *Yours sincerely,* (khi biết tên người nhận) | *Best wishes, / Warm regards, / All the best,* |

### 2.2. Khung xương cấu trúc 4 phần chuẩn mực của một lá thư B2

```
+----------------------------------------------------------------------------------------------------+
| 1. SALUTATION (LỜI CHÀO):                                                                          |
|    - Formal: Dear Sir or Madam, / Dear Mr. Davis,                                                  |
|    - Informal: Dear Michael,                                                                       |
+----------------------------------------------------------------------------------------------------+
| 2. OPENING PARAGRAPH (ĐOẠN MỞ ĐẦU - ~25-30 từ):                                                    |
|    - Formal: Nêu trực tiếp mục đích viết thư (I am writing to express my dissatisfaction with...).  |
|    - Informal: Lời hỏi thăm thân thiện + Lý do viết thư (I hope you are doing well. I'm writing...).|
+----------------------------------------------------------------------------------------------------+
| 3. BODY PARAGRAPHS (CÁC ĐOẠN THÂN BÀI - ~80-100 từ):                                              |
|    - Thường chia thành 2 đoạn nhỏ (Body 1 & Body 2).                                               |
|    - Phải giải quyết triệt để TẤT CẢ các gợi ý (bullet points) mà đề bài yêu cầu.                 |
|    - Sử dụng liên từ để kết nối các chi tiết mạch lạc.                                             |
+----------------------------------------------------------------------------------------------------+
| 4. CLOSING & SIGN-OFF (ĐOẠN KẾT & KÝ TÊN - ~20-25 từ):                                             |
|    - Nêu kỳ vọng hành động tiếp theo (I look forward to hearing from you at your earliest...).     |
|    - Ký tên đầy đủ (Formal) hoặc tên gọi thân mật (Informal).                                      |
+----------------------------------------------------------------------------------------------------+
```

### 2.3. Cẩm nang từ vựng & cấu trúc theo 5 dạng thư VSTEP kinh điển

#### 1. Thư Khiếu nại (Letter of Complaint - Formal):
- *I am writing to express my profound dissatisfaction with the substandard service I received at...*
- *To my utter dismay, the product failed to operate in accordance with the advertised specifications.*
- *Under these circumstances, I believe it is entirely reasonable to request a full refund or an immediate replacement.*
- *I trust that this grievance will be addressed with the urgency it warrants.*

#### 2. Thư Hỏi thông tin (Letter of Inquiry - Formal):
- *I am writing to formally inquire about the admission prerequisites for the postgraduate program in...*
- *I would be exceptionally grateful if you could furnish me with comprehensive details regarding...*
- *Could you please clarify whether tuition fees encompass instructional materials and laboratory access?*
- *Thank you in advance for your kind assistance and prompt response.*

#### 3. Thư Xin việc / Ứng tuyển (Letter of Application - Formal):
- *I am writing to submit my application for the position of Marketing Executive, as advertised on...*
- *As indicated in my enclosed curriculum vitae, I possess over three years of professional experience in...*
- *I am confident that my analytical acumen and cross-cultural adaptability make me an ideal candidate.*
- *I would welcome the opportunity to discuss my qualifications further in a personal interview.*

#### 4. Thư Xin lỗi (Letter of Apology - Formal / Semi-formal):
- *Please accept my sincere apologies for my unforeseen absence from yesterday's scheduled seminar.*
- *Due to an unexpected medical emergency, I was completely incapacitated and unable to notify you in advance.*
- *I assure you that every necessary measure has been taken to prevent any recurrence of this oversight.*
- *I deeply regret any operational inconvenience this matter may have caused.*

#### 5. Thư Tư vấn / Khuyên bảo (Letter of Advice - Informal):
- *I was thrilled to receive your letter, and I completely understand the dilemma you are currently grappling with.*
- *If I were in your shoes, the very first thing I would do is weigh the pros and cons carefully.*
- *Have you ever contemplated the possibility of taking a gap year to gain practical workplace exposure?*
- *Whatever you ultimately decide, remember that I am always here to support you through thick and thin.*

---

### 2.4. Bài mẫu 1: Thư khiếu nại dịch vụ (Formal Complaint Letter) - Band 8.0

> **Đề bài:** *You recently stayed at a hotel during a business conference, but you experienced several serious problems with your room and the customer service. Write a formal letter of complaint (at least 120 words) to the hotel general manager. In your letter:*
> - *Explain the details of your stay (dates, room number).*
> - *Describe the specific problems you encountered.*
> - *State clearly what action you expect the hotel to take.*

**Model Letter (158 words - Band 8.0):**

> Dear Sir or Madam,
> 
> I am writing to express my profound dissatisfaction with the substandard quality of accommodation and customer service I experienced during my recent stay at your establishment. I occupied Room 408 from October 12th to 14th while attending the International Trade Symposium.
> 
> Regrettably, my stay was severely disrupted by multiple operational deficiencies. Firstly, despite my prior request for a quiet business suite, the air conditioning unit malfunctioned continuously, emitting an intolerable mechanical noise that made restorative sleep impossible. Furthermore, upon raising this issue with the front-desk personnel, I was met with complete indifference; the receptionist merely dismissed my grievance without offering either a technician or an alternative room. 
> 
> Given the exorbitant room rates charged and the disruption to my professional commitments, I believe it is entirely reasonable to request a 50% refund of my total accommodation expenses. I trust this matter will receive your immediate attention, and I await your prompt response.
> 
> Yours faithfully,  
> Nguyen Van Anh

**Phân tích Điểm sáng Ngữ pháp & Từ vựng B2:**
- *profound dissatisfaction with the substandard quality:* sự bất mãn sâu sắc với chất lượng dưới chuẩn
- *operational deficiencies:* những khiếm khuyết trong vận hành
- *intolerable mechanical noise:* tiếng ồn cơ khí không thể chịu đựng nổi
- *restorative sleep:* giấc ngủ phục hồi thể lực
- *met with complete indifference:* bị đối xử bằng thái độ hoàn toàn thờ ơ, lạnh nhạt
- *exorbitant room rates:* giá phòng đắt đỏ cắt cổ
- Cấu trúc rút gọn phân từ: *"Given the exorbitant room rates charged..."*

---

### 2.5. Bài mẫu 2: Thư tư vấn bạn bè (Informal Advice Letter) - Band 8.0

> **Đề bài:** *Your English-speaking friend, David, is planning to visit Vietnam for two weeks this winter. He wrote to ask for your advice on which places to visit and what cultural etiquette he should keep in mind. Write an informal email (at least 120 words) to David.*

**Model Email (154 words - Band 8.0):**

> Dear David,
> 
> It was wonderful to hear from you! I'm absolutely thrilled that you're finally visiting Vietnam this winter—you are going to have an unforgettable trip.
> 
> Since you have a two-week itinerary, I would strongly recommend spending your first week exploring the northern region. You definitely shouldn't miss Hanoi's historic Old Quarter for its incredible street food, followed by a two-day cruise across Ha Long Bay, where the limestone karsts are truly breathtaking. Afterwards, catch a domestic flight down to Da Nang and Hoi An; the ancient lanterns and tranquil coastal vibe there are magical.
> 
> As for cultural etiquette, Vietnamese people are exceptionally welcoming, but there are a few customs worth noting. When visiting Buddhist pagodas or historical temples, make sure to dress modestly by covering your shoulders and knees. Also, removing your shoes before entering someone's home is a customary sign of respect.
> 
> Let me know your flight details soon so we can catch up in person!
> 
> Best wishes,  
> Minh
"""

with open(target_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Part 1 of Writing Master written successfully. Bytes:", len(content))
