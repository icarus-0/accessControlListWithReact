import React, { useState, useEffect } from "react";
import Request from "../Action/Request";
import axios from "axios";

function Table(props) {
  let [users, setUsers] = useState([]);
  let [groups, setGroups] = useState([]);

  async function getAccountsData() {
    const config = {
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
    };
    const res = await axios.get(Request.getAccounts, config);
    setUsers(res.data);
  }
  async function getRightGroupsData() {
    const config = {
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
    };
    const res = await axios.get(Request.getRightGroups, config);
    setGroups(res.data);
  }

  useEffect(() => {
    getAccountsData();
    getRightGroupsData();
  }, [users, groups]);

  const userTable = (title) => {
    return (
      <div className="mt-5">
        <h4>{title}</h4>
        <table className="table table-hover">
          <thead>
            <tr>
              <th scope="col">Email</th>
              <th scope="col">Name</th>
            </tr>
          </thead>
          <tbody>
            {users.map((user) => {
              return (
                <tr>
                  <th scope="row">{user.email}</th>
                  <td>{user.name}</td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    );
  };

  const groupsTable = (title) => {
    return (
      <div className="mt-5">
        <h4>{title}</h4>
        <table className="table table-hover">
          <thead>
            <tr>
              <th scope="col">Id</th>
              <th scope="col">Group Name</th>
            </tr>
          </thead>
          <tbody>
            {groups.map((group) => {
              return (
                <tr>
                  <th scope="row">{group.id}</th>
                  <td>{group.name}</td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    );
  };

  if (props.title === "Users") {
    return userTable(props.title);
  } else if (props.title === "Groups") {
    return groupsTable(props.title);
  }
}

export default Table;
