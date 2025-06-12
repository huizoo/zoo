// // import Hello from './components/Hello'
// // import World from './components/World'
// import Heading from "./components/Heading";

// import { useState } from "react";

// export default function App() {
//   const [value, setValue] = useState(0);

//   return (
//     <div>
//       {/* <Hello type='h1'>Hello</Hello> */}
//       {/* <World /> */}
//       <Heading type="h1">Hello</Heading>
//       <Heading type="h2">World</Heading>
//       <h1>value: {value}</h1>
//       <button
//         onClick={() => {
//           console.log("Increase value1", value);
//           setValue(value + 1);
//           console.log("Increase value2", value);
//         }}
//       >
//         Increase value
//       </button>
//       <button onClick={() => setValue(0)}>Reset value</button>
//     </div>
//   );
// }












// import React, { Component } from "react";

// export default class App extends Component {
//   state = {
//     value: 0,
//   };

//   constructor(props) {
//     super(props);
//     this.state = {
//       value: 1,
//     };
//   }

//   resetValue() {
//     this.setState({ value: 0 });
//   }

//   render() {
//     return (
//       <div>
//         <h1>value: {this.state.value}</h1>
//         <button
//           onClick={() => {
//             this.setState((state) => ({
//               value: state.value + 1,
//             }));
//           }}
//         >
//           Increase value
//         </button>
//         <button onClick={this.resetValue.bind(this)}>Reset value</button>
//       </div>
//     );
//   }
// }







import CourseCard from './components/CourseCard.jsx'

const App = () => {
  return (
    <div style={{ padding: 30 }}>
      <CourseCard
      img="https://dst6jalxvbuf5.cloudfront.net/media/images/Course/cover_image/210909_191531/23.png"
      tags={['발표', '패키지', '최대할인']}
      title="비즈니스 올인원, 방구석 어학연수 패키지"
      startPrice={349000}
      types={['동영상 강의']}
       />
    </div>
  )
}

export default App