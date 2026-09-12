import { useState, useRef } from 'react'

export default function UploadForm({ onSubmit, isLoading }) {
  const [file, setFile] = useState(null)
  const [jobDescription, setJobDescription] = useState('')
  const [dragging, setDragging] = useState(false)
  const inputRef = useRef(null)

  // Handle file selection from input or drag
  function handleFile(selectedFile) {
    if (selectedFile && selectedFile.type === 'application/pdf') {
      setFile(selectedFile)
    } else {
      alert('Please upload a PDF file.')
    }
  }

  function handleDragOver(e) {
    e.preventDefault()
    setDragging(true)
  }

  function handleDragLeave() {
    setDragging(false)
  }

  function handleDrop(e) {
    e.preventDefault()
    setDragging(false)
    const droppedFile = e.dataTransfer.files[0]
    handleFile(droppedFile)
  }

  function handleSubmit(e) {
    e.preventDefault()
    if (!file || !jobDescription.trim()) return
    onSubmit(file, jobDescription)
  }

  const canSubmit = file && jobDescription.trim() && !isLoading

  return (
    <form onSubmit={handleSubmit}>
      {/* File Upload */}
      <div className="card">
        <p className="card-label">Resume</p>
        <div
          className={`upload-zone ${dragging ? 'dragging' : ''} ${file ? 'has-file' : ''}`}
          onClick={() => inputRef.current.click()}
          onDragOver={handleDragOver}
          onDragLeave={handleDragLeave}
          onDrop={handleDrop}
        >
          <input
            ref={inputRef}
            type="file"
            accept=".pdf"
            onChange={(e) => handleFile(e.target.files[0])}
          />
          <div className="upload-icon">{file ? '📄' : '⬆'}</div>
          {file
            ? <p className="file-name">{file.name}</p>
            : <p>Drop your PDF here or <strong>click to browse</strong></p>
          }
        </div>
      </div>

      {/* Job Description */}
      <div className="card">
        <p className="card-label">Job Description</p>
        <textarea
          placeholder="Paste the job description here..."
          value={jobDescription}
          onChange={(e) => setJobDescription(e.target.value)}
        />
      </div>

      <button className="btn" type="submit" disabled={!canSubmit}>
        {isLoading ? 'Analyzing...' : 'Run ATS Check'}
      </button>
    </form>
  )
}
