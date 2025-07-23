import "./index.css";

const MemoItem = ({ children, onClickItem, isSelected, onClickDelete }) => {
  return (
    <div
      className={"MemoItem" + (isSelected ? " selected" : "")}
      onClick={onClickItem}
    >
      <div className="MemoItem__title">{children}</div>
      <button className="MemoItem__delete-button" onClick={onClickDelete}>
        X
      </button>
    </div>
  );
};

export default MemoItem;
