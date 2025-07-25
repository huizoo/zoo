import { useState } from 'react';

const CheckBox = () => {
  const [value, setValue] = useState(false);

  console.log('[CheckBox] render', value);

  return (
    <input
      type="checkbox"
      value={value}
      onChange={(e) => {
        setValue(e.target.checked);
      }}
    />
  );
}

export default CheckBox;
