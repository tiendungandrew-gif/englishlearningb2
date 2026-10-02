# -*- coding: utf-8 -*-
"""
Script to append Part 2 to master_reading_b2.md:
- Question Types 6 to 10 with B2 academic passages & explanations
- Section 4: The 5 Classic Traps & POE (Process of Elimination) Heuristics
"""
import os

target_path = os.path.join(r"d:\projectbuild\hoctienganh", "06_reading", "master_reading_b2.md")

content = r"""
### DẠNG 6: INFERENCE QUESTIONS (CÂU HỎI SUY LUẬN NGẦM)

#### 1. Dấu hiệu nhận biết
- *It can be inferred from paragraph X that...*
- *The author implies that...*
- *Which of the following is most likely true regarding...?*
- *What does the passage suggest about...?*

#### 2. Quy trình 4 bước xử lý chuẩn
- **Bước 1: Hiểu bản chất câu suy luận:** Đáp án đúng **KHÔNG ĐƯỢC NÊU TRỰC TIẾP** trong bài nhưng là **KẾT LUẬN LOGIC TẤT YẾU** rút ra từ dữ liệu của bài. Nếu bài nói "A lớn hơn B" thì suy luận được "B nhỏ hơn A".
- **Bước 2:** Scan vị trí thông tin liên quan đến đối tượng được hỏi trong đoạn văn.
- **Bước 3: Nguyên tắc Bước nhảy Logic 1 Nhịp (One-Step Logical Leap):**
  - Chỉ suy luận đúng 1 nhịp từ bằng chứng hiển ngôn của văn bản ($A \rightarrow B$).
  - **LOẠI BỎ NGAY** các phương án suy diễn quá xa, suy diễn chủ quan hoặc dựa vào định kiến xã hội bên ngoài ($A \rightarrow B \rightarrow C \rightarrow D$).
- **Bước 4: Đối chiếu phương án:** Đáp án đúng thường dùng các từ ngữ cẩn trọng (hedging language): *may, might, could, tend to, suggest, indicate, likely*.

#### 3. Bẫy kinh điển
- **Bẫy Suy diễn quá đà (Wild Speculation):** Một phương án nghe rất hợp lý và sâu sắc trong triết học hoặc thực tế xã hội, nhưng văn bản hoàn toàn không cung cấp dữ liệu chứng minh.

#### 4. Ví dụ học thuật B2 & Phân tích chuyên sâu
> **Text Snippet:**
> "Prior to the late 19th century, nocturnal urban illumination depended almost exclusively on whale-oil lamps and early gas fixtures, both of which produced a faint, flickering amber glow that scarcely penetrated thick fog or darkened alleys. The commercial introduction of the incandescent tungsten filament bulb abruptly transformed urban life. For the first time in history, manufacturing factories could operate around the clock with standard shifts, municipal crime rates in brightly lit districts declined dramatically, and commercial retail hours extended well past dusk."
>
> **Question:** *What can be inferred from the passage about urban life before the late 19th century?*
> A. Factories rarely organized nocturnal manufacturing shifts due to inadequate illumination.
> B. Criminal activities were completely eradicated once gas fixtures were introduced.
> C. Whale oil was so expensive that ordinary citizens could not afford domestic heating.
> D. Incandescent light bulbs had already been invented but were banned by municipalities.
>
> **Phân tích:**
> - Bài viết nói: Trước cuối thế kỷ 19, ánh sáng đô thị yếu ớt... Sau khi bóng đèn vonfram xuất hiện, **lần đầu tiên trong lịch sử (for the first time in history)** các nhà máy sản xuất có thể vận hành suốt ngày đêm theo ca làm việc tiêu chuẩn.
> - **Suy luận logic 1 nhịp:** Nếu sau khi có bóng đèn vonfram, lần đầu tiên nhà máy mới vận hành ca đêm liên tục được, thì TRƯỚC ĐÓ, do ánh sáng không đủ nên các nhà máy hiếm khi/không thể tổ chức sản xuất ca đêm!
> - Đối chiếu:
>   - B sai: Bài không nói tội phạm bị diệt trừ hoàn toàn (*completely eradicated* - từ bẫy cực đoan).
>   - C sai: Bài không đề cập gì đến việc sưởi ấm gia đình (*domestic heating*).
>   - D sai: Bóp méo thông tin lịch sử.
>   - **A đúng: Suy luận chính xác 1 nhịp từ cụm "for the first time in history, factories could operate around the clock".**

---

### DẠNG 7: SENTENCE SIMPLIFICATION / PARAPHRASING (CÂU TƯƠNG ĐƯƠNG Ý NGHĨA)

#### 1. Dấu hiệu nhận biết
- *Which of the following best expresses the essential information in the highlighted sentence?*
- *(Incorrect options leave out essential information or change the meaning in important ways.)*

#### 2. Quy trình 4 bước xử lý chuẩn
- **Bước 1: Bóc tách câu gốc thành 2-3 Mảnh ghép Ý nghĩa cốt lõi (Core Meaning Chunks):**
  - Mảnh 1: Quan hệ logic (Nguyên nhân - Kết quả, Nhượng bộ, Tương phản, hay Điều kiện).
  - Mảnh 2: Chủ ngữ + Hành động chính.
  - Mảnh 3: Kết quả hoặc điều kiện ràng buộc đi kèm.
- **Bước 2: Tìm Mối quan hệ logic then chốt (Key Logical Connector):**
  - *Although / Despite* $\rightarrow$ Đối lập, nhượng bộ.
  - *Because / Owing to / Consequently* $\rightarrow$ Quan hệ nhân quả.
  - *Provided that / Unless* $\rightarrow$ Điều kiện.
- **Bước 3: Loại trừ nhanh các phương án:**
  - Sai mối quan hệ logic (Ví dụ: câu gốc là Nhượng bộ nhưng đáp án biến thành Nhân quả).
  - Bỏ sót thông tin cốt lõi (Omission of essential facts).
  - Thêm thông tin không có trong câu gốc (Extraneous information).
  - Đảo ngược chiều tác động (Reversed agent and patient).
- **Bước 4: Chọn câu diễn đạt ngắn gọn nhưng giữ trọn vẹn thông điệp.**

#### 3. Bẫy kinh điển
- Thí sinh bị hoa mắt bởi từ vựng đồng nghĩa, không chú ý rằng liên từ logic đã bị tráo từ "mặc dù" sang "bởi vì".

#### 4. Ví dụ học thuật B2 & Phân tích chuyên sâu
> **Highlighted Sentence:**
> *"Although proponents of renewable microgrids emphasize their remarkable resilience during catastrophic weather events, the substantial upfront capital expenditure and regulatory inertia continue to hinder their widespread municipal deployment."*
>
> **Question:** *Which of the following best expresses the essential information in the highlighted sentence?*
> A. Renewable microgrids are rarely used during severe storms because of their fragile technical design.
> B. Despite their proven durability in extreme weather, high initial costs and slow regulation impede the widespread use of renewable microgrids.
> C. Municipal governments are eager to invest large capital into microgrids once regulatory policies are relaxed.
> D. Because extreme weather damages electrical infrastructure, microgrids have become obligatory for all cities.
>
> **Phân tích:**
> - Bóc tách câu gốc:
>   - Vế 1 (Nhượng bộ): Mặc dù những người ủng hộ nhấn mạnh khả năng chống chịu bão đáng nể của lưới điện vi mô (*resilience during catastrophic weather*).
>   - Vế 2 (Rào cản): Chi phí đầu tư ban đầu quá lớn (*upfront capital expenditure*) và sự trì trệ cơ chế (*regulatory inertia*).
>   - Vế 3 (Hậu quả): Tiếp tục cản trở việc triển khai rộng rãi ở cấp đô thị (*hinder widespread deployment*).
> - Đối chiếu:
>   - A sai: Ngược thông tin (bảo thiết kế mong manh, trong khi câu gốc khen có tính chống chịu cao).
>   - C sai: Thêu dệt thông tin (chính quyền thành phố hào hứng đầu tư).
>   - D sai: Biến đổi thành quan hệ nhân quả và từ cực đoan "obligatory" (bắt buộc).
>   - **B đúng: Tóm gọn hoàn hảo vế nhượng bộ (durability in extreme weather) và hai rào cản cốt lõi (high initial costs and slow regulation) cản trở việc triển khai.**

---

### DẠNG 8: AUTHOR'S PURPOSE / TONE / ATTITUDE (MỤC ĐÍCH, GIỌNG ĐIỆU, THÁI ĐỘ TÁC GIẢ)

#### 1. Dấu hiệu nhận biết
- *Why does the author mention X in paragraph Y?*
- *The author discusses [example] in order to...*
- *What is the author's tone / attitude toward the proposed theory?*

#### 2. Quy trình 4 bước xử lý chuẩn
- **Bước 1: Phân biệt Câu hỏi Mục đích (Purpose) và Câu hỏi Chi tiết (Detail):**
  - Câu hỏi *Why does the author mention X?* **KHÔNG HỎI X LÀ GÌ**, mà hỏi **TẠI SAO TÁC GIẢ LẠI DÙNG X (Chức năng lập luận của X)**.
- **Bước 2: Tìm luận điểm mà X làm dẫn chứng:**
  - Nhìn lên **1-2 câu ngay trước X**. Thông thường tác giả đưa ra một luận điểm khái quát, sau đó dẫn chứng X bằng các từ nối: *for example, for instance, such as, as demonstrated by, to illustrate*.
  - $\rightarrow$ Mục đích của X là để minh họa/chứng minh cho luận điểm đứng ngay trước nó!
- **Bước 3: Nhận diện Từ chỉ Thái độ & Giọng điệu (Tone Vocabulary):**

| Giọng điệu / Thái độ | Thuật ngữ tiếng Anh | Dấu hiệu văn bản |
| :--- | :--- | :--- |
| **Khách quan / Khoa học** | *Objective, neutral, impartial, analytical* | Dùng nhiều số liệu, dữ kiện, tránh dùng từ ngữ cảm xúc, cân bằng cả 2 luồng quan điểm |
| **Phê phán / Nghi ngờ** | *Critical, skeptical, dubious, disapproving* | Dùng từ chỉ khiếm khuyết: *flawed, questionable, dubious, lack of empirical rigour* |
| **Ủng hộ / Ca ngợi** | *Advocative, approving, optimistic, commendatory* | Dùng từ tích cực: *groundbreaking, commendable, vital, invaluable* |
| **Thận trọng / Cảnh giác** | *Cautious, guarded, reserved, provisional* | Dùng từ hạn định: *preliminary, further research required, potential limitations* |

- **Bước 4: Loại trừ các thái độ cực đoan:** Các bài đọc học thuật B2-C1 hầu như **KHÔNG BAO GIỜ** có thái độ thù địch gay gắt (*hostile, cynical, sarcastic, contemptuous*) hoặc ca ngợi mù quáng (*unconditional worship*).

#### 3. Ví dụ học thuật B2 & Phân tích chuyên sâu
> **Text Snippet:**
> "Traditional economic models frequently presume that human agents operate with absolute rationality, systematically evaluating probabilities to maximize individual utility. However, real-world fiscal behaviors routinely defy these mathematical postulates. To illustrate this fundamental divergence, behavioral economists point to the 'sunk cost fallacy'—the universal tendency for individuals to persist with an unproductive endeavor merely because they have already invested non-recoverable time or monetary resources into it."
>
> **Question:** *Why does the author mention the 'sunk cost fallacy' in the passage?*
> A. To prove that economic agents always maximize their individual financial utility.
> B. To provide concrete evidence that human decisions frequently deviate from pure rationality.
> C. To criticize behavioral economists for relying on outdated mathematical formulas.
> D. To encourage consumers to invest more time in non-recoverable financial assets.
>
> **Phân tích:**
> - Luận điểm đứng ngay trước: *"real-world fiscal behaviors routinely defy these mathematical postulates"* (hành vi tài chính thực tế thường xuyên đi ngược lại các giả định toán học thuần lý trí).
> - Sau đó xuất hiện liên từ: *"To illustrate this fundamental divergence, economists point to the sunk cost fallacy..."*.
> - Vậy mục đích đưa ra hiện tượng "sunk cost fallacy" là để làm ví dụ minh họa cụ thể cho việc con người hành động không thuần túy lý trí.
> - **B đúng: To provide concrete evidence that human decisions frequently deviate from pure rationality.**

---

### DẠNG 9: SENTENCE INSERTION (CHÈN CÂU VÀO MẠCH VĂN BẢN)

#### 1. Dấu hiệu nhận biết
- *Look at the four squares [A], [B], [C], and [D] that indicate where the following sentence could be added to the passage.*
- *Where would the sentence best fit?*

#### 2. Quy trình 4 bước xử lý chuẩn
- **Bước 1: Phân tích Kỹ càng Câu Cần Chèn (Target Sentence) để tìm "Mấu nối" (Hooks):**
  - **Mấu nối Đại từ / Chỉ định từ:** *This, that, these, those, such, they, it*. Nếu câu có *"These discrepancies..."*, thì câu đứng ngay trước vị trí chèn BẮT BUỘC phải nói về các sự sai lệch (*discrepancies*).
  - **Mấu nối Liên từ chuyển tiếp (Transition words):**
    - Tương phản: *However, nevertheless, in contrast, on the other hand*.
    - Bổ sung: *Furthermore, in addition, moreover*.
    - Nhân quả: *Therefore, consequently, as a result*.
  - **Mấu nối Mạo từ:** *A / an* (nhắc đến lần đầu) $\rightarrow$ *The* (nhắc lại lần 2).
- **Bước 2: Quét qua 4 vị trí [A], [B], [C], [D] trong bài đọc.**
- **Bước 3: Thử nghiệm lắp ghép:** Đọc câu đứng trước + [Câu chèn] + Câu đứng sau. Kiểm tra xem dòng chảy lập luận (Coherence & Cohesion) có bị gãy đoạn không.
- **Bước 4: Nguyên tắc Không phá vỡ cặp liên kết:** Tuyệt đối không chèn câu vào giữa một đại từ và danh từ quy chiếu của nó, hoặc giữa một câu hỏi và câu trả lời trực tiếp.

#### 3. Ví dụ học thuật B2 & Phân tích chuyên sâu
> **Sentence to be inserted:**
> *"Consequently, marine predators that depend on visual acuity are forced to expend significantly more energy to locate prey."*
>
> **Text with Markers:**
> "Anthropogenic sediment runoff from coastal construction has substantially elevated ocean turbidity in coastal bays. [A] This increased water cloudiness drastically diminishes the depth to which sunlight can penetrate the water column. [B] Photosynthetic benthic algae and seagrasses experience stunted growth rates due to this severe light limitation. [C] Furthermore, elevated suspended particles alter the optical properties of the marine environment, impairing underwater visibility. [D] Over time, these cumulative ecological strains cause a collapse in the local food web."
>
> **Question:** *Where would the sentence best fit?*
> A. [A]
> B. [B]
> C. [C]
> D. [D]
>
> **Phân tích:**
> - Phân tích câu cần chèn: Có liên từ *"Consequently"* (Do đó) + *"marine predators that depend on visual acuity"* (động vật săn mồi phụ thuộc vào thị lực) + *"forced to expend significantly more energy to locate prey"* (buộc phải tiêu tốn nhiều năng lượng hơn để tìm con mồi).
> - Để có kết quả "săn mồi khó khăn do giảm thị lực", câu đứng trước nó phải nói về việc **tầm nhìn dưới nước bị suy giảm (impaired underwater visibility)**.
> - Xét câu trước vị trí [D]: *"Furthermore, elevated suspended particles alter the optical properties of the marine environment, impairing underwater visibility."* (Hạt lơ lửng làm thay đổi đặc tính quang học, làm suy giảm tầm nhìn dưới nước).
> - Kết nối: Tầm nhìn bị suy giảm $\rightarrow$ DO ĐÓ (Consequently), động vật săn mồi bằng mắt gặp khó khăn $\rightarrow$ Vị trí [D] tạo nên mạch nối nhân quả hoàn hảo.
> - **D đúng: Vị trí [D].**

---

### DẠNG 10: STRUCTURAL & RHETORICAL FUNCTION (TỔ CHỨC LẬP LUẬN & TÓM TẮT VĂN BẢN)

#### 1. Dấu hiệu nhận biết
- *How is the information in paragraph 2 related to paragraph 1?*
- *Which of the following best outlines the organization of the passage?*
- *Which sentence best summarizes the final paragraph?*

#### 2. Quy trình 4 bước xử lý chuẩn
- **Bước 1:** Xác định vai trò cấu trúc của từng đoạn văn trong chỉnh thể bài viết:
  - Đoạn 1: Đặt vấn đề / Nêu hiện tượng (Introduce a phenomenon or controversial theory).
  - Đoạn 2: Phân tích nguyên nhân / Cơ chế hoạt động (Explain the underlying mechanism).
  - Đoạn 3: Đưa ra phản biện / Hạn chế / Quan điểm đối lập (Present counterarguments or limitations).
  - Đoạn 4: Đề xuất giải pháp / Xu hướng tương lai (Propose solutions or outline future outlook).
- **Bước 2: Tìm các từ khóa cấu trúc (Rhetorical Signposts):**
  - So sánh: *Similarly, likewise, in parallel*.
  - Đối lập: *On the contrary, whereas, an opposing hypothesis*.
  - Nhân quả: *It follows that, the repercussions are*.
  - Thời gian: *Chronologically, subsequently, historically*.
- **Bước 3:** Đối chiếu với các mô hình cấu trúc kinh điển trong tiếng Anh học thuật:
  - *Problem - Solution* (Vấn đề - Giải pháp).
  - *Cause - Effect* (Nguyên nhân - Hệ quả).
  - *Hypothesis - Evidence - Refutation* (Giả thuyết - Dẫn chứng - Bác bỏ).
  - *Chronological Evolution* (Diễn tiến lịch sử theo thời gian).
- **Bước 4:** Chọn phương án mô tả chính xác mối quan hệ liên kết giữa các đoạn.

#### 3. Ví dụ học thuật B2 & Phân tích chuyên sâu
> **Text Structure Analysis:**
> - Paragraph 1 discusses the discovery of antibiotics and their historical triumph over bacterial infections.
> - Paragraph 2 outlines how the widespread overprescription of these drugs in agriculture and clinical medicine has fostered multidrug-resistant "superbugs".
>
> **Question:** *What is the relationship between paragraph 1 and paragraph 2?*
> A. Paragraph 2 provides additional experimental data to substantiate the hypothesis introduced in paragraph 1.
> B. Paragraph 2 introduces an unintended detrimental consequence of the historical medical breakthrough described in paragraph 1.
> C. Paragraph 2 refutes the scientific validity of the medical discoveries mentioned in paragraph 1.
> D. Paragraph 2 analyzes the biological structure of the diseases listed in paragraph 1.
>
> **Phân tích:**
> - Đoạn 1 nói về bước đột phá lịch sử của kháng sinh (historical medical breakthrough).
> - Đoạn 2 nói về việc lạm dụng kháng sinh tạo ra vi khuẩn kháng thuốc (unintended detrimental consequence - hậu quả tiêu cực ngoài ý muốn).
> - Đáp án B mô tả chuẩn xác 100% mối quan hệ này.
> - **B đúng.**

---

## 4. BỘ 5 BẪY KINH ĐIỂN & CHIẾN THUẬT LOẠI SUY (POE)

Để đạt điểm 8.0+ VSTEP Reading, năng lực **loại trừ các phương án bẫy** quan trọng ngang ngửa năng lực tìm phương án đúng. Các chuyên gia ra đề thi luôn cài cắm 5 loại bẫy tâm lý sau:

### 4.1. Bẫy 1: Verbatim Matching (Bẫy sao chép y hệt từ vựng)
- **Đặc điểm:** Phương án trắc nghiệm copy nguyên văn một cụm từ dài 4-5 từ cực kỳ học thuật và nổi bật từ bài đọc.
- **Tâm lý thí sinh:** Thí sinh lười đọc hoặc vốn từ yếu khi thấy từ trong đáp án giống hệt trên bài đọc sẽ có xu hướng vội vàng chọn ngay vì cảm thấy "thân quen và an toàn".
- **Sự thật:** 85% các câu copy nguyên si từ vựng đều là đáp án SAI! Người ra đề đã tráo đổi vị trí chủ ngữ - tân ngữ, hoặc gắn từ đó vào một bối cảnh hoàn toàn khác. **Đáp án đúng thật sự hầu như luôn được Paraphrase bằng từ đồng nghĩa hoặc cấu trúc khác.**

### 4.2. Bẫy 2: Extreme Modifiers (Bẫy từ ngữ khẳng định tuyệt đối)
- **Đặc điểm:** Các đáp án chứa những trạng từ/tính từ mang tính tuyệt đối hóa 100%:
  - *always, never, all, every, completely, entirely, perfectly, impossible, indisputable, sole, exclusively, eradicated*.
- **Sự thật:** Văn phong học thuật B2-C1 luôn mang tính thận trọng và tương đối (Hedging). Các nhà khoa học hiếm khi khẳng định cái gì là tuyệt đối. Nếu bài đọc dùng *"often, tends to, partially, potentially"*, mà đáp án dùng *"always, completely"* $\rightarrow$ **GẠCH BỎ NGAY LẬP TỨC!**
- **Dấu hiệu đáp án đúng:** Thường chứa các từ mang tính khả dĩ: *may, might, can, likely, often, tend to, suggest, largely*.

### 4.3. Bẫy 3: True in Reality, Not in Text (Đúng với thực tế ngoài đời nhưng bài không nói)
- **Đặc điểm:** Một nhận định nghe hoàn toàn đúng đắn theo tri thức phổ thông hoặc khoa học đời thường (ví dụ: *"Hút thuốc lá gây hại cho phổi"* hoặc *"Tập thể dục giúp giảm căng thẳng"*).
- **Sự thật:** Đề thi VSTEP kiểm tra kỹ năng **Đọc hiểu văn bản (Reading Comprehension)**, KHÔNG kiểm tra kiến thức bách khoa toàn thư của bạn. Nếu thông tin đó không xuất hiện trong bài đọc $\rightarrow$ **KHÔNG ĐƯỢC CHỌN!** Quy tắc vàng: *Nếu bài đọc không nói, coi như thông tin đó không tồn tại.*

### 4.4. Bẫy 4: Reversed Cause-and-Effect (Bẫy đảo lộn quan hệ nhân quả)
- **Đặc điểm:** Đáp án giữ nguyên hai sự vật A và B, nhưng tráo đổi vai trò: Biến Nguyên nhân thành Kết quả và ngược lại.
  - *Bài đọc:* "Severe stress leads to hormonal imbalances." (Stress gây ra mất cân bằng hormone).
  - *Đáp án bẫy:* "Hormonal imbalances are the primary catalyst triggering severe stress." (Mất cân bằng hormone là nguyên nhân chính gây ra stress).
  - $\rightarrow$ Thí sinh đọc lướt thấy đủ từ khóa sẽ mắc bẫy ngay.

### 4.5. Bẫy 5: Half-Right, Half-Wrong (Nửa đầu đúng, nửa đuôi sai thông tin)
- **Đặc điểm:** Nửa đầu của câu đáp án khớp hoàn toàn với bài đọc, khiến thí sinh mừng rỡ và mất cảnh giác. Tuy nhiên, 2-3 từ cuối câu lại bị thay đổi một chi tiết nhỏ (sai mốc thời gian, sai địa điểm, hoặc đổi từ phủ định sang khẳng định).
- **Chiến thuật phòng thủ:** **Luôn đọc trọn vẹn từ chữ đầu tiên đến dấu chấm kết thúc của phương án trước khi quyết định.**

### 4.6. Ma trận loại suy 4 bước (Process of Elimination Heuristics)

```
                     [ĐỌC PHƯƠNG ÁN LỰA CHỌN]
                                |
               +----------------+----------------+
               |                                 |
     [Có từ tuyệt đối?]                [Có giống hệt bài đọc?]
      always/never/sole                 Verbatim matching 100%
               |                                 |
         (CẢNH GIÁC CAO!)                 (KIỂM TRA CÚ PHÁP!)
               |                                 |
               +----------------+----------------+
                                |
             [Kiểm tra Mối quan hệ Logic & Phạm vi]
                                |
       --------------------------------------------------
       |                        |                       |
   [Too Narrow]            [Too Broad]            [Opposite / Out]
   (Chỉ là 1 ý nhỏ)      (Khái quát quá mức)    (Ngược hoặc ngoài bài)
       |                        |                       |
     LOẠI                     LOẠI                    LOẠI
       --------------------------------------------------
                                |
                    [ĐÁP ÁN ĐÚNG DUY NHẤT]
             (Paraphrase chính xác ý nghĩa cốt lõi)
```

---
"""

with open(target_path, "a", encoding="utf-8") as f:
    f.write(content)

print("Part 2 appended successfully. Added bytes:", len(content))
