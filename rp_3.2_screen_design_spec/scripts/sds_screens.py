"""Single source of truth for P-IDs ↔ routes ↔ status ↔ design frames (audit of frontend/src/app/App.tsx).

Status values:
  MVP        built and wired to the real API (learning path) or real auth
  MVP·mock   built, navigable, content from FE mock data (practice workspaces)
  Later*     UI exists with mock data; out of MVP scope for Part 4
  Stub       route renders RouteStatusPage (P-92) placeholder
  Later      flagged off / not built
  Retired    in v0.3.0, no longer in App.tsx
"""
from collections import namedtuple

Screen = namedtuple("Screen", "pid name group route roles level status ft sc flows section drawio frames")

DRAWIO_DIR = "docs/wireframes/screens"  # shared with the FDS


def S(pid, name, group, route, roles, level, status, ft="—", sc="—", flows="—", section="—", drawio=None, frames=()):
    return Screen(pid, name, group, route, roles, level, status, ft, sc, flows, section, drawio, tuple(frames))


SCREENS = [
    # ---- Auth
    S("P-01", "Sign In", "Auth", "/login", "Guest", "AUTH", "MVP", "FT-02, FT-05", "SC-01", "F-01, F-04", "4.1",
      "P-01_SignIn.drawio", ["Populated", "Loading", "Error"]),
    S("P-02", "Sign Up", "Auth", "/register", "Guest", "AUTH", "MVP", "FT-01", "SC-01", "F-01, F-04", "4.2",
      "P-02_SignUp.drawio", ["Populated", "Error"]),
    S("P-03", "Forgot Password", "Auth", "/forgot-password", "Guest", "AUTH", "MVP", "FT-04", "SC-01", "F-01", "4.3",
      "P-03_ForgotPassword.drawio", ["Populated", "Success"]),
    S("P-04", "Reset Password", "Auth", "/reset-password", "Guest", "AUTH", "MVP", "FT-04", "SC-01", "F-01", "4.4",
      "P-04_ResetPassword.drawio", ["Populated", "Success", "Error"]),
    S("P-05", "OAuth Callback", "Auth", "/auth/oauth/callback", "Guest", "AUTH", "Later", "FT-05", "SC-01", "F-01"),
    # ---- Home
    S("P-10", "Home / Landing", "Home", "/home  (/ → /home for Guest)", "Guest, Learner", "PRIMARY", "MVP", "FT-10, FT-11", "SC-06", "F-04, F-01", "4.5",
      "P-10_Home.drawio", ["Populated", "Populated · Learner"]),
    S("P-10a", "Mentor Detail", "Home", "— (former modal)", "Guest, Learner", "MODAL", "Retired"),
    S("P-10b", "Plan Detail", "Home", "— (former modal)", "Guest, Learner", "MODAL", "Retired"),
    S("P-10c", "Key Activation Dialog", "Home", "Modal on P-10", "Guest, Learner", "MODAL", "MVP", "FT-11, FT-12", "SC-06", "F-04", "4.6",
      "P-10c_KeyActivation.drawio", ["Populated"]),
    S("P-11", "Overview Dashboard", "Overview & Classroom", "/overview  (/ → /overview for Learner)", "Learner", "PRIMARY", "Later*", "FT-44, FT-45", "SC-02",
      drawio="P-11_OverviewDashboard.drawio", frames=["Tổng quát", "Dữ liệu chi tiết", "Tab chưa xây dựng", "Menu Dashboard"]),
    # ---- Classroom
    S("P-20", "My Classroom", "Overview & Classroom", "/classroom", "Learner", "PRIMARY", "Later*",
      drawio="P-20_MyClassroom.drawio", frames=["Populated"]),
    S("P-20a", "Lesson Detail", "Overview & Classroom", "Modal on P-20", "Learner", "MODAL", "Later*",
      drawio="P-20a_LessonDetail.drawio", frames=["Populated"]),
    S("P-21", "Lesson Workspace", "Overview & Classroom", "/lessons/:lessonId", "Learner", "DEEP", "Later*",
      drawio="P-21_LessonWorkspace.drawio", frames=["Tài liệu buổi học", "Homework — Ngữ pháp", "Homework — Từ vựng",
                                                    "Homework — Flashcard"]),
    S("P-22", "Join Live Class", "Overview & Classroom", "/classes/:classCode/join", "Guest, Learner", "SUB", "Stub"),
    S("P-23", "Contact Mentor", "Overview & Classroom", "/mentors/:mentorSlug", "Guest, Learner", "SUB", "Stub"),
    # ---- Learning path (course-based)
    S("P-30", "Course List", "Learning Path", "/learn", "Learner", "PRIMARY", "MVP", "FT-20, FT-55", "SC-01, SC-02", "F-02", "4.7",
      "P-30_CourseList.drawio", ["Populated", "Loading", "Empty", "Error"]),
    S("P-30a", "Placement Test", "Learning Path", "/learn/placement", "Learner", "SUB", "MVP", "FT-09, FT-35", "SC-01", "F-02, F-05", "4.8",
      "P-30a_Placement.drawio", ["Survey", "Survey Summary", "Test Hub", "Exam — Reading / Listening", "Exam — Writing",
                                 "Exam — Speaking", "Grading", "Result Report"]),
    S("P-30b", "Topic List (in course)", "Learning Path", "/learn/courses/:courseId", "Learner", "SUB", "MVP", "FT-20, FT-29, FT-55", "SC-02, SC-05", "F-02", "4.9",
      "P-30b_TopicList.drawio", ["Populated", "Loading", "Empty / Error"]),
    S("P-31", "Topic Detail", "Learning Path", "/learn/topics/:topicId", "Learner", "SUB", "MVP", "FT-21, FT-29", "SC-02, SC-05", "F-02", "4.10",
      "P-31_TopicDetail.drawio", ["Populated", "Locked Test / Review Gate"]),
    S("P-32", "Lesson Player", "Learning Path", "/learn/lessons/:lessonId", "Learner", "DEEP", "MVP", "FT-21, FT-22, FT-23, FT-25", "SC-02, SC-04", "F-02", "4.11",
      "P-32_LessonPlayer.drawio", ["Populated", "Completed", "Review Required", "Writing Feedback — Chưa đạt",
                                    "Writing Feedback — Đã đạt"]),
    S("P-33", "Lesson Practice", "Learning Path", "/learn/lessons/:lessonId/practice", "Learner", "DEEP", "MVP", "FT-27", "SC-03, SC-04", "F-02", "4.12",
      "P-33_LessonPractice.drawio", ["Set List", "Attempt", "Outcome"]),
    S("P-34", "Review Session", "Learning Path", "/learn/reviews/:reviewId", "Learner", "DEEP", "MVP", "FT-26, FT-28", "SC-03", "F-02", "4.13",
      "P-34_ReviewSession.drawio", ["Theory", "Practice Set", "Finished"]),
    S("P-35", "Topic / Course Test", "Learning Path", "/learn/tests/:attemptId (?topic= | ?course=)", "Learner", "DEEP", "MVP", "FT-29, FT-30, FT-55", "SC-05", "F-02", "4.14",
      "P-35_TopicTest.drawio", ["Populated", "Confirm Submit"]),
    S("P-36", "Test Result", "Learning Path", "/learn/tests/:attemptId/result", "Learner", "DEEP", "MVP", "FT-31, FT-29, FT-55", "SC-05", "F-02", "4.15",
      "P-36_TestResult.drawio", ["Passed", "Failed"]),
    # ---- Practice
    S("P-40", "Practice Hub (“Thực hành”)", "Practice", "/practice", "Learner", "PRIMARY", "Stub"),
    S("P-41", "Practice Catalog", "Practice", "/practice-tests (?skill=)", "Learner", "PRIMARY", "MVP·mock", "FT-34", "—", "F-03", "4.16",
      "P-41_PracticeCatalog.drawio", ["Populated"]),
    S("P-41a", "Practice Mode Select", "Practice", "Modal on P-41", "Learner", "MODAL", "MVP·mock", "FT-34", "—", "F-03", "4.17",
      "P-41a_PracticeModeSelect.drawio", ["Populated"]),
    S("P-42", "Reading Practice Test", "Practice", "/practice/test/:testId?mode=  (/practice/test)", "Learner", "DEEP", "MVP·mock", "FT-34, FT-42, FT-43", "SC-08", "F-03", "4.18",
      "P-42_ReadingPracticeTest.drawio", ["Practice Mode", "Exam Mode"]),
    S("P-42a", "Create Flashcard", "Practice", "Modal on P-42", "Learner", "MODAL", "MVP·mock", "FT-43", "SC-08", "F-03", "4.19",
      "P-42a_CreateFlashcard.drawio", ["Populated"]),
    S("P-42b", "Dictionary Lookup", "Practice", "Modal on P-42", "Learner", "MODAL", "MVP·mock", "FT-36", "SC-08", "F-03", "4.20",
      "P-42b_DictionaryLookup.drawio", ["Populated"]),
    S("P-42c", "Saved Flashcards", "Practice", "Modal on P-42", "Learner", "MODAL", "MVP·mock", "FT-43", "SC-08", "F-03", "4.21",
      "P-42c_SavedFlashcards.drawio", ["Populated"]),
    S("P-42d", "Floating Notes", "Practice", "Floating panel on P-42", "Learner", "MODAL", "MVP·mock", "FT-42", "SC-08", "F-03", "4.22",
      "P-42d_FloatingNotes.drawio", ["Populated"]),
    S("P-43", "Practice", "Practice", "/practice/listening/:testId", "Learner", "DEEP", "MVP·mock", "FT-24, FT-34", "—", "F-03", "4.23",
      "P-43_ListeningPractice.drawio", ["Catalog", "Mode Select", "Reading", "Reading Exam", "Reading Result", "Reading Result High", "Reading Explanation", "Listening", "Listening Exam", "Listening Result", "Listening Result Top", "Listening Explanation", "Writing Mode Select", "Writing", "Writing Grade Confirm", "Writing Not Enough Points", "Writing Guided", "Writing Guided Grade Confirm", "Writing Result"]),
    S("P-44", "Writing Practice", "Practice", "/practice/writing/:taskId", "Learner", "DEEP", "MVP·mock", "FT-34", "—", "F-03", "4.24",
      "P-44_WritingPractice.drawio", ["Populated", "Bố cục 3 cột (đề xuất)"]),
    S("P-44a", "Writing Chart Zoom", "Practice", "Modal on P-44", "Learner", "MODAL", "MVP·mock", "FT-34", "—", "F-03", "4.25",
      "P-44a_WritingChartZoom.drawio", ["Populated"]),
    S("P-45", "Speaking Practice", "Practice", "/practice/speaking/:cueId", "Learner", "DEEP", "Later*", "FT-39", "SC-08", "F-03",
      drawio="P-45_SpeakingPractice.drawio", frames=["Hướng dẫn chung", "Kiểm tra micro", "Part 1 — Đang ghi âm"]),
    # ---- Vocabulary & personal
    S("P-46", "Mock Test Catalog", "Practice", "/tests", "Learner", "PRIMARY", "Later*", "FT-34", "SC-07",
      drawio="P-46_MockTestCatalog.drawio", frames=["Populated"]),
    S("P-47", "Mock Test Runner", "Practice", "/tests/:attemptId", "Learner", "DEEP", "Later*", "FT-30, FT-34", "SC-07",
      drawio="P-47_MockTestRunner.drawio", frames=["Reading — True / False / Not Given", "Reading — Summary completion",
                                                   "Listening — Note completion", "Nộp bài"]),
    S("P-50", "Vocabulary / Dictionary", "Vocabulary & Personal", "/vocabulary", "Guest, Learner", "PRIMARY", "Later*", "FT-36", "SC-08",
      drawio="P-50_Vocabulary.drawio", frames=["Populated", "Empty search"]),
    S("P-51", "My Flashcards", "Vocabulary & Personal", "/flashcards", "Learner", "SUB", "Later*", "FT-43", "SC-08",
      drawio="P-51_MyFlashcards.drawio", frames=["Danh sách học phần"]),
    S("P-51a", "Create Set", "Vocabulary & Personal", "/flashcards/new", "Learner", "SUB", "Later*", "FT-43", "SC-08",
      drawio="P-51a_CreateSet.drawio", frames=["Tạo học phần"]),
    S("P-51b", "Set Detail", "Vocabulary & Personal", "/flashcards/:setId", "Learner", "SUB", "Later*", "FT-43", "SC-08",
      drawio="P-51b_SetDetail.drawio", frames=["Thẻ ghi nhớ"]),
    S("P-52", "Writing 8.0+ Samples", "Vocabulary & Personal", "/writing-samples", "Learner", "PRIMARY", "Stub"),
    S("P-53", "Student Results", "Vocabulary & Personal", "/student-results", "Learner", "PRIMARY", "Stub"),
    S("P-54", "Submission History", "Vocabulary & Personal", "/submission-history", "Learner", "SUB", "Stub", "FT-30",
      drawio="P-54_SubmissionHistory.drawio", frames=["Populated", "Empty"]),
    S("P-60", "Materials", "Vocabulary & Personal", "/materials (removed)", "Learner", "PRIMARY", "Retired"),
    # ---- Legal
    S("P-70", "Terms of Use", "Info & Legal", "/terms", "Guest, Learner", "SUB", "Stub"),
    S("P-71", "Privacy Policy", "Info & Legal", "/privacy", "Guest, Learner", "SUB", "Stub"),
    S("P-72", "Copyright Policy", "Info & Legal", "/copyright", "Guest, Learner", "SUB", "Stub"),
    # ---- System
    S("P-56", "Dictionary Home", "Vocabulary & Personal", "/vocabulary  (redesign of P-50)", "Learner", "PRIMARY", "Later*", "FT-36, FT-43", "SC-08",
      drawio="P-56_DictionaryHome.drawio", frames=["Trang chủ từ điển"]),
    S("P-57", "Word Detail", "Vocabulary & Personal", "/vocabulary/words/:word", "Guest, Learner", "SUB", "Later*", "FT-36", "SC-08",
      drawio="P-57_WordDetail.drawio", frames=["Định nghĩa", "Thesaurus"]),
    S("P-58", "Vocabulary Map", "Vocabulary & Personal", "/vocabulary/map", "Learner", "SUB", "Later*", "FT-36", "SC-08",
      drawio="P-58_VocabularyMap.drawio", frames=["Populated"]),
    S("P-59", "Vocabulary Set", "Vocabulary & Personal", "/vocabulary/sets/:setId", "Learner", "SUB", "Later*", "FT-36, FT-43", "SC-08",
      drawio="P-59_VocabularySet.drawio", frames=["Tổng quan"]),
    S("P-59a", "Set Study", "Vocabulary & Personal", "/vocabulary/sets/:setId/study", "Learner", "DEEP", "Later*", "FT-43", "SC-08",
      drawio="P-59a_SetStudy.drawio", frames=["Flashcard", "Học trộn — Điền từ", "Dịch từ", "Nối từ", "Game"]),
    S("P-59b", "Topic Lesson Path", "Vocabulary & Personal", "/vocabulary/sets/:setId/topics/:topicId", "Learner", "SUB", "Later*", "FT-36, FT-43", "SC-08",
      drawio="P-59b_TopicLessonPath.drawio", frames=["Lộ trình bài học"]),
    S("P-59c", "Vocabulary Lesson (SPACE)", "Vocabulary & Personal", "/vocabulary/lessons/:lessonId", "Learner", "DEEP", "Later*", "FT-36, FT-43", "SC-08",
      drawio="P-59c_VocabularyLesson.drawio", frames=["S — Khám phá bộ từ", "P — Đoán nghĩa", "P — Đoán nghĩa · sai",
                                                      "P — Đoán nghĩa · đúng", "Hộp thoại bỏ qua", "A — Điền từ vào câu",
                                                      "C — Đặt câu", "Thông báo trước khi nhìn lại", "E — Nhìn lại bài vừa học"]),
    S("P-59d", "Flashcard Effects (F045)", "Vocabulary & Personal", "States of P-21 / Homework — Flashcard", "Learner", "MODAL", "Later*", "FT-43", "SC-08",
      drawio="P-59d_Flashcard.drawio", frames=["Mặt trước · hover", "Đang lật", "Mặt sau", "Mặt sau · nhấn giữ",
                                               "Chế độ giản lược", "Giản lược · mặt sau"]),
    S("P-80", "Account", "Vocabulary & Personal", "/account/*  (user menu)", "Learner", "SUB", "Later*", "FT-06, FT-10, FT-12", "—",
      drawio="P-80_Account.drawio", frames=["Hồ sơ của bạn", "Lịch sử kích hoạt gói", "Lịch sử giao dịch điểm",
                                            "Lịch sử đăng nhập"]),
    S("P-90", "Not Found", "System", "*", "Guest, Learner", "DEEP", "MVP", "—", "—", "—", "4.26",
      "P-90_NotFound.drawio", ["Populated"]),
    S("P-91", "Learning Path Not Found", "System", "/learn/*", "Learner", "DEEP", "MVP", "—", "—", "F-02", "4.27",
      "P-91_LearnNotFound.drawio", ["Populated"]),
    S("P-92", "Route Status (stub template)", "System", "shared by 10 stub routes", "Guest, Learner", "SUB", "MVP", "—", "—", "—", "4.28",
      "P-92_RouteStatus.drawio", ["Populated"]),
]

GROUPS = ["Auth", "Home", "Overview & Classroom", "Learning Path", "Practice", "Vocabulary & Personal", "Info & Legal", "System"]

FLOWS = [
    ("F-01", "Authentication & Account Recovery", "F-01_Authentication"),
    ("F-02", "Course-based Learning Path", "F-02_CourseLearningPath"),
    ("F-03", "Practice Catalog to Skill Workspace", "F-03_Practice"),
    ("F-04", "Guest Home to Auth Gate", "F-04_GuestAuthGate"),
    ("F-05", "Placement Test (detail of F-02 onboarding)", "F-05_PlacementTest"),
]


def by_id(pid):
    return next(s for s in SCREENS if s.pid == pid)


def spec_screens():
    """Screens with a Part 4 section, in section order."""
    return sorted([s for s in SCREENS if s.section != "—"], key=lambda s: [int(x) for x in s.section.split(".")])
