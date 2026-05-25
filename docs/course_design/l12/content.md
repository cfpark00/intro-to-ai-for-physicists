# L12 — Science of Intelligence: From DL to General Intelligence

> Read `../README.md` first.

## TL;DR
Capstone lecture. Opens on the L11 ending (concepts as abstraction-scale phenomena → intelligence is broader than learning a task). Surveys forms of intelligence that go beyond gradient-trained single-agent learning: **evolution, multi-agent dynamics, quality-diversity, open-endedness, creativity, "learning" in its expansive sense**. Ends the course on a question rather than a topic list.

## Aim (user's verbatim)
"L12: Science of Intelligence: From DL to general intelligence. will mostly do a quick overview of a broader view of intelligence: evolution, multi-agent, quality diversity, open-endedness, creativity, 'learning'"

And:
> "L12 can start with that last time comment [from L11], and actually show that intelligence is a much broader phenomenon than learning a task"

## Phenomenon hooks (lecture is meta)
This lecture has fewer "phenomena" in the L7/L11 sense — it's more of a meta-tour. But possible framings:
- **Intelligence has emerged multiple times in nature via very different mechanisms** (evolution, individual learning, cultural learning) — pluralism as a phenomenon.
- **Open-endedness** as a *property* worth seeking — and one we don't yet know how to instantiate reliably in AI.

## Topics

### Opening (the bridge from L11)
- Recap the closing of L11: "what is a concept" → "learning at different abstraction scales."
- Move: if learning lives at multiple abstraction scales, **intelligence is broader than any single learning process.**
- This frames the rest of the lecture: a survey of intelligence-shaped phenomena beyond gradient learning.

### Evolution as a learning process
- Natural selection as an optimization process (no gradient, no centralized objective).
- Evolutionary methods in ML: evolution strategies, neuroevolution, genetic algorithms.
- When evolutionary methods compete with gradient methods (gradient-free RL settings).
- The deep parallel: NN training and evolution are both optimization, but they're not the same kind of optimization.

### Multi-agent intelligence
- **Self-play** — agents training against themselves (AlphaGo, AlphaZero lineage).
- **Nash equilibria** — game-theoretic framing.
- **Multi-agent RL** — emergent behaviors in mixed populations.
- Cooperative vs competitive dynamics.
- The phenomenon: intelligence can be a *property of a population*, not just an individual.

### Quality-diversity (QD)
- Search for *diverse* high-quality solutions, not just optimal ones.
- Novelty search, MAP-Elites.
- Connection to open-endedness.

### Open-endedness
- The aspiration: a learning process that keeps generating new challenges and new capabilities indefinitely.
- POET, OMNI-EPIC.
- Why this is interesting *as a research question* and currently hard.
- Connection to the cultural / evolutionary view of intelligence.

### Creativity
- What does it mean for a system to be creative?
- Surface examples (LLM-generated art, scientific discovery from AI).
- Honest about the ill-definedness — channel the L10 "shit-show debates" framing.

### "Learning" in the expansive view
- Once we've surveyed evolution, multi-agent, QD, open-endedness, creativity — what does "learning" even mean?
- The course's punchline: learning is a much broader phenomenon than the gradient-descent-on-a-loss picture L1 started with.
- Intelligence may be a property of *systems-with-objectives*, of which gradient learning is one instance.

### Brief touches (as time permits)
- **Knightian uncertainty** vs aleatory/epistemic uncertainty — true unknowns where probabilities don't apply.
- **Active learning** — choosing what to learn.
- Connection back to the author's long-term goal ("AI-driven scientific discovery") — what kind of intelligence do we need for *open-ended scientific research*?

### Capstone (close the course)
- The course began with neuroethology and a 5-step methodology.
- 12 lectures later, we've made the methodology concrete (L7, L11) and zoomed out to where it points (L12).
- Open invitation: students should now have the taste to recognize good science-of-DL questions and contribute.

## HW
TBD. The natural HW here is the **project** (presented separately, after this lecture). Could also include a final essay reflecting on the course's framing.

## Cross-references
- **L1 (Introduction)** — bookends the course. L1 set the methodology; L12 zooms out to where it leads.
- **L9 (RL)** — multi-agent, evolutionary, self-play introduced lightly there, deepened here.
- **L11 (Concept Learning)** — direct setup; opens from L11's ending.
- **L10 (World Models)** — "ill-defined debates" framing reused for intelligence/creativity.

## Open questions / TBDs
- Lecture is most at risk of being a grab-bag. Author should pick the through-line (probably "learning at abstraction scales → intelligence as broader") and discipline the content to it.
- How much technical depth vs survey breadth? Lean: survey breadth — this is a capstone, not a deep dive.
- Where does **individuality** (author's industry focus, mentioned briefly) fit? Author indicated it's not load-bearing.
- The role of the **Project presentation** session (separate, not numbered) — how does it relate to this lecture?

## Author voice notes
- Resist the encyclopedia trap. Pick a through-line and stick with it.
- End on a question, not a list. The course is supposed to leave students wanting to investigate, not feeling they "covered" anything.
- This is where the author's long-term research vision ("AI-driven scientific discovery") can finally land explicitly.
