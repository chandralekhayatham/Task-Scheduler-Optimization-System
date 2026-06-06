import React, { useState } from "react";
import "./App.css";

function App() {
  const [data, setData] = useState(null);

  async function loadSchedule() {
    try {
      const response = await fetch("http://127.0.0.1:8000/schedule");
      const result = await response.json();
      setData(result);
    } catch (error) {
      alert("Backend Connection Failed!");
    }
  }

  return (
    <div className="container">

      <h1>Task Scheduler Optimization System</h1>

      <p className="subtitle">
        Smart Task Scheduling using Greedy Algorithm
      </p>

      <button onClick={loadSchedule}>
        Generate Schedule
      </button>

      {data && (
        <div className="card">

          <h2>{data.algorithm}</h2>

          <div className="task-container">
            {data.tasks.map((task, index) => (
              <div className="task-card" key={index}>
                <h3>📋 {task.task_id}</h3>
                <p>⏰ Start : {task.start}</p>
                <p>🏁 End : {task.end}</p>
              </div>
            ))}
          </div>

          <h2>Timeline</h2>

          <div className="timeline">

            <div className="timeline-row">
              <span>T1</span>
              <div className="timeline-bar bar1">
                0 - 2
              </div>
            </div>

            <div className="timeline-row">
              <span>T2</span>
              <div className="timeline-bar bar2">
                2 - 5
              </div>
            </div>

            <div className="timeline-row">
              <span>T3</span>
              <div className="timeline-bar bar3">
                5 - 7
              </div>
            </div>

          </div>

          <div className="stats">

            <div className="box">
              <h3>{data.metrics.total_tasks}</h3>
              <p>📊 Total Tasks</p>
            </div>

            <div className="box">
              <h3>{data.metrics.total_duration}</h3>
              <p>⏱ Total Duration</p>
            </div>

            <div className="box">
              <h3>Greedy</h3>
              <p>⚡ Algorithm</p>
            </div>

          </div>

        </div>
      )}

      <footer>
        Task Scheduler Optimization System © 2026
        <br />
        Developed using FastAPI + React.js
      </footer>

    </div>
  );
}

export default App;