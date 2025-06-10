import "./index.css";

import React from "react";
import { createRoot } from "react-dom/client";

// let text = 'Hello, world!'
// const num = 15
// const obj = {key: 0, a: 1, b: 2}
// const arr = ['a', 'b', 'c']
// const imageUrl = 'https://i.namu.wiki/i/p_1IEyQ8rYenO9YgAFp_LHIAW46kn6DXT0VKmZ_jKNijvYth9DieYZuJX_E_H_4GkCER_sVKhMqSyQYoW94JKA.svg'
// const element = (
//   <div>
//     <h1>변수 넣기</h1>
//     <ul>
//       <li>{text}</li>
//       <li>{text + 'text'}</li>
//     </ul>
//     <h1>숫자 및 계산식 넣기</h1>
//     <ul>
//       <li>{num}</li>
//       <li>{num + 15}</li>
//     </ul>
//     <h1>Boolean, Nullish 값 넣기</h1>
//     <ul>
//       <li>{true}</li>
//       <li>{false}</li>
//       <li>{undefined}</li>
//       <li>{null}</li>
//     </ul>
//     <h1>Object, Array 넣기</h1>
//     <ul>
//       {/* <li>{obj}</li> */}
//       <li>{arr}</li>
//       <li>{[<div>111</div>, <div>222</div>, <div>333</div>]}</li>
//     </ul>
//     {/* <h1>주석 넣기</h1> */}
//     <ul>
//       <li>{/* 주석입니다. */}</li>
//     </ul>
//     <ul>
//       <li><img src={imageUrl} alt="logo" /></li>
//     </ul>
//   </div>
// )

// const arr = [1, 2, 3]
// const arr2 = []
// const text = ''
// const element = (
//   <div>
//     <h1>삼항연산자</h1>
//     <ul>
//       <li>
//         {1 + 1 === 2
//           ? '참입니다.'
//           : '거짓입니다.'}
//       </li>
//     </ul>

//     <h1>AND 연산자</h1>
//     <ul>
//       <li>{1 + 1 === 2 && 'AND 연산자1'}</li>
//       <li>{arr.length && 'AND 연산자2'}</li>
//       <li>{arr2.length && 'AND 연산자3'}</li>
//       <li>{!!arr2.length && 'AND 연산자4'}</li>
//     </ul>

//     <h1>OR 연산자</h1>
//     <ul>
//       <li>{1 + 1 !== 2 || 'OR 연산자1'}</li>
//       <li>{text || 'OR 연산자2'}</li>
//       <li>{text || 'text가 없습니다.'}</li>
//     </ul>

//     <h1>IF문 (즉시실행함수)</h1>
//     <ul>
//       <li>
//         {(() => {
//           if (1 + 1 === 2) return 'IF'
//           else return 'ELSE'
//         })()}
//       </li>
//       <li>
//         {(() => {
//           const data = '즉시실행함수'

//           /* 어떤 연산이든 추가 가능 */
//           /* 일반적으로는 이렇게 즉시실행함수가
//          미리 위에서 가공하여 전달 */

//          return data
//         })()}
//       </li>
//     </ul>
//   </div>
// )

// const arr = ['1번', '2번', '3번']
// const arr2 = []
// for (let i=0; i< arr.length; i++){
//   arr2.push(<h4 key={i}>{arr[i]}</h4>)
// }
// const element = (
//   <div>
//     <h1>배열로 넣기</h1>
//   <ul>
//     <li>{arr}</li>
//     <li>{arr2}</li>
//   </ul>

//   <hr />

//   <h1>Array.map</h1>
//   <ul>
//     <li>
//       {arr.map((item, index) => {
//         return <h4 key={`${item}-${index}`}>{item}</h4>
//       })}
//     </li>
//   </ul>
//   </div>
//   // React에서 key가 필요한 이유 :
//   // Virtual DOM 에서 여러 개의 엘리먼트(리스트)를 렌더링할 때,
//   // 데이터의 변화(추가/삭제/정렬 등)가 일어났을 때
//   // key를 통해 '각 엘리먼트가 이전 렌더링과 같은 객체인지, 새로운 객체인지'
//   // 변화를 빠르게 식별해야 하기 때문.
//   // 실전에서는 key를 index로 쓰지 않음.
//   // 배열의 순서가 변하거나, 요소가 추가/삭제되면 인덱스 값이 같이 바뀌기 때문.
// )

// const roundBoxStyle = {
//   position: "absolute",
//   top: 50,
//   left: 50,
//   width: "50%",
//   height: "200px",
//   padding: 20,
//   background: "rgba(162,216,235,0.6)",
//   // 3. 속성은 camelCase
//   // border-radius 가 아니라 borderRadius
//   // background-color 가 아니라 backgroundColor
//   // borderRadius: 50,
//   // backgroundColor: "#fff",
// };

// const element = (
//   <div
//     // style="position:relative;width:400px"
//     style={{
//       // 1. Object로 css 작성
//       position: "relative",
//       width: 400,
//       height: 1000,
//       background: "#f1f1f1",
//     }}
//   >
//     <div style={roundBoxStyle}>Hello1</div>

//     <div style={{ ...roundBoxStyle, top: 350 }}>
//       {/* 4. className을 통한 스타일링 (CSS-in-JS) */}
//       <div className="highlight">Hello2</div>
//       {/* <div className={"highlight"}>Hello2</div> */}
//       {/* 위 코드처럼 중괄호를 이용해서 className 삽입도 가능 */}
//     </div>

//     <div style={{ ...roundBoxStyle, top: 650 }}>
//       {/* 5. 조건적 스타일 */}
//       <div className={1 + 1 === 2 ? "highlight" : ""}>Hello3</div>
//       <div className={1 + 1 === 2 && "highlight"}>Hello3</div>
//     </div>
//   </div>
// )

const nums = Array.from({ length: 9 }, (_, i) => i + 1);
// Array.from() 은 본질적으로 Array.from(arrayLike).map(...) 을 한 번에 하는 축약 형태
// 하지만 위 코드에서 두번째 인자로 콜백함수를 받지 않게 되면 각 자리에 undefined가 들어감
// Array.from("hello") 같은 경우는 ['h','e','l','l','o'] 로 분해됨

const element = (
  <div style={{ display: "flex" }}>
    {nums.map(
      (n) =>
        n !== 1 &&
        n !== 5 && (
          <div
            key={n}
            style={{ padding: 10, color: n % 2 === 1 ? "blue" : "black" }}
          >
            {/* <div style={{ padding: 10, color: n % 2 ? 'blue' : 'black' }}> */}
            {nums.map((m) => (
              <div key={`${n}-${m}`}>
                {n} x {m} = {n * m}
              </div>
            ))}
          </div>
        )
    )}
  </div>
);

const container = document.getElementById("root");
const root = createRoot(container);
root.render(element);
