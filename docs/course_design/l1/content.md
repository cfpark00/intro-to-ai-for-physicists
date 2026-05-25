# L1 — Introduction

> Read `../README.md` first for course-wide context (philosophy, audience, spine).

## TL;DR
Philosophy, thesis, and a short history of ML/DL/AI. Parallel to neuroscience / neuroethology. Brief gesture at AI / foundation models / NN / SGD ("you all know what these are" — Harvard grad physics audience, no time wasted on basics). Closes on the bitter lesson, including what it doesn't mean.

This is the **thesis statement** of the course. Sets the experimentalist voice and the 5-step methodology that recurs in L7 and L11.

## Aim (user's exact phrasing)
"Introduction to this course's philosophy, and a short history of how current AI is the way it is."

## Flow sketch (verbatim from user — preserve voice)

> "Hi all, welcome to the second half: the experimentalist's view. Before diving into getting GPUs hot, we'll introduce the philosophy here... That being said there are many debates in the general science of intelligence often connecting to philosophy of science. The current paradigm is neural networks, but it's good to know there were always times where things were 'hated' and...
>
> In some sense I might slightly say: feel free to also not think in the theory way: there were cases where theory didn't help! Universal approximation theorem, XOR, or other impossibility results (over-parametrization) etc.
>
> Now on the practical side what has been mostly working is scaling. And we'll try to see what the bitter lesson means, and also what it doesn't."

**NOTE FOR STANDALONE COURSE:** The "second half: the experimentalist's view" framing assumes the joint Harvard offering with the theory prof. For the eventual standalone full course (~25 lectures), this opener needs rewording — there's no "first half" then.

## Topics

### Philosophy / methodology (the spine of L1)

The course mostly follows how physicists study biological systems. Neural networks in their natural habitat — designed for performance, trained on real-world data — are a **big mess**, not a cleanly defined problem. One way to study such systems borrows from **neuroethology**: the study of the neural basis of natural animal behavior in ecological context.

**The 5-step methodology** (also the spine of L7 and L11):

1. **Notice a phenomenon.** Start from an interesting behavior actually observed in a real neural network.
2. **Explore broadly.** Through extensive, open-ended exploration, narrow the phenomenon down to a clear question.
3. **Build a model system.** Develop a synthetic, controllable model that reproduces the phenomenon — small enough to instrument fully.
4. **Experiment on the model system.** Now that the system is tractable, run the kinds of experiments the original network doesn't allow.
5. **Cross-check.** Bring the findings back to the original big monster and verify they hold there.

The order won't always be strict — sometimes a theoretical hunch comes first, sometimes a model system precedes a crisp question — but this is the **guiding philosophy**.

Direct neuroethology parallel: observe animals → find a specific behavior (better if shared across species) → opens a clear question → run experiments on a *model organism* (Drosophila, *C. elegans*, zebrafish), often open-endedly → bring it back to the species that motivated the question.

"Overall, the science here is close in spirit to neurophysics, but takes a heavily experimental approach."

### Short history of AI / ML / DL

- **Connectionism vs symbolism.** Long-running debate. Connectionism (neural-network camp) has won the current paradigm — but tell the story.
- **History/philosophy of science.** How theory has often (nicely) been *against* ML progress:
  - **XOR-era impossibility / universal approximation theorem context** — early theoretical results said NNs couldn't do certain things; people stacked layers and proved them wrong.
  - **Over-parametrization "impossibility"** — classical statistical learning theory said overparametrized models would overfit. They didn't. We now have double descent, grokking, and a generalization mystery.
  - Pattern: when theory says "this can't work," sometimes it just means the theory wasn't general enough yet.
- "Things were 'hated' at various times" — neural networks went through multiple AI winters. Helpful context for students entering a field that *currently* feels like a settled paradigm.

### The bitter lesson (close the lecture on this)

- Sutton's bitter lesson: scaling + general methods consistently beat clever hand-engineering of priors.
- **But also discuss what it DOESN'T mean.** It's not "never think." It's "don't bake in clever priors when scaling will get there anyway." Many people misinterpret it as nihilism about research.
- This sets up L2's "first bitter lesson before scaling laws: bigger is better" and L5's full scaling-laws treatment.

### Quick gesture at the substrate (Harvard grad physicists already know this)

- What an AI / foundation model is — briefly. (~Foundation models go into the glossary.)
- Neural network — briefly.
- SGD — briefly.
- ~5 minutes total. Do not re-teach basics.

## HW

1. **Meta task** (~1 paragraph writing). Choose one or combine:
   - Find something AI cannot do.
   - Speculate about what AI probably still won't be as good as *you* at in 5 years.
   - Are scientists going to get replaced?
2. **Fun fact task.** Find a fun fact about NNs that the instructor doesn't know. **Must be something** — no opting out.

## Phenomena mentioned (briefly, for flavor)

- **Bitter lesson as a recurring pattern** — more compute + general methods > clever hand-engineering. Discuss exceptions and what the pattern doesn't claim.
- **XOR-era impossibility** — as a "theory was wrong" story.
- **Over-parametrized generalization** — as a phenomenon physicists will find weird and that L7 will dissect.

## Cross-references
- **5-step methodology** → revisited explicitly in **L7** (training dynamics phenomena, the first case study of the methodology) and **L11** (concept learning, the second case study).
- **"Bigger is better" intuition** → set up here as the "first bitter lesson," paid off in **L5** with full scaling laws.
- **Bitter lesson** → quoted again in **L2** and central to **L5**.

## Open questions / TBDs
- Reword "welcome to the second half" for the standalone version.
- Time budget for the "brief gesture at NN/SGD" — how brief is brief? (User said audience already knows it, gesture is enough.)
- Whether to formally introduce Tinbergen's four questions (neuroethology framework) or stay informal.
- Maybe add a slide on "why physicists are well-positioned for this kind of work" to motivate the experimentalist framing.

## Author voice notes
- Conversational, slightly irreverent ("getting GPUs hot," "feel free to also not think in the theory way").
- Acknowledges multiple paradigms (theory vs experimental, connectionism vs symbolism) without endorsing one rigidly.
- Wants students to feel they're entering an **open scientific frontier**, not memorizing a settled curriculum.
- Implicit: invites students to question whether even the *current* paradigm is the right one.
