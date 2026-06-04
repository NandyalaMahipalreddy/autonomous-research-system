import React, { useState } from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import { useEffect } from "react";
import {
  PieChart,
  Pie,
  Cell,
  Tooltip,
  ResponsiveContainer,
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid
} from "recharts";

const API_URL = "https://autonomous-research-system-47qs.onrender.com";

function App() {
  const [query, setQuery] = useState("");
  const [report, setReport] = useState("");
  const [pdfFile, setPdfFile] = useState("");
  const [loading, setLoading] = useState(false);
  const [history, setHistory] = useState([]);
  const [agentStatus, setAgentStatus] = useState([]);
  const [file, setFile] = useState(null);

  const [depth, setDepth] = useState("Medium");
  const [maxIterations, setMaxIterations] = useState(5);
  const [costLimit, setCostLimit] = useState(2);
  const [outputFormat, setOutputFormat] = useState("PDF");

  const [tokensUsed, setTokensUsed] = useState(0);
  const [estimatedCost, setEstimatedCost] = useState(0);
  const [budgetLimit, setBudgetLimit] = useState(0);
  const [cost, setCost] = useState(0);

  const [searchCount, setSearchCount] = useState(0);

  const [llmCalls, setLlmCalls] = useState(0);
const costData = [
  { day: "Mon", cost: 0.001 },
  { day: "Tue", cost: 0.002 },
  { day: "Wed", cost: 0.003 },
  { day: "Thu", cost: 0.004 },
  { day: "Fri", cost: 0.002 }
];

  const pieData = [
  { name: "Web Research", value: 65 },
  { name: "Documents", value: 20 },
  { name: "History", value: 10 },
  { name: "Manual", value: 5 }
];



const COLORS = [
  "#3B82F6",
  "#22C55E",
  "#F59E0B",
  "#EF4444"
];

  const loadHistory = async () => {
  try {
    const response = await fetch(`${API_URL}/history`);

    const data = await response.json();

    setHistory(data);

  } catch (error) {
    console.error(error);
  }
};

const loadReport = async (id) => {

  try {

    const response = await fetch(`${API_URL}/history/${id}`);

    const data = await response.json();

    setReport(data.report);

  } catch (error) {

    console.error(error);

  }
};

const deleteHistory = async (id) => {

  try {

    await fetch(`${API_URL}/history/${id}`,
      {
        method: "DELETE"
      }
    );

    loadHistory();

  } catch (error) {

    console.error(error);

  }
};

useEffect(() => {
  loadHistory();
}, []);

  const handleResearch = async () => {
    if (!query.trim()) return;

    setLoading(true);
    setReport("");

    setAgentStatus([
      "🧠 Planner Agent → Running...",
      "🌐 Web Research Agent → Running...",
      "✅ Fact Checker Agent → Running...",
      "⚠️ Contradiction Checker → Running...",
      "📄 Formatter Agent → Running...",
    ]);

    try {
      const formData = new FormData();

      formData.append("query", query);
      formData.append("depth", depth);
      formData.append("max_iterations", maxIterations);
      formData.append("cost_limit", costLimit);
      formData.append("output_format", outputFormat);

      if (file) {
        formData.append("file", file);
      }

      const response = await fetch(
  `${API_URL}/research`,
        {
          method: "POST",
          body: formData,
        }
      );

      const data = await response.json();
      setCost(data.total_cost);

      setSearchCount(data.search_count);

      setLlmCalls(data.llm_calls);

      setAgentStatus([
        "🧠 Planner Agent → Completed",
        "🌐 Web Research Agent → Completed",
        "✅ Fact Checker Agent → Completed",
        "⚠️ Contradiction Checker → Completed",
        "📄 Formatter Agent → Completed",
      ]);

      setReport(data.report);
      setPdfFile(data.pdf_file);

setTokensUsed(data.tokens_used);

setEstimatedCost(data.estimated_cost);

setBudgetLimit(data.budget_limit);

await loadHistory();
      await loadHistory();

    } catch (error) {
      console.error(error);
      setReport("Something went wrong while generating report.");
    }

    setLoading(false);
  };

  const inputStyle = {
    width: "100%",
    padding: "16px",
    fontSize: "18px",
    borderRadius: "12px",
    border: "none",
    outline: "none",
  };

  const cardStyle = {
  background: "rgba(255,255,255,0.08)",
  padding: "20px",
  borderRadius: "16px",
  textAlign: "center",
  color: "white"
};
  return (
    <div
      style={{
        minHeight: "100vh",
        background:
          "linear-gradient(135deg, #0f172a 0%, #1e293b 40%, #2563eb 100%)",
        color: "white",
        padding: "40px",
        fontFamily: "Segoe UI",
      }}
    >
      <div style={{ maxWidth: "1300px", margin: "auto" }}>
        <h1
          style={{
            fontSize: "56px",
            fontWeight: "700",
            marginBottom: "12px",
          }}
        >
          Autonomous Multi-Agent Research System
        </h1>

      


        <p
          style={{
            fontSize: "18px",
            opacity: 0.9,
            marginBottom: "40px",
          }}
        >
          AI-powered research using Planner, Web Research, Fact Checker &
          Formatter Agents
        </p>

        {/* Search Row */}
        <div
          style={{
            display: "grid",
            gridTemplateColumns: "2fr 1fr auto",
            gap: "20px",
            marginBottom: "30px",
          }}
        >
          <input
            type="text"
            placeholder="Enter any research topic..."
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            style={inputStyle}
          />

          <div
            style={{
              background: "rgba(255,255,255,0.1)",
              padding: "16px",
              borderRadius: "12px",
            }}
          >
            <input
              type="file"
              accept=".pdf"
              onChange={(e) => setFile(e.target.files[0])}
              style={{ color: "white" }}
            />
          </div>

          <button
            onClick={handleResearch}
            style={{
              background: "#3b82f6",
              color: "white",
              border: "none",
              borderRadius: "12px",
              padding: "16px 28px",
              fontSize: "18px",
              cursor: "pointer",
              fontWeight: "600",
            }}
          >
            Start Research
          </button>
        </div>

        {/* Config Panel */}
        <div
          style={{
            display: "grid",
            gridTemplateColumns: "repeat(4, 1fr)",
            gap: "20px",
            marginBottom: "30px",
          }}
        >
          <div>
            <label>Research Depth</label>
            <select
              value={depth}
              onChange={(e) => setDepth(e.target.value)}
              style={inputStyle}
            >
              <option>Low</option>
              <option>Medium</option>
              <option>High</option>
            </select>
          </div>

          <div>
            <label>Max Iterations</label>
            <input
              type="number"
              value={maxIterations}
              onChange={(e) => setMaxIterations(e.target.value)}
              style={inputStyle}
            />
          </div>

          <div>
            <label>Cost Limit</label>
            <input
              type="number"
              value={costLimit}
              onChange={(e) => setCostLimit(e.target.value)}
              style={inputStyle}
            />
          </div>

          <div>
            <label>Output Format</label>
            <select
              value={outputFormat}
              onChange={(e) => setOutputFormat(e.target.value)}
              style={inputStyle}
            >
              <option>PDF</option>
              <option>Markdown</option>
            </select>
          </div>
        </div>

        {/* Recent Searches */}
        <div
  style={{
    marginTop: "25px",
    background: "rgba(255,255,255,0.08)",
    padding: "20px",
    borderRadius: "14px",
  }}
>
  <h2>Research History</h2>

  {history.length === 0 ? (
    <p>No history available.</p>
  ) : (
    history.map((item) => (
      <div
        key={item.id}
        style={{
          background: "#334155",
          padding: "12px",
          borderRadius: "10px",
          marginBottom: "10px",
        }}
      >
        <div
  style={{
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center"
  }}
>
  <button
    onClick={() => loadReport(item.id)}
    style={{
      background: "transparent",
      border: "none",
      color: "#60a5fa",
      cursor: "pointer",
      fontSize: "16px",
      fontWeight: "bold"
    }}
  >
    {item.query}
  </button>

  <button
    onClick={() => deleteHistory(item.id)}
    style={{
      background: "#ef4444",
      color: "white",
      border: "none",
      padding: "6px 12px",
      borderRadius: "8px",
      cursor: "pointer"
    }}
  >
    Delete
  </button>
</div>

        <div style={{ fontSize: "12px" }}>
          Cost: ${item.cost}
        </div>

        <div style={{ fontSize: "12px" }}>
          {item.created_at}
        </div>
      </div>
    ))
  )}
</div>


        {/* Live Agent Trace */}
        {agentStatus.length > 0 && (
          <div
            style={{
              background: "rgba(255,255,255,0.08)",
              padding: "25px",
              borderRadius: "16px",
              marginBottom: "30px",
            }}
          >
            <h2>Live Agent Trace</h2>

            {agentStatus.map((agent, index) => (
              <p key={index}>{agent}</p>
            ))}
          </div>
        )}


        {/* Loading */}
        {loading && (
          <h3 style={{ marginBottom: "20px" }}>
            Research in progress...
          </h3>
        )}

<div
  style={{
    display: "grid",
    gridTemplateColumns: "1fr 1fr",
    gap: "20px",
    marginTop: "25px",
    marginBottom: "25px",
  }}
>
  <div
    style={{
      background: "rgba(255,255,255,0.08)",
      padding: "20px",
      borderRadius: "14px",
    }}
  >
    <h2>Cost Tracking</h2>

    <p>🔢 Tokens Used: {tokensUsed}</p>
    <p>💰 Estimated Cost: ${estimatedCost}</p>
    <p>🎯 Budget Limit: ${budgetLimit}</p>
  </div>

  <div
    style={{
      background: "rgba(255,255,255,0.08)",
      padding: "20px",
      borderRadius: "14px",
    }}
  >
    <h2>Research Statistics</h2>

    <p>🔍 Searches: {searchCount}</p>

    <p>🤖 LLM Calls: {llmCalls}</p>

    <p>💰 Cost: ${cost.toFixed(4)}</p>
  </div>
</div>

<div
  style={{
    display: "grid",
    gridTemplateColumns: "repeat(4,1fr)",
    gap: "20px",
    marginBottom: "30px",
  }}
>
  <div style={cardStyle}>
    <h3>Total Jobs</h3>
    <h1>{history.length}</h1>
  </div>

  <div style={cardStyle}>
    <h3>Total Searches</h3>
    <h1>{searchCount}</h1>
  </div>

  <div style={cardStyle}>
    <h3>LLM Calls</h3>
    <h1>{llmCalls}</h1>
  </div>

  <div style={cardStyle}>
    <h3>Total Cost</h3>
    <h1>${cost.toFixed(4)}</h1>
  </div>
</div>

{/* Full Width Cost Trend */}

<div
  style={{
    background: "rgba(255,255,255,0.08)",
    padding: "25px",
    borderRadius: "20px",
    marginBottom: "25px",
    width: "95%"
  }}
>
  <h2
    style={{
      marginBottom: "20px"
    }}
  >
    📈 Cost Trend
  </h2>

  <ResponsiveContainer
    width="100%"
    height={350}
  >
    <LineChart
      data={costData}
    >
      <CartesianGrid
        strokeDasharray="3 3"
      />

      <XAxis
  dataKey="day"
  tick={{
    fill: "#ffffff",
    fontSize: 14,
    fontWeight: "bold"
  }}
/>

<YAxis
  tick={{
    fill: "#ffffff",
    fontSize: 14
  }}
/>

      <Tooltip />

      <Line
        type="monotone"
        dataKey="cost"
        stroke="#3b82f6"
        strokeWidth={4}
      />
    </LineChart>
  </ResponsiveContainer>
</div>

<div
  style={{
    display: "grid",
    gridTemplateColumns: "1fr 1fr 1fr",
    gap: "20px",
    marginBottom: "30px",
  }}
>


  {/* Research Sources */}

  <div
    style={{
      background: "rgba(255,255,255,0.08)",
      padding: "20px",
      borderRadius: "16px",
    }}
  >
    <h2>Research Sources</h2>

    <ResponsiveContainer width="100%" height={250}>
      <PieChart>
        <Pie
          data={pieData}
          dataKey="value"
          outerRadius={80}
        >
          {pieData.map((entry, index) => (
            <Cell
              key={index}
              fill={COLORS[index]}
            />
          ))}
        </Pie>

        <Tooltip />
      </PieChart>
    </ResponsiveContainer>
  </div>

  {/* Agent Activity */}

  <div
    style={{
      background: "rgba(255,255,255,0.08)",
      padding: "20px",
      borderRadius: "16px",
    }}
  >
    <h2>Agent Activity</h2>

    <p>Planner</p>

    <div
      style={{
        height: "12px",
        background: "#22c55e",
        width: "100%",
        borderRadius: "10px",
        marginBottom: "15px",
      }}
    />

    <p>Web Research</p>

    <div
      style={{
        height: "12px",
        background: "#3b82f6",
        width: "95%",
        borderRadius: "10px",
        marginBottom: "15px",
      }}
    />

    <p>Fact Checker</p>

    <div
      style={{
        height: "12px",
        background: "#f59e0b",
        width: "90%",
        borderRadius: "10px",
        marginBottom: "15px",
      }}
    />

    <p>Formatter</p>

    <div
      style={{
        height: "12px",
        background: "#ef4444",
        width: "100%",
        borderRadius: "10px",
      }}
    />
  </div>

  {/* Contradiction Rate */}

  <div
    style={{
      background: "rgba(255,255,255,0.08)",
      padding: "20px",
      borderRadius: "16px",
      textAlign: "center",
    }}
  >
    <h2>Contradiction Rate</h2>

    <h1
      style={{
        fontSize: "70px",
        color: "#f59e0b",
      }}
    >
      12%
    </h1>

    <p>Detected conflicting sources</p>
  </div>
</div>

        {/* Report */}
        {report && (
          <div
            style={{
              background: "white",
              color: "#111",
              padding: "30px",
              borderRadius: "16px",
              width: "100%",
            }}
          >
            <h2>Research Report</h2>

            <div
  style={{
    whiteSpace: "pre-wrap",
    wordBreak: "break-word",
    lineHeight: "1.8",
    fontSize: "16px",
  }}
>
  <ReactMarkdown remarkPlugins={[remarkGfm]}>
  {report}
</ReactMarkdown>
</div>

            {pdfFile && (
              <a
              href={`${API_URL}/${pdfFile}`}
                target="_blank"
                rel="noreferrer"
                style={{
                  display: "inline-block",
                  marginTop: "20px",
                  background: "#2563eb",
                  color: "white",
                  padding: "12px 20px",
                  borderRadius: "10px",
                  textDecoration: "none",
                }}
              >
                Download PDF Report
              </a>
            )}
          </div>
        )}
      </div>
    </div>
  );
}

export default App;