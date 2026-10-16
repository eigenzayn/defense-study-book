# Industry questions (model answers)

1. **Why does this matter to engineering?** — Thermal processes are often slow in temperature and fast in flow; if the flow can be recorded once, many temperature scenarios become cheap. My thesis measures when that works and when it does not.
2. **What did you implement yourself?** — The correction stage in the replay's user hook (limiter, direction weight, stability criterion), a recorded convective-flux channel, the energy-balance analysis and every figure from the solver files.
3. **How is the method evaluated?** — Against its own CFD reference, on four measures: mean temperature, height of the heat, heterogeneity and the end profile, plus the front width. Each correction is also checked for conservation and boundedness.
4. **Does acceleration compromise accuracy?** — The standard replay does: no mixing setting is right for both heat and layering. With the correction, front width and heat content come back in the test tank; the strength is tuned against the reference.
5. **What data and computing do you need?** — One full CFD recording per flow regime. For this small tank the database takes 2.4 GiB (3.1 GiB with the recorded flux, thesis Table 3.x on storage); a replay then takes about two minutes of solver time.
6. **How could this connect to process modelling?** — As a fast surrogate for temperature scenarios inside a regime that has been recorded, with physics checks as acceptance tests. This is a direction, not a result.
7. **What must be validated first?** — The process's own physics (turbulence, several phases, reaction heat), regime coverage, the error on the quantity the process cares about, and measurements.
8. **What is untested in your proposal?** — All three directions on slide 8: a learned mixing closure, regime-aware replay and physics-based acceptance tests for surrogates.
9. **Why should we fund this?** — I would not argue from a result I do not have. I can show how I find the cause of an error and how honestly I report the limit; that is what a research project needs.
10. **Unknown company specifics** — "I do not know your processes or data, so I would start by asking which regime and which quantity matter most to you."
