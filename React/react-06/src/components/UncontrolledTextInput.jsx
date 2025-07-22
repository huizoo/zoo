import { useRef } from 'react';

const UncontrolledTextInput = () => {
  const inputRef = useRef();

  console.log('[UncontrolledTextInput] render');

  return (
    <>
      <input ref={inputRef} type="text" />
      <button
        onClick={() => {
          console.log(inputRef.current.value);
          inputRef.current.value = '바꿨습니다'
          console.log(inputRef.current.value);
        }}
      >
        Get value
      </button>
    </>
  );
}

export default UncontrolledTextInput;
