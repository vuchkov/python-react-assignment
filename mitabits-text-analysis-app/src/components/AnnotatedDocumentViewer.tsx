import React from 'react';
import { Row, Col, Table, Badge } from 'react-bootstrap';
import { Link } from "react-router-dom";

import './AnnotatedDocumentViewer.css';

interface Mention {
    type: string,
    content: string,
    metadata: any

}
interface AnnotatedDocument {
    text: string,
    mentions?: Mention[]
}


const AnnotatedDocumentViewer = ({ document }: { document: AnnotatedDocument }): JSX.Element => {
    const displayMetadata = (type: string, metadata: any): JSX.Element => {
        if (type.toLowerCase() === 'date') {
            return <code>{metadata.iso_date}</code>
        }
        return <React.Fragment />
    }

    if (document.text) {
        let documentTextBlock = React.createElement("div", { className: "annotated-document" }, document.text);
        let mentionRows;
        if (document.mentions) {
            mentionRows = document.mentions.map((mention) =>
                <tr>
                    <td><code>{mention.type}</code></td>
                    <td><em>"{mention.content}"</em></td>
                    <td>{mention.metadata && displayMetadata(mention.type, mention.metadata)}</td>
                    <td>{['PERSON', 'ORGANISATION', 'ROLE'].includes(mention.type) && <Link to={`/search?q=${mention.content}&t=${mention.type.toLowerCase()}`} target="_blank">Lookup</Link>}</td>
                </tr>
            );
        }

        let mentionsTable = (
            <Table size="sm">
                <thead>
                    <tr>
                        <th>Type</th>
                        <th>Content</th>
                        <th>Meta</th>
                        <th></th>
                    </tr>
                </thead>
                <tbody>
                    {mentionRows}
                </tbody>
            </Table>
        )
        return (
            <div>
                <Row>
                    <Col>{documentTextBlock}</Col>
                </Row>
                <Row>
                    <Col>{mentionsTable}</Col>
                </Row>
            </div>
        );
    } else {
        return <React.Fragment />
    }
}

export default AnnotatedDocumentViewer;