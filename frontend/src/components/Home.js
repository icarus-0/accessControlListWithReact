import React from "react";
import Table from "./Table";
import Navbar from "./Navbar";
function Home() {
  return (
    <div>
      <Navbar />
      <div className="container">
        <Table title="Users" />
        <Table title="Groups" />
      </div>
    </div>
  );
}

export default Home;
