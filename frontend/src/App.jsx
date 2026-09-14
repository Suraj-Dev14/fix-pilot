import { useState } from "react";

function App() {
  const [incidentId, setIncidentId] = useState("INC-1001");
  const [service, setService] = useState("product-service");
  const [observedError, setObservedError] = useState("KeyError: price");

  async function handleSubmit(event) {
    event.preventDefault();

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

  const data = await response.json();

  console.log("Investigation result:", data);
  }

  return (
    <main>
      <h1>FixPilot</h1>
      <p>Autonomous Production Incident Investigator</p>

      <form onSubmit={handleSubmit}>
        <div>
          <label>Incident ID</label>
          <input
            value={incidentId}
            onChange={(event) => setIncidentId(event.target.value)}
          />
        </div>

        <div>
          <label>Service</label>
          <input
            value={service}
            onChange={(event) => setService(event.target.value)}
          />
        </div>

        <div>
          <label>Observed Error</label>
          <input
            value={observedError}
            onChange={(event) => setObservedError(event.target.value)}
          />
        </div>

        <button type="submit">Investigate Incident</button>
      </form>
    </main>
  );
}

export default App;