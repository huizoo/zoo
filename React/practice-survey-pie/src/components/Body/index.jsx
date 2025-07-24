import SelectInput from '../SelectInput'
import TextInput from '../TextInput'

const Body = ({ type, answer, setAnswer }) => {
  let InputComponent = null
  if (type === 'select') {
    InputComponent = SelectInput
  } else if (type === 'text') {
    InputComponent = TextInput
  } else if (type === 'textarea') {
  }
  return (
    <>
      <InputComponent answer={answer} setAnswer={setAnswer} />
    </>
  )
}

export default Body
