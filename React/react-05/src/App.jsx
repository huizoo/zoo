// import Counter from "./components/Counter";

// const App = () => {
//   return (
//     <div>
//       <Counter />
//       {/* aaaaa */}
//     </div>
//   );
// };

// import { useState } from "react";
// import ClassComponent from "./components/ClassComponent";
// import FunctionalComponent from "./components/FunctionalComponent";

// const App = () => {
//   const [toggle, setToggle] = useState(true);

//   return (
//     <>
//       {toggle && <ClassComponent />}
//       {toggle || <FunctionalComponent />}

//       <hr />

//       <button onClick={() => setToggle((t) => !t)}>toggle</button>
//     </>
//   );
// };

import Accordion from "./components/Accordion";

const App = () => {
  return (
    <div style={{ fontSize: "2rem", padding: 30 }}>
      <Accordion title="This is a Title" content="This is a content" />
    </div>
  );
};

export default App;
