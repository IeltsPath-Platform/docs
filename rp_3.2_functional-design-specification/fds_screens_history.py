"""Submission history design target, appended to preserve existing FDS section numbers."""
from fds_screens import AUTH, EX_SESSION, ex_menu, screen

SCREENS = [
    screen(
        key="SubmissionHistory", name="Submission History", route="/submission-history · RequireAuth · P-54",
        roles="Signed-in learner", ft="FT-25, FT-27, FT-31, FT-34, FT-39", uc="—",
        fe="placeholder", status="Design target (history list APIs not implemented)",
        frontend="The route currently shows RouteStatusPage. P-54 specifies the populated and empty states; "
                 "the wireframe does not imply a working history API.",
        purpose="Lets the learner find submitted work across Writing, Speaking, Reading, Listening and Mock Test, "
                "check grading status and open the available result or feedback. UI label: Lịch sử nộp bài.",
        mockup="P-54 / Populated and P-54 / Empty in wireframes/screens/P-54_SubmissionHistory.drawio",
        nav_from=[("Trang chủ submenu", 'User selects "Lịch sử nộp bài"')],
        nav_to=[("Writing Feedback", 'User selects "Xem nhận xét" for a lesson Writing submission'),
                ("Test Result / Placement Report", 'User selects "Xem bài" or "Xem nhận xét" for an attempt'),
                ("Original exercise", 'User selects "Làm lại" when the source permits another submission'),
                ("Practice Test Catalog", 'Empty-state CTA "Tiến hành làm bài tập ngay" → /practice-tests')],
        pre=[AUTH], entry=[("History menu", "Any signed-in page", "No user id accepted from navigation")],
        exits=[("Open record", "Record belongs to the learner", "Source result or feedback", "Use the source id"),
               ("Empty-state CTA", "No matching records", "Practice Test Catalog", "/practice-tests"),
               ex_menu(), EX_SESSION],
        comps=[("TAB", "Skill and test type", "Tabs", "One active tab", "Writing · Speaking · Reading · Listening · Mock Test"),
               ("TXT", "Theo tên bài", "Search input", "Trim input", "Filter by exercise name"),
               ("DAT", "Theo ngày nộp", "Date filter", "Valid date", "Filter by submission date"),
               ("TBL", "Submission list", "Paginated table", "Own records only", "Tên bài · Nguồn · Ngày nộp · Trạng thái · Band · Action"),
               ("BDG", "Grading status", "Status label", "Do not infer a final grade", "Đã chấm (AI) · Đang chấm… · Chờ EXAMINER · Chưa đạt · làm lại"),
               ("BTN", "Record action", "Button", "Depends on source and status", "Xem nhận xét · Xem bài · Làm lại"),
               ("BTN", "Pagination", "Previous / next", "Disable unavailable direction", "Trang {page} / {pages} · ‹ Trước · Sau ›"),
               ("BTN", "Empty-state action", "Primary button", "No matching submissions", "Tiến hành làm bài tập ngay")],
        apis=[("Open lesson Writing feedback", "learn.essay", "Path: submission id", "Render Writing Feedback", "404 → unavailable record; 401 → GLB-01"),
              ("Open assessment result", "as.result", "Path: attemptId", "Render source result", "404 / 403 → unavailable record"),
              ("Open placement result", "as.placementResult", "Path: attemptId", "Render Placement Report", "Not ready → retain pending status"),
              ("Open learning Practice detail", "learn.practice", "Path: id", "Render source Practice attempt", "404 → unavailable record")],
        interactions=[("History data availability", [
            "History lists for assessment attempts, lesson Writing submissions and learning Practice attempts are missing.",
            "Their pagination, filtering, sorting and combined-list contract remain design work; no new endpoint is asserted here.",
            "Existing detail APIs require known ids and do not provide a history list.",
            "Keep source type and source id with each row; matching names do not identify the same submission."]),
            ("Filtering and results", [
                "Changing skill, exercise name or submission date resets the page to the first page.",
                "A pending grade shows no band. Show an empty state only after a successful response with no matches.",
                "A failed request shows retry and preserves the selected filters; it must not look like an empty history.",
                "Làm lại opens the original exercise and respects its access and retry rules."])],
        msgs=[("Empty State", "Successful query with no matching submissions", '"Chưa có bài nộp"', 'CTA: "Tiến hành làm bài tập ngay"'),
              ("Error Panel", "History request failed", '"Không tải được lịch sử nộp bài. Vui lòng thử lại."', 'Action: "Thử lại"'),
              ("Status Text", "Grading pending", '"Đang chấm…" / "Chờ EXAMINER"', "Band shown as —")],
        rules=[("BR-27", "History and feedback belong to the signed-in learner", "Server enforces ownership"),
               ("Existing result policy", "Opening history does not bypass answer or feedback release rules", "Source API decides which details are available"),
               ("Design target", "No grade, payment or progress change occurs merely by viewing history", "Read-only list and navigation")],
    ),
]
