![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg) ![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)

# Management Thesis Defense Examiner Skill

A prompt skill that turns any AI into a rigorous **thesis defense committee examiner**, helping graduate students self-check their thesis's theoretical foundation, research design, methodological rigor, and academic writing standards before blind review or external examination.

---

## ✨ Features

- 🎭 **Role-Playing Examiner** — The AI acts as a sharp, rigorous management school defense committee member, simulating real defense pressure
- 🧩 **Systematic Questioning Framework** — Six progressive layers: Theoretical Foundation → Model Specification → Variables & Scales → Research Design → Academic Expression → Soul-Searching Questions
- ⚡ **One-Round Focus Principle** — Only 1–2 key questions per round, giving students ample room to respond
- 🛡️ **Red Flag Warning System** — Built-in checklist of common "automatic fail" issues in external reviews
- 📊 **Multi-Dimension Revision Checklist** — Auto-generates a five-dimension improvement plan (Theory / Method / Design / Language / Format) at the end of the defense
- 📚 **Embedded Question Bank** — Covers mainstream management research paradigms (surveys, experiments, secondary data, grounded theory, etc.)
- 🔄 **Multi-Platform Compatible** — The `SKILL.md` file works directly with ChatGPT, Claude, Kimi, DeepSeek, and other major LLMs
- 🧪 **Sample Dialogue** — Complete fictional defense conversation examples to help you get started quickly

---

## 🚀 Quick Start

### Step 1: Get SKILL.md

Clone or download this repository, then locate the `SKILL.md` file.

```bash
git clone https://github.com/GZgreywolfy/management-thesis-defense-examiner.git
```

### Step 2: Feed It as a System Prompt

The setup varies slightly depending on which AI platform you use:

| Platform | How to Set Up |
|----------|---------------|
| **ChatGPT** | Start a new chat → Click avatar (bottom-left) → **Custom Instructions** → Paste entire `SKILL.md` into the "What would you like ChatGPT to know about you to provide better responses?" field |
| **Claude** | Create a new Project → Open **System Prompt** settings → Paste `SKILL.md` content |
| **Kimi** | Start a new conversation → Click "+" to add a custom template → Paste `SKILL.md` as the system prompt |
| **DeepSeek** | Start a new conversation → Paste `SKILL.md` into the system prompt field |

### Step 3: Start Your Mock Defense

Once the prompt is loaded, send your thesis abstract / research topic / model description / defense statement to the AI. It will automatically role-play as a defense examiner and begin questioning.

**Recommended opening statement:**

> Good morning, professors. My thesis is titled "[Your Title]", based on [Theory Name]. I constructed a model with [variables], collected data through [method], and the main findings are [results]. Please feel free to ask questions.

---

## 💬 Usage Example

Below is a fictional mock defense dialogue excerpt (all data is synthetic and does not involve any real individuals or institutions):

---

### Round 1: Student Statement → Examiner Questioning

**Student:**

> Good morning, professors. My thesis is titled *"The Impact of Intelligent Recommendation Algorithms on User Content Consumption Depth — From the Perspective of Information Foraging Theory"*. Drawing on Information Foraging Theory, I set content novelty (information scent intensity) as the independent variable, user content consumption depth (a composite of reading completion rate + dwell time) as the dependent variable, perceived information redundancy as the mediator, and need for cognitive closure as the moderator, with a total of 5 hypotheses. I obtained 15,000 user behavioral log records from a content platform and conducted multi-level linear regression analysis using Python. The results show that content novelty significantly and positively affects consumption depth, perceived information redundancy plays a partial mediating role, and the moderating effect of need for cognitive closure is significant at low levels.

**Mock Examiner:**

> Interesting topic. Applying Information Foraging Theory to recommendation algorithms does have theoretical appeal. Let me start with a fundamental question — how exactly did you operationalize "content novelty"? In Information Foraging Theory, "information scent" is a perceptual construct, yet you mention using backend log data. How do you infer users' *perceived* novelty from log data? There's a construct-measurement alignment issue here that I'd like you to address.

---

### Round 2: Student Response → Examiner Follow-Up

**Student:**

> I measured content novelty using the proportion of recommended articles that the user did not click on... but I didn't conduct a manipulation check for the perceptual dimension.

**Mock Examiner:**

> That's exactly the point I want to press. You're using a behavioral proxy variable (non-click ratio) to measure a perceptual construct (information scent). In the methodology literature, this is called "measurement mismatch." If you haven't done any manipulation check or pilot study to validate this proxy, an external reviewer will almost certainly flag it. My suggestion: either add a pilot study (e.g., measure perceived novelty with a Likert scale and check its correlation with your behavioral proxy), or reframe your research question around "recommendation diversity" instead of "perceived novelty" to match your measurement. Which approach do you prefer?

---

> 💡 **Tip:** For the complete sample dialogue (with multiple rounds), see [`examples/sample-dialogue.md`](./examples/sample-dialogue.md).

---

## 📂 Directory Structure

```
management-thesis-defense-examiner/
├── SKILL.md                    # Core system prompt file (feed this to the AI)
├── README.md                   # Chinese documentation
├── README.en.md                # This file (English documentation)
├── LICENSE                     # MIT License
├── .gitignore                  # Git ignore rules
├── replace_authors.py          # Script to batch-replace placeholder author names
├── examples/
│   └── sample-dialogue.md      # Fictional mock defense dialogue example
└── knowledge/
    ├── question-bank.md        # Examiner question bank (organized by review dimension)
    └── red-flags.md            # External review / blind review red flag checklist
```

---

## 🔒 Privacy Notice

The questioning logic in this project is distilled from common patterns observed in real thesis defense settings, but all content has been fully de-identified: it contains no real names, universities, classes, actual research topics, or personally identifiable information. All sample dialogues are fictional synthetic data. Original source materials have never been and will never be included in this repository.

**User caution:** When using this Skill, do not input thesis content that contains real personal information (names, student IDs, advisor information, etc.). If your thesis already contains such information, we recommend anonymizing it first.

---

## 🤝 Contribution Guide

We welcome all forms of contribution — whether it's a new idea, a bug report, or code.

### Submitting an Issue

If you have a suggestion or found a problem, feel free to [open an Issue](https://github.com/GZgreywolfy/management-thesis-defense-examiner/issues/new):

1. Clearly describe your suggestion or problem
2. For feature requests, explain the expected behavior and use case
3. For bug reports, include reproduction steps and environment details

### Submitting a Pull Request

1. Fork this repository
2. Create your feature branch: `git checkout -b feat/amazing-feature`
3. Commit your changes: `git commit -m 'feat: add amazing feature'`
4. Push to the branch: `git push origin feat/amazing-feature`
5. Open a Pull Request

### Local Development

```bash
# Clone the repository
git clone https://github.com/GZgreywolfy/management-thesis-defense-examiner.git
cd management-thesis-defense-examiner

# Install dependencies (if there are Python helper scripts)
pip install -r requirements.txt  # if applicable

# After modifying SKILL.md or files under knowledge/, use replace_authors.py to ensure placeholder consistency
python replace_authors.py --check
```

### Contribution Guidelines

- All sample dialogues must be fictional data and must not contain real names, institutions, or research topics
- Questioning logic should follow mainstream management research paradigms
- New knowledge entries should be supported by references to academic literature

---

## 🗺️ Roadmap

### v1.0 (Current Release)
- ✅ Core SKILL.md system prompt
- ✅ Six-layer progressive questioning framework
- ✅ Basic question bank and red flag checklist
- ✅ Fictional mock defense dialogue examples

### v1.1 (Planned)
- 🔄 Sub-skills for different management disciplines (HR, Marketing, Strategic Management, etc.)
- 🔄 Bilingual (Chinese/English) examination mode
- 🔄 More sample dialogues including "mistake → correction" demonstrations

### v1.2 (In Planning)
- ⏳ Student answer quality auto-assessment module
- ⏳ Defense slide checklist
- ⏳ Interactive web-based mock defense application (wrapping this Skill)

### Long-term Vision
- 🌟 Community-built multi-examiner defense committee (multi-role AI simultaneous review)
- 🌟 Integration with thesis writing tools for "pre-submission review" capability

---

## 📄 License

This project is open-sourced under the MIT License — see the [LICENSE](./LICENSE) file for details.

---

<p align="center">Made with ❤️ for better thesis defense preparation</p>