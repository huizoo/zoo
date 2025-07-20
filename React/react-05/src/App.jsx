// import Counter from "./components/Counter";

// const App = () => {
//   return (
//     <div>
//       <Counter />
//     </div>
//   );
// };

import { useState } from "react";
import ClassComponent from "./components/ClassComponent";
import FunctionalComponent from "./components/FunctionalComponent";

const App = () => {
  const [toggle, setToggle] = useState(true);

  return (
    <>
      {toggle && <ClassComponent />}
      {toggle || <FunctionalComponent />}

      <hr />

      <button onClick={() => setToggle((t) => !t)}>toggle</button>
    </>
  );
};

export default App;
