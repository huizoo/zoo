// // import { useCallback } from "react";

// // // 컴포넌트 외부에 함수 선언
// // const handleClick2 = (e) => {
// //   console.log("click2", e);
// // }

// // const App = () => {
// //   /**
// //    * ℹ️합성 이벤트 (SyntheticEvent)
// //    * - React에서 이벤트가 발생할 때, 이벤트 핸들러의 인자로 합성 이벤트 객체가 전달됨
// //    * - 이 합성 이벤트는 javascript 에서 전달 받는 이벤트 객체를 확장(래핑)한 객체임
// //    *   (거의 동일한 인터페이스를 가지고 있음)
// //    * - 원본 이벤트 객체(native event)는 syntheticEvent.nativeEvent 에 있음
// //    * - 지금은 그냥 같은 이벤트 객체라고 생각해도 무방
// //    */
// //   const handleClick1 = (e) => {
// //     console.log("click1", e);
// //   }

// //   /**
// //    * ℹ️이벤트 핸들러(함수)를 만들 때는 react lifecycle을 고려하자!
// //    *  - 컴포넌트가 리랜더링 되면 컴포넌트 내에서 단순 정의한 함수가 새로운 함수로 만들어짐
// //    *  - 이것은 불필요한 작업으로 성능 문제를 야기함
// //    *  - 그래서 함수의 정의를 최대한 컴포넌트 밖으로 빼거나,
// //    *    useCallback으로 감싸줘서 매 랜더링 마다 새로 만들어지지 않도록 해줄 필요가 있음
// //    */
// //   const handleChange = useCallback((e) => {
// //     console.log("change", e.target.value);
// //   }, []);

// //   return (
// //     <div>
// //       <button onClick={handleClick1}>Button1</button>
// //       <button onClick={handleClick2}>Button2</button>
// //       <div>
// //         <input type="text" onChange={handleChange} />
// //       </div>
// //     </div>
// //   );
// // }

// // // /** HTML **/
// // // <>
// // //   /** HTML **/
// // //   <button onclick="handleClick()">handleClick</button>
// // //   /** React **/
// // //   <button onClick={handleClick}>Button</button>
// // // </>;

// const App = () => {
//   return (
//     <div className="App">
//       <button
//         onClick={() => {
//           console.log('onClick');
//         }}
//         onMouseDown={() => {
//           console.log('onMouseDown');
//         }}
//         onMouseUp={() => {
//           console.log('onMouseUp');
//         }}
//       >
//         Button
//       </button>
//       <div
//         className="box"
//         onClick={() => {
//           console.log('onClick');
//         }}
//         onMouseEnter={() => {
//           console.log('onMouseEnter');
//         }}
//         onMouseLeave={() => {
//           console.log('onMouseLeave');
//         }}
//         onMouseMove={() => {
//           console.log('onMouseMove');
//         }}
//       ></div>
//       <div>
//         <input
//           type="text"
//           onKeyDown={() => {
//             console.log('onKeyDown');
//           }}
//           onKeyUp={() => {
//             console.log('onKeyUp');
//           }}
//           onFocus={() => {
//             console.log('onFocus');
//           }}
//           onBlur={() => {
//             console.log('onBlur');
//           }}
//           onChange={() => {
//             console.log('onChange');
//           }}
//         />
//       </div>
//     </div>
//   );
// }

// import CheckBox from './components/CheckBox';
// import Select from './components/Select';
// import TextArea from './components/TextArea';
// import TextInput from './components/TextInput';
// import UncontrolledTextInput from './components/UncontrolledTextInput';

// const App = () => {
//   return (
//     <div className="App">
//       <div>
//         <TextInput />
//       </div>
//       <div>
//         <TextArea />
//       </div>
//       <div>
//         <Select />
//       </div>
//       <div>
//         <CheckBox />
//       </div>
//       <div>
//         <UncontrolledTextInput />
//       </div>
//     </div>
//   );
// }

import { useState } from "react";
import TextInput from "./components/TextInput2";
import Select from "./components/Select2";

const countryOptions = ["한국", "중국", "일본", "러시아", "미국"];

const App = () => {
  const [formValue, setFormValue] = useState({
    name: "",
    country: "",
    address: "",
  });

  console.log(formValue);

  return (
    <div className="App">
      <div className="form">
        <div className="form-item">
          <h1>1. 이름이 무엇인가요?</h1>
          <TextInput
            value={formValue.name}
            setValue={(value) => {
              // setFormValue({
              //   ...formValue,
              //   name: value,
              // });
              setFormValue((prev) => ({
                ...prev,
                name: value,
              }));
            }}
          />
        </div>
        <div className="form-item">
          <h1>2. 사는 곳은 어딘가요?</h1>
          <Select
            options={countryOptions}
            value={formValue.country}
            setValue={(value) => {
              setFormValue((prev) => ({
                ...prev,
                country: value,
              }));
            }}
          />
        </div>
        {formValue.country === "한국" && (
          <div className="form-item">
            <h1>2-1. 한국 어디에 사나요?</h1>
            <TextInput
              value={formValue.address}
              setValue={(value) => {
                setFormValue((prev) => ({
                  ...prev,
                  address: value,
                }));
              }}
            />
          </div>
        )}
        <div className="button-group">
          <button
            onClick={() => {
              alert("저장되었습니다.");
              setFormValue({
                name: "",
                country: "",
                address: "",
              });
            }}
            disabled={
              (formValue.name === "" || formValue.country === "") && true
            }
          >
            저장
          </button>
        </div>
      </div>
    </div>
  );
};

export default App;
