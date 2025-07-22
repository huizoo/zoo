import { useState } from "react";

const Accordion = ({ title, content }) => {
  const [isOpened, setIsOpend] = useState(false);

  return (
    <div>
      <div
        style={{
          background: "#666",
          color: "white",
          fontWeight: "bold",
          padding: 10,
          display: "flex",
          justifyContent: "space-between",
        }}
        onClick={() => {
          // setIsOpend((state) => {
          //   return !state;
          // });
          setIsOpend((state) => !state);
        }}
      >
        <div>{title}</div>
        <div>{isOpened ? '-' : '+'}</div>
      </div>
      {isOpened && (
        <div
          style={{
            border: "1px solid #999",
            padding: 20,
          }}
        >
          {content}
        </div>
      )}
    </div>
  );
};

export default Accordion;
