import { useState } from "react";

const TextInput = () => {
  const [value, setValue] = useState("");

  console.log("[TextInput] render", value);

  return (
    <div>
      <input
        type="text"
        value={value}
        onChange={(e) => {
          setValue(e.target.value);
        }}
      />
      <h3>{value}</h3>
    </div>
  );
};

export default TextInput;
