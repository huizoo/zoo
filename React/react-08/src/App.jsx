import { useState, useCallback } from "react";
import "./App.css";
import MemoContainer from "./components/MemoContainer";
import SideBar from "./components/SideBar";
import { setItem, getItem } from "./lib/storage";
import debounce from "lodash.debounce";

const debouncedSetItem = debounce(setItem, 5000);

const App = () => {
  const [memos, setMemos] = useState(getItem("memos") || []);

  const [selectedMemoIndex, setSelectedMemoIndex] = useState(0);

  // const setMemo = (newMemo) => {
  //   const newMemos = [...memos];

  //   newMemos[selectedMemoIndex] = newMemo;

  //   setMemos(newMemos);
  // };

  const setMemo = useCallback(
    (newMemo) => {
      setMemos((prev) => {
        const newMemos = [...prev];
        newMemos[selectedMemoIndex] = newMemo;
        debouncedSetItem("memos", newMemos);
        return newMemos;
      });
    },
    [selectedMemoIndex]
  );

  const addMemo = useCallback(() => {
    const now = Date.now();
    setMemos((prev) => {
      const newMemos = [
        ...prev,
        {
          title: "Untitled",
          content: "",
          createdAt: now,
          updatedAt: now,
        },
      ];
      debouncedSetItem("memos", newMemos);
      setSelectedMemoIndex(newMemos.length - 1);
      return newMemos;
    });
  }, []);

  const deleteMemo = useCallBack(
    (index) => {
      setMemos((prev) => {
        const newMemos = [...prev];
        newMemos.splice(index, 1);

        if (index === selectedMemoIndex) {
          setSelectedMemoIndex(0);
        } else if (index < selectedMemoIndex) {
          setSelectedMemoIndex(selectedMemoIndex - 1);
        }

        debouncedSetItem("memos", newMemos);

        return newMemos;
      });
    },
    [selectedMemoIndex]
  );

  return (
    <div className="App">
      <SideBar
        memos={memos}
        addMemo={addMemo}
        selectedMemoIndex={selectedMemoIndex}
        setSelectedMemoIndex={setSelectedMemoIndex}
        deleteMemo={deleteMemo}
      />
      <MemoContainer memo={memos[selectedMemoIndex]} setMemo={setMemo} />
    </div>
  );
};

export default App;
