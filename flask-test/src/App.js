import React, { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [users, setUsers] = useState([]);
  const [text, setText] = useState("");

  const getUser = async () => {
    const data = await axios.get("http://localhost:5000/");
    console.log(data);
    return data;
  };

  const postUser = async () => {
    try {
      const data = await axios.post("http://localhost:5000/", { text });
      console.log(data);
      return data;
    } catch (error) {
      console.log(error);
    }
  };

  useEffect(() => {
    setUsers(getUser());
  }, []);

  console.log(users);
  return (
    <div className="App">
      <div>app</div>
      <input value={text} onChange={e => setText(e.target.value)} />
      <button onClick={postUser}>제출</button>
    </div>
  );
}

export default App;
