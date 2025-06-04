import React, { useState } from 'react';
import axios from 'axios';
import { Row, Col, Form, Button } from 'react-bootstrap';

import AnnotatedDocumentViewer from './AnnotatedDocumentViewer';


const DocumentAnnotator = (): JSX.Element => {
  const defaultTextPlaceholder = "Alan Turing was born on 23/06/1912. During the Second World War, he worked as a scientist for the Government Code and Cypher School (currently GCHQ) at Bletchley Park, Britain's codebreaking centre that produced Ultra intelligence.";
  const emptyDocument = {
    text: "",
  }
  const [inputValue, setInputValue] = useState(defaultTextPlaceholder);
  const [annotatedDoc, setAnnotatedDoc] = useState(emptyDocument);

  const analyzeInput = () => {
    axios.post(`${process.env.REACT_APP_NATURAL_LANG_API_HOST}/api/annotate/`, {
      'text': inputValue
    })
      .then(res => {
        setAnnotatedDoc(res.data);
      })
      .catch(err => console.log(err));
  }

  return (
    <Row>
      <Col>
        <Form>
          <Form.Group controlId="formInputText">
            <Form.Control
              as="textarea" rows={5}
              value={inputValue}
              onChange={e => setInputValue(e.target.value)}
            />
          </Form.Group>
          <Button
            variant="primary"
            onClick={analyzeInput}
            style={{ float: 'right' }}
          >
            Analyze
            </Button>
        </Form>
      </Col>
      <Col>
        <AnnotatedDocumentViewer document={annotatedDoc}></AnnotatedDocumentViewer>
      </Col>
    </Row>
  )
}

export default DocumentAnnotator;