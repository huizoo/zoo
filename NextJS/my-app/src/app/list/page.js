const List = () => {
  const itemList = ["상품1", "상품2", "상품3"];
  return (
    <div>
      <h4 className="text-center">상품목록</h4>
      <div className='space-y-2'>
        {itemList.map((item) => (
          <div className='my-5 mx-auto p-[20px] w-[200px] bg-white text-slate-900 border rounded-xl'>{item} $40</div>
        ))}
      </div>
    </div>
  );
};

export default List;
