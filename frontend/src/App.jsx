import { useState } from "react";

function App() {
  const [incidentId, setIncidentId] = useState("INC-1001");
  const [service, setService] = useState("product-service");
  const [observedError, setObservedError] = useState("KeyError: price");

  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function handleSubmit(event) {
    event.preventDefault();

    setLoading(true);
    setError("");
    setResult(null);

    try {
      const response = await fetch("http://127.0.0.1:8000/investigate", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          incident_id: incidentId,
          service,
          observed_error: observedError,
        }),
      });

      if (!response.ok) {
        throw new Error(`API request failed: ${response.status}`);
      }

      const data = await response.json();

      console.log("Investigation result:", data);

      setResult(data);
    } catch (err) {
      console.error("Investigation failed:", err);
      setError(err.message || "Something went wrong");
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="min-h-screen bg-slate-950 text-white">
      {/* Background */}
      <div className="absolute inset-0 overflow-hidden pointer-events-none">
        <div className="absolute -top-40 -left-40 h-96 w-96 rounded-full bg-blue-500/10 blur-3xl" />
        <div className="absolute top-1/3 -right-40 h-96 w-96 rounded-full bg-violet-500/10 blur-3xl" />
        <div className="absolute bottom-0 left-1/3 h-72 w-72 rounded-full bg-cyan-500/5 blur-3xl" />
      </div>

      <div className="relative mx-auto flex min-h-screen max-w-7xl flex-col px-6 py-8">
        {/* Header */}
        <header className="flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-blue-500/10 ring-1 ring-blue-400/20">
              <span className="text-lg font-bold text-blue-400">F</span>
            </div>

            <div>
              <h1 className="text-lg font-semibold tracking-tight">
                Fix<span className="text-blue-400">Pilot</span>
              </h1>
              <p className="text-xs text-slate-500">
                Production Intelligence
              </p>
            </div>
          </div>
        </header>

        {/* Main */}
        <section className="flex flex-1 justify-center py-16">
          <div className="w-full max-w-3xl">
            {/* Hero */}
            <div className="mb-10 text-center">
              <div className="mb-5 inline-flex items-center gap-2 rounded-full border border-slate-800 bg-slate-900/80 px-4 py-2">
                <span className="text-blue-400">✦</span>
                <span className="text-sm text-slate-400">
                  Autonomous Incident Investigation
                </span>
              </div>

              <h2 className="text-4xl font-bold tracking-tight sm:text-5xl">
                Investigate production
                <span className="block bg-gradient-to-r from-blue-400 via-cyan-400 to-violet-400 bg-clip-text text-transparent">
                  incidents faster.
                </span>
              </h2>

              <p className="mx-auto mt-5 max-w-xl text-base leading-7 text-slate-400">
                Give FixPilot the incident details. The autonomous agent
                investigates logs, API responses, deployments, code changes,
                and regression tests to identify the root cause.
              </p>
            </div>

            {/* Investigation Card */}
            <div className="rounded-2xl border border-slate-800 bg-slate-900/80 p-1 shadow-2xl shadow-black/20 backdrop-blur-xl">
              <div className="rounded-xl border border-slate-800/70 bg-slate-950/80 p-6 sm:p-8">
                {/* Card Header */}
                <div className="mb-7 flex items-start justify-between">
                  <div>
                    <h3 className="text-lg font-semibold">
                      Start Investigation
                    </h3>

                    <p className="mt-1 text-sm text-slate-500">
                      Provide the details of the production incident.
                    </p>
                  </div>

                  <div className="hidden rounded-lg bg-blue-500/10 px-3 py-2 text-xs font-medium text-blue-400 sm:block">
                    AI Agent
                  </div>
                </div>

                <form onSubmit={handleSubmit} className="space-y-5">
                  {/* Incident ID */}
                  <div>
                    <label
                      htmlFor="incidentId"
                      className="mb-2 block text-sm font-medium text-slate-300"
                    >
                      Incident ID
                    </label>

                    <input
                      id="incidentId"
                      type="text"
                      placeholder="e.g. INC-1001"
                      value={incidentId}
                      onChange={(event) => setIncidentId(event.target.value)}
                      className="w-full rounded-xl border border-slate-800 bg-slate-900 px-4 py-3.5 text-sm text-white outline-none transition placeholder:text-slate-600 hover:border-slate-700 focus:border-blue-500 focus:ring-4 focus:ring-blue-500/10"
                    />
                  </div>

                  {/* Service */}
                  <div>
                    <label
                      htmlFor="service"
                      className="mb-2 block text-sm font-medium text-slate-300"
                    >
                      Service
                    </label>

                    <input
                      id="service"
                      type="text"
                      placeholder="e.g. product-service"
                      value={service}
                      onChange={(event) => setService(event.target.value)}
                      className="w-full rounded-xl border border-slate-800 bg-slate-900 px-4 py-3.5 text-sm text-white outline-none transition placeholder:text-slate-600 hover:border-slate-700 focus:border-blue-500 focus:ring-4 focus:ring-blue-500/10"
                    />
                  </div>

                  {/* Error */}
                  <div>
                    <div className="mb-2 flex items-center justify-between">
                      <label
                        htmlFor="observedError"
                        className="text-sm font-medium text-slate-300"
                      >
                        Observed Error
                      </label>

                      <span className="text-xs text-slate-600">
                        Error message or symptom
                      </span>
                    </div>

                    <textarea
                      id="observedError"
                      rows={4}
                      placeholder="e.g. KeyError: price"
                      value={observedError}
                      onChange={(event) =>
                        setObservedError(event.target.value)
                      }
                      className="w-full resize-none rounded-xl border border-slate-800 bg-slate-900 px-4 py-3.5 font-mono text-sm text-white outline-none transition placeholder:text-slate-600 hover:border-slate-700 focus:border-blue-500 focus:ring-4 focus:ring-blue-500/10"
                    />
                  </div>

                  {/* Submit */}
                  <button
                    type="submit"
                    disabled={loading}
                    className="group flex w-full items-center justify-center gap-3 rounded-xl bg-blue-500 px-5 py-3.5 text-sm font-semibold text-white shadow-lg shadow-blue-500/20 transition hover:bg-blue-400 hover:shadow-blue-500/30 active:scale-[0.99] disabled:cursor-not-allowed disabled:opacity-60"
                  >
                    {loading ? (
                      <>
                        <span className="h-4 w-4 animate-spin rounded-full border-2 border-white/30 border-t-white" />
                        <span>Investigating...</span>
                      </>
                    ) : (
                      <>
                        <span>Investigate Incident</span>

                        <span className="transition-transform group-hover:translate-x-1">
                          →
                        </span>
                      </>
                    )}
                  </button>
                </form>

                {/* API Error */}
                {error && (
                  <div className="mt-6 rounded-xl border border-red-500/20 bg-red-500/5 p-4">
                    <p className="text-sm font-medium text-red-400">
                      Investigation failed
                    </p>
                    <p className="mt-1 text-sm text-red-400/70">{error}</p>
                  </div>
                )}
              </div>
            </div>

            {/* ================= RESULT ================= */}
            {result && (
              <div className="mt-8 space-y-5">
                {/* Result Header */}
                <div className="flex items-center justify-between">
                  <div>
                    <h3 className="text-xl font-semibold">
                      Investigation Result
                    </h3>

                    <p className="mt-1 text-sm text-slate-500">
                      Analysis generated by the FixPilot agent
                    </p>
                  </div>

                  <div className="rounded-lg bg-emerald-500/10 px-3 py-2 text-xs font-medium text-emerald-400">
                    Investigation Complete
                  </div>
                </div>

                {/* Incident Info */}
                <div className="rounded-2xl border border-slate-800 bg-slate-900/80 p-6">
                  <div className="grid gap-5 sm:grid-cols-3">
                    <div>
                      <p className="text-xs font-medium uppercase tracking-wider text-slate-600">
                        Incident
                      </p>

                      <p className="mt-2 font-mono text-sm text-white">
                        {result.incident_id}
                      </p>
                    </div>

                    <div>
                      <p className="text-xs font-medium uppercase tracking-wider text-slate-600">
                        Service
                      </p>

                      <p className="mt-2 text-sm text-white">
                        {service}
                      </p>
                    </div>

                    <div>
                      <p className="text-xs font-medium uppercase tracking-wider text-slate-600">
                        Observed Error
                      </p>

                      <p className="mt-2 font-mono text-sm text-red-400">
                        {result.observed_evidence?.[0] || observedError}
                      </p>
                    </div>
                  </div>
                </div>

                {/* Root Cause */}
                <div className="rounded-2xl border border-blue-500/20 bg-blue-500/5 p-6">
                  <div className="mb-3 flex items-center gap-3">
                    <div className="flex h-8 w-8 items-center justify-center rounded-lg bg-blue-500/10 text-blue-400">
                      !
                    </div>

                    <h4 className="font-semibold text-white">
                      Root Cause
                    </h4>
                  </div>

                  <p className="text-sm leading-7 text-slate-300">
                    {result.root_cause}
                  </p>
                </div>

                {/* Evidence */}
                <div className="rounded-2xl border border-slate-800 bg-slate-900/80 p-6">
                  <h4 className="mb-4 font-semibold">
                    Observed Evidence
                  </h4>

                  <div className="space-y-3">
                    {result.observed_evidence?.map((item, index) => (
                      <div
                        key={index}
                        className="flex gap-3 rounded-xl bg-slate-950/70 p-4"
                      >
                        <span className="mt-0.5 text-blue-400">•</span>

                        <p className="text-sm leading-6 text-slate-300">
                          {item}
                        </p>
                      </div>
                    ))}
                  </div>
                </div>

                {/* Inferences */}
                <div className="rounded-2xl border border-slate-800 bg-slate-900/80 p-6">
                  <h4 className="mb-4 font-semibold">
                    Inferences
                  </h4>

                  <div className="space-y-3">
                    {result.inferences?.map((item, index) => (
                      <div
                        key={index}
                        className="flex gap-3 rounded-xl bg-slate-950/70 p-4"
                      >
                        <span className="text-violet-400">→</span>

                        <p className="text-sm leading-6 text-slate-300">
                          {item}
                        </p>
                      </div>
                    ))}
                  </div>
                </div>

                {/* Recommendations */}
                <div className="rounded-2xl border border-amber-500/20 bg-amber-500/5 p-6">
                  <h4 className="mb-4 font-semibold text-amber-300">
                    Recommendations
                  </h4>

                  <div className="space-y-3">
                    {result.recommendations?.map((item, index) => (
                      <div
                        key={index}
                        className="flex gap-3 rounded-xl bg-slate-950/50 p-4"
                      >
                        <span className="text-amber-400">✓</span>

                        <p className="text-sm leading-6 text-slate-300">
                          {item}
                        </p>
                      </div>
                    ))}
                  </div>
                </div>

                {/* Unresolved Hypotheses */}
                <div className="rounded-2xl border border-slate-800 bg-slate-900/80 p-6">
                  <h4 className="mb-4 font-semibold">
                    Unresolved Hypotheses
                  </h4>

                  {result.unresolved_hypotheses?.length > 0 ? (
                    <div className="space-y-3">
                      {result.unresolved_hypotheses.map((item, index) => (
                        <div
                          key={index}
                          className="flex gap-3 rounded-xl bg-slate-950/70 p-4"
                        >
                          <span className="text-slate-500">?</span>

                          <p className="text-sm leading-6 text-slate-400">
                            {item}
                          </p>
                        </div>
                      ))}
                    </div>
                  ) : (
                    <p className="text-sm text-slate-500">
                      No unresolved hypotheses.
                    </p>
                  )}
                </div>
              </div>
            )}
          </div>
        </section>
      </div>
    </main>
  );
}

export default App;