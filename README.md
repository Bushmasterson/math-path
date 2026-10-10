# math-path

> Mathematical animations built with [Manim](https://www.manim.community/) — visual explanations of concepts I'm learning.

---

## Requirements

- Python 3.11+
- [Manim](https://www.manim.community/) (Community edition)

## Install

```bash
git clone https://github.com/Bushmasterson/math-path.git
cd math-path
python -m venv .venv
.\.venv\Scripts\Activate.ps1   # Windows
pip install manim
```

## Render

```bash
manim -pql scenes/unit_circle.py UnitCircleSine   # preview (fast)
manim -pqh scenes/unit_circle.py UnitCircleSine   # high quality
```

Output goes to `media/videos/`.

## Scenes

| File | Class | What it shows |
|------|-------|---------------|
| `scenes/unit_circle.py` | `UnitCircleSine` | Point on the unit circle → synchronized sine wave |

## Structure

```
math-path/
├── scenes/         # Manim scenes, one file per concept
├── media/          # rendered output (gitignored)
├── manim.cfg       # render settings (4K, 90 fps, black bg)
└── README.md
```

## Conventions

- Scene files: `snake_case.py`
- Class names: `PascalCase`
- One concept per file