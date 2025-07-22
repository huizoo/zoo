import { useState } from 'react';

const TextArea = () => {
  const [value, setValue] = useState('');

  console.log('[TextArea] render', value);

  return (
    <div>
    <textarea
      value={value}
      onChange={(e) => {
        setValue(e.target.value);
      }}
    />
    <h3>{value}</h3>
    </div>
  );
}

export default TextArea;
