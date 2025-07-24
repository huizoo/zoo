import { Route, Routes } from 'react-router-dom'

import CompletionPage from './pages/CompletionPage'
import SurveyPage from './pages/SurveyPage'

const App = () => {
  return (
    <div className="App">
      <div>Hello World</div>
      <Routes>
        <Route path="/done" element={<CompletionPage />} />
        <Route path="/survey/:surveyId" element={<SurveyPage />}>
          <Route path=":step" element={<SurveyPage />}></Route>
        </Route>
      </Routes>
    </div>
  )
}

export default App
