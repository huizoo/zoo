import ActionButtons from '../ActionButtons'
import Body from '../Body'
import Desc from '../Desc'
import Title from '../Title'

const QuestionBox = ({
  question,
  questionsLength,
  step,
  answer,
  setAnswer,
}) => {
  return (
    <div>
      <Title>{question.title}</Title>
      <Desc>{question.desc}</Desc>
      <Body
        type={question.type}
        options={question.options}
        answer={answer}
        setAnswer={setAnswer}
      />
      <ActionButtons questionsLength={questionsLength} step={step} />
    </div>
  )
}

export default QuestionBox
