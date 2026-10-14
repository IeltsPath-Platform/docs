"""Wireframes (design target): vocabulary lessons — Topic Lesson Path (P-59b), the SPACE vocabulary lesson (P-59c),
the two-mode flashcard of F045 with its effects (P-59d), and the Flashcard tab of the class Lesson Workspace (P-21).

F045 (Feature Master, P0): "Flashcard 2 chế độ — giản lược và đầy đủ; IPA, audio, hình, nghĩa, ví dụ…", output
attempt / answer / time. Giản lược = word, IPA, audio and short meaning; Đầy đủ = adds the memory image, tag, part
of speech, example with translation. Layout follows the reference screens inside the IELTS Space chrome.
"""
from wf import PRIMARY, PRIMARY_SOFT, INK, MUTED, LINE, SOFT, CANVAS, DARK, MEDIA
from chrome import navbar, footer, screen, DESKTOP_W

X0, CW = 100, 1240
WHITE = "#FFFFFF"
ORANGE = "#F97316"
CARD_BLUE = "#2F5BEA"
GREEN, GREEN_SOFT, RED, RED_SOFT = "#16A34A", "#ECFDF5", "#DC2626", "#FEF2F2"
PHRASE = "A breath of fresh air"
TOPIC = "Hành động khí hậu &amp; Năng lượng"
SPACE = [("S", "Scope", "Khám phá bộ từ"), ("P", "Probe", "Đoán nghĩa"), ("A", "Assemble", "Luyện nhớ"),
         ("C", "Communicate", "Đặt câu"), ("E", "Evaluate", "Kiểm tra")]


def card_style(fill, gradient=None, shadow=False, stroke="none", sw=1):
    st = (f"rounded=1;arcSize=18;absoluteArcSize=1;whiteSpace=wrap;html=1;fillColor={fill};strokeColor={stroke};"
          f"strokeWidth={sw};fontFamily=Arial;")
    if gradient:
        st += f"gradientColor={gradient};gradientDirection=east;"
    if shadow:
        st += "shadow=1;"
    return st


def owl(p, x, y, w=80, h=80, label="🦉"):
    size = int(w * 0.42) if len(label) <= 2 else min(int(w * 0.2), 34)  # emoji alone vs emoji + caption
    p.rect(x, y, w, h, fill=PRIMARY_SOFT, stroke=PRIMARY_SOFT, r=w // 2, value=label.replace(" ", "<br>", 1), size=size)


def audio_dot(p, x, y, d=34, dark=True):
    p.cell("🔊", "ellipse;whiteSpace=wrap;html=1;fontSize=14;" + ("fillColor=#5B7DF0;strokeColor=none;" if dark else
           "fillColor=#E8EDFB;strokeColor=none;"), x, y, d, d)


def flashcard(p, x, y, w, h, side="front", mode="full", effect=None, phrase=PHRASE, ipa="/ə breθ əv freʃ eər/",
              meaning="Một hơi thở không khí trong lành / một làn gió mới", image="Ảnh minh hoạ"):
    """F045 flashcard. side front/back · mode full/simple · effect None/hover/pressed/flipping."""
    if effect == "flipping":  # mid-turn (rotateY ≈ 90°): the card is seen edge-on, narrow and shaded
        nw = int(w * 0.18)
        p.cell("", card_style("#1E3A8A", gradient=CARD_BLUE, shadow=True), x + (w - nw) / 2, y + 12, nw, h - 24)
        p.text(x, y + h / 2 - 12, w, 24, "↻", size=22, color=MUTED, align="center")
        p.text(x, y + h + 6, w, 20, "Đang lật… rotateY 0° → 180° · 400 ms ease-in-out", size=11, color=MUTED, italic=True,
               align="center")
        return
    fill = {"hover": PRIMARY, "pressed": "#0D2B8D"}.get(effect, CARD_BLUE)
    p.cell("", card_style(fill, gradient=ORANGE if effect == "hover" else None, shadow=effect in ("hover", "pressed")),
           x, y, w, h)
    tag = "MẶT TRƯỚC" if side == "front" else "MẶT SAU"
    p.rect(x + 20, y + 18, 84, 22, fill="#4A6FF0", stroke="none", r=11, value=f"<b>{tag}</b>", size=10, color=WHITE)
    if side == "front":
        img_w = int(w * 0.36) if mode == "full" else 0
        tw = w - 40 - (img_w + 20 if img_w else 0)
        p.text(x + 20, y + 52, tw, 44, f"<b>{phrase}</b>", size=min(32, int(w / 16)), color=WHITE)
        audio_dot(p, x + 20, y + 106)
        p.text(x + 20, y + 150, tw, 26, ipa, size=15, color=WHITE)
        if mode == "full":
            p.rect(x + 20, y + 182, 94, 22, fill="#1E3A8A", stroke="none", r=11, value="Cụm cố định", size=10, color=WHITE)
            p.img(x + w - img_w - 20, y + 52, img_w, h - 104, image)
        p.text(x, y + h - 34, w, 20, "nhấn để lật", size=11, color="#C7D2F0", align="center")
    else:
        p.text(x, y + 46, w, 34, f"<b>{phrase}</b>", size=min(26, int(w / 20)), color=WHITE, align="center")
        if mode == "full":
            p.rect(x + w / 2 - 22, y + 84, 44, 20, fill="#4A6FF0", stroke="none", r=10, value="Idiom", size=10, color=WHITE)
            p.text(x + 30, y + 112, w - 60, 40, "I stepped outside and took a breath of fresh air.<br>"
                   "<font color='#C7D2F0'><i>Tôi bước ra ngoài và hít thở bầu không khí trong lành.</i></font>",
                   size=12, color=WHITE, align="center", valign="top")
            audio_dot(p, x + w / 2 - 17, y + 160)
            my = y + 204
        else:
            audio_dot(p, x + w / 2 - 17, y + 92)
            my = y + 140
        p.text(x + 50, my, w - 100, 40, f"<b>{meaning}</b>", size=14, color=WHITE, align="center")
        p.text(x + 18, my + 6, 24, 24, "↻", size=16, color=WHITE, align="center")
        p.text(x, y + h - 30, w, 20, "nhấn để lật lại", size=11, color="#C7D2F0", align="center")
    if effect == "hover":
        p.text(x, y + h + 6, w, 20, "Hover: viền gradient xanh → cam, nổi bóng · 120 ms", size=11, color=MUTED, italic=True,
               align="center")
    elif effect == "pressed":
        p.text(x, y + h + 6, w, 20, "Nhấn giữ: nền tối hơn", size=11, color=MUTED, italic=True, align="center")


def vocab_page(f, pid, frame, title, h, crumbs):
    p = screen(f, pid, frame, title, h=h)
    y = navbar(p, role="learner", active="Sổ ghi nhớ", child="Học") + 22
    trail = "  /  ".join(list(crumbs[:-1]) + [f"<b><font color='#123AB5'>{crumbs[-1]}</font></b>"])
    p.text(X0, y, 900, 24, f"‹   {trail}", size=13, color=MUTED)
    return p, y + 36


# ------------------------------------------------------------------ P-59b Topic Lesson Path
LESSONS = [("Bài 1", "Thiên nhiên", "12 từ · Đã hoàn thành", "done"), ("Bài 2", "Ô nhiễm", "10 từ · Đã hoàn thành", "done"),
           ("Bài 3", "Bảo tồn", "10 từ · Đã hoàn thành", "done"),
           ("Bài 4", "Collocations", "renewable energy · reduce emissions · 5 cụm", "current"),
           ("Bài 5", "Kết nối", "Ôn và nối từ theo ngữ cảnh", "locked"),
           ("Bài 6", "Phát triển bền vững", "Từ vựng học thuật nâng cao", "locked")]


def p59b(f):
    h = 1360
    p, y = vocab_page(f, "P-59b", "Lộ trình bài học", "Topic Lesson Path", h, ("Từ vựng", "IELTS 6.0–7.0", TOPIC))
    p.rect(X0 + CW - 300, y - 40, 300, 34, fill=WHITE, stroke=LINE, r=17, value="⌕  Tra nhanh từ vựng…", size=12, color=MUTED, align="left")
    p.zone(X0 - 36, y, "A")
    p.card(X0, y, CW, 110, r=16)
    p.img(X0 + 20, y + 15, 150, 80, "Ảnh chủ đề")
    p.text(X0 + 190, y + 22, 600, 30, f"<b>{TOPIC}</b>", size=20)
    p.text(X0 + 190, y + 54, 500, 20, "Lộ trình học từ vựng · 6 bài · 1 bài ôn · 1 bài kiểm tra", size=13, color=MUTED)
    p.text(X0 + CW - 300, y + 30, 280, 20, "<b>18/30</b> từ đã học", size=13, align="right")
    p.progress(X0 + CW - 300, y + 58, 240, 60)
    p.text(X0 + CW - 52, y + 50, 40, 20, "60%", size=12, color=MUTED, align="right")
    y += 130
    p.zone(X0 - 36, y, "B")
    p.cell("", "rounded=1;arcSize=20;absoluteArcSize=1;fillColor=#EEF2FF;strokeColor=#C9CED6;gradientColor=#F9FAFB;"
           "gradientDirection=south;", X0, y, CW, 980)
    owl(p, X0 + 960, y + 40, 150, 150, "🦉🚀")
    owl(p, X0 + 60, y + 640, 130, 130, "🦉")
    xs = [470, 560, 470, 380, 470, 560]
    ids = []
    for i, ((n, name, meta, state), nx) in enumerate(zip(LESSONS, xs)):
        ny = y + 50 + i * 130
        cur = state == "current"
        w = 400 if cur else 300
        fill = PRIMARY if state != "locked" else WHITE
        cid = p.rect(X0 + nx, ny, w, 84 if cur else 70, fill=fill, stroke=ORANGE if cur else (PRIMARY if state != "locked" else LINE),
                     r=14, sw=3 if cur else 1, shadow=cur)
        ids.append(cid)
        icon = "✓" if state == "done" else ("▶" if cur else "🔒")
        p.cell(icon, "ellipse;whiteSpace=wrap;html=1;fontSize=14;" + ("fillColor=#16A34A;strokeColor=#FFFFFF;fontColor=#FFFFFF;"
               if state == "done" else "fillColor=#F97316;strokeColor=#FFFFFF;fontColor=#FFFFFF;" if cur else
               "fillColor=#F3F4F6;strokeColor=#C9CED6;fontColor=#6B7280;"), X0 + nx - 18, ny + 18, 36, 36)
        col = WHITE if state != "locked" else INK
        p.text(X0 + nx + 30, ny + 8, w - 140, 20, f"{n}", size=11, color="#C7D2F0" if state != "locked" else MUTED)
        p.text(X0 + nx + 30, ny + 26, w - 140, 24, f"<b>{name}</b>", size=16, color=col)
        p.text(X0 + nx + 30, ny + 48, w - 40, 20, meta, size=11, color="#C7D2F0" if state != "locked" else MUTED)
        if cur:
            p.chip(X0 + nx + w - 110, ny + 10, "Đang học", kind="solid", size=10, w=90)
            p.rect(X0 + nx + w - 110, ny + 42, 92, 30, fill=ORANGE, stroke=ORANGE, r=15, value="<b>Tiếp tục</b>", size=12, color=WHITE)
    for a, b in zip(ids, ids[1:]):
        p.edge(a, b, dashed=True, color=PRIMARY)
    review = p.rect(X0 + 820, y + 360, 200, 44, fill=WHITE, stroke=PRIMARY, r=22, dashed=True,
                    value="↻ Ôn tập giữa chặng", size=13, color=PRIMARY, bold=True)
    p.edge(ids[2], review, dashed=True, color=MUTED)
    final = p.rect(X0 + 500, y + 860, 240, 52, fill=WHITE, stroke=LINE, r=26, value="🔒  Kiểm tra cuối đề", size=14, color=MUTED, bold=True)
    p.edge(ids[-1], final, dashed=True, color=MUTED)
    p.text(X0 + 760, y + 870, 400, 40, "Mở khi xong 6 bài · 20 câu tổng hợp", size=12, color=MUTED, italic=True)
    footer(p, h - 64)
    return p


# ------------------------------------------------------------------ P-59c SPACE vocabulary lesson
def space_header(p, y, step):
    p.cell("", card_style(PRIMARY, gradient="#2A4FC4", shadow=True), X0, y, CW, 170)
    p.text(X0 + 28, y + 18, 600, 36, "<b>Từ vựng môi trường – Bài 4</b>", size=24, color=WHITE)
    p.rect(X0 + 380, y + 24, 104, 24, fill="#4A6FF0", stroke="none", r=12, value="IELTS 6.0–7.0", size=11, color=WHITE, bold=True)
    p.text(X0 + 28, y + 56, 400, 22, "🌱 Chu trình SPACE", size=13, color="#C7D2F0")
    idx = [s[0] for s in SPACE].index(step)
    p.text(X0 + CW - 340, y + 22, 120, 22, f"Bước {idx + 1}/5", size=13, color=WHITE, align="right")
    p.rect(X0 + CW - 210, y + 30, 150, 8, fill="#2A4FC4", stroke="none", r=4)
    p.rect(X0 + CW - 210, y + 30, 30 * (idx + 1), 8, fill=WHITE, stroke="none", r=4)
    p.text(X0 + CW - 52, y + 22, 40, 22, f"{(idx + 1) * 20}%", size=12, color=WHITE, align="right")
    p.rect(X0 + 60, y + 115, CW - 120, 2, fill="#5B7DF0", stroke="none", r=0)
    p.text(X0 + 34, y + 104, 24, 24, "🚀", size=15, align="center")
    p.text(X0 + CW - 58, y + 104, 24, 24, "🚀", size=15, align="center")
    step_w = (CW - 200) / 4
    for i, (letter, en, vi) in enumerate(SPACE):
        cx = X0 + 100 + i * step_w
        cur, done = i == idx, i < idx
        p.cell(f"<b>{letter}</b>", "ellipse;whiteSpace=wrap;html=1;fontSize=16;fontFamily=Arial;" +
               ("fillColor=#F97316;strokeColor=#FFFFFF;strokeWidth=3;fontColor=#FFFFFF;" if cur else
                "fillColor=#FFFFFF;strokeColor=#FFFFFF;fontColor=#123AB5;" if done else
                "fillColor=#FFFFFF;strokeColor=#C9CED6;fontColor=#123AB5;"), cx - 22, y + 94, 44, 44)
        p.text(cx - 80, y + 140, 160, 18, f"<b>{letter} – {en}</b>", size=11, color=WHITE, align="center")
        p.text(cx - 80, y + 154, 160, 16, vi, size=10, color="#C7D2F0", align="center")
        if cur:
            p.text(cx - 16, y + 62, 32, 30, "🦉", size=22, align="center")
    return y + 190


def lesson_page(f, frame, step, h=1080):
    p, y = vocab_page(f, "P-59c", frame, "Vocabulary Lesson", h, ("Từ vựng", TOPIC, "Bài 4: Collocations"))
    p.zone(X0 - 36, y, "A")
    return p, space_header(p, y, step)


def exercise_card(p, y, h, chip, title, sub, counter="Câu 1/5", owl_label="🦉"):
    p.zone(X0 - 36, y, "B")
    cx, cw = X0 + 120, CW - 240
    p.card(cx, y, cw, h, r=18)
    owl(p, cx + 24, y + 22, 76, 76, owl_label)
    p.rect(cx + 116, y + 26, 120, 22, fill=ORANGE, stroke=ORANGE, r=11, value=f"<b>{chip}</b>", size=10, color=WHITE)
    p.text(cx + 116, y + 52, 600, 30, f"<b>{title}</b>", size=21)
    p.text(cx + 116, y + 82, 600, 20, sub, size=12, color=MUTED)
    if counter:
        p.text(cx + cw - 220, y + 26, 90, 20, counter, size=12, align="right")
        p.progress(cx + cw - 120, y + 32, 96, 20)
    return cx, cw, y + 118


def context_sentence(p, cx, cw, y):
    hl = "<span style='background-color:#FFE8D6;color:#F97316;'><b>&nbsp;renewable energy&nbsp;</b></span>"
    p.rect(cx + 24, y, cw - 48, 64, fill=PRIMARY_SOFT, stroke=PRIMARY_SOFT, r=12, size=16, color=PRIMARY,
           value=f"<b>Many countries are investing in</b> {hl} <b>, such as solar and wind power, to reduce pollution.</b> 🔊")
    return y + 80


def exercise_footer(p, cx, cw, y, primary="Kiểm tra", skip=True):
    p.text(cx + 24, y, 160, 30, "💡 <u>Cần gợi ý?</u>", size=13, color=PRIMARY)
    if skip:
        p.text(cx + cw - 300, y, 120, 30, "<u>Bỏ qua ›</u>", size=13, color=PRIMARY, align="right")
    p.rect(cx + cw - 160, y - 6, 136, 42, fill=ORANGE, stroke=ORANGE, r=10, value=f"<b>{primary}</b>", size=14, color=WHITE)


def lesson_nav(p, y):
    p.text(X0, y, 200, 24, "← <u>Quay lại</u>", size=13, color=PRIMARY)
    p.text(X0 + CW - 200, y, 200, 24, "Bài 4 · Collocations", size=12, color=MUTED, align="right")


WORD_CLOUD = [("deforestation", 15, 420, 20), ("carbon footprint", 13, 640, 26), ("drought", 13, 260, 50), ("recycle", 15, 700, 56),
              ("pollution", 15, 300, 96), ("climate change", 13, 520, 92), ("renewable resources", 12, 640, 110),
              ("natural resources", 16, 240, 150), ("renewable energy", 26, 430, 140), ("ecosystem", 16, 700, 150),
              ("conservation", 15, 300, 200), ("biodiversity", 16, 640, 196), ("habitat", 12, 380, 230),
              ("sustainable development", 15, 250, 250), ("reduce emissions", 16, 600, 240), ("protect wildlife", 15, 430, 270)]


def p59c_scope(f):
    h = 1400
    p, y = lesson_page(f, "S — Khám phá bộ từ", "S", h)
    p.zone(X0 - 36, y, "B")
    p.card(X0, y, CW, 470, r=18)
    p.text(X0 + 24, y + 18, 400, 28, "<b>Khám phá bộ từ vựng</b> <font color='#F97316'>●</font>", size=18)
    p.text(X0 + 24, y + 46, 600, 20, "Rê chuột vào từ để xem nhanh; bấm từ để mở thẻ và tự đoán nghĩa.", size=12, color=MUTED)
    p.rect(X0 + CW - 520, y + 18, 500, 30, fill=SOFT, stroke=LINE, r=15, size=11,
           value="🟧 Mục tiêu: dùng từ để nói và viết về chủ đề môi trường   ·   ⏱ 15 phút   ·   5 cụm từ")
    wx = X0 + 24
    for word, size, dx, dy in WORD_CLOUD:
        on = word == "renewable energy"
        p.text(wx + dx - 200, y + 90 + dy, 260, 30, f"<b>{word}</b>" if on else word, size=size,
               color=ORANGE if on else (INK if size >= 15 else MUTED), align="center")
    p.text(X0 + 90, y + 400, 600, 22, "▦ Thẻ từ    ☁ Đám mây từ    ☰ Danh sách", size=12, color=MUTED)
    rx, rw = X0 + CW - 420, 396
    p.card(rx, y + 70, rw, 300, r=14)
    p.text(rx + 16, y + 82, 200, 18, "THẺ ĐANG XEM", size=10, color=MUTED, bold=True)
    p.text(rx + 16, y + 100, 300, 28, "<b>renewable energy</b>", size=18)
    audio_dot(p, rx + rw - 50, y + 98, 30, dark=False)
    p.rect(rx + 16, y + 138, rw - 32, 34, fill=PRIMARY_SOFT, stroke=PRIMARY, r=8, value="☑ Tôi đã biết từ này", size=12, color=PRIMARY, align="left")
    p.text(rx + 16, y + 180, rw - 32, 18, "Nhập nghĩa tiếng Việt bạn đoán", size=11, color=MUTED)
    p.rect(rx + 16, y + 200, rw - 32, 36, fill=WHITE, stroke=DARK, r=8, value="năng lượng tái tạo", size=13, align="left")
    p.btn(rx + 16, y + 244, rw - 32, 36, "Kiểm tra", size=13)
    p.rect(rx + 16, y + 290, rw - 32, 50, fill=GREEN_SOFT, stroke=GREEN, r=8, size=12, align="left",
           value="✓ <b>Chính xác!</b><br><font color='#6B7280'>Năng lượng từ nguồn tự nhiên có thể tái tạo.</font>")
    p.rect(rx + rw - 190, y + 400, 190, 46, fill=ORANGE, stroke=ORANGE, r=12, value="<b>Bắt đầu học →</b>", size=14,
           color=WHITE, shadow=True)
    y += 494
    p.zone(X0 - 36, y, "C")
    p.card(X0, y, CW, 420, r=18)
    p.text(X0 + 24, y + 18, 400, 26, "<b>Danh sách từ vựng</b>", size=17)
    p.text(X0 + 24, y + 44, 600, 18, "Từ bạn đánh dấu đã biết sẽ không xuất hiện trong phần luyện tập.", size=12, color=MUTED)
    heads = [("#", 60), ("Từ vựng", 520), ("Trạng thái", 300), ("Thao tác", 312)]
    hx = X0 + 24
    for label, w in heads:
        p.text(hx, y + 72, w, 30, f"<b>{label}</b>", size=12, color=MUTED)
        hx += w
    for r, (word, state) in enumerate((("renewable energy", "Đã biết"), ("reduce emissions", "Chưa học"),
                                       ("protect wildlife", "Chưa học"), ("natural resources", "Chưa học"),
                                       ("sustainable development", "Chưa học"))):
        ry = y + 104 + r * 50
        p.rect(X0 + 24, ry, CW - 48, 44, fill=SOFT if r % 2 else WHITE, stroke=LINE, r=8)
        p.text(X0 + 36, ry, 40, 44, f"0{r + 1}", size=12, color=MUTED)
        p.text(X0 + 84, ry, 500, 44, f"🔊 <b><font color='#123AB5'>{word}</font></b>", size=13)
        p.chip(X0 + 604, ry + 10, f"● {state}", kind="active" if state == "Đã biết" else "neutral", size=10)
        p.btn(X0 + 904, ry + 6, 190, 32, "Học lại" if state == "Đã biết" else "☑ Tôi đã biết từ này", kind="secondary", size=11)
    p.link(X0 + CW / 2 - 100, y + 370, 200, "Xem thêm 10 từ ⌄", size=13, align="center")
    footer(p, h - 64)
    return p


OPTIONS = ("Năng lượng tái tạo", "Năng lượng hoá thạch", "Năng lượng hạt nhân", "Năng lượng tiết kiệm")


def probe_base(f, frame, h=1080):
    p, y = lesson_page(f, frame, "P", h)
    cx, cw, y = exercise_card(p, y, 600, "P · Đoán nghĩa", "Đoán nghĩa trong ngữ cảnh",
                              "Đọc câu và chọn nghĩa phù hợp của cụm từ được tô màu.")
    y = context_sentence(p, cx, cw, y)
    return p, cx, cw, y


def p59c_probe(f):
    p, cx, cw, y = probe_base(f, "P — Đoán nghĩa")
    p.text(cx, y, cw, 24, "“renewable energy” có nghĩa là gì trong câu trên?", size=14, align="center")
    for i, opt in enumerate(OPTIONS):
        on = i == 0
        p.rect(cx + 180, y + 36 + i * 54, cw - 360, 44, fill=PRIMARY_SOFT if on else WHITE, stroke=PRIMARY if on else LINE,
               r=10, sw=2 if on else 1, value=f"<b>{chr(65 + i)}</b>    {opt}", size=13, align="left")
    exercise_footer(p, cx, cw, y + 280)
    lesson_nav(p, y + 380)
    footer(p, 1080 - 64)
    return p


def p59c_probe_result(f, correct):
    p, cx, cw, y = probe_base(f, "P — Đoán nghĩa · " + ("đúng" if correct else "sai"), h=1140)
    if correct:
        p.rect(cx + 24, y, cw - 48, 40, fill=GREEN_SOFT, stroke=GREEN, r=10, size=13, align="left",
               value="✓ <b>Chính xác!</b> Renewable energy là năng lượng tái tạo.")
    else:
        p.rect(cx + 24, y, cw - 48, 48, fill=RED_SOFT, stroke=RED, r=10, size=13, align="left",
               value="✗ <b>Chưa đúng. Đáp án đúng: Năng lượng tái tạo.</b><br>"
                     "<font color='#6B7280'>Xem flashcard bên dưới rồi thử câu tiếp theo.</font>")
    flashcard(p, cx + cw / 2 - 290, y + 64, 580, 300, side="back" if correct else "front", mode="full",
              phrase="Renewable energy", ipa="/rɪˈnjuː.ə.bəl ˈen.ə.dʒi/", meaning="Năng lượng tái tạo",
              image="Ảnh tấm pin mặt trời, tua-bin gió", effect="hover" if correct else None)
    p.text(cx, y + 372, cw, 20, "Lật thẻ để xem nghĩa và ví dụ thêm", size=12, color=MUTED, align="center")
    exercise_footer(p, cx, cw, y + 410, primary="Tiếp theo ›")
    lesson_nav(p, y + 480)
    footer(p, 1140 - 64)
    return p


def dialog(p, h, w, dh, owl_label, title, body, buttons, festive=False):
    p.overlay(DESKTOP_W, h)
    dx, dy = (DESKTOP_W - w) / 2, 220
    p.cell("", card_style(WHITE, gradient="#E8EDFB" if festive else None, shadow=True), dx, dy, w, dh)
    if festive:
        for sx, sy, s in ((40, 30, "⭐"), (w - 80, 50, "⭐"), (60, dh - 90, "🪐"), (w - 90, dh - 110, "🪐"), (w / 2 + 120, 30, "🎉")):
            p.text(dx + sx, dy + sy, 40, 40, s, size=22, align="center")
        owl(p, dx + w / 2 - 70, dy + 30, 140, 140, owl_label)
        p.rect(dx + 60, dy + 186, w - 120, 110, fill=WHITE, stroke="none", r=14, shadow=True)
        p.text(dx + 60, dy + 196, w - 120, 34, f"<b><font color='#123AB5'>{title}</font></b>", size=24, align="center")
        p.text(dx + 90, dy + 234, w - 180, 50, body, size=13, color=MUTED, align="center", valign="top")
        bx = dx + w / 2 - 70
        p.btn(bx, dy + dh - 70, 140, 42, buttons[0][0], size=14)
    else:
        owl(p, dx + 30, dy + 40, 180, 180, owl_label)
        p.text(dx + 240, dy + 60, w - 270, 70, title, size=24, valign="top")
        p.text(dx + 240, dy + 136, w - 270, 70, body, size=13, color=MUTED, valign="top")
        bx = dx + 240
        for label, kind in buttons:
            p.btn(bx, dy + dh - 76, 180, 44, label, kind=kind, size=13)
            bx += 196


def p59c_skip(f):
    h = 1080
    p, cx, cw, y = probe_base(f, "Hộp thoại bỏ qua", h)
    exercise_footer(p, cx, cw, y + 280)
    dialog(p, h, 680, 300, "🦉 SKIP?", "<b>Bạn có chắc <font color='#123AB5'>bỏ qua</font> bài tập này?</b>",
           "Bài tập này là một phần trong lộ trình giúp bạn ghi nhớ và sử dụng từ vựng hiệu quả hơn. Bỏ qua có thể làm "
           "giảm hiệu quả luyện tập.", [("Vẫn bỏ qua", "secondary"), ("Tiếp tục làm bài", "primary")])
    return p


def p59c_assemble(f):
    h = 1000
    p, y = lesson_page(f, "A — Điền từ vào câu", "A", h)
    cx, cw, y = exercise_card(p, y, 470, "A · Luyện nhớ", "Điền từ vào câu", "Nhớ lại cụm từ vừa học và điền vào chỗ trống.")
    p.rect(cx + cw - 230, y - 80, 206, 32, fill=WHITE, stroke=LINE, r=8, value="Chế độ: Gõ chữ ▾", size=12)
    p.rect(cx + 24, y, cw - 48, 90, fill=PRIMARY_SOFT, stroke=PRIMARY_SOFT, r=12, size=20, color=PRIMARY,
           value="<b>Solar and wind power are examples of ____________ .</b><br>"
                 "<font style='font-size:12px' color='#6B7280'>Gợi ý 1: Năng lượng tái tạo</font>")
    p.text(cx + 24, y + 110, 300, 20, "Câu trả lời của bạn", size=12, bold=True)
    p.rect(cx + 24, y + 134, cw / 2, 44, fill=WHITE, stroke=DARK, r=8, value="Gõ cụm từ tiếng Anh…", color=MUTED, size=13, align="left")
    exercise_footer(p, cx, cw, y + 220, primary="Kiểm tra")
    lesson_nav(p, y + 290)
    footer(p, h - 64)
    return p


def p59c_communicate(f):
    h = 1060
    p, y = lesson_page(f, "C — Đặt câu", "C", h)
    cx, cw, y = exercise_card(p, y, 520, "C · Đặt câu", "Trả lời bằng từ đã học", "Dùng cụm từ gợi ý để trả lời câu hỏi.")
    p.rect(cx + 24, y, cw - 48, 90, fill=PRIMARY_SOFT, stroke=PRIMARY_SOFT, r=12, size=20, color=PRIMARY, align="left",
           value="<font style='font-size:11px' color='#6B7280'>CÂU HỎI</font><br><b>What can your city do to reduce air pollution?</b>")
    p.text(cx + 24, y + 98, 90, 24, "Từ cần dùng:", size=12, color=MUTED)
    p.chip(cx + 112, y + 98, "renewable energy", kind="active", size=11)
    p.chip(cx + 24, y + 134, "✎ Viết", kind="solid", size=11, w=70)
    p.chip(cx + 102, y + 134, "🎙 Nói", kind="neutral", size=11, w=70)
    p.text(cx + 24, y + 166, 300, 20, "Câu trả lời của bạn", size=12, bold=True)
    p.rect(cx + 24, y + 190, cw - 48, 100, fill=WHITE, stroke=DARK, r=8, value="My city could invest more in renewable energy…",
           color=MUTED, size=13, align="left", valign="top")
    p.text(cx + 24, y + 296, cw - 48, 18, "AI nhận xét cách dùng từ, ngữ pháp và độ tự nhiên · 0/200 ký tự", size=11, color=MUTED)
    exercise_footer(p, cx, cw, y + 334, primary="Gửi câu trả lời")
    lesson_nav(p, y + 400)
    footer(p, h - 64)
    return p


def p59c_before_review(f):
    h = 1060
    p, y = lesson_page(f, "Thông báo trước khi nhìn lại", "C", h)
    cx, cw, y = exercise_card(p, y, 520, "C · Đặt câu", "Trả lời bằng từ đã học", "Dùng cụm từ gợi ý để trả lời câu hỏi.")
    dialog(p, h, 640, 380, "🦉🎉", "TỐT RỒI!", "Giờ cùng sửa lại một vài lỗi sai nhé. Chúng ta sẽ xem lại những cụm từ bạn "
           "còn nhầm để ghi nhớ chắc hơn trước khi học bài tiếp theo.", [("Tiếp tục", "primary")], festive=True)
    return p


def p59c_evaluate(f):
    h = 1080
    p, y = lesson_page(f, "E — Nhìn lại bài vừa học", "E", h)
    cx, cw, y = exercise_card(p, y, 560, "E · Kiểm tra", "Nhìn lại bài vừa học", "Bài 4 · Collocations · 5 cụm từ", counter="")
    for i, label in enumerate(("Nhìn lại", "Sửa lỗi", "Tổng kết")):
        sx = cx + cw - 300 + i * 96
        p.cell(str(i + 1), "ellipse;whiteSpace=wrap;html=1;fontSize=12;" + ("fillColor=#123AB5;strokeColor=#123AB5;fontColor=#FFFFFF;"
               if i == 0 else "fillColor=#FFFFFF;strokeColor=#C9CED6;fontColor=#6B7280;"), sx + 30, y - 92, 26, 26)
        p.text(sx, y - 62, 90, 16, label, size=10, color=MUTED, align="center")
    p.rect(cx + 24, y, cw - 48, 96, fill=PRIMARY_SOFT, stroke=PRIMARY_SOFT, r=12)
    sw = (cw - 48) / 3
    for i, (icon, name, score, note) in enumerate((("◎", "Đoán nghĩa", "3/5", "Cần cải thiện"), ("◈", "Luyện nhớ", "4/5", "Khá tốt"),
                                                   ("✎", "Đặt câu", "4/5", "Dùng từ tự nhiên"))):
        p.text(cx + 24 + i * sw, y + 12, sw, 72, f"<font color='#123AB5'>{icon}</font> {name}<br><b><font style='font-size:24px'>"
               f"{score}</font></b><br><font color='#6B7280'>{note}</font>", size=12, align="center", valign="top")
    p.text(cx + 24, y + 116, 400, 26, "<b>Bạn cần xem lại 2 cụm từ</b>", size=16, color=PRIMARY)
    for i, (word, why, color) in enumerate((("renewable energy", "Đoán sai 1 lần", ORANGE), ("reduce emissions", "Điền sai chính tả", RED))):
        ry = y + 152 + i * 56
        p.rect(cx + 24, ry, cw - 48, 46, fill=WHITE, stroke=LINE, r=10)
        p.text(cx + 40, ry, 30, 46, f"{i + 1}", size=12, color=MUTED)
        p.text(cx + 70, ry, 220, 46, f"<b>{word}</b>", size=13)
        p.rect(cx + 290, ry + 12, 150, 22, fill=WHITE, stroke=color, r=11, value=f"● {why}", size=10, color=color)
        p.text(cx + cw - 60, ry, 30, 46, "›", size=16, color=MUTED)
    p.text(cx + 24, y + 270, cw - 48, 22, "💡 Bạn đã dùng đúng 4/5 cụm từ trong câu. Ôn lại 2 cụm trên để mở Bài 5.", size=12, color=MUTED)
    p.text(cx + 24, y + 318, 200, 30, "<u>Xem bài đã làm</u>", size=13, color=PRIMARY)
    p.rect(cx + cw - 180, y + 310, 156, 42, fill=ORANGE, stroke=ORANGE, r=10, value="<b>Hoàn thành</b>", size=14, color=WHITE)
    lesson_nav(p, y + 470)
    footer(p, h - 64)
    return p


# ------------------------------------------------------------------ P-59d Flashcard F045 effects
EFFECT_STATES = [("Mặt trước · hover", ("front", "full", "hover")), ("Đang lật", ("front", "full", "flipping")),
                 ("Mặt sau", ("back", "full", None)), ("Mặt sau · nhấn giữ", ("back", "full", "pressed")),
                 ("Chế độ giản lược", ("front", "simple", None)), ("Giản lược · mặt sau", ("back", "simple", None))]


def build_effects(new):
    """F045 effects shown on the class flashcard screen itself (P-21 / Homework — Flashcard is the resting state)."""
    import screens_dashboard_classroom
    f = new("P-59d_Flashcard")
    for frame, card in EFFECT_STATES:
        screens_dashboard_classroom.lesson_ws(f, frame, "flashcard", pid="P-59d", title="Flashcard Effects (F045)", card=card)
    f.save()


# ------------------------------------------------------------------ P-21 Flashcard tab (called from screens_dashboard_classroom)
def homework_flashcard(p, x, y, w, card=("front", "full", None)):
    """Content of P-21 / Homework — Flashcard: tabs, filters, card, pager and the card list."""
    p.text(x + 28, y + 22, 400, 20, "<b><font color='#123AB5'>● Homework Hub</font></b>  /  Từ vựng", size=12, color=MUTED)
    p.text(x + 28, y + 44, 520, 34, "<b>Bài 1: Nature &amp; Environment</b>", size=22)
    tx = x + 28
    for i, t in enumerate(("Vocabulary list", "Flashcard", "Bài tập")):
        tw = len(t) * 8 + 34
        on = i == 1
        p.rect(tx, y + 88, tw, 34, fill=PRIMARY_SOFT if on else WHITE, stroke=PRIMARY if on else "none", r=8,
               value=f"<b>{t}</b>" if on else t, size=13, color=PRIMARY if on else INK)
        tx += tw + 8
    p.rect(x + 28, y + 128, w - 56, 1, fill=LINE, stroke=LINE, r=0)
    p.chip(x + 40, y + 142, "Tất cả (5)", kind="solid", size=10)
    p.chip(x + 124, y + 142, "Chưa thuộc (3)", kind="outline", size=10)
    p.chip(x + 236, y + 142, "Đã thuộc (1)", kind="active", size=10)
    p.text(x + w - 330, y + 140, 200, 20, "Tiến độ Flashcard <b>1/5</b>", size=11, align="right")
    p.progress(x + w - 124, y + 148, 70, 15, h=6)
    p.text(x + w - 54, y + 140, 30, 20, "15%", size=10, color=ORANGE)
    full = card[1] == "full"
    p.rect(x + w - 236, y + 172, 208, 28, fill=SOFT, stroke=LINE, r=14)
    p.rect(x + w - 234, y + 174, 102, 24, fill=WHITE if full else PRIMARY, stroke=LINE if full else PRIMARY, r=12,
           value="Giản lược" if full else "<b>Giản lược</b>", size=11, color=INK if full else WHITE)
    p.rect(x + w - 130, y + 174, 100, 24, fill=PRIMARY if full else WHITE, stroke=PRIMARY if full else LINE, r=12,
           value="<b>Đầy đủ</b>" if full else "Đầy đủ", size=11, color=WHITE if full else INK)
    side, mode, effect = card
    flashcard(p, x + 90, y + 214, w - 180, 300 if mode == "full" else 240, side=side, mode=mode, effect=effect)
    p.rect(x + w / 2 - 80, y + 528, 160, 30, fill=SOFT, stroke=LINE, r=15, value="✓ Đánh dấu đã học", size=12)
    p.btn(x + 160, y + 572, 130, 36, "‹ Thẻ trước", kind="secondary", size=12)
    p.text(x + w / 2 - 40, y + 572, 80, 22, "<b>1 / 5</b>", size=15, align="center")
    p.progress(x + w / 2 - 50, y + 598, 100, 20, h=4)
    p.btn(x + w - 290, y + 572, 130, 36, "Thẻ sau ›", kind="secondary", size=12)
    ly = y + 640
    p.text(x + 28, ly, 300, 18, "TẤT CẢ THẺ (5)", size=10, color=MUTED, bold=True)
    for r, (word, vi) in enumerate((("a breath of fresh air", "một hơi thở không khí trong lành"), ("scenery", "phong cảnh"),
                                    ("sustainable", "bền vững"), ("biodiversity", "đa dạng sinh học"), ("conserve", "bảo tồn"))):
        ry = ly + 24 + r * 40
        p.rect(x + 28, ry, w - 56, 36, fill=PRIMARY_SOFT if r == 0 else WHITE, stroke=LINE, r=8)
        p.text(x + 40, ry, 24, 36, str(r + 1), size=11, color=MUTED)
        p.text(x + 70, ry, 300, 36, f"<b>{word}</b>", size=13)
        p.text(x + 380, ry, 300, 36, vi, size=12, color=MUTED)
        p.text(x + w - 70, ry, 30, 36, "🔊", size=12)


def build(new):
    f = new("P-59b_TopicLessonPath")
    p59b(f)
    f.save()
    f = new("P-59c_VocabularyLesson")
    p59c_scope(f)
    p59c_probe(f)
    p59c_probe_result(f, correct=False)
    p59c_probe_result(f, correct=True)
    p59c_skip(f)
    p59c_assemble(f)
    p59c_communicate(f)
    p59c_before_review(f)
    p59c_evaluate(f)
    f.save()
    build_effects(new)
