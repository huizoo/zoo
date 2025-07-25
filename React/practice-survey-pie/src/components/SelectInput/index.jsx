import styled from 'styled-components'

const Item = ({ children, onChange, checked }) => {
  return (
    <ItemWrapper>
      <label>
        <input type="checkbox" onChange={onChange} checked={checked} />
        <span />
        <div>{children}</div>
      </label>
    </ItemWrapper>
  )
}

const SelectInput = ({ answer = [], setAnswer, options }) => {
  const handleChange = (isChecked, index) => {
    if (isChecked) {
      setAnswer([...answer, index])
    } else {
      setAnswer(answer.filter((item) => item !== index))
    }
  }

  return (
    <SelectInputWrapper>
      {options.items.map((item, index) => {
        return (
          <Item
            key={index}
            onChange={(e) => {
              handleChange(e.target.checked, index)
            }}
            checked={answer.includes(index)}
          >
            {item}
          </Item>
        )
      })}
    </SelectInputWrapper>
  )
}

const SelectInputWrapper = styled.div`
  display: flex;
  flex-direction: column;
  gap: 24px;
`

const ItemWrapper = styled.div`
  input[type='checkbox'] {
    display: none;
  }

  input[type='checkbox'] ~ span {
    width: 24px;
    height: 24px;
    border: 3px solid #e2dfdf;
    box-sizing: border-box;
    display: inline-block;
    border-radius: 50%;
    vertical-align: middle;
    margin-right: 10px;
  }

  input[type='checkbox']:checked ~ span {
    border: 8px solid #6542f1;
  }

  input[type='checkbox'] ~ div {
    font-size: 14px;
    line-height: 18px;
    display: inline-block;
    vertical-align: middle;
  }

  input[type='checkbox']:checked ~ div {
    font-weight: bold;
  }
`

export default SelectInput
