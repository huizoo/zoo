import Hello from './Hello'
import World from './World'
import Heading from './Heading'

// const App = () => {
//   return (
//     <div>
//       {/* <Hello /> */}
//       {/* <World /> */}
//       <Heading type="h1">Hello</Heading>
//       <Heading type="h2">World</Heading>
//     </div>
//   )
// }

const App = () => {
  let value = 0;
  return (
    <div>
      <h1>value: {value}</h1>
      <button onClick={() => {
        value = value + 1;
      }}>Increase value</button>
      
    </div>
  )
}

export default App