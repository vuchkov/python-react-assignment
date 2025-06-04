import React from 'react'
import { Container } from 'react-bootstrap';
import DocumentAnnotator from '../components/DocumentAnnotator'

const TextAnalysisPage: React.FC<{}> = () => {
    return (
        <Container fluid style={{ padding: '3rem' }}>
            <h4>Text analysis</h4>
            <DocumentAnnotator />
        </Container>
    )

}
export default TextAnalysisPage;