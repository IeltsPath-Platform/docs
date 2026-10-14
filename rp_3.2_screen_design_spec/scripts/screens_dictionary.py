"""Wireframes (design target): the dictionary area — Dictionary Home (P-56), Word Detail (P-57), Vocabulary Map (P-58),
Vocabulary Set (P-59) and Set Study session (P-59a).

Content follows the sheet "Mô tả Từ điển" (Code LMS_TIS.xlsx): Oxford-based word data (word class, OPAL tag, usage
label, UK/US IPA + audio, Gen-AI memory image, Vietnamese and English meaning, examples, collocations, word family,
CEFR, IELTS level; thesaurus, common mistakes, topics), vocabulary sets by IELTS band / topic / Oxford 3000-5000 /
collocations / personal notebook, mixed study modes, and the vocabulary map. Layout follows the reference screens,
without their left sidebar, inside the IELTS Space navbar (Sổ ghi nhớ › Học). The built page is P-50.
"""
from wf import PRIMARY, PRIMARY_SOFT, INK, MUTED, LINE, SOFT, CANVAS, DARK, MEDIA
from chrome import navbar, footer, screen, DESKTOP_W

X0, CW = 100, 1240
WHITE = "#FFFFFF"
ORANGE = "#F97316"
LEARNED, REVIEWING, AGAIN, TODO = PRIMARY, "#F59E0B", "#DC2626", "#E5E7EB"  # vocabulary map states
MAIN_W, SIDE_W = 820, 396  # word detail / set detail columns
SIDE_X = X0 + CW - SIDE_W


def dict_page(f, pid, frame, title, h):
    p = screen(f, pid, frame, title, h=h)
    y = navbar(p, role="learner", active="Sổ ghi nhớ", child="Học") + 24
    return p, y


def crumb(p, y, *parts):
    """‹ Từ điển / … / current (last part bold)."""
    trail = "  /  ".join(parts[:-1] + (f"<b><font color='#123AB5'>{parts[-1]}</font></b>",))
    p.text(X0, y, 900, 24, f"‹   {trail}", size=13, color=MUTED)
    return y + 36


def search_bar(p, y, value="", suggestions=("environment", "sustainable", "perspective"), label="Gần đây:"):
    p.rect(X0, y, CW, 56, fill=WHITE, stroke=LINE, r=14)
    p.text(X0 + 20, y, 700, 56, f"⌕   {value}" if value else "⌕   Tra từ, cụm từ hoặc nhập câu cần tra…",
           size=15, color=INK if value else MUTED)
    p.text(X0 + CW - 300, y, 140, 56, "Anh - Việt ▾", size=14, color=INK, align="right")
    p.btn(X0 + CW - 140, y + 9, 124, 38, "Tra từ", size=14)
    x = X0 + 4 + len(label) * 7 + 10
    p.text(X0, y + 64, 120, 22, label, size=12, color=MUTED)
    for s in suggestions:
        p.text(x, y + 64, len(s) * 7 + 16, 22, f"<u>{s}</u>", size=12, color=PRIMARY)
        x += len(s) * 7 + 22
    return y + 100


def section_title(p, x, y, text, size=17):
    p.text(x, y, 600, 26, f"<b>{text}</b>", size=size)


def cefr_badge(p, x, y, level, d=120):
    p.cell(f"<b><font style='font-size:30px'>{level}</font></b>",
           "ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#123AB5;strokeWidth=10;fontFamily=Arial;fontColor=#123AB5;",
           x, y, d, d)


def weekly_goal(p, x, y, w, done=86, goal=120, days_done=5):
    p.card(x, y, w, 190, r=16)
    section_title(p, x + 20, y + 16, "◎ Mục tiêu tuần", 16)
    p.text(x + 20, y + 50, w - 40, 30, f"<b><font style='font-size:24px'>{done}</font></b> /{goal} từ", size=13, color=MUTED)
    p.text(x + 20, y + 80, w - 40, 20, f"Còn {goal - done} từ để đạt mục tiêu tuần này", size=12, color=MUTED)
    step = (w - 40) / 7
    for i, d in enumerate(("T2", "T3", "T4", "T5", "T6", "T7", "CN")):
        cx = x + 20 + i * step
        p.text(cx, y + 112, step, 18, d, size=11, color=MUTED, align="center")
        on = i < days_done
        p.cell("✓" if on else "", "ellipse;whiteSpace=wrap;html=1;fontSize=12;fontColor=#FFFFFF;"
               + ("fillColor=#123AB5;strokeColor=#123AB5;" if on else "fillColor=#FFFFFF;strokeColor=#C9CED6;"),
               cx + step / 2 - 13, y + 136, 26, 26)


def map_legend(p, x, y):
    for i, (color, label) in enumerate(((LEARNED, "Đã học"), (REVIEWING, "Đang ôn"), (AGAIN, "Cần ôn lại"), (TODO, "Chưa học"))):
        p.rect(x + i * 150, y + 4, 14, 14, fill=color, stroke=color, r=3)
        p.text(x + i * 150 + 22, y, 120, 22, label, size=12, color=MUTED)


# ------------------------------------------------------------------ P-56 Dictionary Home
SET_BANDS = [("🚀", "IELTS 0–3.0", "12 chủ đề", 75), ("🎈", "IELTS 3.0–4.0", "12 chủ đề", 45),
             ("🏙", "IELTS 4.0–5.0", "12 chủ đề", 30), ("⛰", "IELTS 5.0–6.0", "12 chủ đề", 51),
             ("🌐", "IELTS 6.0–7.0", "12 chủ đề", 8), ("📒", "Oxford 3000", "Theo chủ đề", 22)]
CEFR = [("A1", 320, 500, 0.64, 0.06, 0.02), ("A2", 210, 500, 0.42, 0.12, 0.08), ("B1", 470, 1000, 0.47, 0.06, 0.03),
        ("B2", 180, 1000, 0.18, 0.04, 0.03), ("C1", 66, 1000, 0.07, 0.03, 0.02)]


def p56(f):
    h = 1780
    p, y = dict_page(f, "P-56", "Trang chủ từ điển", "Dictionary Home", h)
    p.zone(X0 - 36, y, "A")
    p.text(X0, y, 800, 40, "<b>Từ điển của bạn</b>", size=30)
    p.text(X0, y + 42, 800, 22, "Tra cứu, học và theo dõi hành trình mở rộng vốn từ.", size=14, color=MUTED)
    y = search_bar(p, y + 80)
    p.zone(X0 - 36, y, "B")
    p.rect(X0, y, CW, 230, fill=PRIMARY, stroke=PRIMARY, r=20)
    p.text(X0 + 36, y + 34, 700, 40, "<b>Chào Minh, tiếp tục mở rộng vốn từ nhé!</b>", size=28, color=WHITE)
    p.text(X0 + 36, y + 82, 500, 22, "Bạn đã học <b>1,246 / 4,000</b> từ", size=14, color=WHITE)
    p.rect(X0 + 36, y + 114, 560, 10, fill="#2A4FC4", stroke="#2A4FC4", r=5)
    p.rect(X0 + 36, y + 114, 174, 10, fill=WHITE, stroke=WHITE, r=5)
    p.text(X0 + 604, y + 106, 60, 24, "31%", size=12, color=WHITE)
    p.rect(X0 + 36, y + 152, 170, 46, fill=WHITE, stroke=WHITE, r=10, value="<b>▶ Tiếp tục học</b>", color=PRIMARY, size=14)
    p.rect(X0 + 222, y + 152, 190, 46, fill=PRIMARY, stroke=WHITE, r=10, value="<b>↻ Ôn từ cần nhớ</b>", color=WHITE, size=14)
    p.rect(X0 + CW - 320, y + 24, 280, 182, fill="#2A4FC4", stroke="#2A4FC4", r=16, value="🦉 Mascot<br>(illustration)",
           color="#C7D2F0", size=14)
    y += 254
    p.zone(X0 - 36, y, "C")
    hw = (CW - 20) / 2
    p.card(X0, y, hw, 210, r=16)
    section_title(p, X0 + 20, y + 16, "Đang học")
    p.img(X0 + 20, y + 54, 150, 110, "Ảnh bộ từ")
    p.text(X0 + 186, y + 56, 300, 24, "<b>IELTS 5.0–6.0</b>", size=16)
    p.text(X0 + 186, y + 82, 380, 20, "Chủ đề đang học: <font color='#123AB5'>Sức khoẻ &amp; Wellbeing</font>", size=12, color=MUTED)
    p.progress(X0 + 186, y + 116, hw - 260, 60)
    p.text(X0 + 186, y + 128, 200, 20, "18/30 từ", size=12, color=MUTED)
    p.text(X0 + hw - 70, y + 108, 50, 20, "<b>60%</b>", size=12, align="right")
    p.btn(X0 + hw - 150, y + 154, 130, 38, "Học tiếp ›", size=13)
    rx = X0 + hw + 20
    p.card(rx, y, hw, 210, r=16)
    section_title(p, rx + 20, y + 16, "Trình độ hiện tại")
    cefr_badge(p, rx + 30, y + 60, "B1")
    p.text(rx + 180, y + 74, 300, 20, "Tương đương", size=12, color=MUTED)
    p.text(rx + 180, y + 96, 300, 26, "<b>IELTS 4.0–5.0</b>", size=17)
    p.btn(rx + 180, y + 136, 150, 38, "↗ Kiểm tra lại", kind="secondary", size=13)
    y += 234
    p.zone(X0 - 36, y, "D")
    lw = CW - 420
    p.card(X0, y, lw, 330, r=16)
    section_title(p, X0 + 20, y + 16, "Khám phá bộ từ vựng")
    x = X0 + 20
    for i, tab in enumerate(("Theo band điểm", "Theo chủ đề", "Oxford 3000 / 5000", "Collocations", "Sổ tay")):
        x = p.chip(x, y + 54, tab, kind="solid" if i == 0 else "neutral", size=12)
    tw = (lw - 60) / 3
    for i, (icon, name, meta, pct) in enumerate(SET_BANDS):
        tx, ty = X0 + 20 + (i % 3) * (tw + 10), y + 96 + (i // 3) * 112
        p.card(tx, ty, tw, 100, r=12)
        p.rect(tx + 12, ty + 14, 46, 46, fill=PRIMARY_SOFT, stroke=PRIMARY_SOFT, r=10, value=icon, size=20)
        p.text(tx + 70, ty + 12, tw - 90, 22, f"<b>{name}</b>", size=14)
        p.text(tx + 70, ty + 34, tw - 90, 18, meta, size=11, color=MUTED)
        p.progress(tx + 70, ty + 64, tw - 130, pct)
        p.text(tx + tw - 52, ty + 56, 40, 20, f"{pct}%", size=11, color=MUTED, align="right")
        p.text(tx + tw - 26, ty + 26, 20, 20, "›", size=16, color=MUTED)
    weekly_goal(p, X0 + lw + 20, y, 400)
    p.card(X0 + lw + 20, y + 206, 400, 124, r=16, fill=PRIMARY_SOFT)
    p.text(X0 + lw + 40, y + 222, 360, 24, "<b>✨ AI tạo bộ từ riêng</b>", size=15, color=PRIMARY)
    p.text(X0 + lw + 40, y + 250, 360, 40, "Nhập yêu cầu (chủ đề, band, số từ) để tạo bộ từ của bạn.", size=12, color=MUTED)
    p.chip(X0 + lw + 40, y + 292, "Giai đoạn sau (P3)", kind="outline", size=11)
    y += 354
    p.zone(X0 - 36, y, "E")
    p.card(X0, y, CW, 460, r=16)
    section_title(p, X0 + 24, y + 20, "Bản đồ từ vựng của bạn", 18)
    p.rect(X0 + 380, y + 16, 560, 40, fill=SOFT, stroke=LINE, r=20, size=13,
           value="▤ Trình độ hiện tại: <b>B1</b>      ◎ Cần tập trung: <b>B1 – còn 530 từ</b>")
    p.btn(X0 + CW - 220, y + 16, 196, 40, "Xem bản đồ chi tiết ›", size=13)
    p.text(X0 + 24, y + 70, 300, 20, "Đã học 1,246 / 4,000 từ", size=12, color=MUTED)
    p.progress(X0 + 200, y + 76, CW - 300, 31)
    p.text(X0 + CW - 80, y + 68, 56, 20, "<b>31%</b>", size=12, align="right")
    bw, gap = 110, (CW - 48 - 5 * 110) / 4
    for i, (lvl, done, total, l, r_, a) in enumerate(CEFR):
        bx, top, bh = X0 + 24 + i * (bw + gap), y + 136, 230
        current = lvl == "B1"
        if current:
            p.rect(bx - 16, top - 24, bw + 32, bh + 84, fill=SOFT, stroke=LINE, r=12)
        p.text(bx, top - 22, bw, 18, f"{done}/{total}", size=11, color=MUTED, align="center")
        p.rect(bx, top, bw, bh, fill=TODO, stroke=TODO, r=14)
        y0 = top + bh
        for share, color in ((l, LEARNED), (r_, REVIEWING), (a, AGAIN)):
            seg = bh * share
            p.rect(bx, y0 - seg, bw, seg, fill=color, stroke=color, r=0)
            y0 -= seg
        p.text(bx, top + bh + 8, bw, 22, f"<b>{lvl}</b>", size=14, align="center")
        if current:
            p.chip(bx + 2, top + bh + 34, "Trình độ hiện tại", kind="solid", size=10, w=bw - 4)
    map_legend(p, X0 + CW / 2 - 290, y + 424)
    footer(p, h - 64)
    return p


# ------------------------------------------------------------------ P-57 Word Detail
def word_header(p, y, tab):
    p.card(X0, y, MAIN_W, 940 if tab == "Định nghĩa" else 760, r=16)
    p.text(X0 + 24, y + 22, 300, 40, "<b>sustainable</b>", size=30)
    p.text(X0 + 240, y + 30, 420, 26, "UK /səˈsteɪ.nə.bəl/ 🔊    US /səˈsteɪ.nə.bəl/ 🔊", size=13, color=MUTED)
    p.chip(X0 + 24, y + 70, "OPAL Written", kind="active", size=11)
    p.chip(X0 + 140, y + 70, "formal", kind="outline", size=11)
    p.chip(X0 + 214, y + 70, "IELTS 6.0", kind="neutral", size=11)
    p.rect(X0 + 24, y + 104, MAIN_W - 48, 70, fill=SOFT, stroke=LINE, r=12)
    cols = [("Loại từ", "adjective"), ("CEFR", "B2"), ("Nghĩa (Anh – Việt)", "bền vững; có thể duy trì lâu dài"), ("Chủ đề", "Environment")]
    cx = X0 + 40
    for label, val in cols:
        w = 220 if label.startswith("Nghĩa") else 100
        p.text(cx, y + 112, w, 18, label, size=11, color=MUTED)
        p.text(cx, y + 134, w, 24, f"<b>{val}</b>", size=13, color=PRIMARY if label != "Nghĩa (Anh – Việt)" else INK)
        cx += w + 14
    p.btn(X0 + MAIN_W - 176, y + 120, 140, 38, "🔖 Lưu vào sổ từ", kind="secondary", size=12)
    tx = X0 + 24
    for name, n in (("Định nghĩa", 2), ("Collocations", 34), ("Thesaurus", 18), ("Idioms", 12), ("Examples", 42)):
        w = len(name) * 8 + 50
        on = name == tab
        p.text(tx, y + 192, w, 30, f"{'<b>' if on else ''}{name} <font color='#6B7280'>{n}</font>{'</b>' if on else ''}",
               size=14, color=PRIMARY if on else INK)
        if on:
            p.rect(tx, y + 222, w - 10, 3, fill=PRIMARY, stroke=PRIMARY, r=1)
        tx += w + 16
    p.rect(X0 + 24, y + 226, MAIN_W - 48, 1, fill=LINE, stroke=LINE, r=0)
    return y + 246


def word_side(p, y):
    p.card(SIDE_X, y, SIDE_W, 220, r=16)
    p.text(SIDE_X + 20, y + 14, 300, 24, "<b>Hình ảnh ghi nhớ</b> ⓘ", size=14)
    p.img(SIDE_X + 20, y + 46, SIDE_W - 40, 156, "Ảnh minh hoạ (Gen AI)")
    y += 236
    p.card(SIDE_X, y, SIDE_W, 120, r=16)
    p.text(SIDE_X + 20, y + 14, 300, 24, "<b>Mức độ hiểu từ</b> ⓘ", size=14)
    step = (SIDE_W - 40) / 4
    for i, (icon, label) in enumerate((("?", "Chưa biết"), ("🔖", "Mới biết"), ("▢", "Đang học"), ("✓", "Đã nhớ"))):
        on = label == "Đang học"
        p.rect(SIDE_X + 20 + i * step, y + 48, step - 8, 58, fill=PRIMARY_SOFT if on else WHITE, stroke=PRIMARY if on else "none",
               r=10, value=f"{icon}<br>{label}", size=11, color=PRIMARY if on else MUTED, bold=on)
    y += 136
    p.card(SIDE_X, y, SIDE_W, 250, r=16)
    p.text(SIDE_X + 20, y + 14, 300, 24, "<b>Thông tin nhanh</b> ⓘ", size=14)
    for i, (k, v) in enumerate((("Frequency (COCA)", "★★★★☆  6,120"), ("CEFR", "B2"), ("IELTS Level", "6.0"),
                                ("Academic Word List", "Có"), ("OPAL", "Written"), ("Chủ đề", "Environment"))):
        ry = y + 50 + i * 32
        p.text(SIDE_X + 20, ry, 200, 24, k, size=12, color=MUTED)
        p.text(SIDE_X + SIDE_W - 180, ry, 160, 24, f"<b>{v}</b>", size=12, align="right",
               color=PRIMARY if k in ("Chủ đề", "Academic Word List") else INK)
    y += 266
    p.card(SIDE_X, y, SIDE_W, 250, r=16)
    p.text(SIDE_X + 20, y + 14, 300, 24, "<b>Ghi chú của tôi</b> ⓘ", size=14)
    p.rect(SIDE_X + 20, y + 46, SIDE_W - 40, 80, fill=SOFT, stroke=LINE, r=8, value="Thêm ghi chú hoặc ví dụ của bạn…",
           color=MUTED, size=12, align="left", valign="top")
    p.text(SIDE_X + SIDE_W - 80, y + 128, 60, 18, "0/300", size=11, color=MUTED, align="right")
    p.btn(SIDE_X + 20, y + 156, SIDE_W - 40, 44, "🔖 Lưu và học từ này", size=14)
    p.text(SIDE_X, y + 210, SIDE_W, 22, "<font color='#F97316'>◷ Ôn từ này sau</font>", size=13, align="center")


def p57_definition(f):
    h = 1420
    p, y = dict_page(f, "P-57", "Định nghĩa", "Word Detail", h)
    y = crumb(p, y, "Từ điển", "Tra cứu từ")
    p.text(X0, y, 800, 40, "<b>Từ điển của bạn</b>", size=28)
    y = search_bar(p, y + 50, "sustainable", ("sustainability", "sustain", "sustained", "sustainable development", "unsustainable"), "Gợi ý:")
    p.zone(X0 - 36, y, "A")
    p.zone(SIDE_X - 30, y, "B")
    word_side(p, y)
    cy = word_header(p, y, "Định nghĩa")
    for i, (head, en, note, ex, vi) in enumerate((
            ("1. bền vững; có thể duy trì lâu dài", "Able to continue for a long time without causing harm to the environment or people.",
             "Ngữ pháp &amp; cách dùng · thường đứng trước danh từ", "We need to find sustainable solutions to the world's food problems.",
             "Chúng ta cần tìm ra các giải pháp bền vững cho vấn đề lương thực của thế giới."),
            ("2. (về môi trường) có khả năng duy trì theo thời gian", "Relating to the protection of the environment and the wise use of natural resources.",
             "", "Sustainable practices help reduce pollution and preserve natural resources.",
             "Các thực hành bền vững giúp giảm ô nhiễm và bảo tồn tài nguyên thiên nhiên."))):
        p.text(X0 + 24, cy, MAIN_W - 48, 24, f"<b><font color='#123AB5'>{head}</font></b>", size=15)
        p.text(X0 + 24, cy + 26, MAIN_W - 48, 22, en, size=13)
        oy = cy + 52
        if note:
            nx = p.chip(X0 + 24, oy, "Ngữ pháp & cách dùng", kind="active", size=10, w=150)
            p.text(nx + 4, oy, 400, 24, "thường đứng trước danh từ", size=12, color=MUTED)
            oy += 32
        p.text(X0 + 24, oy, MAIN_W - 48, 44, f"🔊 <b>{ex}</b><br><font color='#6B7280'>{vi}</font>", size=12, valign="top")
        cy = oy + 64
    p.rect(X0 + 24, cy, MAIN_W - 48, 1, fill=LINE, stroke=LINE, r=0)
    for title, body in (("Word family", "sustain (v), sustainability (n), sustainably (adv), unsustainable (adj)"),
                        ("Lỗi thường gặp", "✗ <s>sustainable for the environment</s> → ✓ sustainable development / sustainable growth"),
                        ("Ghi chú sử dụng", "Thường dùng trong ngữ cảnh học thuật và chính sách môi trường (formal).")):
        cy += 18
        p.text(X0 + 24, cy, 300, 22, f"<b>{title}</b>", size=14)
        p.text(X0 + 24, cy + 26, MAIN_W - 48, 22, body, size=12, color=MUTED)
        cy += 52
    p.text(X0 + 24, cy + 18, 300, 22, "<b>Chủ đề liên quan</b>", size=14)
    x = X0 + 24
    for t in ("environment", "climate change", "renewable energy", "conservation", "green living"):
        x = p.chip(x, cy + 48, t, kind="active", size=11)
    p.link(X0 + MAIN_W - 220, y + 900, 200, "Tiếp theo: Collocations ›", size=13, align="right")
    footer(p, h - 64)
    return p


def p57_thesaurus(f):
    h = 1240
    p, y = dict_page(f, "P-57", "Thesaurus", "Word Detail", h)
    y = crumb(p, y, "Từ điển", "Tra cứu từ")
    p.text(X0, y, 800, 40, "<b>Từ điển của bạn</b>", size=28)
    y = search_bar(p, y + 50, "sustainable", ("sustainability", "sustain", "sustained"), "Gợi ý:")
    p.zone(X0 - 36, y, "A")
    word_side(p, y)
    cy = word_header(p, y, "Thesaurus")
    for title, words, kind in (("Từ đồng nghĩa và gần nghĩa (Synonyms)", ("viable", "renewable", "maintainable", "lasting",
                                                                         "eco-friendly", "green", "long-term"), "active"),
                               ("Từ trái nghĩa và gần trái nghĩa (Antonyms)", ("unsustainable", "harmful", "short-term",
                                                                              "wasteful", "destructive"), "outline")):
        p.text(X0 + 24, cy, 500, 24, f"<b>{title}</b>", size=14)
        x, row = X0 + 24, cy + 32
        for w in words:
            nx = p.chip(x, row, w, kind=kind, size=12)
            x = nx
        cy += 84
    p.text(X0 + 24, cy, MAIN_W - 48, 22, "<b>Collocations phổ biến</b> (ozdic)", size=14)
    for i, c in enumerate(("sustainable development", "sustainable growth", "environmentally sustainable", "sustainable tourism")):
        p.rect(X0 + 24 + (i % 2) * 390, cy + 32 + (i // 2) * 46, 376, 38, fill=SOFT, stroke=LINE, r=8, value=c, size=13, align="left")
    p.text(X0 + 24, cy + 140, MAIN_W - 48, 40, "Nguồn: Collins / Merriam-Webster (thesaurus), ozdic (collocations). "
           "Câu dài nhập vào ô tra từ được dịch bằng AI (P2).", size=11, color=MUTED, italic=True, valign="top")
    footer(p, h - 64)
    return p


# ------------------------------------------------------------------ P-58 Vocabulary Map
def p58(f):
    per_row, cell, gap = 36, 22, 4
    rows_total = sum((total // 10 + per_row - 1) // per_row for *_, total, _l, _r, _a in
                     [(lvl, done, total, l, r_, a) for lvl, done, total, l, r_, a in CEFR])
    card_h = 186 + rows_total * (cell + gap) + len(CEFR) * 40 + 60
    top = 72 + 44 + 24 + 36
    h = top + card_h + 90
    p, y = dict_page(f, "P-58", "Populated", "Vocabulary Map", h)
    y = crumb(p, y, "Từ vựng", "Bản đồ từ vựng")
    p.card(X0, y, CW, card_h, r=20)
    p.rect(X0 + 28, y + 28, 52, 52, fill=INK, stroke=INK, r=26, value="<b>TES</b>", size=12, color=WHITE)
    p.text(X0 + 96, y + 26, 600, 34, "<b>Bản đồ từ vựng</b>", size=26)
    p.text(X0 + 96, y + 62, 760, 20, "Mỗi ô vuông = 10 từ. Tô màu để hiển thị tiến độ học tập. Rê chuột vào ô để xem từ.",
           size=13, color=MUTED)
    p.rect(X0 + 28, y + 100, CW - 56, 56, fill=SOFT, stroke=LINE, r=12)
    p.text(X0 + 48, y + 100, 300, 56, "↗  Đã học <b>1,246</b> / 4,000 từ", size=14)
    p.progress(X0 + 360, y + 124, CW - 500, 31)
    p.text(X0 + CW - 120, y + 112, 80, 30, "<b>31%</b>", size=15, color=PRIMARY, align="right")
    gy = y + 186
    p.zone(X0 - 36, gy, "A")
    hover = None
    for lvl, done, total, l, r_, a in CEFR:
        n = total // 10
        rows = (n + per_row - 1) // per_row
        p.text(X0 + 28, gy, 60, 24, f"<b>{lvl}</b>", size=17)
        p.text(X0 + 28, gy + 26, 80, 18, f"{total:,} từ".replace(",", "."), size=11, color=MUTED)
        states = [LEARNED] * round(n * l) + [REVIEWING] * round(n * r_) + [AGAIN] * round(n * a)
        states += [TODO] * (n - len(states))
        for k, color in enumerate(states):
            cx = X0 + 120 + (k % per_row) * (cell + gap)
            cy = gy + (k // per_row) * (cell + gap)
            p.rect(cx, cy, cell, cell, fill=color, stroke=color, r=3)
            if lvl == "A2" and k == len(states) - n + round(n * l) + 1 and hover is None:
                hover = (cx, cy)
        p.text(X0 + CW - 200, gy, 150, 20, f"{done}/{total:,} từ".replace(",", "."), size=12, color=MUTED, align="right")
        p.text(X0 + CW - 200, gy + 22, 150, 26, f"<b>{round(done / total * 100)}%</b>", size=17, color=PRIMARY, align="right")
        p.text(X0 + CW - 44, gy + 4, 20, 20, "⌄", size=14, color=MUTED)
        gy += rows * (cell + gap) + 40
        p.rect(X0 + 28, gy - 20, CW - 56, 1, fill=LINE, stroke=LINE, r=0)
    ax, ay = hover
    p.rect(ax - 2, ay - 2, cell + 4, cell + 4, fill="none", stroke=INK, r=4, sw=2)
    p.card(ax - 110, ay + 30, 270, 156, r=12)
    p.text(ax - 94, ay + 40, 240, 22, "🔊 <b>sustainable</b>", size=14)
    p.text(ax - 94, ay + 62, 240, 18, "/səˈsteɪ.nə.bəl/", size=11, color=MUTED)
    p.text(ax - 94, ay + 84, 240, 34, "Nghĩa:<br><b>Bền vững</b>", size=12, valign="top")
    p.btn(ax - 94, ay + 136, 112, 34, "▭ Flashcard", kind="secondary", size=12)
    p.btn(ax + 28, ay + 136, 116, 34, "✎ Luyện tập", size=12)
    map_legend(p, X0 + 40, gy)
    footer(p, h - 64)
    return p


# ------------------------------------------------------------------ P-59 Vocabulary Set
TOPICS = [("🧬", "Bản sắc &amp; Các thế hệ", 30, 100, "Hoàn thành"), ("🎓", "Lựa chọn giáo dục", 30, 60, "Đang học"),
          ("💼", "Nghề nghiệp &amp; Việc làm", 35, 34, "Đang học"), ("❤", "Sức khoẻ &amp; Wellbeing", 30, 10, "Đang học"),
          ("♻", "Tái chế &amp; Rác thải", 40, 0, "Chưa học")]


def p59(f):
    h = 1560
    p, y = dict_page(f, "P-59", "Tổng quan", "Vocabulary Set", h)
    y = crumb(p, y, "Từ vựng", "Theo band điểm", "IELTS 5.0–6.0")
    p.rect(X0 + CW - 300, y - 40, 300, 34, fill=WHITE, stroke=LINE, r=17, value="⌕  Tra nhanh từ vựng…", size=12, color=MUTED, align="left")
    mw = MAIN_W
    p.zone(X0 - 36, y, "A")
    p.card(X0, y, mw, 230, r=16)
    p.img(X0 + 20, y + 20, 220, 150, "Ảnh bìa bộ từ")
    p.text(X0 + 260, y + 20, 360, 30, "<b>IELTS 5.0–6.0</b>", size=22)
    p.text(X0 + 260, y + 54, 360, 40, "Phát triển vốn từ học thuật và collocations cần thiết để hướng tới band 6.0.", size=12, color=MUTED, valign="top")
    for i, c in enumerate(("📖 1.200 từ", "▤ 12 chủ đề", "↗ Trình độ B1–B2", "◷ Khoảng 10 tuần")):
        p.chip(X0 + 260 + (i % 2) * 140, y + 96 + (i // 2) * 30, c, kind="neutral", size=11, w=130)
    p.text(X0 + 260, y + 160, 360, 20, "<b>Đã học 610/1.200 từ — 51%</b>", size=12)
    p.progress(X0 + 260, y + 186, 360, 51)
    for i, (n, label, icon, color) in enumerate((("386", "Đã thành thạo", "✓", "#16A34A"), ("224", "Đang học", "▢", PRIMARY),
                                                 ("42", "Cần ôn", "◷", ORANGE))):
        p.card(X0 + mw - 150, y + 14 + i * 70, 130, 62, r=12)
        p.text(X0 + mw - 150, y + 16 + i * 70, 130, 60, f"<font color='{color}'>{icon}</font> <b>{n}</b><br>"
               f"<font style='font-size:11px' color='#6B7280'>{label}</font>", size=17, align="center")
    y += 246
    p.btn(X0, y, 360, 48, "▶ Tiếp tục học", size=15)
    p.btn(X0 + 380, y, 200, 48, "↻ Ôn từ cần nhớ", kind="secondary", size=14)
    y += 68
    p.zone(X0 - 36, y, "B")
    tx = X0
    for i, t in enumerate(("Tổng quan", "Chủ đề", "Tất cả từ vựng", "Tiến độ")):
        w = len(t) * 8 + 30
        p.text(tx, y, w, 30, f"<b>{t}</b>" if i == 0 else t, size=14, color=PRIMARY if i == 0 else INK)
        if i == 0:
            p.rect(tx, y + 30, w - 10, 3, fill=PRIMARY, stroke=PRIMARY, r=1)
        tx += w + 20
    p.text(X0 + mw - 120, y, 120, 30, "🔖 Lưu bộ từ", size=13, align="right")
    p.rect(X0, y + 34, mw, 1, fill=LINE, stroke=LINE, r=0)
    y += 54
    section_title(p, X0, y, "1. Tiếp tục lộ trình", 15)
    p.card(X0, y + 32, mw, 120, r=14)
    p.img(X0 + 16, y + 46, 150, 92, "Ảnh chủ đề")
    p.text(X0 + 184, y + 48, 400, 24, "<b>Sức khoẻ &amp; Wellbeing</b>", size=16)
    p.chip(X0 + 400, y + 50, "Đang học", kind="active", size=10)
    p.progress(X0 + 184, y + 86, 300, 60)
    p.text(X0 + 494, y + 78, 120, 20, "18/30 từ · 60%", size=11, color=MUTED)
    p.text(X0 + 184, y + 106, 450, 20, "▢ Bài tiếp theo: Collocations về Wellbeing", size=12, color=MUTED)
    p.btn(X0 + mw - 150, y + 72, 130, 40, "Học tiếp ›", size=13)
    y += 176
    section_title(p, X0, y, "2. Các chủ đề trong bộ từ", 15)
    tw = (mw - 40) / 5
    for i, (icon, name, n, pct, state) in enumerate(TOPICS):
        tx = X0 + i * (tw + 10)
        p.rect(tx, y + 34, tw, 70, fill=PRIMARY_SOFT if state != "Chưa học" else SOFT, stroke=LINE, r=12, value=icon, size=24)
        p.text(tx, y + 110, tw, 34, f"<b>{name}</b>", size=12, valign="top")
        p.text(tx, y + 144, tw, 18, f"{n} từ", size=11, color=MUTED)
        p.progress(tx, y + 168, tw - 40, pct, h=6)
        p.text(tx + tw - 38, y + 162, 38, 18, f"{pct}%", size=10, color=MUTED, align="right")
        p.chip(tx, y + 186, state, kind="active" if state == "Đang học" else "neutral", size=10)
    p.link(X0 + mw / 2 - 100, y + 222, 200, "Xem tất cả 12 chủ đề ›", size=13, align="center")
    y += 260
    section_title(p, X0, y, "3. Từ vựng gần đây", 15)
    p.rect(X0, y + 32, mw, 36, fill=SOFT, stroke=LINE, r=8)
    heads = (("Từ vựng", 200), ("Nghĩa", 240), ("Chủ đề", 200), ("Trạng thái", 180))
    hx = X0
    for label, w in heads:
        p.text(hx + 14, y + 32, w, 36, f"<b>{label}</b>", size=12, color=MUTED)
        hx += w
    for r, (word, vi, topic, state) in enumerate((("identity", "bản sắc", "Bản sắc &amp; Các thế hệ", "Đã nhớ"),
                                                  ("curriculum", "chương trình học", "Lựa chọn giáo dục", "Đang học"),
                                                  ("redundancy", "sự sa thải", "Nghề nghiệp &amp; Việc làm", "Cần ôn"),
                                                  ("wellbeing", "sự khoẻ mạnh, hạnh phúc", "Sức khoẻ &amp; Wellbeing", "Đang học"))):
        ry = y + 74 + r * 40
        p.rect(X0, ry, mw, 36, fill=WHITE, stroke=LINE, r=6)
        hx = X0
        for c, (val, (_, w)) in enumerate(zip((word, vi, topic, state), heads)):
            if c == 3:
                p.chip(hx + 14, ry + 6, val, kind="active" if val == "Đang học" else "neutral", size=10)
            else:
                p.text(hx + 14, ry, w - 20, 36, f"<b><font color='#123AB5'>{val}</font></b>" if c == 0 else val, size=12)
            hx += w
    p.link(X0 + mw / 2 - 100, y + 240, 200, "Xem toàn bộ 1.200 từ ›", size=13, align="center")
    y += 280
    p.rect(X0, y, mw, 80, fill=PRIMARY_SOFT, stroke=PRIMARY_SOFT, r=14)
    p.text(X0 + 24, y + 12, 500, 56, "🚀 <b>Sẵn sàng học tiếp?</b><br><font color='#6B7280'>Còn 12 từ trong chủ đề Sức khoẻ "
           "&amp; Wellbeing hôm nay. Từ đã học được tự loại khỏi phần học.</font>", size=13, valign="top")
    p.btn(X0 + mw - 220, y + 18, 196, 44, "▶ Bắt đầu học 12 từ", size=14)
    # right column
    ry = 72 + 44 + 24 + 36
    p.zone(SIDE_X - 30, ry, "C")
    weekly_goal(p, SIDE_X, ry, SIDE_W)
    ry += 206
    p.card(SIDE_X, ry, SIDE_W, 150, r=16)
    p.text(SIDE_X + 20, ry + 14, 300, 24, "<b>Kết quả gần nhất</b>", size=14)
    cefr_badge(p, SIDE_X + 24, ry + 48, "88%", d=86)
    p.text(SIDE_X + 130, ry + 52, 240, 80, "Chủ đề<br><b>Lựa chọn giáo dục</b><br>27/30 câu đúng<br>"
           "<u><font color='#123AB5'>Xem kết quả ›</font></u>", size=12, valign="top")
    ry += 166
    p.card(SIDE_X, ry, SIDE_W, 220, r=16)
    p.text(SIDE_X + 20, ry + 14, 300, 24, "<b>Cách học đề xuất</b>", size=14)
    for i, (t, d) in enumerate((("Học từ mới", "Flashcard, nghe phát âm và ví dụ"), ("Luyện tập", "Điền từ, dịch từ, nối từ với nghĩa (học trộn)"),
                                ("Ôn theo lịch", "Ôn định kỳ để ghi nhớ lâu dài"))):
        p.cell(str(i + 1), "ellipse;whiteSpace=wrap;html=1;fillColor=#123AB5;strokeColor=#123AB5;fontColor=#FFFFFF;fontSize=12;",
               SIDE_X + 20, ry + 52 + i * 54, 26, 26)
        p.text(SIDE_X + 58, ry + 48 + i * 54, SIDE_W - 80, 44, f"<b>{t}</b><br><font color='#6B7280'>{d}</font>", size=12, valign="top")
    ry += 236
    p.card(SIDE_X, ry, SIDE_W, 140, r=16)
    p.text(SIDE_X + 20, ry + 14, 300, 24, "<b>Thành tích bộ từ</b>", size=14)
    for i, (icon, label) in enumerate((("📗", "Học 7 ngày"), ("🏅", "Hoàn thành 5 chủ đề"), ("🔥", "300 từ thành thạo"))):
        p.text(SIDE_X + 20 + i * 120, ry + 50, 110, 76, f"<font style='font-size:24px'>{icon}</font><br>{label}", size=11,
               color=MUTED, align="center", valign="top")
    footer(p, h - 64)
    return p


# ------------------------------------------------------------------ P-59a Set Study session
MODES = ("Flashcard", "Điền từ", "Dịch từ", "Nối từ", "Học trộn", "Game")


def study_page(f, frame, mode, h=980):
    p, y = dict_page(f, "P-59a", frame, "Set Study", h)
    p.rect(0, y - 24, DESKTOP_W, 60, fill=WHITE, stroke=LINE, r=0)
    p.btn(X0 - 60, y - 12, 110, 36, "← Thoát", kind="secondary", size=13)
    p.text(X0 + 70, y - 12, 520, 36, "<b>IELTS 5.0–6.0 · Sức khoẻ &amp; Wellbeing</b>", size=15)
    p.text(X0 + 640, y - 12, 140, 36, "Từ 5 / 12", size=13, color=MUTED)
    p.progress(X0 + 760, y + 2, 360, 40)
    y += 56
    p.zone(X0 - 36, y, "A")
    x = X0 + 200
    for m in MODES:
        x = p.chip(x, y, m, kind="solid" if m == mode else "neutral", size=12, w=118)
    return p, y + 50


def p59a_mixed(f):
    h = 980
    p, y = study_page(f, "Học trộn — Điền từ", "Học trộn", h)
    p.zone(X0 - 36, y, "B")
    cx, cw = X0 + 170, 900
    p.card(cx, y, cw, 470, r=20)
    p.chip(cx + 24, y + 22, "Câu 6/12 · Điền từ", kind="active", size=12)
    p.text(cx + 24, y + 64, cw - 48, 60, "Regular exercise and enough sleep are essential for your mental ______.", size=20)
    p.text(cx + 24, y + 126, cw - 48, 22, "Gợi ý: (n) trạng thái khoẻ mạnh, hạnh phúc", size=13, color=MUTED)
    for i, opt in enumerate(("wellbeing", "welfare", "wealth", "willpower")):
        on = i == 0
        p.rect(cx + 24 + (i % 2) * 432, y + 170 + (i // 2) * 70, 420, 56, fill=PRIMARY_SOFT if on else WHITE,
               stroke=PRIMARY if on else LINE, r=12, sw=2 if on else 1, value=f"<b>{chr(65 + i)}</b>   {opt}", size=15, align="left")
    p.rect(cx + 24, y + 324, cw - 48, 60, fill="#ECFDF5", stroke="#16A34A", r=12, align="left", size=13,
           value="✓ <b>Chính xác!</b> mental wellbeing — sức khoẻ tinh thần.  🔊 Nghe lại câu")
    p.btn(cx + cw - 200, y + 404, 176, 46, "Câu tiếp ›", size=14)
    p.text(cx, y + 490, cw, 40, "Học trộn xen kẽ Flashcard · Điền từ · Dịch từ · Nối từ với nghĩa. Từ trả lời sai được đưa vào "
           "\"Cần ôn\"; từ đã thành thạo không xuất hiện lại.", size=12, color=MUTED, italic=True, align="center")
    footer(p, h - 64)
    return p


def build(new):
    f = new("P-56_DictionaryHome")
    p56(f)
    f.save()
    f = new("P-57_WordDetail")
    p57_definition(f)
    p57_thesaurus(f)
    f.save()
    f = new("P-58_VocabularyMap")
    p58(f)
    f.save()
    f = new("P-59_VocabularySet")
    p59(f)
    f.save()
    import screens_flashcard_sets as sets
    f = new("P-59a_SetStudy")
    sets.p59a_flashcard(f)
    p59a_mixed(f)
    sets.p59a_translate(f)
    sets.p59a_match(f)
    sets.p59a_game(f)
    f.save()
