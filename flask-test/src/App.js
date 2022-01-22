import React, { useEffect, useState } from "react";
import axios from "axios";

const getUser = async () => {
  const data = await axios.get("http://localhost:5000/");
  console.log(data);
  return data;
};

function App() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    setUsers(getUser());
  }, []);

  console.log(users);
  return (
    <div className="App">
      <div>app</div>
    </div>
  );
}

export default App;
