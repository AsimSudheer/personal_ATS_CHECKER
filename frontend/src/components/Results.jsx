export default function Results({ data }) {
  const { ats_analysis } = data

  const score = ats_analysis.match_score ?? 0
  const matchedKeywords = ats_analysis.matched_keywords ?? []
  const missingKeywords = ats_analysis.missing_keywords ?? []
  const recommendations = ats_analysis.recommendations ?? []
  const summary = ats_analysis.summary ?? ''
  const experienceMatch = ats_analysis.experience_match ?? ''

  return (
    <div className="results">
      <div className="card">
        {/* Score */}
        <div className="score-row">
          <span className="score-label">ATS Match Score</span>
          <span className="score-value">{score}%</span>
        </div>
        <div className="progress-bar">
          <div className="progress-fill" style={{ width: `${score}%` }} />
        </div>

        {/* Summary */}
        <p className="summary-text">{summary}</p>

        <div className="divider" />

        {/* Experience */}
        {experienceMatch && (
          <>
            <p className="section-title">Experience Match</p>
            <p style={{ fontSize: '0.875rem', color: '#6b6b6b' }}>{experienceMatch}</p>
            <div className="divider" />
          </>
        )}

        {/* Matched Keywords */}
        {matchedKeywords.length > 0 && (
          <>
            <p className="section-title">Matched Keywords</p>
            <div className="tag-list">
              {matchedKeywords.map((kw) => (
                <span key={kw} className="tag matched">{kw}</span>
              ))}
            </div>
            <div className="divider" />
          </>
        )}

        {/* Missing Keywords */}
        {missingKeywords.length > 0 && (
          <>
            <p className="section-title">Missing Keywords</p>
            <div className="tag-list">
              {missingKeywords.map((kw) => (
                <span key={kw} className="tag missing">{kw}</span>
              ))}
            </div>
            <div className="divider" />
          </>
        )}

        {/* Recommendations */}
        {recommendations.length > 0 && (
          <>
            <p className="section-title">Recommendations</p>
            <ul className="recommendation-list">
              {recommendations.map((rec, i) => (
                <li key={i}>{rec}</li>
              ))}
            </ul>
          </>
        )}
      </div>
    </div>
  )
}
