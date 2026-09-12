import { useState } from 'react'
import './index.css'
import UploadForm from './components/UploadForm'
import Results from './components/Results'

export default function App() {
  const [result, setResult] = useState(null)
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState(null)

  async function handleSubmit(file, jobDescription) {
    setIsLoading(true)
    setError(null)
    setResult(null)

    try {
      const formData = new FormData()
      formData.append('file', file)
      formData.append('job_description', jobDescription)

      const response = await fetch('https://personal-ats-checker.onrender.com/uploads/', {
        method: 'POST',
        body: formData,
      })

      const data = await response.json()
      setResult(data)

    } catch (err) {
      setError('Something went wrong. Make sure the backend is running.')
    }

    setIsLoading(false)
  }

  return (
    <main className="app">
      <header className="header">
        <h1>ATS Resume Checker</h1>
        <p>Upload your resume and a job description to see how well they match.</p>
      </header>

      <UploadForm onSubmit={handleSubmit} isLoading={isLoading} />

      {isLoading && <p className="loading-text">Analyzing your resume...</p>}

      {error && <p className="error-text">{error}</p>}

      {result && result.success && <Results data={result} />}
    </main>
  )
}
