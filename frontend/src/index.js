import React from "react";
import ReactDOM from "react-dom/client";
import Garlic from "./App.js";
import About from "./About.js";

import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

let root = ReactDOM.createRoot(document.getElementById("root"));

function App() {
  return (
    <div>
      <Router>
        <Routes>
          <Route path="/" element={<Garlic />} />
          <Route exact path="/home" element={<Garlic />} />
          <Route path="/about" element={<About />} />
        </Routes>
      </Router>
    </div>
  );
}

root.render(<App></App>);
