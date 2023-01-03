import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import Home from "./components/Home";
import Users from "./components/Users";
import Groups from "./components/Groups";

function App() {
  return (
    <>
      <Router>
        <Routes>
          <Route exact path="/" element={<Home />} />
          <Route exact path="/users" element={<Users />} />
          <Route exact path="/groups" element={<Groups />} />
        </Routes>
      </Router>
    </>
  );
}

export default App;
