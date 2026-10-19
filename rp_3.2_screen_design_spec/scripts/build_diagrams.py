"""Generate every SDS draw.io file (wireframes, shell, site map, navigation, flows).

Usage:  python build_diagrams.py [--only P-01_SignIn,...]
Output: docs/wireframes/screens/*.drawio and docs/wireframes/IELTSPath_Prototype.drawio (shared with the FDS),
        ../diagrams/*.drawio (IA), ../diagrams/flows/*.drawio
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from wf import DrawioFile  # noqa: E402

ROOT = os.path.normpath(os.path.join(HERE, ".."))
WIREFRAMES = os.path.normpath(os.path.join(ROOT, "..", "wireframes"))  # docs/wireframes, next to the rp_* reports
WIRE_DIR = os.path.join(WIREFRAMES, "screens")
FLOW_DIR = os.path.join(ROOT, "diagrams", "flows")
IA_DIR = os.path.join(ROOT, "diagrams")


def make_new(folder):
    def new(stem):
        return DrawioFile(os.path.join(folder, f"{stem}.drawio"))
    return new


def main():
    import screens_auth_home
    import screens_learn
    import screens_practice
    import screens_system
    import screens_dashboard_classroom
    import screens_exam_account
    import screens_dictionary
    import screens_vocab_lesson
    import screens_flashcard_sets
    import diagrams_ia_flows

    for d in (WIRE_DIR, FLOW_DIR):
        os.makedirs(d, exist_ok=True)
    wire = make_new(WIRE_DIR)
    screens_system.build_shell(wire)
    screens_auth_home.build_auth(wire)
    screens_auth_home.build_home(wire)
    screens_learn.build(wire)
    screens_practice.build(wire)
    screens_dashboard_classroom.build(wire)
    screens_exam_account.build(wire)
    screens_dictionary.build(wire)
    screens_vocab_lesson.build(wire)
    screens_flashcard_sets.build(wire)
    screens_system.build_system(wire)
    diagrams_ia_flows.build_ia(make_new(IA_DIR))
    diagrams_ia_flows.build_flows(make_new(FLOW_DIR))

    import prototype
    pages, links, problems = prototype.build(
        os.path.join(WIREFRAMES, "IELTSPath_Prototype.drawio"),
        [screens_system.build_shell, screens_auth_home.build_auth, screens_auth_home.build_home,
         screens_learn.build, screens_practice.build, screens_dashboard_classroom.build, screens_exam_account.build, screens_dictionary.build, screens_vocab_lesson.build, screens_flashcard_sets.build,
         screens_system.build_system])
    print(f"prototype: {pages} tabs, {links} clickable shapes")
    for line in problems:
        print("  WARN", line)
    print("draw.io files written")


if __name__ == "__main__":
    main()
