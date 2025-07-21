const Heading = (props) => {
  if (props.type === 'h2') {
    console.log(props)
    return <h2>{props.children}</h2>
  }
  console.log(props)
  return <h1>{props.children}</h1>
}

export default Heading