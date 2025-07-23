import MemoItem from "./MemoItem";

const MemoList = ({
  memos,
  setSelectedMemoIndex,
  selectedMemoIndex,
  deleteMemo,
}) => {
  return (
    <div>
      {memos.map((memo, index) => (
        <MemoItem
          key={index}
          onClickItem={() => {
            setSelectedMemoIndex(index);
          }}
          onClickDelete={(e) => {
            deleteMemo(index);
            e.preventDefault();
            e.stopPropagation();
          }}
          isSelected={index === selectedMemoIndex}
          index={index}
          setSelectedMemoIndex={setSelectedMemoIndex}
        >
          {memo.title}
        </MemoItem>
      ))}
    </div>
  );
};

export default MemoList;
