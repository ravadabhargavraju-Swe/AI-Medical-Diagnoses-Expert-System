# AI Medical Diagnosis Expert System

An interactive, web-based clinical expert system implemented with Flask and powered by a deterministic, rule-based inference engine. The system uses forward-chaining deduction rules to evaluate user-submitted symptoms, derive intermediate health states, and deliver preliminary diagnostic classifications alongside clinical care recommendations.

---

## 🚀 Project Architecture

The application is structured into an optimized layout, cleanly separating the backend logic layers from the dynamic presentation layer:

```text
├── app.py                  # Flask Web Controller & Routing Framework
├── rules.py                # Rule-Based Inference Mechanism (Forward Chaining)
├── templates/
│   └── index.html          # Dynamic User Interface (HTML5 / Jinja2 Template)
├── static/
│   └── style.css           # UI Styling Sheet & Responsive Layout Grid
└── README.md               # Project Documentation
