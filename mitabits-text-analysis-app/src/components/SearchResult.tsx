import React from 'react';
import { Card, Badge } from 'react-bootstrap';

interface Object {
    name: string,
    html: string,
}
interface SearchInstance {
    object: Object,
    score: any
}
const SearchResult = ({ instance }: { instance?: SearchInstance }): JSX.Element => {
    if (instance) {
        return (
            <Card>
                <Card.Body>
                    <div className="text-right">
                        <Badge pill variant="info">
                            {instance.score * 100}% match
                    </Badge>

                    </div>
                    <div dangerouslySetInnerHTML={{ __html: instance.object.html }}></div>
                </Card.Body>
            </Card>
        )
    }
    return <React.Fragment />
}
export default SearchResult