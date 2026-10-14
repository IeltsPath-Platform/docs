"""Wireframes (design target): Speaking Practice (P-45), the 3-column Writing Practice frame (P-44), Mock Test Catalog
(P-46), the computer-based Mock Test Runner (P-47), Submission History (P-54) and Account (P-80).

Layout follows reference screens of a computer-delivered IELTS platform, restyled with the IELTS Space chrome
(navbar, #123AB5 accent, orange underline on the current menu item). Not built in the frontend yet, except the
mock Speaking / Writing practice pages.
"""
from wf import PRIMARY, PRIMARY_SOFT, INK, MUTED, LINE, SOFT, CANVAS, DARK, MEDIA
from chrome import navbar, footer, screen, eyebrow, back_link, DESKTOP_W

X0, CW = 100, 1240
WHITE = "#FFFFFF"
ORANGE = "#F97316"


# ------------------------------------------------------------------ shared pieces
def subbar(p, y, title, right=None):
    """Practice workspace bar: ← Thoát · title · optional right text."""
    p.rect(0, y, DESKTOP_W, 56, fill=WHITE, stroke=LINE, r=0)
    p.btn(X0 - 60, y + 10, 110, 36, "← Thoát", kind="secondary", size=13)
    p.text(X0 + 70, y + 10, 700, 36, f"<b>{title}</b>", size=15)
    if right:
        p.text(X0 + CW - 360, y + 10, 400, 36, right, size=14, color=MUTED, align="right")
    return y + 56


def part_progress(p, y, parts, active_part, active_q=None, done=0):
    """Bottom navigator: one box per part with question bubbles (speaking / exam style)."""
    p.rect(0, y, DESKTOP_W, 72, fill=PRIMARY_SOFT, stroke=LINE, r=0)
    x = X0 + 40
    for label, count in parts:
        w = 70 + count * 34
        on = label == active_part
        p.rect(x, y + 12, w, 48, fill=WHITE, stroke=PRIMARY if on else LINE, r=10, sw=2 if on else 1)
        p.text(x + 10, y + 12, 60, 48, f"<b>{label}</b>" if on else label, size=13, color=PRIMARY if on else MUTED)
        for i in range(count):
            n = i + 1
            cur = on and active_q == n
            filled = on and n <= done
            st = ("ellipse;whiteSpace=wrap;html=1;fontFamily=Arial;fontSize=11;"
                  + ("fillColor=#123AB5;strokeColor=#123AB5;fontColor=#FFFFFF;" if cur else
                     "fillColor=#E8EDFB;strokeColor=#123AB5;fontColor=#123AB5;" if filled else
                     "fillColor=#FFFFFF;strokeColor=#C9CED6;fontColor=#6B7280;"))
            p.cell(str(n), st, x + 64 + i * 34, y + 23, 26, 26)
        x += w + 12


def exam_top(p, title, remaining, audio=False):
    """Computer-delivered test header: logo · test title · time left · status icons."""
    p.rect(0, 0, DESKTOP_W, 64, fill=WHITE, stroke=LINE, r=0)
    p.rect(24, 12, 120, 40, fill=PRIMARY, stroke=PRIMARY, r=6, value="IELTS Space", color=WHITE, size=12, bold=True)
    p.text(164, 10, 500, 24, f"<b>{title}</b>", size=16)
    if audio:
        p.rect(164, 36, 120, 22, fill=SOFT, stroke=LINE, r=11, value="🔊 Audio player", size=11)
        p.text(296, 36, 200, 22, remaining, size=12, color=MUTED)
    else:
        p.text(164, 36, 300, 22, remaining, size=12, color=MUTED)
    p.text(DESKTOP_W - 150, 18, 130, 28, "📶   🔔   ☰", size=16, color=INK, align="right")


def exam_part_banner(p, y, part, instruction):
    p.rect(16, y, DESKTOP_W - 32, 60, fill=SOFT, stroke=LINE, r=6)
    p.text(32, y + 8, 600, 22, f"<b>{part}</b>", size=15)
    p.text(32, y + 30, 900, 22, instruction, size=13, color=INK)
    return y + 76


def exam_bottom(p, h, parts, active, current):
    """Part navigator: active part shows question numbers, others '{done} of {n}'; ✓ submits."""
    y = h - 64
    p.rect(0, y, DESKTOP_W, 64, fill=CANVAS, stroke=LINE, r=0)
    x = 24
    for label, n in parts:
        if label == active:
            p.text(x, y + 20, 60, 24, f"<b>{label}</b>", size=13)
            for i in range(n):
                on = i + 1 == current
                p.rect(x + 66 + i * 26, y + 18, 22, 26, fill=WHITE, stroke=PRIMARY if on else "none", r=3, sw=2,
                       value=str(i + 1), size=12, color=PRIMARY if on else INK, bold=on)
            x += 80 + n * 26 + 120
        else:
            p.text(x, y + 20, 160, 24, f"<b>{label}</b>  0 of {n}", size=13, align="left")
            x += 330
    p.rect(DESKTOP_W - 72, y, 72, 64, fill=SOFT, stroke=LINE, r=0, value="✓", size=20, color=INK)
    p.rect(DESKTOP_W - 168, y - 70, 52, 48, fill=DARK, stroke=DARK, r=4, value="←", size=20, color=WHITE)
    p.rect(DESKTOP_W - 108, y - 70, 52, 48, fill=INK, stroke=INK, r=4, value="→", size=20, color=WHITE)


PASSAGE = ("People from almost every culture love collecting things. They might collect stamps, books, cards, priceless "
           "paintings or worthless ticket stubs to old sports games. Their collection might hang on the walls of a "
           "mansion or be stored in a box under the bed. So what is it that drives people to collect? …")


def passage(p, y, h):
    p.text(24, y, 680, 120, PASSAGE, size=13, valign="top")
    p.lines(24, y + 136, 680, n=10, gap=22, h=9)
    p.lines(24, y + 380, 680, n=6, gap=22, h=9)
    p.rect(712, y - 6, 8, h, fill=MEDIA, stroke=MEDIA, r=4)
    p.rect(718, y + h / 2 - 16, 28, 32, fill=WHITE, stroke=LINE, r=4, value="↔", size=13)


# ------------------------------------------------------------------ P-45 Speaking Practice
SPEAKING_PARTS = [("Intro", 0), ("Part 1", 12), ("Part 2", 1), ("Part 3", 4)]


def speaking_page(f, frame, h=900):
    p = screen(f, "P-45", frame, "Speaking Practice", h=h)
    y = navbar(p, role="learner", active="Luyện tập 4 kỹ năng", child="Speaking")
    y = subbar(p, y, "Speaking · Cue card: Describe your hometown", "◷ Speaking time 00:00")
    return p, y


def p45_intro(f):
    h = 900
    p, y = speaking_page(f, "Hướng dẫn chung", h)
    p.zone(X0 - 36, y + 24, "A")
    p.card(X0, y + 24, CW, 520, r=14)
    p.text(X0, y + 44, CW, 30, "<b>Hướng dẫn chung</b>", size=20, align="center")
    p.rect(X0 + 30, y + 90, CW - 60, 66, fill=WHITE, stroke=LINE, r=10, align="left", size=14,
           value="☐  <b>Luôn hiển thị sẵn câu hỏi trên màn hình</b><br>"
                 "<font style='font-size:12px' color='#6B7280'>Nếu tick vào lựa chọn này, câu hỏi sẽ được hiển thị song song với "
                 "Audio được phát</font>")
    p.text(X0 + 30, y + 176, CW - 60, 24, "Để việc làm bài diễn ra thật thuận lợi, bạn hãy chú ý những điểm quan trọng sau:", size=15)
    for i, (head, body) in enumerate((
            ("Kiểm tra và đảm bảo Loa/Tai nghe và Microphone đã kết nối.", "Hãy Test microphone trước khi làm bài để bài làm được ghi nhận đầy đủ."),
            ("Làm bài ở nơi yên tĩnh, ít tiếng ồn.", "Nói gần microphone để ghi âm được chất lượng tốt nhất; tạp âm ảnh hưởng tới việc chấm điểm."),
            ("Lưu ý giới hạn thời gian trả lời!", "Giống thi thật, hệ thống chuyển sang câu tiếp theo khi hết thời gian của câu."))):
        p.text(X0 + 60, y + 214 + i * 74, CW - 120, 64,
               f"<b><font color='#123AB5'>{head}</font></b> {body}", size=14, valign="top")
    p.text(X0 + 30, y + 448, CW - 60, 24, "<i>(*) Từ sau màn này, toàn bộ hướng dẫn làm bài sẽ là Tiếng Anh.</i>", size=13, color=MUTED)
    p.btn(X0 + CW / 2 - 90, y + 474, 180, 46, "▶| Next step", size=15)
    part_progress(p, h - 88, SPEAKING_PARTS, "Intro")
    return p


def p45_mic(f):
    h = 900
    p, y = speaking_page(f, "Kiểm tra micro", h)
    p.zone(X0 - 36, y + 24, "A")
    p.card(X0, y + 24, CW, 520, r=14)
    p.text(X0, y + 44, CW, 30, "<b>TEST YOUR MICROPHONE</b>", size=17, align="center")
    p.text(X0 + 380, y + 170, 600, 120, "•  You have 20 seconds to speak.<br>•  To complete this activity, you must allow "
           "access to your system's microphone.<br>•  Click the button <b>“Test microphone”</b> below to start.", size=16, valign="top")
    p.rect(X0 + CW / 2 - 60, y + 414, 120, 26, fill=PRIMARY_SOFT, stroke=PRIMARY_SOFT, r=6, value="Kiểm tra micrô", size=12, color=PRIMARY)
    p.btn(X0 + CW / 2 - 100, y + 448, 200, 46, "🎙 Test microphone", size=15)
    p.link(X0 + CW - 120, y + 460, 90, "▶| Skip", size=14)
    part_progress(p, h - 88, SPEAKING_PARTS, "Intro")
    return p


def p45_recording(f):
    h = 900
    p, y = speaking_page(f, "Part 1 — Đang ghi âm", h)
    p.zone(X0 - 36, y + 24, "A")
    p.card(X0, y + 24, CW, 520, r=14)
    eyebrow(p, X0 + 40, y + 48, "Part 1 · Question 3 of 12")
    p.text(X0 + 40, y + 74, CW - 80, 34, "<b>Do you like the place where you live? Why / why not?</b>", size=22)
    p.cell("🎙", "ellipse;whiteSpace=wrap;html=1;fillColor=#E8EDFB;strokeColor=#123AB5;strokeWidth=3;fontSize=40;",
           X0 + CW / 2 - 70, y + 170, 140, 140)
    p.text(X0, y + 326, CW, 30, "<b>Đang ghi âm · 00:14 / 00:30</b>", size=17, color=PRIMARY, align="center")
    p.progress(X0 + CW / 2 - 200, y + 366, 400, 47)
    p.btn(X0 + CW / 2 - 110, y + 410, 220, 46, "■ Dừng & sang câu tiếp", size=14)
    p.text(X0, y + 476, CW, 22, "Tự chuyển câu khi hết 30 giây. Bản ghi được tải lên khi nộp phần thi.", size=13,
           color=MUTED, align="center")
    part_progress(p, h - 88, SPEAKING_PARTS, "Part 1", active_q=3, done=2)
    return p


# ------------------------------------------------------------------ P-44 Writing Practice — 3-column frame
def writing_three_columns(f):
    h = 980
    p = screen(f, "P-44", "Bố cục 3 cột (đề xuất)", "Writing Practice", h=h)
    y = navbar(p, role="learner", active="Luyện tập 4 kỹ năng", child="Writing")
    y = subbar(p, y, "[Writing] Task 1 · Daily oil production in 4 countries", "")
    y += 20
    c1, c2, c3 = (X0 - 60, 470), (X0 + 430, 520), (X0 + 970, 330)
    p.zone(c1[0] - 30, y, "A")
    p.card(c1[0], y, c1[1], 720, r=18)
    p.rect(c1[0] + 16, y + 16, c1[1] - 32, 80, fill=WHITE, stroke=DARK, r=4, align="left", size=13,
           value="<b><i>The table below shows daily oil production in 4 countries from 2000 to 2004. Summarise the "
                 "information by selecting and reporting the main features.</i></b>")
    p.rect(c1[0] + 16, y + 120, c1[1] - 32, 340, fill=PRIMARY_SOFT, stroke=LINE, r=12)
    p.text(c1[0] + 16, y + 130, c1[1] - 32, 22, "<b>Daily oil production in 4 countries (barrels per day)</b>", size=13,
           color=PRIMARY, align="center")
    cols = ["Country", "2000", "2001", "2002", "2003", "2004"]
    rows = [["Nigeria", "205,000", "201,000", "190,000", "210,000", "213,000"], ["Chad", "0", "0", "0", "8,000", "50,000"],
            ["Congo", "275,000", "234,000", "222,000", "215,000", "203,000"], ["Somalia", "5,000", "8,000", "17,000", "21,000", "50,000"]]
    cw = (c1[1] - 48) / 6
    for r, row in enumerate([cols] + rows):
        for c, val in enumerate(row):
            head = r == 0
            p.rect(c1[0] + 24 + c * cw, y + 160 + r * 56, cw, 56, fill=PRIMARY if head else (PRIMARY_SOFT if c == 0 else WHITE),
                   stroke=LINE, r=0, value=f"<b>{val}</b>" if head or c == 0 else val, size=11,
                   color=WHITE if head else (PRIMARY if c == 0 else INK))
    p.btn(c1[0] + 16, y + 480, 180, 36, "⤢ Phóng to biểu đồ", kind="secondary", size=12)
    p.zone(c2[0] - 30, y, "B")
    p.card(c2[0], y, c2[1], 720, r=18)
    p.rect(c2[0], y, c2[1], 50, fill=SOFT, stroke=LINE, r=0)
    p.text(c2[0] + c2[1] - 220, y + 12, 200, 26, "✎ Word count: <b>0/150</b>", size=14, align="right")
    for i, label in enumerate(("Introduction", "Overview", "Body 1", "Body 2")):
        sy = y + 66 + i * 130
        p.text(c2[0] + 16, sy, 300, 22, f"<b>{label}</b>", size=15)
        p.rect(c2[0] + 16, sy + 28, c2[1] - 32, 90 if i else 66, fill=WHITE, stroke=LINE, r=8,
               value="Nhập phần viết của bạn ở đây", color=MUTED, size=13, align="left", valign="top")
    p.text(c2[0] + 16, y + 640, 200, 44, "Thời gian:<br><b>00:00:19</b>", size=13)
    p.btn(c2[0] + c2[1] - 156, y + 646, 140, 42, "Hoàn thành", size=14)
    p.zone(c3[0] - 30, y, "C")
    p.card(c3[0], y, c3[1], 720, r=18)
    p.text(c3[0] + 20, y + 18, 260, 28, "<b>📖 Tra từ vựng</b> <font color='#16A34A'>●</font>", size=16)
    p.text(c3[0] + 20, y + 70, c3[1] - 40, 300, "Kết quả tra cứu hiện ở đây: từ, phiên âm, nghĩa, ví dụ và nút "
           "“Lưu vào Flashcard”.", size=12, color=MUTED, italic=True, valign="top")
    p.card(c3[0] + 16, y + 520, c3[1] - 32, 180, r=12, fill=SOFT)
    p.rect(c3[0] + 16, y + 520, c3[1] - 32, 40, fill=WHITE, stroke=LINE, r=0, value="<b>Tra Anh-Việt</b>", size=13)
    p.text(c3[0] + 32, y + 572, c3[1] - 64, 40, "Nhập từ hoặc cụm Tiếng Anh cần tra", size=13, color=MUTED)
    p.text(c3[0] + 32, y + 656, 120, 24, "0/50 ký tự", size=12, color=MUTED)
    p.btn(c3[0] + c3[1] - 140, y + 650, 108, 34, "Tra từ vựng", kind="disabled", size=12)
    p.text(X0 - 60, y + 732, 1340, 22, "Design target: the dictionary panel and the paragraph editor replace the single text box "
           "of the current Writing page; the panels can be resized (⠿ handles).", size=12, color=MUTED, italic=True)
    return p


# ------------------------------------------------------------------ P-46 Mock Test Catalog
def p46(f):
    h = 1300
    p = screen(f, "P-46", "Populated", "Mock Test Catalog", h=h)
    y = navbar(p, role="learner", active="Luyện tập 4 kỹ năng") + 28
    p.zone(X0 - 36, y, "A")
    eyebrow(p, X0, y, "Thi thử IELTS trên máy")
    p.text(X0, y + 22, 800, 40, "<b>Đề thi thử đầy đủ 4 kỹ năng</b>", size=30)
    p.text(X0, y + 66, 900, 22, "Làm bài giống thi thật trên máy: tính giờ từng phần, nộp tự động khi hết giờ. Writing "
           "và Speaking được chấm bởi EXAMINER.", size=14, color=MUTED)
    y += 110
    for i, (label, on) in enumerate((("Tất cả", True), ("Academic", False), ("General", False))):
        p.chip(X0 + i * 100, y, label, kind="solid" if on else "neutral", w=90)
    p.text(X0 + CW - 300, y, 300, 24, "Còn <b>2</b> lượt chấm EXAMINER · <b>30</b> điểm", size=13, align="right")
    y += 44
    p.zone(X0 - 36, y, "B")
    tests = [("Onboarding Test", "Academic · 4 kỹ năng · 2 giờ 45 phút", "Chưa làm", "Bắt đầu"),
             ("Cambridge 18 — Test 1", "Academic · 4 kỹ năng · 2 giờ 45 phút", "Đang làm · Reading 60%", "Làm tiếp"),
             ("Cambridge 18 — Test 2", "Academic · 4 kỹ năng", "Band 6.5 · 05/10/2026", "Xem kết quả"),
             ("Cambridge 17 — Test 1", "Academic · 4 kỹ năng", "Premium", "🔒 Nâng cấp"),
             ("General Training — Test 1", "General · 4 kỹ năng", "Chưa làm", "Bắt đầu"),
             ("Cambridge 17 — Test 2", "Academic · 4 kỹ năng", "Premium", "🔒 Nâng cấp")]
    cw = (CW - 32) / 3
    for i, (name, meta, state, cta) in enumerate(tests):
        cx, cy = X0 + (i % 3) * (cw + 16), y + (i // 3) * 250
        locked = cta.startswith("🔒")
        p.card(cx, cy, cw, 234, r=14, fill=SOFT if locked else WHITE)
        p.img(cx + 16, cy + 16, cw - 32, 80, "Ảnh bìa đề")
        p.text(cx + 16, cy + 108, cw - 32, 26, f"<b>{name}</b>", size=16)
        p.text(cx + 16, cy + 136, cw - 32, 20, meta, size=12, color=MUTED)
        p.chip(cx + 16, cy + 166, state, kind="active" if state.startswith("Đang") else "neutral", size=11)
        p.btn(cx + cw - 156, cy + 182, 140, 38, cta, kind="secondary" if locked or cta == "Xem kết quả" else "primary", size=13)
    p.rect(X0 + 260, y + 540, 720, 64, fill=WHITE, stroke=PRIMARY, r=12, sw=2, align="left", size=13,
           value="<b>Bắt đầu “Onboarding Test”?</b> Bài gồm Listening 30', Reading 60', Writing 60', Speaking 15'. "
                 "Thời gian tính ngay khi bắt đầu.  [Huỷ]  [Bắt đầu làm bài]")
    p.text(X0 + 260, y + 610, 720, 20, "Confirm dialog (drawn inline) before POST /api/assessments/attempts.", size=11,
           color=MUTED, italic=True)
    footer(p, h - 64)
    return p


# ------------------------------------------------------------------ P-47 Mock Test Runner
READING_PARTS = [("Part 1", 13), ("Part 2", 13), ("Part 3", 14)]


def runner(f, frame, h=900, title="Onboarding Reading", remaining="60 minutes remaining", audio=False):
    p = screen(f, "P-47", frame, "Mock Test Runner", h=h)
    exam_top(p, title, remaining, audio)
    return p


def p47_tfng(f):
    h = 900
    p = runner(f, "Reading — True / False / Not Given")
    y = exam_part_banner(p, 80, "Part 1", "Read the text and answer questions 1-13")
    p.zone(4, y, "A")
    passage(p, y + 8, 640)
    qx = 760
    p.zone(qx - 30, y, "B")
    p.text(qx, y + 8, 600, 22, "<b>Questions 1-6</b>", size=14)
    p.text(qx, y + 34, 640, 80, "Do the following statements agree with the information given in the passage?<br>"
           "<b>TRUE</b> if the statement agrees · <b>FALSE</b> if it contradicts · <b>NOT GIVEN</b> if there is no information",
           size=12, valign="top")
    for qi, (q, sel) in enumerate((("Dr Maria Richter believes that people become interested in collecting in early childhood.", 1),
                                   ("A form of collecting may have helped some ancient humans to survive.", None))):
        qy = y + 120 + qi * 230
        p.rect(qx, qy, 26, 26, fill=WHITE, stroke=PRIMARY if qi == 0 else "none", r=4, sw=2, value=f"<b>{qi + 1}</b>", size=12)
        p.text(qx + 36, qy, 600, 26, q, size=13)
        p.text(qx + 650, qy, 20, 26, "🔖", size=12, color=MUTED)
        for oi, opt in enumerate(("TRUE", "FALSE", "NOT GIVEN")):
            on = sel == oi
            p.rect(qx, qy + 40 + oi * 46, 660, 40, fill=PRIMARY_SOFT if on else WHITE, stroke=PRIMARY if on else "none", r=6,
                   value=f"{'◉' if on else '○'}  {opt}", size=13, align="left", color=PRIMARY if on else INK)
    exam_bottom(p, h, READING_PARTS, "Part 1", 1)
    return p


def p47_summary(f):
    h = 900
    p = runner(f, "Reading — Summary completion")
    y = exam_part_banner(p, 80, "Part 1", "Read the text and answer questions 1-13")
    p.zone(4, y, "A")
    passage(p, y + 8, 640)
    qx = 760
    p.zone(qx - 30, y, "B")
    p.text(qx, y + 8, 600, 22, "<b>Questions 7-13</b>", size=14)
    p.text(qx, y + 34, 640, 40, "Choose ONE WORD ONLY from the passage for each answer.", size=12)
    p.text(qx, y + 70, 640, 24, "<b>SOME SIGNIFICANT PRIVATE COLLECTIONS</b>", size=14, align="center")
    p.rect(qx, y + 104, 660, 420, fill=WHITE, stroke=INK, r=0)
    lines = [("<b>15th-17th Centuries</b>", None), ("• The Medici family made their money from", 7),
             ("• The Palazzo Medici had a hidden 'studio' which had no", 8),
             ("• Ole Worm made an important", 9), ("<b>19th Centuries</b>", None),
             ("• Lady Charlotte Guest created a collection of", 10), ("• Joseph Mayer paid for", 11),
             ("<b>20th Centuries</b>", None), ("• Beatrix Potter did not give away her collection of", 12),
             ("• Franklin D. Roosevelt believed collecting helped him deal with the", 13)]
    for i, (text, n) in enumerate(lines):
        ly = y + 116 + i * 40
        p.text(qx + 14, ly, 420, 28, text, size=12)
        if n:
            p.rect(qx + 440, ly + 2, 110, 24, fill=WHITE, stroke=PRIMARY if n == 7 else DARK, r=4, sw=2 if n == 7 else 1,
                   value=f"<b>{n}</b>", size=11)
    exam_bottom(p, h, READING_PARTS, "Part 1", 7)
    return p


def p47_listening(f):
    h = 900
    p = runner(f, "Listening — Note completion", title="Onboarding Listening", remaining="27 minutes remaining", audio=True)
    y = exam_part_banner(p, 80, "Part 1", "Listen and answer questions 1-10")
    p.zone(4, y, "A")
    p.text(24, y, 600, 22, "<b>Questions 1-8</b>", size=14)
    p.text(24, y + 24, 900, 22, "Complete the notes below. Write ONE WORD AND/OR A NUMBER for each answer.", size=12)
    p.text(24, y + 56, 600, 26, "<b>Enquiry about Airmail</b>", size=16)
    rows = [("Reasons for moving: Family reunion · Pleasant", 1, ""), ("Type of work:", 2, "job"),
            ("Post address:", 3, "Street, Sydney"), ("Accommodation: free for the first", 4, ""),
            ("Name: Jennifer", 5, ""), ("Current address:", 6, "Road, Auckland"), ("Postcode:", 7, ""), ("Mailing date:", 8, "")]
    for i, (lead, n, tail) in enumerate(rows):
        ry = y + 96 + i * 36
        lw = int(len(lead) * 6.6) + 12
        p.text(24, ry, lw, 26, lead, size=12)
        p.rect(24 + lw, ry + 1, 110, 24, fill=WHITE, stroke=PRIMARY if n == 1 else DARK, r=4, sw=2 if n == 1 else 1,
               value=f"<b>{n}</b>", size=11)
        p.text(24 + lw + 118, ry, 200, 26, tail, size=12)
    p.text(24, y + 400, 600, 22, "<b>Questions 9-10</b> · Choose TWO letters, A-E.", size=13)
    for i, opt in enumerate(("A  files", "B  medicine", "C  books")):
        p.text(40, y + 430 + i * 30, 300, 24, f"☐  {opt}", size=12)
    p.rect(980, y + 96, 400, 140, fill=SOFT, stroke=LINE, r=10, align="left", size=12,
           value="<b>🔊 Audio</b> phát một lần theo thời gian thi; không tua lại.<br>Âm lượng ━━━●━━  · "
                 "30 giây đọc đề trước mỗi phần.")
    exam_bottom(p, h, [("Part 1", 10), ("Part 2", 10), ("Part 3", 10), ("Part 4", 10)], "Part 1", 1)
    return p


def p47_submit(f):
    h = 900
    p = runner(f, "Nộp bài")
    y = exam_part_banner(p, 80, "Part 3", "Read the text and answer questions 27-40")
    passage(p, y + 8, 640)
    exam_bottom(p, h, READING_PARTS, "Part 3", 14)
    p.overlay(DESKTOP_W, h)
    dx, dw = 470, 500
    p.card(dx, 250, dw, 300, r=16)
    p.text(dx + 30, 276, dw - 60, 30, "<b>Nộp phần Reading?</b>", size=20)
    p.text(dx + 30, 316, dw - 60, 80, "Bạn đã trả lời <b>38/40</b> câu. Câu chưa trả lời: <b>12, 31</b>.<br>"
           "Sau khi nộp, bạn không quay lại phần này được.", size=14, valign="top")
    p.chip(dx + 30, 410, "Còn 08:12", kind="active", w=100)
    p.btn(dx + 30, 470, 200, 46, "Xem lại", kind="secondary", size=14)
    p.btn(dx + dw - 230, 470, 200, 46, "Nộp và sang Writing", size=14)
    return p


# ------------------------------------------------------------------ P-54 Submission History
SKILL_TABS = [("✎", "Writing"), ("🎙", "Speaking"), ("▤", "Reading"), ("🎧", "Listening"), ("▣", "Mock Test")]


def p54(f, frame, empty):
    h = 1100 if not empty else 950
    p = screen(f, "P-54", frame, "Submission History", h=h)
    y = navbar(p, role="learner", active="Trang chủ", child="Lịch sử nộp bài") + 28
    p.zone(X0 - 36, y, "A")
    p.text(X0, y, 600, 34, "<b>◷ Lịch sử nộp bài</b>", size=22)
    y += 50
    ch = 420 if empty else 600
    p.card(X0, y, CW, ch, r=16)
    x = X0 + 16
    for i, (icon, label) in enumerate(SKILL_TABS):
        w = int(len(label) * 9) + 60
        on = i == 0
        p.rect(x, y + 14, w, 40, fill=PRIMARY_SOFT if on else WHITE, stroke=PRIMARY_SOFT if on else "none", r=20,
               value=f"{icon}  {label}", size=14, color=PRIMARY if on else MUTED, bold=on)
        x += w + 10
    p.text(X0 + 20, y + 66, 140, 30, "<b>Theo tên bài</b>", size=14, color=PRIMARY)
    p.rect(X0 + 20, y + 96, 110, 3, fill=ORANGE, stroke=ORANGE, r=1)
    p.text(X0 + 170, y + 66, 140, 30, "Theo ngày nộp", size=14, color=MUTED)
    p.rect(X0, y + 102, CW, 1, fill=LINE, stroke=LINE, r=0)
    p.zone(X0 - 36, y + 110, "B")
    if empty:
        p.rect(X0 + CW / 2 - 70, y + 140, 140, 100, fill=PRIMARY_SOFT, stroke=PRIMARY_SOFT, r=50, value="📝", size=40)
        p.text(X0 + CW / 2 - 200, y + 256, 400, 44, "Bạn hiện chưa làm bài tập nào! Hãy chọn dạng phù hợp và luyện tập "
               "ngay nào!", size=14, align="center")
        p.btn(X0 + CW / 2 - 120, y + 320, 240, 44, "Tiến hành làm bài tập ngay", size=14)
    else:
        heads = [("Tên bài", 360), ("Nguồn", 180), ("Ngày nộp", 170), ("Trạng thái", 200), ("Band", 110), ("", 160)]
        hx = X0 + 20
        for label, w in heads:
            p.text(hx, y + 116, w, 30, f"<b>{label}</b>", size=13, color=MUTED)
            hx += w
        rows = [("Task 1 · Daily oil production", "Luyện tập", "12/10/2026 21:05", "Đã chấm (AI)", "6.0", "Xem nhận xét"),
                ("Task 2 · Education essay", "Bài học · Writing 3", "11/10/2026 19:40", "Đang chấm…", "—", "Xem bài"),
                ("Task 2 · Technology", "Thi thử · Cambridge 18", "10/10/2026 08:12", "Chờ EXAMINER", "—", "Xem bài"),
                ("Task 1 · Museum visitors", "Placement test", "05/10/2026 20:00", "Đã chấm (AI)", "5.5", "Xem nhận xét"),
                ("Task 1 · Line graph", "Bài học · Writing 1", "02/10/2026 18:30", "Chưa đạt · làm lại", "5.0", "Làm lại")]
        for r, row in enumerate(rows):
            ry = y + 156 + r * 76
            p.rect(X0 + 10, ry, CW - 20, 66, fill=SOFT if r % 2 else WHITE, stroke=LINE, r=10)
            hx = X0 + 20
            for c, (val, (_, w)) in enumerate(zip(row, heads)):
                if c == 3:
                    p.chip(hx, ry + 21, val, kind="active" if val.startswith("Đã chấm") else "neutral", size=11)
                elif c == 5:
                    p.btn(hx, ry + 14, 140, 38, val, kind="secondary", size=12)
                else:
                    p.text(hx, ry, w - 10, 66, f"<b>{val}</b>" if c in (0, 4) else val, size=13, color=INK if c in (0, 4) else MUTED)
                hx += w
        p.text(X0 + 20, y + 552, 400, 24, "Trang 1 / 3", size=13, color=MUTED)
        p.btn(X0 + CW - 230, y + 544, 100, 36, "‹ Trước", kind="disabled", size=12)
        p.btn(X0 + CW - 120, y + 544, 100, 36, "Sau ›", kind="secondary", size=12)
    footer(p, h - 64)
    return p


# ------------------------------------------------------------------ P-80 Account


def account_page(f, frame, active, h=760):
    """Account section without a sidebar: every section is opened from the user menu (◯ Học viên ▾)."""
    p = screen(f, "P-80", frame, "Account", h=h)
    y = navbar(p, role="learner") + 24
    p.zone(X0 - 36, y, "A")
    p.text(X0, y, 700, 24, f"<font color='#6B7280'>◯ Học viên ▾  ›</font>  <b>{active}</b>", size=13)
    p.text(X0 + CW - 560, y, 560, 24, "Các mục tài khoản mở từ user menu (◯ Học viên ▾) trên thanh điều hướng.",
           size=11, color=MUTED, italic=True, align="right")
    return p, y + 44, X0, CW


def p80_profile(f):
    p, y, mx, mw = account_page(f, "Hồ sơ của bạn", "Hồ sơ của bạn")
    p.zone(mx - 30, y, "B")
    p.text(mx, y, 300, 28, "<b>👤 Hồ sơ của bạn</b>", size=17)
    p.text(mx + mw - 520, y + 2, 520, 24, "Quản lý thông tin cá nhân, gồm số điện thoại và địa chỉ email.", size=13, align="right")
    p.card(mx, y + 44, mw, 104, r=14)
    p.rect(mx + 20, y + 62, 68, 68, fill=PRIMARY_SOFT, stroke=PRIMARY, r=34, value="<b>HS</b>", size=18, color=PRIMARY)
    p.text(mx + 104, y + 64, 400, 24, "<b>Hong Son Le</b>", size=16)
    p.text(mx + 104, y + 90, 400, 20, "learner@example.com", size=12, color=MUTED)
    p.text(mx + 104, y + 110, 400, 20, "0912 345 678 <font color='#16A34A'>✔</font>", size=12, color=MUTED)
    p.btn(mx + mw - 210, y + 78, 190, 40, "Thay đổi ảnh đại diện", kind="secondary", size=13)
    fy = y + 172
    p.text(mx, fy, 300, 22, "👤 Họ và tên", size=13)
    p.rect(mx, fy + 26, mw / 2 - 10, 44, fill=WHITE, stroke=DARK, r=8, value="Hong Son Le", size=14, align="left")
    p.text(mx, fy + 90, 300, 22, "✉ Email", size=13)
    p.rect(mx, fy + 116, mw / 2 - 10, 44, fill=SOFT, stroke=LINE, r=8, value="learner@example.com", color=MUTED, size=14, align="left")
    p.text(mx + mw / 2 + 10, fy + 90, 300, 22, "☎ Số điện thoại", size=13)
    p.rect(mx + mw / 2 + 10, fy + 116, mw / 2 - 10, 44, fill=SOFT, stroke=LINE, r=8, value="0912 345 678", color=MUTED, size=14, align="left")
    p.text(mx, fy + 180, 300, 22, "Tên hiển thị · Band tự đánh giá · Múi giờ", size=13)
    p.rect(mx, fy + 206, mw, 44, fill=WHITE, stroke=DARK, r=8, value="Sone · 5.5 · Asia/Ho_Chi_Minh", size=14, align="left")
    p.btn(mx + mw - 200, fy + 280, 200, 42, "✓ Cập nhật thông tin", kind="disabled", size=13)
    p.text(mx, fy + 336, mw, 22, "Email không đổi được ở đây; số điện thoại lưu trong tài khoản (PUT /api/users/me).", size=11,
           color=MUTED, italic=True)
    return p


def history_table(p, mx, mw, y, heads, rows):
    total = sum(w for _, w in heads)
    heads = [(label, w * mw / total) for label, w in heads]  # columns stretch to the table width
    hx = mx
    p.rect(mx, y, mw, 40, fill=SOFT, stroke=LINE, r=8)
    widths = [w for _, w in heads]
    for label, w in heads:
        p.text(hx + 14, y, w - 20, 40, f"<b>{label}</b>", size=13, color=MUTED)
        hx += w
    for r, row in enumerate(rows):
        ry = y + 48 + r * 54
        p.rect(mx, ry, mw, 48, fill=WHITE, stroke=LINE, r=8)
        hx = mx
        for c, val in enumerate(row):
            p.text(hx + 14, ry, widths[c] - 20, 48, val, size=13)
            hx += widths[c]
    return y + 48 + len(rows) * 54


def p80_payments(f):
    p, y, mx, mw = account_page(f, "Lịch sử kích hoạt gói", "Lịch sử kích hoạt gói")
    p.zone(mx - 30, y, "B")
    p.text(mx, y, 400, 28, "<b>◷ Lịch sử kích hoạt gói</b>", size=17)
    p.card(mx, y + 44, mw, 96, r=14, fill=PRIMARY_SOFT)
    p.text(mx + 20, y + 58, 500, 26, "<b>Premium 30 Ngày</b> · còn 18 ngày · hết hạn 31/10/2026", size=15)
    p.text(mx + 20, y + 88, 600, 22, "Kích hoạt bằng mã Key; còn 2 lượt chấm EXAMINER.", size=13, color=MUTED)
    p.btn(mx + mw - 190, y + 70, 170, 42, "Nhập mã Key", size=13)
    end = history_table(p, mx, mw, y + 164, [("Thời gian", 200), ("Sản phẩm", 260), ("Mã Key", 220), ("Hiệu lực", 180), ("Trạng thái", 80)],
                        [("01/10/2026 20:15", "Premium 30 Ngày", "IP-7K2M-••••-Q9", "01/10 → 31/10", "✔"),
                         ("15/09/2026 09:02", "Thẻ Point 50", "IP-3XA1-••••-L4", "+50 điểm", "✔"),
                         ("02/09/2026 18:44", "Premium 30 Ngày", "IP-9PQ0-••••-7C", "02/09 → 02/10", "Hết hạn")])
    p.text(mx, end + 16, mw, 22, "Hệ thống chưa có cổng thanh toán: mỗi dòng là một lần kích hoạt mã Key.", size=11,
           color=MUTED, italic=True)
    return p


def p80_points(f):
    p, y, mx, mw = account_page(f, "Lịch sử giao dịch điểm", "Lịch sử giao dịch điểm")
    p.zone(mx - 30, y, "B")
    p.text(mx, y, 400, 28, "<b>✦ Lịch sử giao dịch điểm</b>", size=17)
    p.card(mx, y + 44, 300, 96, r=14, fill=PRIMARY_SOFT)
    p.text(mx + 20, y + 56, 260, 22, "Số dư hiện tại", size=13, color=MUTED)
    p.text(mx + 20, y + 80, 260, 40, "<b>30 điểm</b>", size=26, color=PRIMARY)
    for i, (label, on) in enumerate((("Tất cả", True), ("Cộng", False), ("Trừ", False))):
        p.chip(mx + 340 + i * 90, y + 80, label, kind="solid" if on else "neutral", w=80)
    end = history_table(p, mx, mw, y + 164, [("Thời gian", 200), ("Nội dung", 400), ("Thay đổi", 160), ("Số dư", 180)],
                        [("12/10/2026 21:05", "Chấm bài luận AI · Writing Task 1", "−3", "30"),
                         ("11/10/2026 19:40", "Chấm bài luận AI · Bài học Writing 3", "−3", "33"),
                         ("10/10/2026 08:20", "Hoàn điểm: chấm bài lỗi", "+3", "36"),
                         ("09/10/2026 16:45", "Điều chỉnh bởi quản trị viên", "−17", "33"),
                         ("15/09/2026 09:02", "Nạp thẻ Point 50", "+50", "50")])
    p.text(mx, end + 16, 300, 24, "Trang 1 / 4", size=13, color=MUTED)
    p.btn(mx + mw - 220, end + 8, 100, 36, "‹ Trước", kind="disabled", size=12)
    p.btn(mx + mw - 110, end + 8, 100, 36, "Sau ›", kind="secondary", size=12)
    return p


def p80_logins(f):
    p, y, mx, mw = account_page(f, "Lịch sử đăng nhập", "Lịch sử đăng nhập")
    p.zone(mx - 30, y, "B")
    p.text(mx, y, 400, 28, "<b>🔒 Lịch sử đăng nhập</b>", size=17)
    p.text(mx, y + 34, mw, 22, "Các phiên đăng nhập gần đây. Đăng xuất phiên lạ ngay nếu không phải bạn.", size=13, color=MUTED)
    end = history_table(p, mx, mw, y + 70, [("Thời gian", 200), ("Thiết bị / trình duyệt", 300), ("IP", 160), ("Trạng thái", 160), ("", 120)],
                        [("13/10/2026 08:01", "Chrome · Windows", "113.161.•.•", "Phiên hiện tại", ""),
                         ("12/10/2026 21:00", "Safari · iPhone", "14.232.•.•", "Đang hoạt động", "Đăng xuất"),
                         ("05/10/2026 07:45", "Edge · Windows", "113.161.•.•", "Đã đăng xuất", ""),
                         ("01/10/2026 19:12", "Chrome · Android", "171.224.•.•", "Hết hạn", "")])
    p.btn(mx + mw - 260, end + 16, 260, 42, "Đăng xuất mọi thiết bị khác", kind="secondary", size=13)
    return p


# ------------------------------------------------------------------ builders
def build(new):
    f = new("P-45_SpeakingPractice")
    p45_intro(f)
    p45_mic(f)
    p45_recording(f)
    f.save()
    f = new("P-46_MockTestCatalog")
    p46(f)
    f.save()
    f = new("P-47_MockTestRunner")
    p47_tfng(f)
    p47_summary(f)
    p47_listening(f)
    p47_submit(f)
    f.save()
    f = new("P-54_SubmissionHistory")
    p54(f, "Populated", empty=False)
    p54(f, "Empty", empty=True)
    f.save()
    f = new("P-80_Account")
    p80_profile(f)
    p80_payments(f)
    p80_points(f)
    p80_logins(f)
    f.save()
